# Lifecycle management prerequisites for Image Builder images

Complete these steps before you create lifecycle policies.

- Create an IAM role that grants Image Builder permission to run lifecycle
  policies. You have three options:

  - Choose **Create lifecycle execution role using service
    defaults** in the Image Builder console when you create a lifecycle
    policy. This attaches the
    `EC2ImageBuilderLifecycleExecutionPolicy` managed policy
    automatically.
  - Choose **Create a new lifecycle execution role**
    in the Image Builder console. This opens IAM with pre-filled settings for
    one-click role creation.
  - Create the role manually. For instructions, see
    [Create an IAM role for Image Builder lifecycle management](#image-lifecycle-prereq-role "#image-lifecycle-prereq-role").

- Create an IAM role in each destination account where you distributed
  associated resources across accounts. This role grants Image Builder permission to
  perform lifecycle actions in that account. For instructions, see
  [Create an IAM role for Image Builder cross-account lifecycle management](#image-lifecycle-prereq-cross-acct-role "#image-lifecycle-prereq-cross-acct-role").

###### Note

This prerequisite does not apply if you only granted launch
permissions for an output AMI. With launch permissions, all AMI
resources remain in your account.

- For container images, add the tag
  `LifecycleExecutionAccess: EC2 Image Builder` to your ECR
  repositories. This tag grants Image Builder access to run lifecycle actions on
  container images in the repository.

## Create an IAM role for Image Builder lifecycle management

Create a service role that grants Image Builder permission to perform lifecycle
actions on your image resources.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** from the navigation pane.
3. Choose **Create role**.
4. Select **Custom trust policy** for the
   **Trusted entity type**.
5. Paste the following JSON trust policy into the
   **Custom trust policy** text area, replacing the
   sample text. This policy allows Image Builder to assume the role for lifecycle
   actions.

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

6. Select
   **EC2ImageBuilderLifecycleExecutionPolicy**
   from the managed policy list, then choose
   **Next**.

###### Tip

Filter on `image` to streamline results. 7. Enter a **Role name**. 8. Review your settings, then choose **Create
role**.

## Create an IAM role for Image Builder cross-account lifecycle management

Create this role in each destination account where Image Builder distributed
associated resources. The role grants Image Builder permission to perform lifecycle
actions in that account.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** from the navigation pane.
3. Choose **Create role**.
4. Select **Custom trust policy** for the
   **Trusted entity type**.
5. Paste the following JSON trust policy into the
   **Custom trust policy** text area, replacing the
   sample text. This policy allows Image Builder to assume the role for lifecycle
   actions.

###### Note

Image Builder uses this role on behalf of the destination account owner.
Set the `aws:SourceAccount` to the
account where Image Builder distributed the resources.

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
                "ArnLike": {
                    "aws:SourceArn": "arn:*:imagebuilder:*:*:image/*/*/*"
                }
            }
        }
    ]
}
```

6. Select
   **EC2ImageBuilderLifecycleExecutionPolicy**
   from the managed policy list, then choose
   **Next**.

###### Tip

Filter on `image` to streamline results. 7. Enter `Ec2ImageBuilderCrossAccountLifecycleAccess` as the
**Role name**. You must use this exact name. 8. Review your settings, then choose **Create
role**.
