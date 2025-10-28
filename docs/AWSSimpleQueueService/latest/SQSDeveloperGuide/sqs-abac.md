# Attribute-based access control for Amazon SQS

## What is ABAC?

Attribute-based access control (ABAC) is an authorization process that defines permissions
based on tags that are attached to users and AWS resources. ABAC provides
granular and flexible access control based on attributes and values, reduces security risk
related to reconfigured role-based policies, and centralizes auditing and access policy
management. For more details about ABAC, see [What is ABAC for
AWS](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

Amazon SQS supports ABAC by allowing you to control access to your Amazon SQS queues based on the
tags and aliases that are associated with an Amazon SQS queue. The tag and alias condition keys
that enable ABAC in Amazon SQS authorize IAM principals to use Amazon SQS queues without editing
policies or managing grants. To learn more about ABAC condition keys, see [Condition keys for Amazon SQS](../../../service-authorization/latest/reference/list_amazonsqs.md#amazonsqs-policy-keys "../../../service-authorization/latest/reference/list_amazonsqs.md#amazonsqs-policy-keys") in the _Service Authorization Reference_.

With ABAC, you can use tags to configure IAM access permissions and policies for your
Amazon SQS queues, which helps you to scale your permissions management. You can create a single
permissions policy in IAM using tags that you add to each business role—without
having to update the policy each time you add a new resource. You can also attach tags to
IAM principals to create an ABAC policy. You can design ABAC policies to allow Amazon SQS
operations when the tag on the IAM user role that's making the call matches the Amazon SQS queue
tag. To learn more about tagging in AWS, see [AWS Tagging Strategies](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") and
[Amazon SQS cost allocation tags](sqs-queue-tags.md "sqs-queue-tags.md").

###### Note

ABAC for Amazon SQS is currently available in all AWS Commercial Regions where
Amazon SQS is available, with the following exceptions:

- Asia Pacific (Hyderabad)
- Asia Pacific (Melbourne)
- Europe (Spain)
- Europe (Zurich)

## Why should I use ABAC in Amazon SQS?

Here are some benefits of using ABAC in Amazon SQS:

- ABAC for Amazon SQS requires fewer permissions policies. You don't have to create different
  policies for different job functions. You can use resource and request tags that apply to
  more than one queue, which reduces operational overhead.
- Use ABAC to scale teams quickly. Permissions for new resources are automatically
  granted based on tags when resources are appropriately tagged during their
  creation.
- Use permissions on the IAM principal to restrict resource access. You can create
  tags for the IAM principal and use them to restrict access to specific actions that
  match the tags on the IAM principal. This helps you to automate the process of granting
  request permissions.
- Track who's accessing your resources. You can determine the identity of a session by
  looking at user attributes in AWS CloudTrail.

###### Topics

- [Tagging for access control](sqs-abac-tagging-resource-control.md "sqs-abac-tagging-resource-control.md")
- [Creating IAM users and Amazon SQS queues](sqs-abac-creating-queues.md "sqs-abac-creating-queues.md")
- [Testing attribute-based access control](sqs-abac-testing-access-control.md "sqs-abac-testing-access-control.md")
