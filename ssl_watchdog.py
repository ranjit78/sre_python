#!/usr/bin/env python3
import socket
import ssl
import datetime


def check_ssl_expiry(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()

    # Parse the expiration string from the certificate
    expire_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    days_left = (expire_date - datetime.datetime.utcnow()).days

    print(f"Host: {hostname} | Days Remaining: {days_left}")
    if days_left < 14:
        print("🚨 WARNING: Certificate expiring soon!")


# Quick triage check
check_ssl_expiry("example.com")
