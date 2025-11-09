End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# AWS managed policies for AWS Panorama

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

AWS Panorama provides the following managed policies. For the full contents and change history of each policy, see
the linked pages in the IAM console.

######

- [AWSPanoramaFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSPanoramaFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSPanoramaFullAccess") – Provides full access to AWS Panorama, AWS Panorama access points in Amazon S3, appliance credentials in AWS Secrets Manager,
  and appliance logs in Amazon CloudWatch. Includes permission to create a [service-linked role](permissions-services.md "permissions-services.md") for AWS Panorama.
- [AWSPanoramaServiceLinkedRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSPanoramaServiceLinkedRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSPanoramaServiceLinkedRolePolicy") – Allows AWS Panorama to manage resources in AWS IoT, AWS Secrets Manager, and AWS Panorama.
- [AWSPanoramaApplianceServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSPanoramaApplianceServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSPanoramaApplianceServiceRolePolicy") – Allows an AWS Panorama Appliance to upload logs to CloudWatch, and to get objects from
  Amazon S3 access points created by AWS Panorama.

## AWS Panorama updates to AWS managed policies

The following table describes updates to managed policies for AWS Panorama.

| Change                                                               | Description                                                                                                                                                                                                                                                                               | Date       |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| AWSPanoramaApplianceServiceRolePolicy – Update to an existing policy | Replace StringLike condition with ArnLike for writing ARNs.                                                                                                                                                                                                                               | 2024-12-10 |
| AWSPanoramaFullAccess – Update to an existing policy                 | Replace StringLike condition with ArnLike for writing ARNs.                                                                                                                                                                                                                               | 2024-12-10 |
| AWSPanoramaFullAccess – Update to an existing policy                 | Added permissions to the user policy to allow users to view log groups in the CloudWatch Logs console.                                                                                                                                                                                    | 2022-01-13 |
| AWSPanoramaFullAccess – Update to an existing policy                 | Added permissions to the user policy to allow users to manage the AWS Panorama [service-linked role](using-service-linked-roles.md "using-service-linked-roles.md"), and to access AWS Panorama resources in<br>other services including IAM, Amazon S3, CloudWatch, and Secrets Manager. | 2021-10-20 |
| AWSPanoramaApplianceServiceRolePolicy – New policy                   | New policy for the AWS Panorama Appliance service role                                                                                                                                                                                                                                    | 2021-10-20 |
| AWSPanoramaServiceLinkedRolePolicy – New policy                      | New policy for the AWS Panorama service-linked role.                                                                                                                                                                                                                                      | 2021-10-20 |
| AWS Panorama started tracking changes                                | AWS Panorama started tracking changes for its AWS managed policies.                                                                                                                                                                                                                       | 2021-10-20 |
