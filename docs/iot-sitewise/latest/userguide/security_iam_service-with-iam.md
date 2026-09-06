

# How AWS IoT SiteWise works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use AWS Identity and Access Management (IAM) to manage access to AWS IoT SiteWise, you should understand what IAM features are available to use with AWS IoT SiteWise.


|  IAM feature  |  Supported by AWS IoT SiteWise?  | 
| --- | --- | 
| [Identity-based policies with resource-level permissions](security_iam_service-with-iam-id-based-policies.md) | Yes | 
| [Policy actions](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-actions) | Yes | 
| [Policy resources](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-resources) | Yes | 
| [Policy condition keys](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-conditionkeys) | Yes | 
| Resource-based policies | No | 
| Access control lists (ACLs) | No | 
| [Tags-based authorization (ABAC)](security_iam_service-with-iam-tags.md) | Yes | 
| [Temporary credentials](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-tempcreds) | Yes | 
| [Forward access sessions (FAS) ](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-principal-permissions) | Yes | 
| [Service-linked roles](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service-linked) | Yes | 
| [Service roles](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service-linked) | Yes | 

To get a high-level view of how AWS IoT SiteWise and other AWS services work with IAM, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Contents**
+ [AWS IoT SiteWise IAM roles](security_iam_service-with-iam-roles.md)
  + [Use temporary credentials with AWS IoT SiteWise](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-tempcreds)
  + [Forward access sessions (FAS) for AWS IoT SiteWise](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-principal-permissions)
  + [Service-linked roles](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service-linked)
  + [Service roles](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service)
  + [Choose an IAM role in AWS IoT SiteWise](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-choose)
+ [Authorization based on AWS IoT SiteWise tags](security_iam_service-with-iam-tags.md)
+ [AWS IoT SiteWise identity-based policies](security_iam_service-with-iam-id-based-policies.md)
  + [Policy actions](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-actions)
    + [BatchPutAssetPropertyValue authorization](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-batchputassetpropertyvalue-action)
  + [Policy resources](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-resources)
  + [Policy condition keys](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-conditionkeys)
  + [Examples](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-examples)
+ [AWS IoT SiteWise identity-based policy examples](security_iam_id-based-policy-examples.md)
  + [Policy best practices](security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices)
  + [Use the AWS IoT SiteWise console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console)
  + [Allow users to view their own permissions](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-own-permissions)
  + [Allow users to ingest data to assets in one hierarchy](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-ingest-to-one-asset-hierarchy)
  + [View AWS IoT SiteWise assets based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-asset-tags)
+ [Manage access using policies in AWS IoT SiteWise](security_iam_access-manage.md)
  + [Identity-based policies](security_iam_access-manage.md#security_iam_access-manage-id-based-policies)
  + [Resource-based policies](security_iam_access-manage.md#security_iam_access-manage-resource-based-policies)
  + [Access control lists (ACLs)](security_iam_access-manage.md#security_iam_access-manage-acl)
  + [Other policy types](security_iam_access-manage.md#security_iam_access-manage-other-policies)
  + [Multiple policy types](security_iam_access-manage.md#security_iam_access-manage-multiple-policies)