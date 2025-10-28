# Create an ACM certificate

By default, RES hosts the web portal under an application load balancer using the
domain amazonaws.com. To use your own domain, you will need to configure a public SSL/TLS
certificate provided by you or requested from AWS Certificate Manager (ACM). If you use ACM, you will
receive an AWS resource name you will need to provide as a parameter to encrypt the SSL/TLS
channel between the client and web services host.

###### Tip

If you are deploying the external resources demo package, you will need to enter your
chosen domain in `PortalDomainName` when deploying the external resources stack in
[Create external resources](create-external-resources.md "create-external-resources.md").

###### To create a certificate for custom domains:

1. From the console, open [AWS Certificate Manager](https://console.aws.amazon.com/acm/home#/certificates/request "https://console.aws.amazon.com/acm/home#/certificates/request") to request a public certificate. If you are deploying in a
   GovCloud Region, create the certificate in your GovCloud partition account.
2. Choose **Request a public certificate**, and choose
   **Next**.
3. Under **Domain names**, request a certificate for both
   `*.PortalDomainName` and `PortalDomainName`.
4. Under **Validation method**, choose **DNS
   validation**.
5. Choose **Request**.
6. From the **Certificates** list, open your requested certificates.
   Each certificate will have **Pending validation** as the status.

###### Note

If you do not see your certificates, refresh the list. 7. Do one of the following:

    * **Commercial deployment:**


    From the **Certificate details** for each requested certificate,
     choose **Create records in Route 53**. The status of the certificate
     should change to **Issued**.
    * **GovCloud deployment:**


    If you are deploying in a GovCloud region, copy the CNAME key and value.
     From the commercial partition account, use the values to create a new record
     in the Public Hosted Zone. The status of the certificate should change to
     **Issued**.

8. Copy the new certificate ARN to input as the parameter for
   `ACMCertificateARNforWebApp`.
