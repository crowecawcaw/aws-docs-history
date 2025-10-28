**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Security in your use of the AWS Shield network security director

###### Note

AWS Shield network security director is in public preview release and is subject to change.

This section describes the key security considerations for using this network security director preview.

###### Data sources

When you run an analysis, network security director retrieves information about your [AWS resources](https://aws.amazon.com/resourceexplorer/ "https://aws.amazon.com/resourceexplorer/") using public AWS API endpoints. The information retrieved includes resource attributes that are available to your account through the public AWS APIs. For 60 days after you perform a network analysis, the information from the scan informs the findings and remediation recommendations provided by network security director.

AWS Shield network security director also uses internal AWS data sources and threat intelligence to identify findings and recommend remediations.

###### Data encryption

Review the following encryption considerations when using network security director.

- **Encryption at rest** – All data is protected at rest.
- **Encryption in transit** – All data is protected in transit using Transport Layer Security (TLS) encryption. All communication is authenticated using Amazon Simple Storage Service AWS Signature Version 4 (SigV4). For information about SigV4, see [Authenticating Requests (AWS Signature Version 4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md") in the _Amazon S3 User Guide_.
- **Key management** – Customer-managed keys are not currently supported.

###### Topics

- [Identity and Access Management for AWS Shield network security director](nsd-iam.md "nsd-iam.md")
- [Identity-based
  policy examples for AWS Shield network security director](security-nsd-with-iam-id-based-policies.md "security-nsd-with-iam-id-based-policies.md")
- [Using service-linked roles for AWS Shield network security director](security_iam_nsd-with-iam-roles-service-linked.md "security_iam_nsd-with-iam-roles-service-linked.md")
