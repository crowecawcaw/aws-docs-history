End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Using the AWS IoT Events

console

To access the AWS IoT Events console, you must have a minimum set of permissions. These
permissions must allow you to list and view details about the AWS IoT Events resources in your
AWS account. If you create an identity-based policy that is more restrictive than the
minimum required permissions, the console won't function as intended for entities (users
or roles) with that policy.

To ensure that those entities can still use the AWS IoT Events console, also attach the
following AWS managed policy to the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotevents:BatchPutMessage",
 "iotevents:BatchUpdateDetector",
 "iotevents:CreateDetectorModel",
 "iotevents:CreateInput",
 "iotevents:DeleteDetectorModel",
 "iotevents:DeleteInput",
 "iotevents:DescribeDetector",
 "iotevents:DescribeDetectorModel",
 "iotevents:DescribeInput",
 "iotevents:DescribeLoggingOptions",
 "iotevents:ListDetectorModelVersions",
 "iotevents:ListDetectorModels",
 "iotevents:ListDetectors",
 "iotevents:ListInputs",
 "iotevents:ListTagsForResource",
 "iotevents:PutLoggingOptions",
 "iotevents:TagResource",
 "iotevents:UntagResource",
 "iotevents:UpdateDetectorModel",
 "iotevents:UpdateInput",
 "iotevents:UpdateInputRouting"
 ],
 "Resource": "arn:aws:iotevents:`us-east-1`:`123456789012`:detectorModel/`your-detector-model-name`",
 "Resource": "arn:aws:iotevents:`us-east-1`:`123456789012`:input/`your-input-name`"
 }
 ]
}`

```

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that you're trying to perform.
