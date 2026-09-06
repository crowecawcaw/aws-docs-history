

# Resource control policies (RCPs)
<a name="orgs_manage_policies_rcps"></a>

**Note**  
**Service control policies (SCPs) and resource control policies (RCPs)**  
Use an SCP when you need to limit permissions of IAM principals within your organization's member accounts.  
Use an RCP when you need to restrict IAM principals that are external to your organization accounts making requests to access resources within your organization’s member accounts.  
For more information, see [Understanding SCPs and RCPs](orgs_manage_policies_authorization_policies.md).

Resource control policies (RCPs) are a type of organization policy that you can use to manage permissions in your organization. RCPs offer central control over the maximum available permissions for resources in your organization. RCPs help you to ensure resources in your accounts stay within your organization’s access control guidelines. RCPs are available only in an organization that has [all features enabled](orgs_manage_org_support-all-features.md). RCPs aren't available if your organization has enabled only the consolidated billing features. For instructions on enabling RCPs, see [Enabling a policy type](enable-policy-type.md).

RCPs alone are not sufficient in granting permissions to the resources in your organization. No permissions are granted by an RCP. An RCP defines a permissions guardrail, or sets limits, on the actions that identities can take on resources in your organizations. The administrator must still attach identity-based policies to IAM users or roles, or resource-based policies to resources in your accounts to actually grant permissions. For more information, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) in the *IAM User Guide*.

The [effective permissions](#rcp-effects-on-permissions) are the logical intersection between what is allowed by the RCPs and [service control policies (SCPs)](orgs_manage_policies_scps.md) and what is allowed by the identity-based and resource-based policies.

**RCPs don't affect resources in the management account**  
RCPs don't affect resources in the management account. They only affect resources in the member accounts within your organization. This also means that RCPs apply to member accounts that are designated as delegated administrators.

****Topics on this page****
+ [List of AWS services that support RCPs](#rcp-supported-services)
+ [Testing effects of RCPs](#rcp-warning-testing-effect)
+ [Maximum size of RCPs](#rcp-size-limit)
+ [Attaching RCPs to different levels in the organization](#rcp-about-inheritance)
+ [RCP effects on permissions](#rcp-effects-on-permissions)
+ [Resources and entities not restricted by RCPs](#actions-not-restricted-by-rcps)
+ [RCP evaluation](orgs_manage_policies_rcps_evaluation.md)
+ [RCP syntax](orgs_manage_policies_rcps_syntax.md)
+ [Resource control policy examples](orgs_manage_policies_rcps_examples.md)

## List of AWS services that support RCPs
<a name="rcp-supported-services"></a>

RCPs apply to actions for the following AWS services:
+ [Amazon CloudFront](https://docs.aws.amazon.com/cloudfront) `(prefix:cloudfront)`
+ [Amazon CloudSearch](https://docs.aws.amazon.com/cloudsearch) `(prefix:cloudsearch)`
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/cloudwatch) `(prefix:logs)`
+ [Network Synthetic Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html) `(prefix:networkmonitor)`
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito) `(prefix:cognito-identity)`
+ [Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito) `(prefix:cognito-idp)`
+ [Amazon Comprehend](https://docs.aws.amazon.com/comprehend) `(prefix:comprehend)`
+ [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical) `(prefix:comprehendmedical)`
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose) `(prefix:firehose)`
+ [Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb) `(prefix:dynamodb)`
+ [DynamoDB Accelerator](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html) `(prefix:dax)`
+ [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling) `(prefix:autoscaling)`
+ [Amazon Elastic Container Registry](https://docs.aws.amazon.com/ecr) `(prefix:ecr)`
+ [Amazon Inspector Scan](https://docs.aws.amazon.com/inspector) `(prefix:inspector-scan)`
+ [Amazon Kendra](https://docs.aws.amazon.com/kendra) `(prefix:kendra)`
+ [Amazon Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video) `(prefix:kinesisvideo)`
+ [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb) `(prefix:memorydb)`
+ [Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service) `(prefix:aoss)`
+ [Amazon Polly](https://docs.aws.amazon.com/polly) `(prefix:polly)`
+ [Amazon S3](https://docs.aws.amazon.com/s3) `(prefix:s3)`
+ [Amazon SQS](https://docs.aws.amazon.com/sqs) `(prefix:sqs)`
+ [Amazon Textract](https://docs.aws.amazon.com/textract) `(prefix:textract)`
+ [Amazon Timestream for InfluxDB](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb) `(prefix:timestream-influxdb)`
+ [Amazon Transcribe](https://docs.aws.amazon.com/transcribe) `(prefix:transcribe)`
+ [Amazon Translate](https://docs.aws.amazon.com/translate) `(prefix:translate)`
+ [Amazon AppStream](https://docs.aws.amazon.com/appstream2) `(prefix:appstream)`
+ [AWS AppConfig](https://docs.aws.amazon.com/appconfig) `(prefix:appconfig)`
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild) `(prefix:codebuild)`
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit) `(prefix:codecommit)`
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline) `(prefix:codepipeline)`
+ [AWS Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub) `(prefix:cost-optimization-hub)`
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge) `(prefix:events)`
+ [AWS Fault Injection Service](https://docs.aws.amazon.com/fis) `(prefix:fis)`
+ [AWS Health](https://docs.aws.amazon.com/health) `(prefix:health)`
+ [AWS Key Management Service](https://docs.aws.amazon.com/kms) `(prefix:kms)`
+ [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service) `(prefix:opensearch)`
+ [AWS Pricing Calculator](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html) `(prefix:pricing)`
+ [AWS Private CA Connector for Active Directory](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-ad) `(prefix:pca-connector-ad)`
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager) `(prefix:secretsmanager)`
+ [AWS Security Token Service](https://docs.aws.amazon.com/iam/#sts) `(prefix:sts)`
+ [AWS Sign-In](https://docs.aws.amazon.com/signin) `(prefix:signin)`
+ [AWS Support](https://docs.aws.amazon.com/aws-support) `(prefix:support)`
+ [AWS Transfer Family](https://docs.aws.amazon.com/transfer) `(prefix:transfer)`
+ [AWS WAF](https://docs.aws.amazon.com/waf) `(prefix:wafv2)`

## Testing effects of RCPs
<a name="rcp-warning-testing-effect"></a>

AWS strongly recommends that you don't attach RCPs to the root of your organization without thoroughly testing the impact that the policy has on resources in your accounts. You can begin by attaching RCPs to individual test accounts, moving them up to OUs lower in the hierarchy, and then working your way up through the organization structure as needed. One way to determine impact is to review AWS CloudTrail logs for Access Denied errors.

## Maximum size of RCPs
<a name="rcp-size-limit"></a>

All characters in your RCP count against its [maximum size](orgs_reference_limits.md#min-max-values). The examples in this guide show the RCPs formatted with extra white space to improve their readability. However, to save space if your policy size approaches the maximum size, you can delete any white space, such as space characters and line breaks that are outside quotation marks.

**Tip**  
Use the visual editor to build your RCP. It automatically removes extra white space.

## Attaching RCPs to different levels in the organization
<a name="rcp-about-inheritance"></a>

You can attach RCPs directly to individual accounts, OUs, or the organization root. For a detailed explanation of how RCPs work, see [RCP evaluation](orgs_manage_policies_rcps_evaluation.md).

## RCP effects on permissions
<a name="rcp-effects-on-permissions"></a>

RCPs are a type of AWS Identity and Access Management (IAM) policy. They are most closely related to [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html). However, an RCP never grants permissions. Instead, RCPs are access controls that specify the maximum available permissions for resources in your organization. For more information, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the *IAM User Guide*.
+ RCPs apply to resources for a subset of AWS services. For more information, see [List of AWS services that support RCPs](#rcp-supported-services).
+ RCPs ***affect only resources*** that are managed by accounts that are part of the organization which has attached the RCPs. They don't affect resources from accounts outside the organization. For example, consider an Amazon S3 bucket that's owned by Account A in an organization. The bucket policy (a resource-based policy) grants access to users from Account B outside the organization. Account A has an RCP attached. That RCP applies to the S3 bucket in Account A even when accessed by users from Account B. However, that RCP does not apply to resources in Account B when accessed by users in Account A.
+ An RCP restricts permissions for resources in member accounts. Any resource in an account has only those permissions permitted by ***every*** parent above it. If a permission is blocked at any level above the account, a resource in the affected account does not have that permission, even if the resource owner attaches a resource-based policy that allows full access to any user.
+ RCPs apply to the resources that are authorized as part of an operation request. These resources can be found in the “Resource type” column of the Action table in the [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html#actions_table). If a resource is specified in the "Resource type" column, then the RCPs of the calling principal account are applied. For example, `s3:GetObject` authorizes the object resource. Whenever a `GetObject` request is made, an applicable RCP will apply to determine whether the requesting principal can invoke the `GetObject` operation. An *applicable RCP* is an RCP that has been attached to an account, to an organizational unit (OU), or to the root of the organization that owns the resource being accessed.
+ RCPs affect only resources in ***member*** accounts in the organization. They have no effect on resources in the management account. This also means that RCPs apply to member accounts that are designated as delegated administrators. For more information, see [Best practices for the management account](orgs_best-practices_mgmt-acct.md).
+ When a principal makes a request to access a resource within an account that has an attached RCP (a resource with an applicable RCP), the RCP is included in the policy evaluation logic to determine whether the principal is allowed or denied access.
+ RCPs impact the effective permissions of principals trying to access resources in a member account with an applicable RCP, regardless of whether the principals belong to the same organizations or not. This includes root users. The exception is when principals are service-linked roles because RCPs do not apply to calls made by service-linked roles. Service-linked roles enable AWS services to perform necessary actions on your behalf and can't be restricted by RCPs. 
+ Users and roles must still be granted permissions with appropriate IAM permission policies, including identity-based and resource-based policies. A user or role without any IAM permission policies has no access, even if an applicable RCP allows all services, all actions, and all resources.

## Resources and entities not restricted by RCPs
<a name="actions-not-restricted-by-rcps"></a>

You ***can't*** use RCPs to restrict the following:
+ Any action on resources in the management account.
+ RCPs do not impact the effective permissions of any service-linked role. Service-linked roles are a unique type of IAM role that is linked directly to an AWS service and include all the permissions that the service requires to call other AWS services on your behalf. The permissions of service-linked roles can't be restricted by RCPs. RCPs also do not impact AWS services' ability to assume a service-linked role; that is, the service-linked role's trust policy is also not impacted by RCPs.
+ RCPs do not apply to [AWS managed keys for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk). AWS managed keys are created, managed, and used on your behalf by an AWS service. You cannot change or manage their permissions.
+ RCPs do not impact following permissions:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html)