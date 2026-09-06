

# Choosing how to issue certificates with AWS
<a name="service-options"></a>

AWS offers several ways to issue and manage X.509 certificates. Choose the option that best fits your use case.



|  | **ACM** | **ACM with ACME** | **AWS Private CA (direct issuance)** | 
| --- | --- | --- | --- | 
| Best for | Public or private certificates for AWS integrated services (Elastic Load Balancing, CloudFront, API Gateway) | Public certificates for customer-managed infrastructure (on-premises, Kubernetes, hybrid) | Private certificates where you supply the CSR and manage the private key yourself | 
| Certificate trust | Public (Amazon Trust Services) or private (via AWS Private CA integration) | Public (Amazon Trust Services) | Private (your CA hierarchy) | 
| Private key management | AWS generates and manages the private key (you can export it for use outside AWS) | Your ACME client generates and holds the private key | You generate and hold the private key | 
| Renewal | ACM managed renewal (automatic) | Client-driven (your ACME client renews before expiry) | Manual (you call IssueCertificate again) | 
| Deployment | Bound to AWS integrated services, or exported for use anywhere | Installed on your systems by the ACME client | You install the certificate on your systems | 
| Automation | AWS SDK and CLI | Industry-standard ACME clients (Certbot, cert-manager, acme.sh) | AWS SDK and CLI | 

**AWS Certificate Manager (ACM)**  
Use ACM when you need certificates for AWS integrated services such as Elastic Load Balancing, Amazon CloudFront, and Amazon API Gateway, or when you want AWS to manage the certificate lifecycle including renewal. ACM generates and manages the private key and automates renewal. For workloads outside of AWS integrated services, ACM also supports exportable certificates that let you retrieve the private key and use the certificate on your own infrastructure. ACM can issue public certificates from Amazon Trust Services or private certificates when integrated with AWS Private CA.

**ACM with ACME certificate automation**  
Use ACME when you need publicly trusted certificates for customer-managed infrastructure and want to automate the lifecycle using industry-standard ACME clients (Certbot, cert-manager, acme.sh) rather than AWS APIs. The private key is generated and held by your ACME client and never leaves your systems. Certificates issued through ACME appear in your ACM inventory for central visibility but cannot be bound to AWS integrated services. For more information, see [ACME certificate automation](acm-acme.md).

**AWS Private CA (direct issuance)**  
Use AWS Private CA directly when you need private certificates and want full control over the private key. You create your own CA hierarchy, generate your own private key and CSR, and call `IssueCertificate`. Certificates issued by a private CA are not publicly trusted and cannot be used on the public internet. For more information, see the [AWS Private CA User Guide](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html).

*Both ACM and ACME certificate automation are covered in this guide. You are in the right place.*