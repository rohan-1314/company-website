import smtplib, ssl


def send_email(message):
    password = 'tycioonycqrosntr'
    username = 'rohan.vagadiya14@gmail.com'
    host = 'smtp.gmail.com'
    port = 465
    reciever = 'rohan.vagadiya14@gmail.com'
    context = ssl.create_default_context()

    # we did context=context because the func has multiple args and context
    # comes later and host, port are 1st,2nd, so they are in order
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
