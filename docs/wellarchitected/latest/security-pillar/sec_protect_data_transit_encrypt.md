# SEC09-BP02 Enforce encryption in transit

Enforce your defined encryption requirements based on your organization’s policies, regulatory obligations and standards to help meet organizational, legal, and compliance requirements. Only use protocols with encryption when transmitting sensitive data outside of your virtual private cloud (VPC). Encryption helps maintain data confidentiality even when the data transits untrusted networks.

**Desired outcome:** You encrypt
network traffic between your resources and the internet to mitigate
unauthorized access to the data. You encrypt network traffic within
your internal AWS environment according to your security
requirements. You encrypt data in transit using secure TLS protocols
and cipher suites.

**Common anti-patterns:**

- Using deprecated versions of SSL, TLS, and cipher suite components (for example, SSL v3.0, 1024-bit RSA keys, and RC4 cipher).
- Allowing unencrypted (HTTP) traffic to or from public-facing resources.
- Not monitoring and replacing X.509 certificates prior to expiration.
- Using self-signed X.509 certificates for TLS.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

AWS services provide HTTPS endpoints using TLS for communication,
providing encryption in transit when communicating with the AWS
APIs. Insecure HTTP protocols can be audited and blocked in a
Virtual Private Cloud (VPC) through the use of security groups.
HTTP requests can also be
[automatically
redirected to HTTPS](../../../AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.md "../../../AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.md") in Amazon CloudFront or on an
[Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-listeners.md#redirect-actions "../../../elasticloadbalancing/latest/application/load-balancer-listeners.md#redirect-actions"). You can use an
[Amazon Simple Storage Service (Amazon S3) bucket policy](https://aws.amazon.com/blogs/storage/enforcing-encryption-in-transit-with-tls1-2-or-higher-with-amazon-s3/ "https://aws.amazon.com/blogs/storage/enforcing-encryption-in-transit-with-tls1-2-or-higher-with-amazon-s3/") to
restrict the ability to upload objects through HTTP, effectively
enforcing the use of HTTPS for object uploads to your bucket(s).
You have full control over your computing resources to implement
encryption in transit across your services. Additionally, you can
use VPN connectivity into your VPC from an external network or
[AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/") to facilitate encryption of traffic. Verify
that your clients make calls to AWS APIs using at least TLS 1.2,
as
[AWS has deprecated the use of earlier versions of TLS as of February
2024](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/ "https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/"). We recommend you use TLS 1.3. If you have special
requirements for encryption in transit, you can find third-party
solutions available in the AWS Marketplace.

### Implementation steps

- **Enforce encryption in transit:** Your defined encryption requirements should be based on the latest standards and best practices and only allow secure protocols. For example, configure a security group to only allow the HTTPS protocol to an application load balancer or Amazon EC2 instance.
- **Configure secure protocols in edge services:** [Configure HTTPS with Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/using-https.md "../../../AmazonCloudFront/latest/DeveloperGuide/using-https.md") and use a [security profile appropriate for your security posture and use case](../../../AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.md#secure-connections-supported-ciphers "../../../AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.md#secure-connections-supported-ciphers").
- **Use a [VPN for external connectivity](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md"):** Consider using an IPsec VPN for securing point-to-point or network-to-network connections to help provide both data privacy and integrity.
- **Configure secure protocols in load balancers:** Select a security policy that provides the strongest cipher suites supported by the clients that will be connecting to the listener. [Create an HTTPS listener for your Application Load Balancer](../../../elasticloadbalancing/latest/application/create-https-listener.md "../../../elasticloadbalancing/latest/application/create-https-listener.md").
- **Configure secure protocols in Amazon Redshift:** Configure your cluster to require a [secure socket layer (SSL) or transport layer security (TLS) connection](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md").
- **Configure secure protocols:** Review AWS service documentation to determine encryption-in-transit capabilities.
- **Configure secure access when uploading to Amazon S3 buckets:** Use Amazon S3 bucket policy controls to [enforce secure access](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md") to data.
- **Consider using [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/"):** ACM allows you to provision, manage, and deploy public TLS certificates for use with AWS services.
- **Consider using [AWS Private Certificate Authority](https://aws.amazon.com/private-ca/ "https://aws.amazon.com/private-ca/") for private PKI needs:** AWS Private CA allows you to create private certificate authority (CA) hierarchies to issue end-entity X.509 certificates that can be used to create encrypted TLS channels.

## Resources

**Related documents:**

- [Using HTTPS with CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/using-https.md "../../../AmazonCloudFront/latest/DeveloperGuide/using-https.md")
- [Connect your VPC to remote networks using AWS Virtual Private Network](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md")
- [Create an HTTPS listener for your Application Load Balancer](../../../elasticloadbalancing/latest/application/create-https-listener.md "../../../elasticloadbalancing/latest/application/create-https-listener.md")
- [Tutorial: Configure SSL/TLS on Amazon Linux 2](../../../AWSEC2/latest/UserGuide/SSL-on-amazon-linux-2.md "../../../AWSEC2/latest/UserGuide/SSL-on-amazon-linux-2.md")
- [Using SSL/TLS to encrypt a connection to a DB instance](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md")
- [Configuring security options for connections](../../../redshift/latest/mgmt/connecting-ssl-support.md "../../../redshift/latest/mgmt/connecting-ssl-support.md")
