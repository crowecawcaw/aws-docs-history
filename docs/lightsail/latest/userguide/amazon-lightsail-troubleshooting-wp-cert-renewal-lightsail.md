

# Certificate did not automatically renew
<a name="amazon-lightsail-troubleshooting-wp-cert-renewal-lightsail"></a>

Lightsail Setup configures automatic renewal of your Let's Encrypt SSL/TLS certificate. If your website displays a security or certificate error, your certificate might not have renewed automatically.

**Important**  
If your certificate was issued before August 9, 2026, your certificate will not renew automatically. Restart Lightsail Setup (Option 1) to renew your certificate and restore automatic renewal. You can find when your certificate was issued on your WordPress instance's **Connect** tab.  

![Certificate issue date displayed on the Connect tab in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup-cert-issue-date.png)


The following image shows an example of a certificate error in Chrome (this might vary for different browsers).

![SSL certificate error displayed in a web browser.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup-cert-error.png)


## Option 1: Restart Lightsail Setup (Recommended)
<a name="cert-renewal-rerun-lightsail-setup"></a>

Restart Lightsail Setup with the same domain and DNS configuration as your previous setup. This regenerates your certificate and restores automatic renewal. To restart Lightsail Setup, complete the following steps:

1. Open the Lightsail console at [https://lightsail.aws.amazon.com/](https://lightsail.aws.amazon.com/).

1. Choose your WordPress instance from the instance list.

1. Choose the **Connect** tab and choose **Restart setup**.  
![The Restart setup button on the Connect tab in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup-restart.png)

1. Complete the setup using the same domain and DNS configuration as your previous setup.

After Lightsail Setup completes, your certificate is renewed and automatic renewal is restored.

## Option 2: Renew your certificate manually
<a name="cert-renewal-manual-troubleshooting-lightsail"></a>

### Step 1: Check if your certificate has expired
<a name="cert-renewal-check-expired-lightsail"></a>

Connect to your instance by using the Lightsail [browser-based SSH client](lightsail-how-to-connect-to-your-instance-virtual-private-server.md).

Run the following command to check the certificate status:

```
$ sudo certbot certificates
```

If the expiry date shown in the output is in the past, your certificate has expired and automatic renewal has failed. Continue to Step 2.

### Step 2: Re-enable automatic renewal
<a name="cert-renewal-reenable-lightsail"></a>

The Lightsail blueprint uses a systemd timer to automatically renew the certificate. If this timer is inactive or disabled, the certificate will not renew automatically.

Run the following command to check the status of the renewal timer:

```
$ sudo systemctl status certbot-renew.timer
```

If the timer is active, you should see output similar to the following:

![Output of the certbot-renew.timer status command showing the timer is active.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/wp-cert-renewal-timer-status.png)


If the timer is not active or the command returns an error, run the following command to re-enable it:

```
$ sudo systemctl enable --now certbot-renew.timer
```

Re-enabling the timer restores automatic renewal for future renewals, but does not renew the certificate immediately. If your certificate has already expired, continue to Step 3.

### Step 3: Manually renew the expired certificate
<a name="cert-renewal-manual-lightsail"></a>

Run the following commands to stop the web server, force a certificate renewal, and restart the web server:

```
$ sudo systemctl stop apache2
```

```
$ sudo certbot renew --force-renewal
```

```
$ sudo systemctl restart apache2
```