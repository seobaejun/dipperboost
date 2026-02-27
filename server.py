#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
북두칠성학원 입학상담 폼 서버
Python Flask를 사용한 이메일 전송 서버
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

app = Flask(__name__)
CORS(app)  # CORS 허용

# 이메일 설정
SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'belluna15@naver.com'  # 발신 이메일
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')  # 환경변수에서 비밀번호 가져오기
RECIPIENT_EMAIL = 'belluna15@naver.com'  # 수신 이메일

# 문의 유형 한글 변환
SUBJECT_MAP = {
    'course': '강의 문의',
    'admission': '입학 문의',
    'other': '기타 문의'
}

from flask import send_from_directory

@app.route('/assets/php/mail.php', methods=['POST', 'OPTIONS'])
def send_mail():
    """입학상담 폼 이메일 전송"""
    print(f"\n{'='*50}")
    print(f"요청 수신: {request.method}")
    print(f"Content-Type: {request.content_type}")
    print(f"Is JSON: {request.is_json}")
    print(f"{'='*50}\n")
    
    # CORS preflight 요청 처리
    if request.method == 'OPTIONS':
        print("OPTIONS 요청 처리")
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
    
    try:
        # 폼 데이터 수신
        if request.is_json:
            data = request.get_json()
            print(f"JSON 데이터 수신: {data}")
        else:
            data = request.form
            print(f"Form 데이터 수신: {dict(data)}")
        
        data = data if data else {}
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        # 필수 필드 검증
        if not all([name, email, phone, subject, message]):
            return jsonify({
                'success': False,
                'message': '모든 필드를 입력해주세요.'
            }), 400
        
        # 이메일 형식 검증
        if '@' not in email or '.' not in email:
            return jsonify({
                'success': False,
                'message': '올바른 이메일 주소를 입력해주세요.'
            }), 400
        
        # 문의 유형 한글 변환
        subject_korean = SUBJECT_MAP.get(subject, subject)
        
        # 이메일 본문 구성
        email_body = f"""=== 입학상담 문의 ===

이름: {name}
이메일: {email}
전화번호: {phone}
문의 유형: {subject_korean}

메시지:
{message}
"""
        
        # 이메일 제목
        email_subject = f'[북두칠성학원] 입학상담 문의 - {subject_korean}'
        
        # 이메일 전송 (SMTP 사용)
        if EMAIL_PASSWORD:
            # SMTP를 통한 실제 이메일 전송
            msg = MIMEText(email_body, 'plain', 'utf-8')
            msg['Subject'] = Header(email_subject, 'utf-8')
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = RECIPIENT_EMAIL
            msg['Reply-To'] = email
            
            try:
                server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
                server.quit()
                
                return jsonify({
                    'success': True,
                    'message': '문의가 성공적으로 전송되었습니다. 빠른 시일 내에 답변드리겠습니다.'
                })
            except Exception as e:
                print(f"이메일 전송 오류: {str(e)}")
                # 이메일 전송 실패 시에도 성공으로 처리 (개발 환경)
                return jsonify({
                    'success': True,
                    'message': '문의가 접수되었습니다. (개발 모드: 이메일 전송 설정 필요)'
                })
        else:
            # 이메일 비밀번호가 설정되지 않은 경우 (개발 모드)
            print("=" * 50)
            print("입학상담 문의 접수")
            print("=" * 50)
            print(email_body)
            print("=" * 50)
            
            return jsonify({
                'success': True,
                'message': '문의가 접수되었습니다. (개발 모드: 콘솔에 출력됨)'
            })
            
    except Exception as e:
        print(f"서버 오류: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'서버 오류가 발생했습니다: {str(e)}'
        }), 500

@app.after_request
def add_no_cache_headers(response):
    """모든 응답에 캐시 비활성화 헤더 추가"""
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def index():
    """메인 페이지"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """정적 파일 서빙"""
    return send_from_directory('.', path)

if __name__ == '__main__':
    print("=" * 50)
    print("북두칠성학원 개발 서버 시작")
    print("=" * 50)
    print("서버 주소: http://localhost:8000")
    print("=" * 50)
    app.run(host='0.0.0.0', port=8000, debug=True)

