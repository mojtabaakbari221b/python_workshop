from configs import SMS_FROM, SMS_API_KEY, NUMBERS
from sms_ir import SmsIr

mes = """به دوره پایتون از صفر تا هفتاد دانشگاه نوشیروانی خوش اومدید :)
اطلاع رسانی و ارتباط با مربی و سایر شرکت کنندگان دوره، از طریق کانال پیام رسان بله انجام میشه :)\n
لینک عضویت در بله: 
@nit_python_workshop
"""


sms_ir = SmsIr(
    SMS_API_KEY,
    SMS_FROM,
)


s = sms_ir.send_bulk_sms(
    NUMBERS,
    mes,
)

print(s.status_code)
if s.status_code == 200 :
    print(s.json())
else :
    print('Exception Raised :(')


