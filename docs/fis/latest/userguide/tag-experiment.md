# Tag an experiment

You can apply tags to experiments to help you organize them. You can also
implement [tag-based IAM policies](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags") to control access to experiments.

###### To tag an experiment using the console

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/ "https://console.aws.amazon.com/fis/").
2. In the navigation pane, choose **Experiments**.
3. Select the experiment and choose **Actions**,
   **Manage tags**.
4. To add a new tag, choose **Add new tag**, and specify a
   key and value.

To remove a tag, choose **Remove** for the tag. 5. Choose **Save**.

###### To tag an experiment using the CLI

Use the [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/tag-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/tag-resource.html")
command.
