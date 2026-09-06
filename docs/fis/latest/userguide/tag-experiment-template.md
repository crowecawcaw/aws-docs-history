

# Tag experiment templates
<a name="tag-experiment-template"></a>

You can apply your own tags to experiment templates to help you organize them. You can also implement [tag-based IAM policies](security_iam_service-with-iam.md#security_iam_service-with-iam-tags) to control access to experiment templates.

**To tag an experiment template using the console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiment templates**.

1. Select the experiment template and choose **Actions**, **Manage tags**.

1. To add a new tag, choose **Add new tag**, and then specify a key and value.

   To remove a tag, choose **Remove** for the tag.

1. Choose **Save**.

**To tag an experiment template using the CLI**  
Use the [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/tag-resource.html) command.