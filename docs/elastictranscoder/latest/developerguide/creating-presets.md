End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Creating a Preset in Elastic Transcoder

You can create a preset using either the AWS Management Console or the Elastic Transcoder Create Preset API
action. The following procedure explains how to create a preset using the console. For
information about how to create a preset using the API, see [Create Preset](create-preset.md "create-preset.md").

###### Note

You cannot update an existing preset. If you need to change settings in a preset,
create a new preset based on the preset that you want to change, update the
applicable values, and save the new preset.

###### To create a preset using the Elastic Transcoder console

1. Sign in to the AWS Management Console and open the Elastic Transcoder console at [https://console.aws.amazon.com/elastictranscoder/](https://console.aws.amazon.com/elastictranscoder/ "https://console.aws.amazon.com/elastictranscoder/").
2. In the navigation bar of the Elastic Transcoder console, select the region in which you want
   to create the preset.
3. In the left pane of the console, click **Presets**.
4. On the **Presets** page, click **Create New
   Preset**.
5. Enter the applicable values. For more information about each field, see [Settings that You Specify When You Create an Elastic Transcoder Preset](preset-settings.md "preset-settings.md").
6. Click **Create Preset**.
