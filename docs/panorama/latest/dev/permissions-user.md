End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# Identity-based IAM policies for AWS Panorama

To grant users in your account access to AWS Panorama, you use identity-based policies in AWS Identity and Access Management (IAM). Apply
identity-based policies to IAM roles that are associated with a user. You can also grant users in another account
permission to assume a role in your account and access your AWS Panorama resources.

AWS Panorama provides managed policies that grant access to AWS Panorama API actions and, in some cases, access to other
services used to develop and manage AWS Panorama resources. AWS Panorama updates the managed policies as needed, to ensure that
your users have access to new features when they're released.

- **AWSPanoramaFullAccess** – Provides full access to AWS Panorama, AWS Panorama access points in Amazon S3, appliance credentials in AWS Secrets Manager,
  and appliance logs in Amazon CloudWatch. Includes permission to create a [service-linked role](permissions-services.md "permissions-services.md") for AWS Panorama. [View policy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSPanoramaFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSPanoramaFullAccess")
  The `AWSPanoramaFullAccess` policy allows you to tag AWS Panorama resources, but does not have all tag-related
  permissions used by the AWS Panorama console. To grant these permissions, add the following policy.

- **ResourceGroupsandTagEditorFullAccess** – [View policy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess")
  The `AWSPanoramaFullAccess` policy does not include permission to purchase devices from the AWS Panorama
  console. To grant these permissions, add the following policy.

- **ElementalAppliancesSoftwareFullAccess** – [View policy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ElementalAppliancesSoftwareFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ElementalAppliancesSoftwareFullAccess")
  Managed policies grant permission to API actions without restricting the resources that a user can modify. For
  finer-grained control, you can create your own policies that limit the scope of a user's permissions. Use the
  full-access policy as a starting point for your policies.

###### Creating service roles

The first time you use [the AWS Panorama console](https://console.aws.amazon.com/panorama/home "https://console.aws.amazon.com/panorama/home"), you need
permission to create the [service role](permissions-services.md "permissions-services.md") used by the AWS Panorama Appliance. A
service role gives a service permission to manage resources or interact with other services. Create this role
before granting access to your users.

For details on the resources and conditions that you can use to limit the scope of a user's permissions in
AWS Panorama, see [Actions, resources, and condition keys for AWS Panorama](../../../service-authorization/latest/reference/list_awspanorama.md "../../../service-authorization/latest/reference/list_awspanorama.md")
in the Service Authorization Reference.
