End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# View AWS IoT Events

inputs based on tags

Tags help you organize AWS IoT Events resources. You can use conditions in your identity-based
policy to control access to AWS IoT Events resources based on tags. This example shows how you
might create a policy that allows viewing an `input`. However,
permission is granted only if the `input` tag
`Owner` has the value of that user's user name. This policy also grants
the permissions necessary to complete this action on the console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListInputsInConsole",
 "Effect": "Allow",
 "Action": "iotevents:ListInputs",
 "Resource": "*"
 },
 {
 "Sid": "ViewInputsIfOwner",
 "Effect": "Allow",
 "Action": "iotevents:ListInputs",
 "Resource": "arn:aws:iotevents:*:*:input/*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

You can attach this policy to the users in your account. If a user named
`richard-roe` attempts to view an AWS IoT Events `input`,
the `input` must be tagged `Owner=richard-roe` or
`owner=richard-roe`. Otherwise he is denied access. The condition tag key
`Owner` matches both `Owner` and `owner` because
condition key names are not case-sensitive. For more information, see [IAM JSON policy
elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
