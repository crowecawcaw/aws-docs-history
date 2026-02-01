# DSSEC02-BP02 Control access to sensitive data

Data access controls are fundamental to digital sovereignty, verifying that only authorized
users and services can access data in adherence to regulatory requirements.

**Desired outcome:** Data remains accessible only to authorized
users and services within designated sovereign boundaries, with unauthorized access attempts
blocked before they occur.

**Common anti-patterns:**

- Zone of trust is not known or not clearly established.
- Relying on a single layer of defense. For example using only detective controls to
  detect violations, rather than applying preventative controls to stop violations in the
  first place.
- Not considering cross-service and intra-service data flows across AWS Regions.
- Overlooking encryption key management, including the residency of keys and the location
  of encryption and decryption operations.

**Benefits of establishing this best practice:**

- Maintain adherence to regional data sovereignty requirements.
- Enables developers to modify and extend application functionality without inadvertently
  exposing data.
- Improves transparency and visibility of data access controls leading to better
  auditability.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Implement granular data access controls for digital sovereignty through a layered
approach:

**Foundation:** Establish a data perimeter using the three core
principles - trusted identities accessing trusted resources from expected networks. This
creates your primary zone of trust and blocks unauthorized access attempts.

**Policy controls:** Use IAM global condition keys to restrict
access by region, IP address, VPC, and other request properties. Apply these controls to both
identity-based and resource-based policies for comprehensive coverage.

**Network security:** Implement VPC architecture with security
groups, leverage AWS PrivateLink for private connectivity, and use DNS controls to block
resolution of non-compliant endpoints.

**Data protection:** Classify and tag resources for compliance,
then enable encryption at rest across data storage services using appropriate KMS keys.

**Monitoring:** Prioritize preventive controls over detective
controls, but implement comprehensive logging with CloudTrail, CloudWatch, and AWS Config rules to detect and
remediate compliance gaps.

Consider the following implementation steps.

### Implementation steps

1. **Build a data perimeter**: Begin by building a data
   perimeter that clearly establishes your zone of trust. Then apply principles of least
   privilege on AWS [principals](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") and [resources](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md"). A data perimeter is a set of preventive controls that verifies
   that only _trusted identities_ are accessing _trusted
   resources_ from _expected networks_. This is a
   foundational step designed to block untrusted entities from accessing sensitive data
   held within your accounts. Use [AWS IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md")
   to regularly validate your policies and maintain visible, transparent, and enforceable
   controls. The following 3 principles are central to this:
   1. **Only trusted identities**: Only _trusted
      identities_ can access _my resources_ and only
      _trusted identities_ are allowed from _my
      networks_.
   2. **Only trusted resources**: _My
      principals_ can only access _trusted resources_ and
      that access from _my networks_ only targets _trusted
      resources_ (regardless of the principal involved).
   3. **Only expected networks**: Only _expected
      networks_ can be the source of requests from _my
      principals_ or to _my resources_.
   4. For more detail, see [Blog Post Series: Establishing a
      Data Perimeter on AWS](https://aws.amazon.com/identity/data-perimeters-blog-post-series/ "https://aws.amazon.com/identity/data-perimeters-blog-post-series/").

2. **Use global-condition keys to restrict access**: Create
   IAM policies that use global-condition keys. You can restrict access to AWS
   resources by requested region, IP Address, organization ID, source VPC, source VPC
   Endpoint and several other properties sent as part of API requests. For example, you
   can:
   - Restrict users to make changes to [Amazon EC2](../../../ec2.md "../../../ec2.md") instances in the eu-central-1 Region only, by using the [aws:RequestedRegion](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion") condition key.
   - Restrict users access to an [Amazon S3](../../../s3.md "../../../s3.md")
     bucket unless their [aws:SourceIP](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip") address (CIDR range) matches the condition specified.
   - Use the [aws:SourceVpc](../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md#example-bucket-policies-restrict-access-vpc "../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md#example-bucket-policies-restrict-access-vpc") condition to deny access to an S3 bucket unless the request
     originates from within a specific [VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

3. **Apply resource-based policies:** Global condition keys
   can be combined with resource-based policies. For example, you can:
   - Deny access to an S3 bucket unless the request originates [from a specific
     VPC endpoint](https://repost.aws/knowledge-center/block-s3-traffic-vpc-ip "https://repost.aws/knowledge-center/block-s3-traffic-vpc-ip").
   - Use a VPC Endpoint policy (a type of resource-based policy) to [restrict which S3 Buckets](../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-policies-gateway "../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-policies-gateway") can be accessed from a VPC Gateway type
     endpoint. Similar restrictions can also be applied to VPC Interface endpoints and
     Gateway Load Balancer endpoints. See [Control access to VPC
     endpoints using endpoint policies - AWS PrivateLink](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md").
   - For a complete list of global condition keys, see [AWS global
     condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md").

4. **Implement network-level controls**: Apply an additional
   layer of enforcement using network-level controls. Use VPC Design and Security Groups to
   implement a strict VPC architecture with security groups that limit traffic flows:
   - Establish zonal separation based on data sensitivity, access patterns, privacy
     requirements and export controls. Separating Accounts, VPCs, applying Network ACLs
     and Security groups are a few strategies that you should consider.
   - Inspect and restrict traffic between zones. The [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.md "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.md")
     whitepaper provides several blueprints for you to consider.
   - Limit internet access to block unauthorized data transfers.
   - Use AWS PrivateLink to establish private connectivity between VPCs and services:
     - Create interface endpoints for AWS services
     - Implement endpoint policies to restrict access
     - Avoid using public endpoints for sensitive services
     - Monitor endpoint usage for compliance

   - Implement DNS controls to block resolution of non-compliant endpoints:
     - Use [Amazon Route 53](../../../route53.md "../../../route53.md") Resolver
       rules to control DNS resolution
     - Block resolution of service endpoints in non-compliant Regions
     - Implement DNS query logging for auditing purposes

5. **Implement data protection controls**: Encrypt data at
   rest so that, if unauthorized parties were to somehow obtain the encrypted data, the
   unencrypted plaintext would not be available to them. Consider using AWS KMS keys with
   post-quantum cryptographic algorithms for enhanced security. For more information, see
   [AWS KMS
   post-quantum TLS](../../../kms/latest/developerguide/pqtls.md "../../../kms/latest/developerguide/pqtls.md").
   - Start by implementing a comprehensive data classification and tagging strategy:
     - Tag resources with data classification tags (such as
       data-classification:sovereign, data-classification:public, or
       data-classification:confidential) to identify sovereignty requirements
     - Create automated processes that verify tag compliance
     - Implement tag-based access controls where possible

   - Enable encryption at rest for data storage services. The following are
     examples. Refer to the security documentation for each AWS service you use for
     complete encryption guidance:
     - Enable S3 bucket default encryption with customer-managed KMS keys
     - Enable [Amazon EBS](../../../ebs.md "../../../ebs.md") encryption by
       default in Regions where you operate
     - Enable [Amazon RDS](../../../rds.md "../../../rds.md") storage
       encryption for databases
     - Use encrypted AMIs for EC2 instances For detailed encryption guidance, see
       [Setting default
       server-side encryption behavior for Amazon S3 buckets](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md") and the security
       documentation for each service.

6. **Implement logging and monitoring**: Prioritize preventive
   controls over detective controls, because it is more secure to block non-compliant
   access attempts before they occur rather than to detect such attempts after they occur.
   Apply detective controls to fill in coverage gaps and to provide an extra layer of
   defense. This can be considered as manual enforcement of data access controls.
   - Implement [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")
     and [Amazon CloudWatch](../../../cloudwatch.md "../../../cloudwatch.md") for comprehensive
     logging and monitoring:
     - Enable CloudTrail in Regions where you operate with a single trail
     - Create CloudWatch alarms for suspicious activities
     - Set up automated notifications for compliance issues

   - Implement [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") rules to
     detect non-compliant resources
     - Create custom rules for region-specific compliance
     - Set up remediation actions for non-compliant resources
     - Aggregate config data to a central account
     - Generate compliance reports regularly

## Resources

**Related best practices:**

- [SEC08-BP04 Enforce access control](../security-pillar/sec_protect_data_rest_access_control.md "../security-pillar/sec_protect_data_rest_access_control.md")
- [SEC01-BP06 Automate testing and validation of security controls in pipelines](../security-pillar/sec_securely_operate_test_validate_pipeline.md "../security-pillar/sec_securely_operate_test_validate_pipeline.md")

**Related documents:**

- [Identity and Access Management](../../../whitepapers/latest/aws-caf-security-perspective/identity-and-access-management.md "../../../whitepapers/latest/aws-caf-security-perspective/identity-and-access-management.md")
- [Data Residency: AWS Policy Perspectives](https://d1.awsstatic.com/whitepapers/compliance/Data_Residency_Whitepaper.pdf "https://d1.awsstatic.com/whitepapers/compliance/Data_Residency_Whitepaper.pdf")
- [Data Residency with Hybrid Cloud Services Lens - AWS Well-Architected](../data-residency-hybrid-cloud-services-lens/data-residency-with-hybrid-cloud-services-lens.md "../data-residency-hybrid-cloud-services-lens/data-residency-with-hybrid-cloud-services-lens.md")
- [Data
  Classification](../../../whitepapers/latest/data-classification/data-classification.md "../../../whitepapers/latest/data-classification/data-classification.md")
- [Data security and risk management](../../../whitepapers/latest/tagging-best-practices/data-security-and-risk-management.md "../../../whitepapers/latest/tagging-best-practices/data-security-and-risk-management.md")

**Related videos:**

- [AWS re:Invent 2024 - Amazon S3
  security and access control best practices](https://www.youtube.com/watch?v=vRmUI0VdsQw "https://www.youtube.com/watch?v=vRmUI0VdsQw")
- [AWS re:Invent 2019 - Provable
  access control: Know who can access your AWS resources](https://www.youtube.com/watch?v=6DX7p-OirGU "https://www.youtube.com/watch?v=6DX7p-OirGU")
- [AWS re:Inforce 2022 - AWS Identity and Access Management
  (IAM) deep dive](https://www.youtube.com/watch?v=YMj33ToS8cI "https://www.youtube.com/watch?v=YMj33ToS8cI")
- [AWS re:Invent 2018: The Theory
  and Math Behind Data Privacy and Security Assurance](https://www.youtube.com/watch?v=F3JmBhTQmyY "https://www.youtube.com/watch?v=F3JmBhTQmyY")

**Related services:**

- [AWS Identity and Access Management
  (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md")
- [AWS Key Management Service
  (KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
- [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")
