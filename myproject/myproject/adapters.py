from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def authentication_error(self, request, provider_id, error=None, **kwargs):
        # 로그인 취소 시 메인 페이지로 리디렉트
        return redirect('/')