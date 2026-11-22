

# SEC09-BP02 Enforce encryption in transit

 Encryption in transit protects data as it moves between systems and across networks you do not control. Enforcing it means requiring secure protocols for sensitive traffic, rejecting weak or outdated ones, and confirming that both endpoints negotiate strong parameters. Your organization's policies, regulatory obligations, and standards define what counts as strong for your workloads. 

 **Desired outcome:** 
+  You encrypt traffic between your resources and the internet to prevent unauthorized access to data in transit. 
+  You encrypt internal traffic within your environment according to your security requirements. 
+  Your TLS connections use current protocol versions and cipher suites that provide Perfect Forward Secrecy (PFS), so recorded traffic stays protected even if a key is later exposed. 
+  Your services reject deprecated protocols and weak cipher suites. 

 **Common anti-patterns:** 
+  Teams use deprecated versions of SSL, TLS, or cipher suite components. 
+  Public-facing resources accept unencrypted HTTP traffic. 
+  X.509 certificates expire without monitoring or replacement. 
+  Services use self-signed X.509 certificates for TLS. 
+  Cipher suites without Perfect Forward Secrecy (PFS) remain in use. 
+  Teams configure cipher suites once and never review them against current standards. 

 **Benefits of establishing this best practice:** 
+  Data confidentiality and integrity hold during transmission. 
+  Eavesdropping and on-path attacks are prevented. 
+  Regulatory adherence for data protection improves. 
+  Perfect Forward Secrecy preserves the confidentiality of past communications if a key is later exposed. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A service can support HTTPS while still accepting plaintext HTTP on the same port. Unauthorized users or misconfigured clients can then use the plaintext path. Enforcement means refusing the insecure option. A public endpoint that answers on both HTTP and HTTPS lets sensitive data travel unencrypted. 

 TLS security depends on the protocol version and the negotiated cipher suite. Older versions of SSL and TLS contain known weaknesses, and [AWS requires TLS 1.2 or later](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/) for its endpoints. We recommend TLS 1.3 where your clients support it, and TLS 1.2 as the minimum. A cipher suite with Perfect Forward Secrecy (PFS) derives a unique key for each session, so a private key exposed later cannot decrypt traffic captured earlier. TLS 1.3 includes only PFS cipher suites. 

 Algorithms change, so build for crypto agility. Post-quantum key agreement requires TLS 1.3, and many AWS service endpoints negotiate hybrid post-quantum key agreement when the client supports it. [Migration to post-quantum cryptography](https://aws.amazon.com/security/post-quantum-cryptography/migrating-to-post-quantum-cryptography/) records which capabilities AWS delivers and which ones you apply yourself. Name the security policy explicitly wherever your infrastructure as code creates or updates a load balancer or API endpoint. A blank or default policy can fall back to an older one that favors compatibility. Use IAM condition keys to prevent policy regressions, and AWS Config rules to detect drifting resources. Keep your AWS SDKs current, because client support determines whether a session negotiates the newer algorithms. CloudTrail events record the TLS version and cipher suite, and the key exchange for many services. Load balancer access and connection logs record the same detail when you enable them. 

 You enforce encryption at the points where traffic enters or leaves a boundary. AWS API endpoints already require TLS. For your own public endpoints, you can [redirect HTTP to HTTPS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html) in Amazon CloudFront or on an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/rule-action-types.html#redirect-actions), and block plaintext with security groups. For object storage, an [Amazon S3 bucket policy](https://aws.amazon.com/blogs/storage/enforcing-encryption-in-transit-with-tls1-2-or-higher-with-amazon-s3/) can deny requests that do not use TLS. For traffic leaving your network, several [network-to-Amazon VPC connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html) provide encrypted transport between your network and AWS. 

 Internal traffic is where enforcement often stops. Encrypt service-to-service communication scaled to data sensitivity. Enforcement also depends on valid certificates, so monitor expiry and renew before certificates lapse. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define your encryption requirements:** Review your organization's policies, regulatory obligations, and industry standards to set the required protocol versions, cipher suites, and key lengths for data in transit. 

1.  **Enforce encryption for internet-facing services:** Configure HTTPS on public endpoints such as [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) and [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html), select security policies that prefer TLS 1.3, and redirect or block plaintext HTTP. 

1.  **Enforce TLS for Amazon S3 access:** Apply [S3 bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) that deny requests not sent over TLS, for both uploads and downloads. 

1.  **Encrypt internal traffic to your requirements:** Configure TLS for service-to-service traffic within your VPC, scaled to the sensitivity of the data each flow carries. 

1.  **Require TLS for database connections:** Configure database services such as [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html), [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html), and [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html) to require SSL/TLS connections. 

1.  **Protect traffic leaving your network:** Review the patterns in the [Network-to-Amazon VPC connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html) to determine the best approach for securely connecting remote networks to your Amazon AWS resources. 

1.  **Provision and renew certificates automatically:** Use [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) to provision and deploy public TLS certificates, and monitor expiration so certificates renew before they lapse. For a private PKI, use [AWS Private Certificate Authority](https://aws.amazon.com/private-ca/). 

1.  **Review protocols and cipher suites on a cadence:** Select security policies that prefer modern TLS versions and PFS cipher suites, and re-check these configurations against current standards on a regular schedule. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC09-BP01 Implement secure key and certificate management](sec09-bp01.md) 
+  [SEC09-BP03 Authenticate network communications](sec09-bp03.md) 
+  [SEC08-BP02 Enforce encryption at rest](sec08-bp02.md) 

 **Related documents:** 
+  [Migration to post-quantum cryptography](https://aws.amazon.com/security/post-quantum-cryptography/migrating-to-post-quantum-cryptography/) 
+  [AWS support for post-quantum confidentiality](https://aws.amazon.com/security/post-quantum-cryptography/aws-pq-readiness-confidentiality/) 
+  [Using HTTPS with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) 
+  [Create an HTTPS listener for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) 
+  [Connect your VPC to remote networks using AWS Virtual Private Network](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html) 
+  [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) 
+  [Configuring security options for connections](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html) 
+  [Configure SSL/TLS on Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/ug/SSL-on-amazon-linux-2023.html) 