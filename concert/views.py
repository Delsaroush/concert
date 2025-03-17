from django.shortcuts import render
from .models import Concert, Ticket


from django.core.paginator import Paginator

from django.shortcuts import render
from .models import Concert

def concert_list(request):
    concerts = Concert.objects.all()
    return render(request, 'concert_list.html', {'concerts': concerts})

def filter_concerts(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    concerts = Concert.objects.all()

    if start_date:
        concerts = concerts.filter(date__gte=start_date)
    if end_date:
        concerts = concerts.filter(date__lte=end_date)

    return render(request, 'concert_list.html', {'concerts': concerts})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Concert

def concert_create(request):
    if request.method == 'POST':
        Concert.objects.create(
            name=request.POST['name'],
            date=request.POST['date'],
            venue=request.POST['venue'],
            available_tickets=request.POST['available_tickets']
        )
        return redirect('concert_list')
    return render(request, 'concert_form.html')

def concert_edit(request, id):
    concert = get_object_or_404(Concert, id=id)
    if request.method == 'POST':
        concert.name = request.POST['name']
        concert.date = request.POST['date']
        concert.venue = request.POST['venue']
        concert.available_tickets = request.POST['available_tickets']
        concert.save()
        return redirect('concert_list')
    return render(request, 'concert_form.html', {'concert': concert})

def concert_delete(request, id):
    concert = get_object_or_404(Concert, id=id)
    if request.method == 'POST':
        concert.delete()
        return redirect('concert_list')
    return render(request, 'concert_confirm_delete.html', {'concert': concert})



from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect
from .models import Concert

from django.shortcuts import get_object_or_404, render, redirect
from .models import Concert


    # Render the form for a GET request
def book_ticket(request, concert_id):
    concert = get_object_or_404(Concert, id=concert_id)  # Fetch the selected concert
    return render(request, 'book_ticket.html', {'concert': concert})

from django.shortcuts import render
from .models import Concert

from django.shortcuts import render
from .models import Concert

def filter_concerts(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    concerts = Concert.objects.all()
    if start_date:
        concerts = concerts.filter(date__gte=start_date)
    if end_date:
        concerts = concerts.filter(date__lte=end_date)

    return render(request, 'concert_list.html', {'concerts': concerts})
def success_page(request):
    return render(request, 'booking_successful.html')

def booking_successful(request, concert_name):
    return render(request, 'booking_successful.html', {'concert_name': concert_name})

from django.shortcuts import redirect

def process_booking(request):
    # Logic to process booking
    concert_name = 'Rock Symphony'  # Replace with dynamic data
    return redirect('booking_successful', concert_name=concert_name)


from django.shortcuts import render, redirect

from django.shortcuts import render, redirect


def submit_booking(request):
    if request.method == 'POST':
        concert_name = request.POST.get('concert_name')
        tickets = request.POST.get('tickets')
        payment_method = request.POST.get('payment_method')

        # Simulate payment validation and booking success
        if payment_method and concert_name and tickets:
            # Example: Save booking data to the database (not implemented here)
            return redirect('booking_successful', concert_name=concert_name)

    # If something is missing, redirect back or show an error
    return redirect('concert_list')
def my_bookings(request):
    # You can replace this with real booking data from the database.
    bookings = [
        {'concert_name': 'Rock Symphony', 'date': 'March 18, 2025', 'tickets': 2},
        {'concert_name': 'Jazz & Blues Evening', 'date': 'May 22, 2025', 'tickets': 3},
    ]

    return render(request, 'my_bookings.html', {'bookings': bookings})

def contact_us(request):
    return render(request, 'contact_us.html')
def pay(request):
    if request.method == 'POST':
        concert_name = request.POST.get('concert_name')
        tickets = request.POST.get('tickets')
        payment_method = request.POST.get('payment_method')
        ticket_price = request.POST.get('ticket_price')

        try:
            # Validate ticket_price and calculate total price
            ticket_price = float(ticket_price) if ticket_price else 0.0
            tickets = int(tickets)
            total_price = tickets * ticket_price

            # Pass data to the payment page
            context = {
                'concert_name': concert_name,
                'tickets': tickets,
                'total_price': total_price,
                'payment_method': payment_method,
            }
            return render(request, 'pay.html', context)

        except ValueError:
            # Handle errors for missing or invalid data
            messages.error(request, 'Invalid data received. Please try again.')
            return redirect('concert_list')

    return redirect('concert_list')  # Fallback for GET requests
def confirm_mpesa(request):
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        concert_name = request.POST.get('concert_name')

        # Simulate validation of the transaction ID
        if transaction_id and transaction_id.startswith('MP'):
            # Example: Assume the Mpesa transaction ID is valid
            messages.success(request, f'Payment for {concert_name} was successful!')
            return redirect('booking_successful', concert_name=concert_name)
        else:
            messages.error(request, 'Invalid Mpesa Transaction ID. Please try again.')
            return redirect('pay')  # Redirect back to payment page if invalid

    return redirect('concert_list')  # Fallback in case of GET request

def process_payment(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')
        concert_name = request.POST.get('concert_name')

        # Simulate card payment processing
        if card_number and expiry and cvv:
            # Example: Assume payment succeeds if card details are filled
            messages.success(request, f'Payment for {concert_name} was successful!')
            return redirect('booking_successful', concert_name=concert_name)
        else:
            messages.error(request, 'Invalid card details. Please try again.')
            return redirect('pay')  # Redirect back to payment page if invalid

    return redirect('concert_list')  # Fallback in case of GET request

def submit_refund(request):
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        refund_reason = request.POST.get('refund_reason')

        # Simulate refund processing
        if transaction_id and refund_reason:
            # Example logic: check if the transaction ID is valid
            if transaction_id.startswith('MP') or len(transaction_id) > 5:  # Example check
                messages.success(request, 'Your refund request has been submitted successfully.')
                # Add logic to process the refund in the system (e.g., flag transaction for refund)
                return redirect('concert_list')
            else:
                messages.error(request, 'Invalid transaction ID. Please try again.')
                return redirect('booking_successful', concert_name="Concert Name")

    # Fallback for GET request
    messages.error(request, 'Refund request failed. Please contact support.')
    return redirect('concert_list')
from django.shortcuts import render

def payment_view(request):
    return render(request, 'payment_page.html')
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test_view(request):
    return HttpResponse('CSRF validation bypassed for debugging.')









