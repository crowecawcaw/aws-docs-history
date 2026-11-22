

# Certificate lifecycle automation

AWS Certificate Manager (ACM) can renew your certificates and deploy them where you use them. How you automate depends on where the certificate runs.


| Method | Use it when | 
| --- | --- | 
| [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md) | You request a certificate from ACM. ACM issues a new certificate before the current one expires and keeps the same ARN, so you do not track expiration dates or request replacements. | 
| [Managed automation with integrated services](acm-services.md) | An integrated AWS service, such as Elastic Load Balancing or CloudFront, uses the certificate. The service uses each renewed certificate for you. | 
| [ACME certificate automation](acm-acme.md) | You need public certificates on hosts that you manage, and you can run an ACME client such as Certbot or cert-manager. The client requests, renews, and installs the certificates. | 
| [AWS Workload Credentials Provider](acm-certificate-automation.md) | You export ACM certificates to hosts that you manage and cannot use ACME. The provider deploys each renewed certificate to your hosts. | 

**Topics**
+ [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md)
+ [Managed automation with integrated services](acm-services.md)
+ [ACME certificate automation](acm-acme.md)
+ [AWS Workload Credentials Provider](acm-certificate-automation.md)