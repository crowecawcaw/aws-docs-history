# Use AMS SSP to provision AWS Certificate Manager in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Certificate Manager (ACM) capabilities directly in your AMS managed account. AWS Certificate Manager is a service that lets you provision, manage, and deploy public and private
Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services
and your internal connected resources. SSL/TLS certificates are used to secure network
communications and establish the identity of websites over the internet as well as resources on
private networks. AWS Certificate Manager removes the time-consuming manual process of purchasing,
uploading, and renewing SSL/TLS certificates.

With AWS Certificate Manager, you can request a certificate, deploy it on ACM-integrated AWS resources,
such as Elastic Load Balancers, Amazon CloudFront distributions, and APIs on API Gateway, and let
AWS Certificate Manager handle certificate renewals. It also enables you to create private certificates for your
internal resources and manage the certificate lifecycle centrally. Public and private certificates
provisioned through AWS Certificate Manager for use with ACM-integrated services are free. You pay only for
the AWS resources you create to run your application. With
[AWS Private Certificate Authority](https://aws.amazon.com/certificate-manager/private-certificate-authority/ "https://aws.amazon.com/certificate-manager/private-certificate-authority/"),
you pay monthly for the operation of the AWS Private CA and for the private certificates you issue. To learn more, see
[AWS Certificate Manager - AWS Documentation](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md").

## ACM in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS Certificate Manager in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM role to your account: `customer_acm_create_role`. You can use this role to
create and manage ACM certificates. After it's provisioned in your account, you must onboard the role in your federation solution.

ACM certificates can be created using the following change types, even if you haven't
added the `customer_acm_create_role` IAM role:

- [ACM | Create Public Certificate](../ctref/deployment-advanced-acm-create-public-certificate.md "../ctref/deployment-advanced-acm-create-public-certificate.md")
- [ACM | Create Private Certificate](../ctref/deployment-advanced-acm-create-private-certificate.md "../ctref/deployment-advanced-acm-create-private-certificate.md")
- [ACM Certificate with additional SANs | Create](../ctref/deployment-advanced-acm-certificate-with-additional-sans-create.md "../ctref/deployment-advanced-acm-certificate-with-additional-sans-create.md")

**Q: What are the restrictions to using the AWS Certificate Manager?**

You must submit a Request for Change (RFC) to AMS to delete or modify existing certificates, as those actions require full admin access (use the
Management | Other | Other | Update change type (ct-0xdawir96cy7k). Note that the IAM policy can't exclude rights based on tag names (mc\*, ams\*, etc).
Certificates do not incur a cost, so deleting unused certificates is not time sensitive.

**Q: What are the prerequisites or dependencies to using Certificate Manager?**

Existing public DNS name, and access to create DNS CNAME records, but those do not need to be hosted in the managed account.
