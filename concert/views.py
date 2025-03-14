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

def book_ticket(request, concert_id):
    concert = get_object_or_404(Concert, id=concert_id)
    if request.method == 'POST':
        purchaser_name = request.POST.get('purchaser_name')
        if concert.available_tickets > 0:
            concert.available_tickets -= 1
            concert.save()
            messages.success(request, 'Ticket successfully booked!')
        else:
            messages.error(request, 'Sorry, no tickets are available.')

        return redirect('concert_list')
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









