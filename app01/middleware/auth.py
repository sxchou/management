from django.shortcuts import render, redirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info in ["/login/", "/image/code/"]:
            return
        session_info = request.session.get('info')
        if session_info:
            return
        return redirect('/login/')
