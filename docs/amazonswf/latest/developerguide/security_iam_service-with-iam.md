# How Amazon Simple Workflow Service works with IAM

Before you use IAM to manage access to Amazon SWF, learn what IAM features are
available to use with Amazon SWF.

| IAM features you can use with Amazon Simple Workflow Service                                                                                                                                            | IAM feature | Amazon SWF support |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------ |
| [Identity-based policies](swf-dev-iam.md#security_iam_service-with-iam-id-based-policies "swf-dev-iam.md#security_iam_service-with-iam-id-based-policies")                                              | Yes         |
| [Resource-based policies](swf-dev-iam.md#security_iam_service-with-iam-resource-based-policies "swf-dev-iam.md#security_iam_service-with-iam-resource-based-policies")                                  | No          |
| [Policy actions](swf-dev-iam.md#security_iam_service-with-iam-id-based-policies-actions "swf-dev-iam.md#security_iam_service-with-iam-id-based-policies-actions")                                       | Yes         |
| [Policy resources](swf-dev-iam.md#security_iam_service-with-iam-id-based-policies-resources "swf-dev-iam.md#security_iam_service-with-iam-id-based-policies-resources")                                 | Yes         |
| [Policy condition keys (service-specific)](swf-dev-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys "swf-dev-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes         |
| [ACLs](swf-dev-iam.md#security_iam_service-with-iam-acls "swf-dev-iam.md#security_iam_service-with-iam-acls")                                                                                           | No          |
| [ABAC (tags in<br>policies)](swf-dev-iam.md#security_iam_service-with-iam-tags "swf-dev-iam.md#security_iam_service-with-iam-tags")                                                                     | Partial     |
| [Temporary<br>credentials](swf-dev-iam.md#security_iam_service-with-iam-roles-tempcreds "swf-dev-iam.md#security_iam_service-with-iam-roles-tempcreds")                                                 | Yes         |
| [Principal permissions](swf-dev-iam.md#security_iam_service-with-iam-principal-permissions "swf-dev-iam.md#security_iam_service-with-iam-principal-permissions")                                        | Yes         |
| [Service<br>roles](swf-dev-iam.md#security_iam_service-with-iam-roles-service "swf-dev-iam.md#security_iam_service-with-iam-roles-service")                                                             | Yes         |
| [Service-linked roles](swf-dev-iam.md#security_iam_service-with-iam-roles-service-linked "swf-dev-iam.md#security_iam_service-with-iam-roles-service-linked")                                           | No          |

To get a high-level view of how Amazon SWF and other AWS services work with most IAM
features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.
