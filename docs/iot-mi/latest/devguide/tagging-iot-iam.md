# Using tags with IAM policies

You can apply tag-based resource-level permissions in the IAM policies you use for managed integrations
API actions. This gives you better control over what resources a user can create, modify, or
use. You use the `Condition` element (also called the `Condition` block)
with the following condition context keys and values in an IAM policy to control user access
(permissions) based on a resource's tags:

- Use `aws:ResourceTag/`tag-key`:
`tag-value`` to allow or deny user actions on resources
  with specific tags.
- Use `aws:RequestTag/`tag-key`:
`tag-value`` to require that a specific tag be used (or
  not used) when making an API request to create or modify a resource that allows
  tags.
- Use `aws:TagKeys: [`tag-key`, ...]` to require
  that a specific set of tag keys be used (or not used) when making an API request to create
  or modify a resource that allows tags.

###### Note

The condition context keys and values in an IAM policy apply only to those managed integrations
actions where an identifier for a resource capable of being tagged is a required parameter.
For example, the use of [GetCustomEndpoint](../APIReference/API_GetCustomEndpoint.md "../APIReference/API_GetCustomEndpoint.md") is not
allowed or denied on the basis of condition context keys and values because no taggable
resource (managed things, provisioning profiles, credential lockers, over-the-air tasks) is
referenced in this request. For more information about managed integrations resources that are taggable
and condition keys they support, read [Actions, resources, and condition keys for AWS IoT managed integrations feature of
AWS IoT Device Management](../../../service-authorization/latest/reference/list_awsiotmanagedintegrationsfeatureofiotdevicemanagement.md "../../../service-authorization/latest/reference/list_awsiotmanagedintegrationsfeatureofiotdevicemanagement.md").

For more information about using tags, see [Controlling Access Using
Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _AWS Identity and Access Management User Guide_. The [IAM JSON Policy
Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") section of that guide has detailed syntax, descriptions, and examples of
the elements, variables, and evaluation logic of JSON policies in IAM.

The following example policy applies two tag-based restrictions for the
`CreateManagedThing` action. An IAM user restricted by this policy:

- Can't create a managed thing with the tag "env=prod" (in the example, see the line
  `"aws:RequestTag/env" : "prod"`).
- Can't modify or access a managed thing that has an existing tag "env=prod" (in the
  example, see the line `"aws:ResourceTag/env" : "prod"`).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "iotmanagedintegrations:CreateManagedThing",
 "Resource": "arn:aws:iotmanagedintegrations:`us-east-1`:`123456789012`:managed-thing/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/env": "prod"
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "iotmanagedintegrations:CreateManagedThing",
 "iotmanagedintegrations:DeleteManagedThing",
 "iotmanagedintegrations:GetManagedThing",
 "iotmanagedintegrations:UpdateManagedThing"
 ],
 "Resource": "arn:aws:iotmanagedintegrations:`us-east-1`:`123456789012`:managed-thing/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/env": "prod"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotmanagedintegrations:CreateManagedThing",
 "iotmanagedintegrations:DeleteManagedThing",
 "iotmanagedintegrations:GetManagedThing",
 "iotmanagedintegrations:UpdateManagedThing"
 ],
 "Resource": "*"
 }
 ]
}`

```

You can also specify multiple tag values for a given tag key by enclosing them in a list,
like this:

```

            "StringEquals" : {
              "aws:ResourceTag/env" : ["dev", "test"]
            }
```

###### Note

If you allow or deny users access to resources based on tags, you must consider
explicitly denying users the ability to add those tags to or remove them from the same
resources. Otherwise, it's possible for a user to circumvent your restrictions and gain
access to a resource by modifying its tags.
