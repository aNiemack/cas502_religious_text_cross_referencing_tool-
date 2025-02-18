from django.shortcuts import render, HttpResponse
import re


# Create your views here.
def index(request):
    return render(request, "dashboard/index.html")


def search(request):
    print("searching...")
    # Mock loading in the text here just as we would on initial page load
    # shorten to make testing easier
    text = """
          Lorem ipsum odor amet, consectetuer adipiscing elit. Ridiculus sit
          nisl laoreet facilisis aliquet. Potenti dignissim litora eget montes
          rhoncus sapien neque urna. Cursus libero sapien integer magnis ligula
          lobortis quam ut.Lorem ipsum odor amet, consectetuer adipiscing elit.
          Ridiculus sit nisl laoreet facilisis aliquet. Potenti dignissim litora
          eget montes rhoncus sapien neque urna. Cursus libero sapien integer
          magnis ligula lobortis quam ut.Lorem ipsum odor amet, consectetuer
          adipiscing elit. Ridiculus sit nisl laoreet facilisis aliquet. Potenti
          dignissim litora eget montes rhoncus sapien neque urna. Cursus libero
          sapien integer magnis ligula lobortis quam ut."""

    searched = request.GET.get("text-search-1", "")

    
    return HttpResponse(highlight_searched(searched, text))


def highlight_searched(searched, text):
        if searched:
            return re.sub(re.escape(searched), lambda m: f"<mark>{m.group(0)}</mark>", text, flags=re.IGNORECASE)
        else:
             return text
