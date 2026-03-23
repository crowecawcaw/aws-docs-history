# [AG.SAD.7] Implement rotation policies for secrets, keys, and certificates

**Category:** RECOMMENDED

Regular rotation of secrets, keys, and certificates is a best
practice in securing access, limiting the potential damage
that can occur should these security resources become
compromised. In a DevOps environment, pipelines often require
access to sensitive environments and workloads, making them
potential targets for attacks. The routine rotation of these
resources that are used by pipelines can help to significantly
mitigate this risk.

Establish a policy that clearly defines the lifecycle of these
resources, including their creation, usage, rotation, and
retirement intervals. Enforce these policies by automatically
rotating secrets and keys to reduce the risk of oversights,
delays, and human error.

Certificates play an important role in service-to-service
authentication and providing encryption for both internal and
external facing workloads and environments. When managing
certificates, consider not only those issued within your
organization but also those imported from external sources
which may not be automatically renewable.

Monitoring systems that track the lifespan of these assets and
alert administrators as they near expiration can contribute to
this process. This approach can help prevent service
disruptions caused by expired certificates and, in some cases,
can trigger automated renewal procedures.

**Related information:**

- [Blog: How
  to monitor expirations of imported certificates in AWS Certificate Manager (ACM)](https://aws.amazon.com/blogs/security/how-to-monitor-expirations-of-imported-certificates-in-aws-certificate-manager-acm/ "https://aws.amazon.com/blogs/security/how-to-monitor-expirations-of-imported-certificates-in-aws-certificate-manager-acm/")
- [Rotate
  AWS Secrets Manager secrets - AWS Secrets Manager](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md")
- [Managing
  access keys for IAM users - AWS IAM](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md")
- [Rotating
  AWS KMS keys - AWS Key Management Service](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md")
