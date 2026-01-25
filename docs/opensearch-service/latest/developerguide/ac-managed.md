# AWS managed policies for Amazon OpenSearch Service

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AmazonOpenSearchDirectQueryGlueCreateAccess

Grants Amazon OpenSearch Service Direct Query Service access to the `CreateDatabase`,
`CreatePartition`,`CreateTable`, and
`BatchCreatePartition` AWS Glue API.

You can find the [AmazonOpenSearchDirectQueryGlueCreateAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchDirectQueryGlueCreateAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchDirectQueryGlueCreateAccess") policy in the IAM
console.

## AmazonOpenSearchServiceFullAccess

Grants full access to the OpenSearch Service configuration API operations and resources for an
AWS account.

You can find the [AmazonOpenSearchServiceFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceFullAccess") policy in the IAM console.

## AmazonOpenSearchServiceReadOnlyAccess

Grants read-only access to all OpenSearch Service resources for an AWS account.

You can find the [AmazonOpenSearchServiceReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceReadOnlyAccess") policy in the IAM
console.

## AmazonOpenSearchServiceRolePolicy

You can't attach `AmazonOpenSearchServiceRolePolicy` to your IAM
entities. This policy is attached to a service-linked role that allows OpenSearch Service to
access account resources. For more information, see [Permissions](slr-aos.md#slr-permissions "slr-aos.md#slr-permissions").

You can find the [AmazonOpenSearchServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceRolePolicy") policy in the IAM console.

## AmazonOpenSearchServiceCognitoAccess

Provides the minimum Amazon Cognito permissions necessary to enable [Cognito authentication](cognito-auth.md "cognito-auth.md").

You can find the [AmazonOpenSearchServiceCognitoAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceCognitoAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceCognitoAccess") policy in the IAM
console.

## AmazonOpenSearchIngestionServiceRolePolicy

You can't attach `AmazonOpenSearchIngestionServiceRolePolicy` to your
IAM entities. This policy is attached to a service-linked role that allows
OpenSearch Ingestion to enable VPC access for ingestion pipelines, create tags, and
publish ingestion-related CloudWatch metrics to your account. For more information, see
[Using service-linked roles for Amazon OpenSearch Service](slr.md "slr.md").

You can find the [AmazonOpenSearchIngestionServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy") policy in the IAM
console.

## OpenSearchIngestionSelfManagedVpcePolicy

You can't attach `OpenSearchIngestionSelfManagedVpcePolicy` to your
IAM entities. This policy is attached to a service-linked role that allows
OpenSearch Ingestion to enable self-managed VPC access for ingestion pipelines, create
tags, and publish ingestion-related CloudWatch metrics to your account. For more
information, see [Using service-linked roles for Amazon OpenSearch Service](slr.md "slr.md").

You can find the [OpenSearchIngestionSelfManagedVpcePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/OpenSearchIngestionSelfManagedVpcePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/OpenSearchIngestionSelfManagedVpcePolicy") policy in the IAM
console.

## AmazonOpenSearchIngestionFullAccess

Grants full access to the OpenSearch Ingestion API operations and resources for an
AWS account.

You can find the [AmazonOpenSearchIngestionFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionFullAccess") policy in the IAM console.

## AmazonOpenSearchIngestionReadOnlyAccess

Grants read-only access to all OpenSearch Ingestion resources for an
AWS account.

You can find the [AmazonOpenSearchIngestionReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionReadOnlyAccess") policy in the IAM
console.

## AmazonOpenSearchServerlessServiceRolePolicy

Provides the minimum Amazon CloudWatch permissions necessary to send
OpenSearch Serverless metric data to CloudWatch.

You can find the [AmazonOpenSearchServerlessServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServerlessServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServerlessServiceRolePolicy") policy in the IAM
console.

## OpenSearch Service updates to AWS managed policies

View details about updates to AWS managed policies for OpenSearch Service since this service
began tracking changes.

| Change                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| Updated the<br>`AmazonOpenSearchIngestionServiceRolePolicy`                                                                                                    | The update gives OpenSearch Ingestion permission to modify VPC<br>endpoints created by OpenSearch in order to share pipelines<br>across VPCs.<br>For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy").                                                                                                                                      | 28 August 2025    |
| Updated the<br>`AmazonOpenSearchServiceRolePolicy`                                                                                                             | Added the following statement to the policy. When Amazon OpenSearch Service<br>assumes the<br>`AWSServiceRoleForAmazonOpenSearchService`<br>service-linked role, this new statement in the policy enables<br>OpenSearch to update the access scope of any AWS IAM Identity Center<br>application that is only managed by OpenSearch.<br>`<br>{<br>"Effect": "Allow",<br>"Action": "sso:PutApplicationAccessScope",<br>"Resource": "arn:aws:sso::*:application/*/*",<br>"Condition": {<br>"StringEquals": {<br>"aws:ResourceOrgID": "${aws:PrincipalOrgID}"<br>}<br>}<br>}<br>` | 31 March 2025     |
| Updated<br>`AmazonOpenSearchServerlessServiceRolePolicy`                                                                                                       | Added the Sid `AllowAOSSCloudwatchMetrics` to the<br>policy `AmazonOpenSearchServerlessServiceRolePolicy`.<br>A Sid is a statement ID that acts as an optional identifier for<br>the policy statement.                                                                                                                                                                                                                                                                                                                                                                         | 12 July 2024      |
| Added<br>`OpenSearchIngestionSelfManagedVpcePolicy`                                                                                                            | A new policy that allows OpenSearch Ingestion to enable<br>self-managed VPC access for ingestion pipelines, create tags,<br>and publish ingestion-related CloudWatch metrics to your<br>account.<br>For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy").                                                                                   | 12 June 2024      |
| Added`AmazonOpenSearchDirectQueryGlueCreateAccess`                                                                                                             | Grants Amazon OpenSearch Service Direct Query Service access to the<br>`CreateDatabase`,<br>`CreatePartition`,`CreateTable`, and<br>`BatchCreatePartition` AWS Glue API.                                                                                                                                                                                                                                                                                                                                                                                                       | 6 May 2024        |
| Updated `AmazonOpenSearchServiceRolePolicy` and<br>`AmazonElasticsearchServiceRolePolicy`                                                                      | Added the permissions necessary for [the service-linked role](slr-aos.md#slr-permissions "slr-aos.md#slr-permissions") to<br>assign and unassign IPv6 addresses.<br>The deprecated Elasticsearch policy has also been updated to<br>ensure backwards compatibility.                                                                                                                                                                                                                                                                                                            | 18 October 2023   |
| Added<br>`AmazonOpenSearchIngestionServiceRolePolicy`                                                                                                          | A new policy that allows OpenSearch Ingestion to enable VPC access<br>for ingestion pipelines, create tags, and publish<br>ingestion-related CloudWatch metrics to your account.<br>For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionServiceRolePolicy").                                                                                                   | 26 April 2023     |
| Added `AmazonOpenSearchIngestionFullAccess`                                                                                                                    | A new policy that grants full access to the OpenSearch Ingestion<br>API operations and resources for an AWS account.<br>For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionFullAccess").                                                                                                                                                                             | 26 April 2023     |
| Added<br>`AmazonOpenSearchIngestionReadOnlyAccess`                                                                                                             | A new policy that grants read-only access to all<br>OpenSearch Ingestion resources for an AWS account.<br>For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchIngestionReadOnlyAccess").                                                                                                                                                                                   | 26 April 2023     |
| Added<br>`AmazonOpenSearchServerlessServiceRolePolicy`                                                                                                         | A new policy that provides the minimum permissions necessary<br>to send OpenSearch Serverless metric data to Amazon CloudWatch.<br>For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServerlessServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServerlessServiceRolePolicy").                                                                                                                                                  | 29 November 2022  |
| Updated `AmazonOpenSearchServiceRolePolicy` and<br>`AmazonElasticsearchServiceRolePolicy`                                                                      | Added the permissions necessary for [the service-linked role](slr-aos.md#slr-permissions "slr-aos.md#slr-permissions") to<br>create [OpenSearch Service-managed VPC<br>endpoints](slr-aos.md#slr-permissions "slr-aos.md#slr-permissions"). Some actions can only be performed when<br>the request contains the tag<br>`OpenSearchManaged=true`.<br>The deprecated Elasticsearch policy has also been updated to<br>ensure backwards compatibility.                                                                                                                            | 7 November 2022   |
| Updated `AmazonOpenSearchServiceRolePolicy` and<br>`AmazonElasticsearchServiceRolePolicy`                                                                      | Added support for the `PutMetricData` action, which<br>is required to publish OpenSearch cluster metrics to<br>Amazon CloudWatch.<br>The deprecated Elasticsearch policy has also been updated to<br>ensure backwards compatibility.<br>For the policy JSON, see the [IAM console](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonOpenSearchServiceRolePolicy").                                                                 | 12 September 2022 |
| Updated `AmazonOpenSearchServiceRolePolicy` and<br>`AmazonElasticsearchServiceRolePolicy`                                                                      | Added support for the `acm` resource type. The<br>policy provides the minimum AWS Certificate Manager (ACM) read-only<br>permission necessary for the [service-linked role](slr-aos.md#slr-permissions "slr-aos.md#slr-permissions") to verify and validate ACM<br>resources in order to create and update [custom endpoint](customendpoint.md "customendpoint.md") enabled<br>domains.<br>The deprecated Elasticsearch policy has also been updated to<br>ensure backwards compatibility.                                                                                     | 28 July 2022      |
| Updated `AmazonOpenSearchServiceCognitoAccess` and<br>`AmazonESCognitoAccess`                                                                                  | Added support for the `UpdateUserPoolClient`<br>action, which is required to set Cognito user pool configuration<br>during upgrade from Elasticsearch to OpenSearch.<br>Corrected permissions for the<br>`SetIdentityPoolRoles` action to allow access to<br>all resources.<br>The deprecated Elasticsearch policy has also been updated to<br>ensure backwards compatibility.                                                                                                                                                                                                 | 20 December 2021  |
| Updated `AmazonOpenSearchServiceRolePolicy`                                                                                                                    | Added support for the `security-group` resource<br>type. The policy provides the minimum Amazon EC2 and Elastic Load Balancing<br>permissions necessary for [the<br>service-linked role](slr-aos.md#slr-permissions "slr-aos.md#slr-permissions") to enable [VPC access](cognito-auth.md "cognito-auth.md").                                                                                                                                                                                                                                                                   | 9 September 2021  |
| • Added<br>`AmazonOpenSearchServiceFullAccess`<br>• Deprecated `AmazonESFullAccess`                                                                            | This new policy is meant to replace the old policy. Both<br>policies provide full access to the OpenSearch Service configuration API and<br>all HTTP methods for the OpenSearch APIs. [Fine-grained access control](fgac.md "fgac.md") and [resource-based policies](ac.md#ac-types-resource "ac.md#ac-types-resource")<br>can still restrict access.                                                                                                                                                                                                                          | 7 September 2021  |
| • Added<br>`AmazonOpenSearchServiceReadOnlyAccess`<br>• Deprecated `AmazonESReadOnlyAccess`                                                                    | This new policy is meant to replace the old policy. Both<br>policies provide read-only access to the OpenSearch Service configuration API<br>(`es:Describe*`, `es:List*`, and<br>`es:Get*`) and \*no<br>• access to the HTTP methods for the<br>OpenSearch APIs.                                                                                                                                                                                                                                                                                                               | 7 September 2021  |
| • Added<br>`AmazonOpenSearchServiceCognitoAccess`<br>• Deprecated `AmazonESCognitoAccess`                                                                      | This new policy is meant to replace the old policy. Both<br>policies provide the minimum Amazon Cognito permissions necessary to<br>enable [Cognito<br>authentication](cognito-auth.md "cognito-auth.md").                                                                                                                                                                                                                                                                                                                                                                     | 7 September 2021  |
| • Added [AmazonOpenSearchServiceRolePolicy](slr-aos.md#slr-permissions "slr-aos.md#slr-permissions")<br>• Deprecated<br>`AmazonElasticsearchServiceRolePolicy` | This new policy is meant to replace the old policy. Both<br>policies provide the minimum Amazon EC2 and Elastic Load Balancing permissions<br>necessary for [the service-linked<br>role](slr-aos.md#slr-permissions "slr-aos.md#slr-permissions") to enable [VPC<br>access](cognito-auth.md "cognito-auth.md").                                                                                                                                                                                                                                                                | 7 September 2021  |
| Started tracking changes                                                                                                                                       | Amazon OpenSearch Service now tracks changes to AWS-managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 7 September 2021  |
