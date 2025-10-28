# Security best practices for Resource Groups

The following best practices are general guidelines and don’t represent a complete
security solution. Because these best practices might not be appropriate or sufficient for
your environment, treat them as helpful considerations rather than prescriptions.

- **Use the principle of least privilege** to grant
  access to groups. Resource Groups supports resource-level permissions. Grant access to
  specific groups only as required for specific users. Avoid using asterisks in policy
  statements that assign permissions to all users or all groups. For more information
  about least privilege, see [Grant Least
  Privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _IAM User Guide_.
- **Keep private information out of public fields.**
  The name of a group is treated as service metadata. Group names are not encrypted.
  Do not put sensitive information in group names. Group descriptions are
  private.

Do not put private or sensitive information in tag keys or tag values.

- **Use authorization based on tagging** whenever
  appropriate. Resource Groups supports authorization based on tags. You can tag groups, then
  update policies that are attached to your IAM principals, such as users and roles,
  to set their level of access based on the tags that are applied to a group. For more
  information about how to use authorization based on tags, see [Controlling access
  to AWS resources using resource tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User
  Guide_.

Many AWS services support authorization based on tags for their resources. Be
aware that tag-based authorization might be configured for member resources in a
group. If access to a group's resources is restricted by tags, unauthorized users or
groups might not be able to perform actions or automations on those resources. For
example, if an Amazon EC2 instance in one of your groups is tagged with a tag key of
`Confidentiality` and a tag value of `High`, and you are
not authorized to run commands on resources tagged
`Confidentiality:High`, actions or automations that you perform on the
EC2 instance will fail, even if actions are successful for other resources in the
resource group. For more information about which services support tag-based
authorization for their resources, see [AWS
Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User
Guide_.

For more information about developing a tagging strategy for your AWS resources,
see [AWS Tagging Strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/ "https://aws.amazon.com/answers/account-management/aws-tagging-strategies/").
