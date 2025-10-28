# What is the right AWS certificate service for my

needs?

AWS offers two options to customers deploying managed X.509 certificates. Choose
the best one for your needs.

1. **AWS Certificate Manager (ACM)**—This service is for
   enterprise customers who need a secure web presence using TLS. ACM
   certificates are deployed through Elastic Load Balancing, Amazon CloudFront, Amazon API Gateway, and other
   [integrated AWS services](acm-services.md "acm-services.md"). The most
   common application of this kind is a secure public website with significant
   traffic requirements. ACM also simplifies security management by automating
   the renewal of expiring certificates. _You are in the
   right place for this service._
2. **AWS Private CA**—This service is for
   enterprise customers building a public key infrastructure (PKI) inside the AWS
   cloud and intended for private use within an organization. With AWS Private CA, you
   can create your own certificate authority (CA) hierarchy and issue certificates
   with it for authenticating users, computers, applications, services, servers,
   and other devices. Certificates issued by a private CA cannot be used on the
   internet. For more information, see the [AWS Private CA User Guide](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md").
