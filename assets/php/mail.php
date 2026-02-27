<?php
// JSON 응답을 위한 헤더 설정
header('Content-Type: application/json; charset=UTF-8');

// 입학상담 폼 이메일 설정
$to = 'belluna15@naver.com';
$subject_prefix = '[북두칠성학원] 입학상담 문의';

// 폼 데이터 수신 및 보안 처리
$name = isset($_POST['name']) ? htmlspecialchars(trim($_POST['name']), ENT_QUOTES, 'UTF-8') : '';
$email = isset($_POST['email']) ? filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL) : '';
$phone = isset($_POST['phone']) ? htmlspecialchars(trim($_POST['phone']), ENT_QUOTES, 'UTF-8') : '';
$subject = isset($_POST['subject']) ? htmlspecialchars(trim($_POST['subject']), ENT_QUOTES, 'UTF-8') : '';
$message = isset($_POST['message']) ? htmlspecialchars(trim($_POST['message']), ENT_QUOTES, 'UTF-8') : '';

// 필수 필드 검증
if (empty($name) || empty($email) || empty($phone) || empty($subject) || empty($message)) {
    echo json_encode(['success' => false, 'message' => '모든 필드를 입력해주세요.']);
    exit;
}

// 이메일 형식 검증
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo json_encode(['success' => false, 'message' => '올바른 이메일 주소를 입력해주세요.']);
    exit;
}

// 이메일 헤더 설정
$headers = "From: " . $email . "\r\n";
$headers .= "Reply-To: " . $email . "\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

// 문의 유형 한글 변환
$subject_korean = '';
switch($subject) {
    case 'course':
        $subject_korean = '강의 문의';
        break;
    case 'admission':
        $subject_korean = '입학 문의';
        break;
    case 'other':
        $subject_korean = '기타 문의';
        break;
    default:
        $subject_korean = $subject;
}

// 이메일 본문 구성
$body = "=== 입학상담 문의 ===\n\n";
$body .= "이름: " . $name . "\n";
$body .= "이메일: " . $email . "\n";
$body .= "전화번호: " . $phone . "\n";
$body .= "문의 유형: " . $subject_korean . "\n\n";
$body .= "메시지:\n" . $message . "\n";

// 이메일 제목 설정
$email_subject = $subject_prefix . " - " . $subject;

// 이메일 전송
$send = mail($to, $email_subject, $body, $headers);

// 결과 반환
if ($send) {
    echo json_encode(['success' => true, 'message' => '문의가 성공적으로 전송되었습니다. 빠른 시일 내에 답변드리겠습니다.']);
} else {
    echo json_encode(['success' => false, 'message' => '문의 전송에 실패했습니다. 다시 시도해주세요.']);
}
?>