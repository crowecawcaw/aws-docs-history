End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Access one

AWS IoT Events input

Granular access control to AWS IoT Events inputs is important for maintaining security in
multi-user or multi-team environments. This section shows how to create IAM policies
that grant access to specific AWS IoT Events inputs while restricting access to others.

In this example, you can grant a user in your AWS account access to one of your
AWS IoT Events inputs, `exampleInput`. You also can allow the user to add, update, and
delete inputs.

The policy grants the
`iotevents:ListInputs`, `iotevents:DescribeInput`,
`iotevents:CreateInput`, `iotevents:DeleteInput`, and
`iotevents:UpdateInput` permissions to the user.
For an example
walkthrough for the Amazon Simple Storage Service (Amazon S3) that grants permissions to users and tests them
using the console, see [Controlling access to a bucket with
user policies](../../../AmazonS3/latest/userguide/walkthrough1.md "../../../AmazonS3/latest/userguide/walkthrough1.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ListInputsInConsole",
 "Effect":"Allow",
 "Action":[
 "iotevents:ListInputs"
 ],
 "Resource":"arn:aws:iotevents:`us-east-2`:`123456789012`:input/*"
 },
 {
 "Sid":"ViewSpecificInputInfo",
 "Effect":"Allow",
 "Action":[
 "iotevents:DescribeInput"
 ],
 "Resource":"arn:aws:iotevents:`us-east-1`:`123456789012`:input/`inputName`"
 },
 {
 "Sid":"ManageInputs",
 "Effect":"Allow",
 "Action":[
 "iotevents:CreateInput",
 "iotevents:DeleteInput",
 "iotevents:DescribeInput",
 "iotevents:ListInputs",
 "iotevents:UpdateInput"
 ],
 "Resource":"arn:aws:iotevents:`us-east-1`:`123456789012`:input/*"
 }
 ]
}`

```
