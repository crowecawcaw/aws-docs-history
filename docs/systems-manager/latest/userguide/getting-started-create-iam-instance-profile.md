AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Create a custom

IAM role for Session Manager

You can create an AWS Identity and Access Management (IAM) role that grants Session Manager the permission
to perform actions on your Amazon EC2 managed instances. You can also include a
policy to grant the permissions needed for session logs to be sent to Amazon Simple Storage Service
(Amazon S3) and Amazon CloudWatch Logs.

After you create the IAM role, for information about how to attach the role
to an instance, see [Attach or Replace an Instance Profile](https://aws.amazon.com/premiumsupport/knowledge-center/attach-replace-ec2-instance-profile/ "https://aws.amazon.com/premiumsupport/knowledge-center/attach-replace-ec2-instance-profile/") at the AWS re:Post website.
For more information about IAM instance profiles and roles, see [Using instance profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md") in the _IAM User Guide_ and [IAM roles for
Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md") in the _Amazon Elastic Compute Cloud User Guide for Linux
Instances_. For more information about creating an IAM service
role for on-premises machines, see [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md").

###### Topics

- [Creating an IAM role with
  minimal Session Manager permissions (console)](#create-iam-instance-profile-ssn-only "#create-iam-instance-profile-ssn-only")
- [Creating an IAM
  role with permissions for Session Manager and Amazon S3 and CloudWatch Logs (console)](#create-iam-instance-profile-ssn-logging "#create-iam-instance-profile-ssn-logging")

## Creating an IAM role with

minimal Session Manager permissions (console)

Use the following procedure to create a custom IAM role with a policy
that provides permissions for only Session Manager actions on your
instances.

###### To create an instance profile with minimal Session Manager permissions

(console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, and
   then choose **Create policy**. (If a **Get
   Started** button is displayed, choose it, and then
   choose **Create Policy**.)
3. Choose the **JSON** tab.
4. Replace the default content with the following policy. To encrypt
   session data using AWS Key Management Service (AWS KMS), replace
   `key-name` with the Amazon Resource
   Name (ARN) of the AWS KMS key that you want to use.

###### Note

If the `ssmmessages:OpenControlChannel` permission
is removed from policies attached to your IAM instance profile
or IAM service role,SSM Agent on the managed node loses
connectivity to the Systems Manager service in the cloud. However, it can
take up to 1 hour for a connection to be terminated after the
permission is removed. This is the same behavior as when the
IAM instance role or IAM service role is deleted.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:UpdateInstanceInformation",
 "ssmmessages:CreateControlChannel",
 "ssmmessages:CreateDataChannel",
 "ssmmessages:OpenControlChannel",
 "ssmmessages:OpenDataChannel"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-name`"
 }
 ]
}`

```

For information about using a KMS key to encrypt session data,
see [Turn on KMS key
encryption of session data (console)](session-preferences-enable-encryption.md "session-preferences-enable-encryption.md").

If you won't use AWS KMS encryption for your session data, you can
remove the following content from the policy.

```
,
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": "`key-name`"
        }
```

5. Choose **Next: Tags**.
6. (Optional) Add tags by choosing **Add tag**, and
   entering the preferred tags for the policy.
7. Choose **Next: Review**.
8. On the **Review policy** page, for
   **Name**, enter a name for the inline policy,
   such as `SessionManagerPermissions`.
9. (Optional) For **Description**, enter a
   description for the policy.
10. Choose **Create policy**.
11. In the navigation pane, choose **Roles**, and
    then choose **Create role**.
12. On the **Create role** page, choose
    **AWS service**, and for **Use
    case**, choose **EC2**.
13. Choose **Next**.
14. On the **Add permissions** page, select the check
    box to the left of name of the policy you just created, such as
    `SessionManagerPermissions`.
15. Choose **Next**.
16. On the **Name, review, and create** page, for
    **Role name**, enter a name for the IAM role,
    such as `MySessionManagerRole`.
17. (Optional) For **Role description**, enter a
    description for the instance profile.
18. (Optional) Add tags by choosing **Add tag**, and
    entering the preferred tags for the role.

Choose **Create role**.

For information about `ssmmessages` actions, see [Reference: ec2messages,
ssmmessages, and other API operations](systems-manager-setting-up-messageAPIs.md "systems-manager-setting-up-messageAPIs.md").

## Creating an IAM

role with permissions for Session Manager and Amazon S3 and CloudWatch Logs (console)

Use the following procedure to create a custom IAM role with a policy
that provides permissions for Session Manager actions on your instances. The policy
also provides the permissions needed for session logs to be stored in
Amazon Simple Storage Service (Amazon S3) buckets and Amazon CloudWatch Logs log groups.

###### Important

To output session logs to an Amazon S3 bucket owned by a different
AWS account, you must add the `s3:PutObjectAcl` permission
to the IAM role policy. Additionally, you must ensure that the bucket
policy grants cross-account access to the IAM role used by the owning
account to grant Systems Manager permissions for managed instances. If the bucket
uses Key Management Service (KMS) encryption, then the bucket's KMS
policy must also grant this cross-account access. For more information
about configuring cross-account bucket permissions in Amazon S3, see [Granting cross-account bucket permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md") in the
_Amazon Simple Storage Service User Guide_. If the cross-account
permissions aren't added, the account that owns the Amazon S3 bucket can't
access the session output logs.

For information about specifying preferences for storing session logs, see
[Enabling and disabling session logging](session-manager-logging.md "session-manager-logging.md").

###### To create an IAM role with permissions for Session Manager and Amazon S3 and

CloudWatch Logs (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, and
   then choose **Create policy**. (If a **Get
   Started** button is displayed, choose it, and then
   choose **Create Policy**.)
3. Choose the **JSON** tab.
4. Replace the default content with the following policy. Replace
   each `example resource placeholder` with
   your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssmmessages:CreateControlChannel",
 "ssmmessages:CreateDataChannel",
 "ssmmessages:OpenControlChannel",
 "ssmmessages:OpenDataChannel",
 "ssm:UpdateInstanceInformation"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`s3-prefix`/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetEncryptionConfiguration"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-name`"
 },
 {
 "Effect": "Allow",
 "Action": "kms:GenerateDataKey",
 "Resource": "*"
 }
 ]
}`

```

5. Choose **Next: Tags**.
6. (Optional) Add tags by choosing **Add tag**, and
   entering the preferred tags for the policy.
7. Choose **Next: Review**.
8. On the **Review policy** page, for
   **Name**, enter a name for the inline policy,
   such as `SessionManagerPermissions`.
9. (Optional) For **Description**, enter a
   description for the policy.
10. Choose **Create policy**.
11. In the navigation pane, choose **Roles**, and
    then choose **Create role**.
12. On the **Create role** page, choose
    **AWS service**, and for **Use
    case**, choose **EC2**.
13. Choose **Next**.
14. On the **Add permissions** page, select the check
    box to the left of name of the policy you just created, such as
    `SessionManagerPermissions`.
15. Choose **Next**.
16. On the **Name, review, and create** page, for
    **Role name**, enter a name for the IAM role,
    such as `MySessionManagerRole`.
17. (Optional) For **Role description**, enter a
    description for the role.
18. (Optional) Add tags by choosing **Add tag**, and
    entering the preferred tags for the role.
19. Choose **Create role**.
