from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .currency import create_currency_plot
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def generate_graph(request):
    if request.method == 'POST':
        # Extract parameters from the POST request
        selected_currency = request.POST.get('currency')
        time_interval = request.POST.get('time_interval')

        graph_html = create_currency_plot(selected_currency, time_interval)
        # Return the HTML content as JSON
        return render(request, "index.html", context={'graph_html': graph_html})

    # If the request method is not POST, return an empty response
    return JsonResponse({"graph_html" : graph_html})

def index(request):
    return render(request, 'index.html')