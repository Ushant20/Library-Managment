from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from django.db.models import Sum
from datetime import date, timedelta
from .models import Payment
from .serializers import PaymentSerializer
from .models import Settings
from .serializers import SettingsSerializer
from .utils import generate_receipt, generate_payment_receipt

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):

        payment = serializer.save()

        receipt_url = generate_payment_receipt(payment)

        payment.receipt_url = receipt_url

        payment.save()

class LoginView(APIView):

    def post(self, request):

        print("DATA:", request.data)

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("USER:", user)

        if user is not None:
            return Response({
                "success": True,
                "message": "Login Successful"
            })

        return Response(
            {
                "success": False,
                "message": "Invalid Credentials"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_update(self, serializer):

        old_student = self.get_object()

        student = serializer.save()

        # Renewal detect karo
        if (
            old_student.fee_status != "Paid"
            and student.fee_status == "Paid"
        ):

            student.last_payment_date = date.today()

            if student.fee_due_date:
                student.fee_due_date = (
                    student.fee_due_date + timedelta(days=30)
                )
            else:
                student.fee_due_date = (
                    date.today() + timedelta(days=30)
                )

            Payment.objects.create(
                student=student,
                amount=student.fee_amount
            )

            student.save()

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):

     student = serializer.save()

    # Payment entry create karo
     Payment.objects.create(
        student=student,
        amount=student.fee_amount
     )

     receipt_url = generate_receipt(student)

     student.receipt_url = receipt_url

     student.save()


class DashboardView(APIView):

    def get(self, request):

        total_students = Student.objects.count()

        paid_students = Student.objects.filter(
            fee_status="Paid"
        ).count()

        pending_students = Student.objects.filter(
            fee_status="Pending"
        ).count()

        today = date.today()

        due_today = Student.objects.filter(
            fee_due_date=today
        ).count()

        due_this_week = Student.objects.filter(
            fee_due_date__range=[
                today,
                today + timedelta(days=7)
            ]
        ).count()

        total_collection = Payment.objects.aggregate(
            total=Sum("amount")
        )["total"] or 0

        pending_collection = Student.objects.filter(
            fee_status="Pending"
        ).aggregate(
            total=Sum("fee_amount")
        )["total"] or 0

        return Response({
            "total_students": total_students,
            "paid_students": paid_students,
            "pending_students": pending_students,
            "total_collection": total_collection,
            "pending_collection": pending_collection,
            "due_today": due_today,
            "due_this_week": due_this_week,
        })
    

class PaymentStatsView(APIView):
    def get(self, request):
        total_collection = Payment.objects.aggregate(
            total=Sum("amount")
        ).get("total") or 0

        return Response({
            "total_collection": float(total_collection)
        })

class SettingsView(APIView):

    def get(self, request):

        settings = Settings.objects.first()

        if not settings:
            settings = Settings.objects.create(
                library_name="Front Benchers Library",
                library_address="",
                contact_number="",
                email="",
                opening_time="07:00",
                closing_time="23:00",
                cafe_name="Front Benchers Cafe"
            )

        serializer = SettingsSerializer(settings)

        return Response(serializer.data)

    def put(self, request):

        settings = Settings.objects.first()

        serializer = SettingsSerializer(
            settings,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=400
        )