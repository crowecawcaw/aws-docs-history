# Replace the SSL certificate for your Classic Load Balancer

If you have an HTTPS listener, you deployed an SSL server certificate on your load
balancer when you created the listener. Each certificate comes with a validity period.
You must ensure that you renew or replace the certificate before its validity period
ends.

Certificates provided by AWS Certificate Manager and deployed on your load balancer can be renewed
automatically. ACM attempts to renew certificates before they expire. For more
information, see [Managed renewal](../../../acm/latest/userguide/managed-renewal.md "../../../acm/latest/userguide/managed-renewal.md") in
the _AWS Certificate Manager User Guide_. If you imported a certificate into ACM, you
must monitor the expiration date of the certificate and renew it before it expires. For
more information, see [Importing
certificates](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md") in the _AWS Certificate Manager User Guide_. After a certificate
that is deployed on a load balancer is renewed, new requests use the renewed
certificate.

To replace a certificate, you must first create a new certificate by following the
same steps that you used when you created the current certificate. Then, you can replace
the certificate. After a certificate that is deployed on a load balancer is replaced,
new requests use the new certificate.

Note that renewing or replacing a certificate does not affect requests that were
already received by a load balancer node and are pending routing to a healthy
target.

###### Contents

- [Replace the SSL certificate using the
  console](#us-update-lb-SSLcert-console "#us-update-lb-SSLcert-console")
- [Replace the SSL certificate using the
  AWS CLI](#us-update-lb-SSLcert-cli "#us-update-lb-SSLcert-cli")

## Replace the SSL certificate using the

console

You can replace the certificate deployed on your load balancer with a certificate
provided by ACM or a certificate uploaded to IAM.

###### To replace the SSL certificate for an HTTPS load balancer using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners** tab, choose **Manage listeners**.
5. On the **Manage listeners** page, locate the listener to be updated, choose **Edit** under **Default SSL cert** and do one of the
   following:
   - If you created or imported a certificate using AWS Certificate Manager, choose
     **From ACM**, select the certificate from
     the list, and then choose
     **Save changes**.

   ###### Note

   This option is available only in Regions that support
   AWS Certificate Manager.
   - If you imported a certificate using IAM, choose **From IAM**,
     select the certificate from from the list, and
     then choose **Save changes**.
   - If you have an SSL certificate to import to ACM, select **Import**
     and **To ACM**. In **Certificate private key**, copy and paste
     the contents of the PEM-encoded private key file. In
     **Certificate body**, copy and paste the
     contents of the PEM-encoded public key certificate file. In
     **Certificate chain - optional**, copy and paste the
     contents of the PEM-encoded certificate chain file, unless you are
     using a self-signed certificate and it's not important that browsers
     implicitly accept the certificate.
   - If you have an SSL certificate to import but ACM is not
     supported in this Region, select **Import** and **To IAM**.
     In **Certificate name** type the name of
     the certificate. In **Certificate private key**, copy and paste
     the contents of the PEM-encoded private key file. In
     **Certificate body**, copy and paste the
     contents of the PEM-encoded public key certificate file. In
     **Certificate chain - optional**, copy and paste the
     contents of the PEM-encoded certificate chain file, unless you are
     using a self-signed certificate and it's not important that browsers
     implicitly accept the certificate.
   - Choose **Save changes**.

## Replace the SSL certificate using the

AWS CLI

You can replace the certificate deployed on your load balancer with a certificate
provided by ACM or a certificate uploaded to IAM.

###### To replace an SSL certificate with a certificate provided by ACM

1. Use the following [request-certificate](../../../cli/latest/reference/acm/request-certificate.md "../../../cli/latest/reference/acm/request-certificate.md") command to request a new
   certificate:

```
`aws acm request-certificate --domain-name `www.example.com``
```

2. Use the following [set-load-balancer-listener-ssl-certificate](../../../cli/latest/reference/elb/set-load-balancer-listener-ssl-certificate.md "../../../cli/latest/reference/elb/set-load-balancer-listener-ssl-certificate.md") command to set the
   certificate:

```
`**aws elb** set-load-balancer-listener-ssl-certificate --load-balancer-name `my-load-balancer` --load-balancer-port 443 --ssl-certificate-id arn:aws:acm:`region`:`123456789012`:certificate/`12345678-1234-1234-1234-123456789012``
```

###### To replace an SSL certificate with a certificate uploaded to IAM

1. If you have an SSL certificate but have not uploaded it, see [Uploading a server certificate](../../../IAM/latest/UserGuide/id_credentials_server-certs.md#upload-server-certificate "../../../IAM/latest/UserGuide/id_credentials_server-certs.md#upload-server-certificate") in the
   _IAM User Guide_.
2. Use the following [get-server-certificate](../../../cli/latest/reference/iam/get-server-certificate.md "../../../cli/latest/reference/iam/get-server-certificate.md") command to get the ARN of the
   certificate:

```
`aws iam get-server-certificate --server-certificate-name `my-new-certificate``
```

3. Use the following [set-load-balancer-listener-ssl-certificate](../../../cli/latest/reference/elb/set-load-balancer-listener-ssl-certificate.md "../../../cli/latest/reference/elb/set-load-balancer-listener-ssl-certificate.md") command to set the
   certificate:

```
`aws elb set-load-balancer-listener-ssl-certificate --load-balancer-name `my-load-balancer` --load-balancer-port 443 --ssl-certificate-id arn:aws:iam::`123456789012`:server-certificate/`my-new-certificate``
```
