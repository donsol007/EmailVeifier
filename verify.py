import re
import dns.resolver
import socket
import smtplib

#Email address to verify is store in the array email_address
email_address = ['me@example2231.com','info@yabarconsult.com','john@google.com','contact@microsoft.com', 'dex@dons0125ol.com']
def validate_email(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if (match !=None):
        return email

def check_email(email):
    try:
    # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        # SMTP Conversation
        host = email.split('@')[1]
        server.connect(mxRecord)
        server.helo(host)
        server.mail('change_me_to_email address that can send message')
        code, message = server.rcpt(str(email))
        server.quit()
        # Assume 250 as Success
        if code == 250:
            return email
    except:
        pass

for email in email_address:
    try:
        validated_email = validate_email(email)
        domain = validated_email.split('@')[1]
        result = dns.resolver.resolve(domain, 'MX')
        mxRecord = result[0].exchange
        mxRecord = str(mxRecord)
        #print(mxRecord)
        print(check_email(validated_email))
    except:
        pass