# Editing the trust relationship for an existing IAM

role

You can assign your existing IAM roles to your AWS Directory Service users and groups. To do this,
however, the role must have a trust relationship with AWS Directory Service. When you use AWS Directory Service to
create a role using the procedure in [Creating a new IAM role](create_role.md "create_role.md"), this trust relationship is automatically set.

###### Note

You only need to establish this trust relationship for IAM roles that are not
created by AWS Directory Service.

###### To establish a trust relationship for an existing IAM role to AWS Directory Service

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, under **Access
   management**, choose **Roles**.

The console displays the roles for your account. 3. Choose the name of the role that you want to modify, and once on the role's
page, select the **Trust relationships** tab. 4. Choose **Edit trust policy**. 5. Under **Edit trust policy**, paste the following, and then
choose **Update policy**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "ds.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

You can also update this policy document using the AWS CLI. For more information, see
[update-trust](../../../cli/latest/reference/ds/update-trust.md "../../../cli/latest/reference/ds/update-trust.md") in the _AWS CLI Command Reference_.
