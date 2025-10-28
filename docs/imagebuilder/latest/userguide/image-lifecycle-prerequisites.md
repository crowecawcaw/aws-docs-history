# Lifecycle management prerequisites for

Image Builder images

Before you can define EC2 Image Builder lifecycle management policies and rules for your image
resources, you must meet the following prerequisites.

- Create an IAM role that grants permission for Image Builder to run lifecycle policies.
  To create the role, see [Create an IAM role for Image Builder lifecycle management](#image-lifecycle-prereq-role "#image-lifecycle-prereq-role").
- Create an IAM role in the destination account for associated resources that
  were distributed across accounts. The role grants permission for Image Builder to perform lifecycle
  actions in the destination account for associated resources. To create the role, see
  [Create an IAM role for Image Builder cross-account lifecycle management](#image-lifecycle-prereq-cross-acct-role "#image-lifecycle-prereq-cross-acct-role").

###### Note

This prerequisite doesn't apply if you've granted launch permissions for an
output AMI. With launch permissions, the account you shared with owns the
instances that are launched from the shared AMI, but all of the AMI resources
remain in your account.

- For container images, you must add the following tag to your
  ECR repositories to grant access for Image Builder to run lifecycle actions on the
  container images stored in the repository:
  `LifecycleExecutionAccess: EC2 Image Builder`.

## Create an IAM role for Image Builder lifecycle management

To grant permission for Image Builder to run lifecycle policies, you must first
create the IAM role that it uses to perform lifecycle actions. Follow these
steps to create the service role that grants permission.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** from the navigation pane.
3. Choose **Create role**. This opens to the first
   step in the process **Select trusted entity** to
   create your role.
4. Select the **Custom trust policy** option for the
   **Trusted entity type**.
5. Copy the following JSON trust policy and paste it into the
   **Custom trust policy** text area, replacing the sample text.
   This trust policy allows Image Builder to assume the role that you create to
   run lifecycle actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "imagebuilder.amazonaws.com"
 ]
 }
 }
 ]
}`

```

6. Select the following managed policy from the list:
   **EC2ImageBuilderLifecycleExecutionPolicy**,
   then choose **Next**. This opens the
   **Name, review, and create** page.

###### Tip

Filter on `image` to streamline results. 7. Enter a **Role name**. 8. After you've reviewed your settings, choose **Create role**.

## Create an IAM role for Image Builder cross-account lifecycle management

To grant permission for Image Builder to perform lifecycle actions in destination accounts
for associated resources, you must first create the IAM role that it uses to perform
lifecycle actions in those accounts. You must create the role in the destination account.

Follow these steps to create the service role that grants permission
_in the destination account_.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** from the navigation pane.
3. Choose **Create role**. This opens to the first
   step in the process **Select trusted entity** to
   create your role.
4. Select the **Custom trust policy** option for the
   **Trusted entity type**.
5. Copy the following JSON trust policy and paste it into the
   **Custom trust policy** text area, replacing the sample text.
   This trust policy allows Image Builder to assume the role that you create to
   run lifecycle actions.

###### Note

When Image Builder uses this role in the destination account to act on associated
resources that were distributed across accounts, it's acting on behalf of
the destination account owner. The AWS account that you configure as the
`aws:SourceAccount` in the trust policy is
the account where Image Builder distributed those resources.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "imagebuilder.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`444455556666`"
                },
                "StringLike": {
                    "aws:SourceArn": "arn:*:imagebuilder:*:*:image/*/*/*"
                }
            }
        }
    ]
}
```

6. Select the following managed policy from the list:
   **EC2ImageBuilderLifecycleExecutionPolicy**,
   then choose **Next**. This opens the
   **Name, review, and create** page.

###### Tip

Filter on `image` to streamline results. 7. Enter `Ec2ImageBuilderCrossAccountLifecycleAccess` as the
**Role name**.

###### Important

`Ec2ImageBuilderCrossAccountLifecycleAccess` must be
the name of this role. 8. After you've reviewed your settings, choose **Create role**.
