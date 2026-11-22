

# SEC09-BP01 Implement secure key and certificate management

 Digital certificates and their private keys establish trust in network communications and prove the identity of services, devices, and users. Proper certificate management means that you provision, distribute, renew, and revoke certificates without exposing private key material or letting certificates lapse. Automate these tasks, as manual certificate handling can cause security incidents. 

 **Desired outcome:** 
+  You have a certificate management system that provisions, deploys, stores, renews, and revokes certificates across a public key infrastructure (PKI). 
+  Your certificate private keys are protected from disclosure and are never accessible to human identities. 
+  Your certificates renew automatically before expiration, which helps prevent service disruption caused by expired certificates. 
+  Your certificate management integrates with the services that need TLS certificates for secure communication and machine identity. 

 **Common anti-patterns:** 
+  Teams perform manual steps during certificate deployment or renewal. 
+  Teams build a private certificate authority without planning the certificate authority (CA) hierarchy. 
+  Public resources use self-signed certificates. 
+  Teams store certificate private keys in insecure locations or share them through insecure channels. 
+  Certificate expiration dates go unmonitored, which leads to unexpected downtime. 

 **Benefits of establishing this best practice:** 
+  Automated deployment and renewal reduce operational effort and remove the manual steps where most certificate failures start. 
+  Encryption of data in transit becomes the default, because valid certificates are readily available. 
+  Certificate actions taken by the CA are auditable, which increases security and traceability. 
+  Separating CA responsibilities across hierarchy layers isolates duties and limits the impact of unauthorized access. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Certificates follow a lifecycle where a certificate authority (CA) issues them, systems deploy them, and they expire on a fixed date unless something renews them. An unrenewed certificate can take a service offline until someone notices and reissues it. A private key copied to a shared location or handled by a person might let an unauthorized party impersonate the service. Automated provisioning and renewal remove the manual steps where these kinds of failures originate. 

 The trust model determines which kind of certificate to issue. Public-facing endpoints need publicly trusted certificates, because browsers and operating systems already trust the issuing CA. Internal services can use certificates from a private CA that you operate, which gives you control over the trust chain, certificate contents, and validity periods. Publicly trusted certificates are simpler to run but bound by public CA rules. A private CA gives you flexibility for short-lived certificates or non-TLS uses, at the cost of operating the CA yourself. 

 AWS provides two general-purpose PKI services. [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) provisions, deploys, and renews certificates. It [integrates](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html) with many AWS services so certificates reach load balancers and endpoints without manual handling. ACM issues publicly trusted certificates from [Amazon Trust Services](https://www.amazontrust.com/repository/) and private certificates through [AWS Private Certificate Authority (AWS Private CA)](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html). With AWS Private CA, you can run your own root or subordinate CA and issue certificates through an API, including certificates for Kubernetes pods, code signing, and other uses through a [custom template](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html). For workloads outside AWS, [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) uses X.509 certificates from your private CA to grant temporary credentials. For devices at scale, [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) provides mechanisms for onboarding devices into your PKI. Services such as [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) and [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) consume certificates directly to secure application connections. 

 A private CA is a hierarchy. A root CA sits at the top, signs some intermediate CA certificates, then stays out of day-to-day issuance. Intermediate CAs sign the end-entity certificates that your services and devices present. This structure limits exposure, because if an intermediate CA is affected, you can revoke it without replacing the root and everything beneath it. We recommend deploying each level into a separate account so the impact of unauthorized access stays small and CA activity is easier to isolate in audit logs. Plan the hierarchy before you issue any certificates, as restructuring a live CA is disruptive. 

 Certificate and key algorithms change over time. Use certificates that a service issues and renews for you, and remove self-signed certificates and any certificate that never expires, because both must be replaced manually when an algorithm or validity rule changes. With ACM, AWS Private CA, AWS KMS, and AWS Secrets Manager, you can change algorithms and rotate key material without redesigning the workload. This crypto agility looks more like making configuration changes than performing costly migrations or deprecations. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select the certificate services for your use case:** Use [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) for publicly trusted certificates on web servers, load balancers, and other public endpoints. Choose [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) when you need your own CA hierarchy or exportable certificates, then issue [end-entity certificates](https://docs.aws.amazon.com/privateca/latest/userguide/PcaIssueCert.html) through ACM. For embedded devices provisioned at scale, use [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html). For mutual TLS at the edge of your services, use native support in [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) or [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html). 

1.  **Design your CA hierarchy and account layout:** Place the root CA in a dedicated account used only to issue intermediate CA certificates. Create intermediate CAs in separate accounts to issue certificates to your services, users, and devices. For resiliency, cross-Region replication, and cross-account sharing decisions, follow [Planning your AWS Private CA deployment](https://docs.aws.amazon.com/privateca/latest/userguide/PcaPlanning.html). 

1.  **Automate certificate renewal:** ACM provides [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html) for the certificates it issues and for the integrated services that use them, so certificates rotate before expiration without manual action. Not all certificates qualify for managed renewal, including imported certificates, so you may need custom automation so those rotate on the same schedule. 

1.  **Establish logging and audit trails:** Confirm the accounts that hold your certificate authorities are covered by a CloudTrail trail with [log file integrity validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html), and set retention to match your organization's compliance policies. Generate and review [audit reports](https://docs.aws.amazon.com/privateca/latest/userguide/PcaAuditReport.html) that list issued and revoked certificates on a regular cadence. 

1.  **Configure certificate revocation:** Provision storage for the certificate revocation list (CRL) so clients can check whether a certificate is still valid. See [Planning a certificate revocation list (CRL)](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html) to configure the CRL based on your requirements. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC09-BP02 Enforce encryption in transit](sec09-bp02.md) 
+  [SEC09-BP03 Authenticate network communications](sec09-bp03.md) 
+  [SEC08-BP01 Implement secure key management](sec08-bp01.md) 
+  [SEC02-BP02 Use temporary credentials](sec02-bp02.md) 

 **Related documents:** 
+  [Private CA best practices](https://docs.aws.amazon.com/privateca/latest/userguide/ca-best-practices.html) 
+  [How to host and manage an entire private certificate infrastructure in AWS](https://aws.amazon.com/blogs/security/how-to-host-and-manage-an-entire-private-certificate-infrastructure-in-aws/) 
+  [How to secure an enterprise scale ACM Private CA hierarchy for automotive and manufacturing](https://aws.amazon.com/blogs/security/how-to-secure-an-enterprise-scale-acm-private-ca-hierarchy-for-automotive-and-manufacturing/) 
+  [How to use AWS RAM to share your ACM Private CA cross-account](https://aws.amazon.com/blogs/security/how-to-use-aws-ram-to-share-your-acm-private-ca-cross-account/) 

 **Related videos:** 
+  [AWS Security Innovations and AI Integration (re:Inforce 2024)](https://aws.amazon.com/video/watch/b4236060453/) 

 **Related tools:** 
+  [Kubernetes cert-manager plugin for AWS Private CA](https://github.com/cert-manager/aws-privateca-issuer) 

 **Related workshops:** 
+  [Private CA workshop](https://catalog.workshops.aws/certificatemanager/en-US/introduction) 