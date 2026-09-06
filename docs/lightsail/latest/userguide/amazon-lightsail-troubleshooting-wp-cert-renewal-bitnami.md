

# Certificate did not automatically renew
<a name="amazon-lightsail-troubleshooting-wp-cert-renewal-bitnami"></a>

The WordPress guided workflow configures automatic renewal of your Let's Encrypt SSL/TLS certificate. The Bitnami blueprint uses a cron job that runs a Python script twice daily to check and renew the certificate. If your certificate expires despite automatic renewal being configured, use the following steps to diagnose and resolve the issue.

## Step 1: Check if your certificate has expired
<a name="cert-renewal-check-expired-bitnami"></a>

Connect to your instance by using the Lightsail [browser-based SSH client](lightsail-how-to-connect-to-your-instance-virtual-private-server.md).

Run the following command to check the certificate status:

```
$ sudo /opt/certbot/bin/certbot certificates
```

**Note**  
On Bitnami instances, `certbot` is not in the system PATH. Use the full path `/opt/certbot/bin/certbot`.

If the expiry date shown in the output is in the past, your certificate has expired and automatic renewal has failed. Continue to Step 2.

## Step 2: Re-enable automatic renewal
<a name="cert-renewal-reenable-bitnami"></a>

The Bitnami blueprint uses a cron job that runs a Python script twice daily to check and renew the certificate. If this cron job was removed or stopped, the certificate will not renew automatically.

Run the following command to verify that the renewal cron job exists:

```
$ sudo grep le-cert-renewal /etc/crontab
```

If the cron job is active, you should see output similar to the following:

![Output of the grep le-cert-renewal command showing the cron job is active.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/wp-cert-renewal-cron-status.png)


If no output is returned, the cron job is missing. Run the following command to recreate it:

```
$ sudo sh -c 'echo "0 0,12 * * * root /usr/bin/python3 /opt/bitnami/lightsail/scripts/le-cert-renewal.py WebsiteSetupLECert" >> /etc/crontab'
```

Recreating the cron job restores automatic renewal for future renewals, but does not renew the certificate immediately. If your certificate has already expired, continue to Step 3.

If the cron job exists but renewal still failed, continue to Step 3 to manually renew the certificate.

## Step 3: Manually renew the expired certificate
<a name="cert-renewal-manual-bitnami"></a>

Run the following commands to stop all services, renew the certificate, and restart all services:

```
$ sudo /opt/bitnami/ctlscript.sh stop
```

```
$ sudo /opt/certbot/bin/certbot renew --force-renewal
```

```
$ sudo /opt/bitnami/ctlscript.sh start
```