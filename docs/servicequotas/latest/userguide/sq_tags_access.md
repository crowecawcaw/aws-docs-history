# Controlling access using Service Quotas tags

To control access to Service Quotas resources based on tags, you provide the tag information in
the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`aws:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about these condition
keys, see [Controlling access to AWS
resources using resource tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the
_IAM User Guide_.

For example, when you attach the following policy to an AWS Identity and Access Management (IAM) role or
user, that principal can request an increase to Amazon Athena applied quotas
that are tagged with the tag key `Owner` and tag value
`admin`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["servicequotas:RequestServiceQuotaIncrease"],
 "Resource": "arn:aws:servicequotas:*:*:athena/*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/Owner": "admin"}
 }
 }
 ]
}`

```

You can also attach tags to IAM principals to use attribute-based access control
(ABAC). ABAC is an authorization strategy that defines permissions based on attributes.
Tagging entities and resources is the first step of ABAC. Then you design ABAC policies
to allow operations when the principal's tag matches the tag on the resource that
they're trying to access. ABAC is helpful in environments that are growing rapidly and
helps with situations where policy management becomes cumbersome.

For more information about ABAC, see [What is
ABAC?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with
steps for setting up ABAC, see [IAM tutorial:
Define permissions to access AWS resources based on tags](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the
_IAM User Guide_.
