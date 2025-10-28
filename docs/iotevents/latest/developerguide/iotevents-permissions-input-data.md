End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Securing input data in AWS IoT Events

It's important to consider who can grant access to input data for use in a detector
model. If you have a user or entity whose overall permissions you want to restrict, but that
is permitted to create or update a detector model, you must also grant permission for that
user or entity to update input routing. This means that in addition to granting permission
for `iotevents:CreateDetectorModel` and
`iotevents:UpdateDetectorModel`, you must also grant permission for
`iotevents:UpdateInputRouting`.

###### Example

The following policy adds permission for
`iotevents:UpdateInputRouting`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "updateRoutingPolicy",
 "Effect": "Allow",
 "Action": [
 "iotevents:UpdateInputRouting"
 ],
 "Resource": "*"
 }
 ]
}`

```

You can specify a list of input Amazon Resource Names (ARNs) instead of the wildcard
"`*`" for the "`Resource`" to limit this permission to specific
inputs. This enables you to restrict access to the input data that is consumed by detector
models created or updated by the user or entity.
