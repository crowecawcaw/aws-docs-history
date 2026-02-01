• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Add

Session Manager permissions to an existing IAM role

Use the following procedure to add Session Manager permissions to an existing
AWS Identity and Access Management (IAM) role. By adding permissions to an existing role, you can
enhance the security of your computing environment without having to use the
AWS `AmazonSSMManagedInstanceCore` policy for instance
permissions.

###### Note

Note the following information:

- This procedure assumes that your existing role already includes
  other Systems Manager `ssm` permissions for actions you want to
  allow access to. This policy alone isn't enough to use
  Session Manager.
- The following policy example includes an
  `s3:GetEncryptionConfiguration` action. This action
  is required if you chose the **Enforce S3 log
  encryption** option in Session Manager logging
  preferences.
- If the `ssmmessages:OpenControlChannel` permission is
  removed from policies attached to your IAM instance profile or
  IAM service role,SSM Agent on the managed node loses connectivity
  to the Systems Manager service in the cloud. However, it can take up to 1 hour
  for a connection to be terminated after the permission is removed.
  This is the same behavior as when the IAM instance role or IAM
  service role is deleted.

###### To add Session Manager permissions to an existing role (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Select the name of the role that you are adding the permissions
   to.
4. Choose the **Permissions** tab.
5. Choose **Add permissions**, and then select
   **Create inline policy**.
6. Choose the **JSON** tab.
7. Replace the default policy content with the following content. Replace
   `key-name` with the Amazon Resource Name
   (ARN) of the AWS Key Management Service key (AWS KMS key) that you want to use.

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
 "ssmmessages:OpenDataChannel"
 ],
 "Resource": "*"
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
 }
 ]
}`

```

For information about using a KMS key to encrypt session data, see
[Turn on KMS key
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

8. Choose **Next: Tags**.
9. (Optional) Add tags by choosing **Add tag**, and
   entering the preferred tags for the policy.
10. Choose **Next: Review**.
11. On the **Review policy** page, for
    **Name**, enter a name for the inline policy, such
    as `SessionManagerPermissions`.
12. (Optional) For **Description**, enter a description
    for the policy.

Choose **Create policy**.
For information about the `ssmmessages` actions, see [Reference: ec2messages,
ssmmessages, and other API operations](systems-manager-setting-up-messageAPIs.md "systems-manager-setting-up-messageAPIs.md").
