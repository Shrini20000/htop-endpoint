from django.http import HttpResponse
import datetime
import pytz
import subprocess
import os

def get_top_output():
    try:
        cmd = "ps aux | head -n 15"
        result = subprocess.check_output(cmd, shell=True).decode()
        return result
    except Exception as e:
        return str(e)

def htop_view(request):
    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Get system username
    username = os.getlogin()
    
    # Get top output
    top_data = get_top_output()
    
    # Create HTML response
    html_response = f"""
    <html>
    <body style="font-family: monospace; white-space: pre;">
Name: {os.getenv('FULL_NAME', 'Set FULL_NAME environment variable')}
user: {username}
Server Time (IST): {current_time}
TOP output:
{top_data}
    </body>
    </html>
    """
    return HttpResponse(html_response)