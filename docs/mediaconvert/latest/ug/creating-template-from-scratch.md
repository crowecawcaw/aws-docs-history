# Creating a template

Job templates specify the settings that apply to all outputs of a transcoding job. System
job templates have settings that are specified for you; custom job templates have
settings that are specified by you or by another user of your AWS account.

You can create a job template by individually specifying the settings for each output. Or
you can create a custom preset by specifying a preset for each output's settings, as
described in [Specifying a preset](using-a-preset-to-specify-a-job-output.md "using-a-preset-to-specify-a-job-output.md").

###### To create a custom job template

1. Open the [Job templates](https://console.aws.amazon.com/mediaconvert/home#/templates/list "https://console.aws.amazon.com/mediaconvert/home#/templates/list") page in the MediaConvert console.
2. In the **Job templates** pane, choose the **Create
   template** button.
3. In the **General information** pane, specify at a minimum the name of the
   new job template. Optionally, provide a description and a category.

These values help you find the custom template later. For more information, see [Listing templates](listing-job-templates.md "listing-job-templates.md"). 4. In the **Job template** pane, add inputs, output groups, outputs, and
job-wide settings.

The procedure for this is the same as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md"), except that you don't specify the
location and file name of your input, and you don't specify the IAM role that
the service assumes so that it can access your resources.

###### Note

If you set up outputs by referring to output presets, make sure to specify input audio
and captions selectors to correspond with any output audio and captions that
are specified in the preset. For example, if you use an output preset with
three audio tracks that use audio selectors 1, 2, and 3, make sure that the
input that you specify has audio selectors 1, 2, and 3. 5. Choose the **Create** button at the bottom of the page.
