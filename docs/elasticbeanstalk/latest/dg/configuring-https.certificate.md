# Server certificates

This topic describes the different types of certificates you can use to configure HTTPS and when to apply each. The subtopics
in this section provide instructions to create your own certificate and how to upload it.

###### AWS Certificate Manager (ACM)

ACM is the preferred tool to provision, manage, and deploy your server certificates. You can do so programmatically or using the AWS CLI. With ACM
you can create a trusted certificate for your domain names for free.

ACM certificates can only be used with AWS load balancers and Amazon CloudFront distributions, and ACM is available only in certain AWS Regions. To
use an ACM certificate with Elastic Beanstalk, see [Configuring HTTPS Termination at the load balancer](configuring-https-elb.md "configuring-https-elb.md"). For more information about ACM
see the [_AWS Certificate Manager User Guide_](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md").

###### Note

For a list of regions where ACM is available, see [ACM endpoints and quotas](../../../general/latest/gr/acm.md "../../../general/latest/gr/acm.md")
in the _Amazon Web Services General Reference_.

If ACM is not available in your AWS Region, you can upload a third-party or self-signed certificate and private key to AWS Identity and Access Management (IAM). You can
use the AWS CLI to upload the certificate. Certificates stored in IAM can be used with load balancers and CloudFront distributions. For more information, see
[Upload a certificate to IAM](configuring-https-ssl-upload.md "configuring-https-ssl-upload.md").

###### Third party certificate

If ACM is not available in your region, you can purchase a trusted certificate from a third party. A third-party certificate can be used to
decrypt HTTPS traffic at your load balancer, on the backend instances, or both.

###### Self-signed certificate

For development and testing, you can [create and sign a certificate](configuring-https-ssl.md "configuring-https-ssl.md") yourself with open source tools.
Self-signed certificates are free and easy to create, but cannot be used for front-end decryption on public sites. If you attempt to use a self-signed
certificate for an HTTPS connection to a client, the user's browser displays an error message indicating that your web site is unsafe. You can, however,
use a self-signed certificate to secure backend connections without issue.
