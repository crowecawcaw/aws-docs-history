# Using tags with IAM policies

You can apply tag-based resource-level permissions in the IAM policies you use for AWS IoT
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

The condition context keys and values in an IAM policy apply only to those AWS IoT actions
where an identifier for a resource capable of being tagged is a required parameter. For
example, the use of [DescribeEndpoint](../apireference/API_DescribeEndpoint.md "../apireference/API_DescribeEndpoint.md") is not
allowed or denied on the basis of condition context keys and values because no taggable
resource (thing groups, thing types, topic rules, jobs, or security profile) is referenced
in this request. For more information about AWS IoT resources that are taggable and condition
keys they support, read [Actions, resources, and condition keys for AWS IoT](../../../service-authorization/latest/reference/list_awsiot.md "../../../service-authorization/latest/reference/list_awsiot.md").

For more information about using tags, see [Controlling Access Using
Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _AWS Identity and Access Management User Guide_. The [IAM JSON Policy
Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") section of that guide has detailed syntax, descriptions, and examples of
the elements, variables, and evaluation logic of JSON policies in IAM.

The following example policy applies two tag-based restrictions for the
`ThingGroup` actions. An IAM user restricted by this policy:

- Can't create a thing group the tag "env=prod" (in the example, see the line
  `"aws:RequestTag/env" : "prod"`).
- Can't modify or access a thing group that has an existing tag "env=prod" (in the
  example, see the line `"aws:ResourceTag/env" : "prod"`).

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "iot:CreateThingGroup",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/env": "prod"
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "iot:CreateThingGroup",
 "iot:DeleteThingGroup",
 "iot:DescribeThingGroup",
 "iot:UpdateThingGroup"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/env": "prod"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:CreateThingGroup",
 "iot:DeleteThingGroup",
 "iot:DescribeThingGroup",
 "iot:UpdateThingGroup"
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
