

# Security in AWS Abuse Signal API

You’re responsible for securing the credentials you use to call the API. Use IAM identities with only the abuse: permissions they need, and prefer roles with temporary credentials. Sign every request with Signature Version 4 or Signature Version 4A. Requests must use TLS 1.2 or later; we recommend TLS 1.3. You can call the API from your VPC without crossing the public internet by using AWS PrivateLink.

**Topics**
+ [Data protection](data-protection.md)
+ [Identity and access management](security-iam.md)
+ [VPC endpoints (AWS PrivateLink)](vpc-interface-endpoints.md)
+ [Security best practices](security-best-practices.md)