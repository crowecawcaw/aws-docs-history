End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Modifying Presets in Elastic Transcoder

Elastic Transcoder doesn't allow you to change the settings in an existing preset. This is true both
for the default presets included with Elastic Transcoder and the presets you've added. However, you
can easily achieve the same result by making a copy of the preset that you want to
change, changing the applicable settings, saving the new preset, and deleting the old
preset, as the following procedure explains.

###### To modify a preset using the Elastic Transcoder console

1. Sign in to the AWS Management Console and open the Elastic Transcoder console at [https://console.aws.amazon.com/elastictranscoder/](https://console.aws.amazon.com/elastictranscoder/ "https://console.aws.amazon.com/elastictranscoder/").
2. In the navigation bar of the Elastic Transcoder console, select the region that contains the
   preset that you want to change.
3. In the left pane of the console, click **Presets**.
4. Select the check box for the preset that you want to change.
5. Click **Copy**.
6. Change the applicable values in the copy of the preset that you want to
   change. For more information about each field, see [Settings that You Specify When You Create an Elastic Transcoder Preset](preset-settings.md "preset-settings.md").
7. Click **Create Preset**.
8. Back on the **Presets** page, select the check box for the
   old version of the preset.
9. Click **Remove**.
