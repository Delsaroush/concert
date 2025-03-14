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

def book_ticket(request, concert_id):
    # Get the concert object or return a 404 error if not found
    concert = get_object_or_404(Concert, id=concert_id)

    if request.method == 'POST':
        # Handle POST request (form submission)
        purchaser_name = request.POST.get('purchaser_name')
        payment_details = request.POST.get('payment_details')

        # Check if tickets are available
        if concert.available_tickets > 0:
            concert.available_tickets -= 1
            concert.save()
            # Optionally process payment details here
            return redirect('success_page')  # Redirect to success page
        else:
            # If no tickets are available, render the form with an error
            return render(request, 'book_ticket.html', {
                'concert': concert,
                'error': 'No tickets available!',
            })

    # Render the form for a GET request
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
    return render(request, 'success.html')










