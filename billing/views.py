from django.shortcuts import render, redirect

from billing.models import consumerBilling


# Create your views here.

def employeeview(request):
    return render(request, "employee.html")
def meter_readingFormview(request):
    if request.method == 'POST':
        invoice_id = request.POST.get("invoice_id")
        consumer_id = request.POST.get("consumer_id")
        consumer_name = request.POST.get("consumer_name")
        previous_unit = request.POST.get("previous_unit")
        current_unit = request.POST.get("current_unit")
        amount = request.POST.get("amount")
        date = request.POST.get("date")
        status = request.POST.get("status")
        meter_number = request.POST.get("meter_number")

        print(consumer_id)

        consumerBilling.objects.create(
            invoice_id=invoice_id,
            consumer_id=consumer_id,
            consumer_name=consumer_name,
            previous_unit=previous_unit,
            current_unit=current_unit,
            amount=amount,
            date=date,
            status=status,
            meter_number=meter_number
        )
        # print("user created!")
        return redirect("/employee/employee_dashboard")
    return render(request, "meter_readingForm.html")