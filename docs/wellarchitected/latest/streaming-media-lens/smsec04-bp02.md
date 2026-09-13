

# SMSEC04-BP02 Encrypt content ingest traffic using TLS
<a name="smsec04-bp02"></a>

AWS Elemental Media Services require HTTPS connections where possible. Use HTTPS over HTTP wherever possible and avoid outdated security ciphers. Using up to date versions of TLS encryption keeps traffic secure in transit either coming into your workflows or leaving your workflows.

**Desired outcome:**
+ Network traffic between sites or on the internet is protected from unauthorized users
+ You have all content ingest traffic encrypted using TLS 1.2 or higher

**Common anti-patterns:**
+ Organizations configure media ingest endpoints to accept unencrypted HTTP or Real-Time Messaging Protocol (RTMP) connections for live contribution feeds, exposing content to interception on public network paths.
+ Teams use outdated TLS versions (TLS 1.0 or 1.1) or weak cipher suites for media transport, leaving encrypted connections vulnerable to known cryptographic attacks.
+ Organizations allow self-signed or expired certificates on ingest endpoints without validation, enabling man-in-the-middle attacks on contribution feeds.
+ Teams transmit live event feeds over unencrypted satellite or fiber backhaul links without applying transport-layer encryption, assuming private network paths are inherently secure.
+ Organizations fail to enforce HTTPS-only policies on content delivery endpoints, allowing downgrade attacks that strip encryption from viewer-facing streams.

**Benefits of establishing this best practice:**
+ TLS encryption blocks interception of live contribution feeds and video on demand (VOD) transfers on public network paths, protecting unreleased content from unauthorized capture.
+ Encrypted transport blocks media content from being tampered with or modified in transit between content sources and ingest endpoints.
+ TLS 1.2 or higher satisfies content security requirements from major studios and licensors who mandate encrypted transport for premium content delivery.
+ Anycast networks like AWS Global Accelerator combined with TLS provide encrypted, optimized paths for international contribution feeds without exposing content on intermediate network hops.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

To block content from being intercepted between the publisher and ingest endpoints, encrypt uploads in transit and use TLS at both the source and destination. Some AWS and AWS Elemental Services will already enforce TLS where possible. Choose to use TLS and other up to date ciphers when the option is available. Also turn off or restrict security methods you want to avoid, such as HTTP.

To simplify configuration for global connectivity over public network paths, use anycast networks, such as AWS Global Accelerator, which helps clients connect to the closest available endpoint. Source and destination IPs should be restricted to only allow connections from trusted services or IPs whenever possible through the use of Access Control Lists (ACLs), passphrases, or other credentials.

Also consider using Amazon Certificate Manager to manage private keys and public certificates to secure traffic and applications. Review the benefits and implementation steps in the [Well-Architected Framework Security Pillar.](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_key_cert_mgmt.html)

### Implementation steps
<a name="implementation-steps"></a>

1. **Configure HTTPS:** Configure HTTPS where possible, such as in [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) delivery.

1. **Manage certificates:** Consider using [Amazon Certificate Manager](https://aws.amazon.com/certificate-manager/) to manage TLS certificates.

1. **Use AWS Global Accelerator:** Use [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/features/) to deliver content to AWS at specific endpoints instead of the open internet.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC04-BP01 Use Access Control Lists to restrict content to trusted providers only](smsec04-bp01.html)
+ [SMSEC04-BP03 Use private connectivity when working with partners](smsec04-bp03.html)

**Related documents**
+ [Using HTTPS with Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html)
+ [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)
+ [AWS Global Accelerator Features](https://aws.amazon.com/global-accelerator/features/)
+ [Well-Architected Security Pillar - Key and Certificate Management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_key_cert_mgmt.html)

**Related services**
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [Amazon Certificate Manager](https://aws.amazon.com/certificate-manager/)
+ [Amazon Global Accelerator](https://aws.amazon.com/global-accelerator/)