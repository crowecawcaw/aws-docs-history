# IAM policies for

Amazon Connect

If you want AWS End User Messaging SMS to use an existing IAM role or if you create a new role, attach
the following policies to that role so that AWS End User Messaging SMS can assume it. For information about
how to modify an existing trust relationship of a role, see [Modifying a Role](../../../IAM/latest/UserGuide/id_roles_manage.md "../../../IAM/latest/UserGuide/id_roles_manage.md") in the [_IAM
user guide_](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").

To create new IAM polices, do the following:

1.  Create a new **permission policy** by following
    the directions in [Creating policies using the JSON editor](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") in the
    IAM User Guide.
    1. In step 4 use the **permission policy**
       defined below.

2.  Create a new **trust policy** by following the
    directions in [Creating a role using custom trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in
    the IAM User Guide.

        1. In step 4 use the **trust policy**
         defined below.
        2. In step 11 add the **permission policy**
         that you created in the previous step.

    The following is the **permission policy** for the IAM
    role to allow for publishing to Amazon Connect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "connect:SendChatIntegrationEvent"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following is the **trust policy** for the IAM role,
make the following changes:

- Replace `accountId` with the unique ID for your
  AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SMSVoice",
 "Effect": "Allow",
 "Principal": {
 "Service": "sms-voice.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`accountId`"
 }
 }
 }
 ]
}`

```
