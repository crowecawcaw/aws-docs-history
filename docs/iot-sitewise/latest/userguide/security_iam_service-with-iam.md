# How AWS IoT SiteWise works with IAM

Before you use AWS Identity and Access Management (IAM) to manage access to AWS IoT SiteWise, you should understand what
IAM features are available to use with AWS IoT SiteWise.

| IAM feature                                                                                                                                                                                                                                                  | Supported by AWS IoT SiteWise? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| [Identity-based<br>policies with resource-level permissions](security_iam_service-with-iam-id-based-policies.md "security_iam_service-with-iam-id-based-policies.md")                                                                                        | Yes                            |
| [Policy<br>actions](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-actions")                 | Yes                            |
| [Policy<br>resources](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-resources")           | Yes                            |
| [Policy condition keys](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-conditionkeys "security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes                            |
| Resource-based policies                                                                                                                                                                                                                                      | No                             |
| Access control lists<br>(ACLs)                                                                                                                                                                                                                               | No                             |
| [Tags-based authorization<br>(ABAC)](security_iam_service-with-iam-tags.md "security_iam_service-with-iam-tags.md")                                                                                                                                          | Yes                            |
| [Temporary<br>credentials](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-tempcreds "security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-tempcreds")                                                      | Yes                            |
| [Forward<br>access sessions (FAS)](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-principal-permissions "security_iam_service-with-iam-roles.md#security_iam_service-with-iam-principal-permissions")                                  | Yes                            |
| [Service-linked roles](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service-linked "security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service-linked")                                                | Yes                            |
| [Service<br>roles](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service-linked "security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service-linked")                                                    | Yes                            |

To get a high-level view of how AWS IoT SiteWise and other AWS services work with IAM, see
[AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Contents

- [AWS IoT SiteWise IAM
  roles](security_iam_service-with-iam-roles.md "security_iam_service-with-iam-roles.md")
  - [Use temporary credentials
    with AWS IoT SiteWise](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-tempcreds "security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-tempcreds")
  - [Forward access
    sessions (FAS) for AWS IoT SiteWise](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-principal-permissions "security_iam_service-with-iam-roles.md#security_iam_service-with-iam-principal-permissions")
  - [Service-linked
    roles](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service-linked "security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service-linked")
  - [Service roles](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service "security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-service")
  - [Choose an IAM role in
    AWS IoT SiteWise](security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-choose "security_iam_service-with-iam-roles.md#security_iam_service-with-iam-roles-choose")

- [Authorization based on AWS IoT SiteWise
  tags](security_iam_service-with-iam-tags.md "security_iam_service-with-iam-tags.md")
- [AWS IoT SiteWise identity-based
  policies](security_iam_service-with-iam-id-based-policies.md "security_iam_service-with-iam-id-based-policies.md")
  - [Policy
    actions](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-actions")
    - [BatchPutAssetPropertyValue authorization](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-batchputassetpropertyvalue-action "security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-batchputassetpropertyvalue-action")

  - [Policy
    resources](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-resources")
  - [Policy
    condition keys](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-conditionkeys "security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-conditionkeys")
  - [Examples](security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-examples "security_iam_service-with-iam-id-based-policies.md#security_iam_service-with-iam-id-based-policies-examples")

- [AWS IoT SiteWise identity-based policy
  examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
  - [Policy best
    practices](security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices "security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices")
  - [Use the AWS IoT SiteWise
    console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console")
  - [Allow users
    to view their own permissions](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-own-permissions "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-own-permissions")
  - [Allow users to ingest data to assets in one hierarchy](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-ingest-to-one-asset-hierarchy "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-ingest-to-one-asset-hierarchy")
  - [View AWS IoT SiteWise assets
    based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-asset-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-asset-tags")

- [Manage access using policies in AWS IoT SiteWise](security_iam_access-manage.md "security_iam_access-manage.md")
  - [Identity-based
    policies](security_iam_access-manage.md#security_iam_access-manage-id-based-policies "security_iam_access-manage.md#security_iam_access-manage-id-based-policies")
  - [Resource-based
    policies](security_iam_access-manage.md#security_iam_access-manage-resource-based-policies "security_iam_access-manage.md#security_iam_access-manage-resource-based-policies")
  - [Access control lists (ACLs)](security_iam_access-manage.md#security_iam_access-manage-acl "security_iam_access-manage.md#security_iam_access-manage-acl")
  - [Other policy types](security_iam_access-manage.md#security_iam_access-manage-other-policies "security_iam_access-manage.md#security_iam_access-manage-other-policies")
  - [Multiple policy
    types](security_iam_access-manage.md#security_iam_access-manage-multiple-policies "security_iam_access-manage.md#security_iam_access-manage-multiple-policies")
