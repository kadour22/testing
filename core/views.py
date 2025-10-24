from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

def index(request):
    return render(request, "index.html")


class index_api_view(APIView) :
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request):
        book = {"title":"arch linux"}
        return Response(book)