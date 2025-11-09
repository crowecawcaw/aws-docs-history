# AWS managed policies for Amazon CloudFront

To add permissions to users, groups, and roles, it’s easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your users with only the permissions they need. To
get started quickly, you can use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can’t change the permissions
in AWS managed policies. Services occasionally add additional permissions to an AWS
managed policy to support new features. This type of update affects all identities (users,
groups, and roles) where the policy is attached. Services are most likely to update an AWS
managed policy when a new feature is launched or when new permissions become available.
Services do not remove permissions from an AWS managed policy, so policy updates won’t break
your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

###### Topics

- [AWS managed policy:
  CloudFrontReadOnlyAccess](#security-iam-awsmanpol-cloudfront-read-only "#security-iam-awsmanpol-cloudfront-read-only")
- [AWS managed policy:
  CloudFrontFullAccess](#security-iam-awsmanpol-cloudfront-full-access "#security-iam-awsmanpol-cloudfront-full-access")
- [AWS managed policy:
  AWSCloudFrontLogger](#security-iam-awsmanpol-cloudfront-logger "#security-iam-awsmanpol-cloudfront-logger")
- [AWS managed policy:
  AWSLambdaReplicator](#security-iam-awsmanpol-lambda-replicator "#security-iam-awsmanpol-lambda-replicator")
- [AWS managed policy:
  AWSCloudFrontVPCOriginServiceRolePolicy](#security-iam-awsmanpol-vpc-origin "#security-iam-awsmanpol-vpc-origin")
- [CloudFront updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy:

CloudFrontReadOnlyAccess

You can attach the **CloudFrontReadOnlyAccess** policy to
your IAM identities. This policy allows read-only permissions to CloudFront resources. It also
allows read-only permissions to other AWS service resources that are related to CloudFront and
that are visible in the CloudFront console.

**Permissions details**

This policy includes the following permissions.

- `cloudfront:Describe*` – Allows principals to get information about
  metadata about CloudFront resources.
- `cloudfront:Get*` – Allows principals to get detailed information and
  configurations for CloudFront resources.
- `cloudfront:List*` – Allows principals to get lists of CloudFront
  resources.
- `cloudfront-keyvaluestore:Describe*` - Allows principals to get
  information about the key value store.
- `cloudfront-keyvaluestore:Get*` - Allows principals to get detailed
  information and configurations for the key value store.
- `cloudfront-keyvaluestore:List*` - Allows principals to get lists of
  the key value stores.
- `acm:DescribeCertificate` – Allows principals to get details
  about an ACM certificate.
- `acm:ListCertificates` – Allows principals to get a list of ACM
  certificates.
- `iam:ListServerCertificates` – Allows principals to get a list of
  server certificates stored in IAM.
- `route53:List*` – Allows principals to get lists of Route 53
  resources.
- `waf:ListWebACLs` – Allows principals to get a list of web ACLs in
  AWS WAF.
- `waf:GetWebACL` – Allows principals to get detailed information about
  web ACLs in AWS WAF.
- `wafv2:ListWebACLs` – Allows principals to get a list of web ACLs in
  AWS WAF.
- `wafv2:GetWebACL` – Allows principals to get detailed information about
  web ACLs in AWS WAF.

To view the permissions for this policy, see [CloudFrontReadOnlyAccess](../../../aws-managed-policy/latest/reference/CloudFrontReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/CloudFrontReadOnlyAccess.md") in the _AWS Managed Policy
Reference_.

## AWS managed policy:

CloudFrontFullAccess

You can attach the **CloudFrontFullAccess** policy to your
IAM identities. This policy allows administrative permissions to CloudFront resources. It also
allows read-only permissions to other AWS service resources that are related to CloudFront and
that are visible in the CloudFront console.

**Permissions details**

This policy includes the following permissions.

- `s3:ListAllMyBuckets` – Allows principals to get a list of all Amazon S3
  buckets.
- `acm:DescribeCertificate` – Allows principals to get details
  about an ACM certificate.
- `acm:ListCertificates` – Allows principals to get a list of ACM
  certificates.
- `acm:RequestCertificate` – Allows principals to request managed
  certificates from ACM.
- `cloudfront:*` – Allows principals to perform all actions on all CloudFront
  resources.
- `cloudfront-keyvaluestore:*` - Allows principals to perform all actions
  on the key value store.
- `iam:ListServerCertificates` – Allows principals to get a list of
  server certificates stored in IAM.
- `waf:ListWebACLs` – Allows principals to get a list of web ACLs in
  AWS WAF.
- `waf:GetWebACL` – Allows principals to get detailed information about
  web ACLs in AWS WAF.
- `wafv2:ListWebACLs` – Allows principals to get a list of web ACLs in
  AWS WAF.
- `wafv2:GetWebACL` – Allows principals to get detailed information about
  web ACLs in AWS WAF.
- `kinesis:ListStreams` – Allows principals to get a list of Amazon Kinesis
  streams.
- `ec2:DescribeInstances` - Allows principals to get detailed information
  about instances in Amazon EC2.
- `elasticloadbalancing:DescribeLoadBalancers` - Allows principals to get
  detailed information about load balancers in Elastic Load Balancing.
- `ec2:DescribeInternetGateways` - Allows principals to get detailed
  information about internet gateways in Amazon EC2.
- `kinesis:DescribeStream` – Allows principals to get detailed
  information about a Kinesis stream.
- `iam:ListRoles` – Allows principals to get a list of roles in
  IAM.

To view the permissions for this policy, see [CloudFrontFullAccess](../../../aws-managed-policy/latest/reference/CloudFrontFullAccess.md "../../../aws-managed-policy/latest/reference/CloudFrontFullAccess.md") in the _AWS Managed Policy
Reference_.

###### Important

If you want CloudFront to create and save access logs, you need to grant additional
permissions. For more information, see [Permissions](standard-logging-legacy-s3.md#AccessLogsBucketAndFileOwnership "standard-logging-legacy-s3.md#AccessLogsBucketAndFileOwnership").

## AWS managed policy:

AWSCloudFrontLogger

You can’t attach the **AWSCloudFrontLogger** policy to your
IAM identities. This policy is attached to a service-linked role that allows CloudFront to
perform actions on your behalf. For more information, see [Service-linked roles for Lambda@Edge](lambda-edge-permissions.md#using-service-linked-roles-lambda-edge "lambda-edge-permissions.md#using-service-linked-roles-lambda-edge").

This policy allows CloudFront to push log files to Amazon CloudWatch. For details about the permissions
included in this policy, see [Service-linked role permissions for CloudFront
logger](lambda-edge-permissions.md#slr-permissions-cloudfront-logger "lambda-edge-permissions.md#slr-permissions-cloudfront-logger").

To view the permissions for this policy, see [AWSCloudFrontLogger](../../../aws-managed-policy/latest/reference/AWSCloudFrontLogger.md "../../../aws-managed-policy/latest/reference/AWSCloudFrontLogger.md") in the _AWS Managed Policy
Reference_.

## AWS managed policy:

AWSLambdaReplicator

You can’t attach the **AWSLambdaReplicator** policy to your
IAM identities. This policy is attached to a service-linked role that allows CloudFront to
perform actions on your behalf. For more information, see [Service-linked roles for Lambda@Edge](lambda-edge-permissions.md#using-service-linked-roles-lambda-edge "lambda-edge-permissions.md#using-service-linked-roles-lambda-edge").

This policy allows CloudFront to create, delete, and disable functions in AWS Lambda to
replicate Lambda@Edge functions to AWS Regions. For details about the permissions
included in this policy, see [Service-linked role permissions for
Lambda replicator](lambda-edge-permissions.md#slr-permissions-lambda-replicator "lambda-edge-permissions.md#slr-permissions-lambda-replicator").

To view the permissions for this policy, see [AWSLambdaReplicator](../../../aws-managed-policy/latest/reference/AWSLambdaReplicator.md "../../../aws-managed-policy/latest/reference/AWSLambdaReplicator.md") in the _AWS Managed Policy
Reference_.

## AWS managed policy:

AWSCloudFrontVPCOriginServiceRolePolicy

You can't attach the **AWSCloudFrontVPCOriginServiceRolePolicy** policy to your IAM entities. This
policy is attached to a service-linked role that allows CloudFront to perform actions on your
behalf. For more information, see [Use service-linked roles for
CloudFront](using-service-linked-roles.md "using-service-linked-roles.md").

This policy allows CloudFront to manage EC2 elastic network interfaces and security groups on
your behalf. For details about the permissions included in this policy, see [Service-linked role permissions for CloudFront VPC Origins](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions").

To view the permissions for this policy, see [AWSCloudFrontVPCOriginServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSCloudFrontVPCOriginServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSCloudFrontVPCOriginServiceRolePolicy.md") in the _AWS Managed Policy
Reference_.

## CloudFront updates to AWS managed

policies

View details about updates to AWS managed policies for CloudFront since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the CloudFront [Document history](WhatsNew.md "WhatsNew.md") page.

| Change                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                          | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [CloudFrontReadOnlyAccess](#security-iam-awsmanpol-cloudfront-read-only "#security-iam-awsmanpol-cloudfront-read-only")<br>– Update to existing policy                                                                                                                                       | CloudFront added new permission for<br>ACM.<br>The new permission allows principals to get details about an ACM<br>certificate.                                                                                                                      | April 28, 2025    |
| [CloudFrontFullAccess](#security-iam-awsmanpol-cloudfront-full-access "#security-iam-awsmanpol-cloudfront-full-access")<br>– Update to existing policy                                                                                                                                       | CloudFront added new permissions for ACM.<br>The new permissions allow principals to get<br>details<br>about an ACM certificate and<br>to<br>request a managed certificate from ACM.                                                                 | April 28, 2025    |
| [CloudFrontFullAccess](#security-iam-awsmanpol-cloudfront-full-access "#security-iam-awsmanpol-cloudfront-full-access")<br>– Update to existing policy                                                                                                                                       | CloudFront added new permissions for Amazon EC2 and Elastic Load Balancing.<br>The new permissions allow CloudFront to get detailed information about load<br>balancers in Elastic Load Balancing and instances and internet gateways in Amazon EC2. | November 20, 2024 |
| [AWSCloudFrontVPCOriginServiceRolePolicy](#security-iam-awsmanpol-vpc-origin "#security-iam-awsmanpol-vpc-origin") – New<br>policy                                                                                                                                                           | CloudFront added a new policy.<br>This policy allows CloudFront to manage EC2 elastic network interfaces and<br>security groups on your behalf.                                                                                                      | November 20, 2024 |
| [CloudFrontReadOnlyAccess](#security-iam-awsmanpol-cloudfront-read-only "#security-iam-awsmanpol-cloudfront-read-only") and<br>[CloudFrontFullAccess](#security-iam-awsmanpol-cloudfront-full-access "#security-iam-awsmanpol-cloudfront-full-access") -<br>Update to two existing policies. | CloudFront added new permissions for key value stores.<br>The new permissions allow users to get information about, and take action<br>on, key value stores.                                                                                         | December 19, 2023 |
| [CloudFrontReadOnlyAccess](#security-iam-awsmanpol-cloudfront-read-only "#security-iam-awsmanpol-cloudfront-read-only") –<br>Update to an existing policy                                                                                                                                    | CloudFront added a new permission to describe CloudFront Functions.<br>This permission allows the user, group, or role to read information and<br>metadata about a function, but not the function’s code.                                            | September 8, 2021 |
| CloudFront started tracking changes                                                                                                                                                                                                                                                          | CloudFront started tracking changes for its AWS managed policies.                                                                                                                                                                                    | September 8, 2021 |
