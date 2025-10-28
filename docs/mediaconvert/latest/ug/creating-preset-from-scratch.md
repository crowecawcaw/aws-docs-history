# Creating a preset

Output presets specify the settings that apply to a single output of a transcoding job.
System presets have the output settings that are specified for you; custom presets have
settings that are specified by you or by another user of your AWS account.

You can create a custom preset by individually specifying the settings, as described
in this topic. Or you can create a custom preset by duplicating and modifying an
existing preset, as described in [Creating a preset, based on a system preset](create-custom-preset-from-system-preset.md "create-custom-preset-from-system-preset.md").

###### To create a custom output preset

1. Open the [Output presets](https://console.aws.amazon.com/mediaconvert/home#/presets/list "https://console.aws.amazon.com/mediaconvert/home#/presets/list") page in the MediaConvert console.
2. In the **Output presets** pane, choose the **Create
   preset** button.
3. In the **Preset settings** pane, specify at a minimum the name of the new
   preset. Optionally, provide a description and a category.

These values help you find the custom preset later. For more information see [Listing presets](listing-presets.md "listing-presets.md"). 4. In the **Preset settings** pane, choose the container for the
output.

###### Tip

It's important to specify a container that is appropriate to the output type that you
intend to create with the preset. When you choose a system or custom preset
as part of creating a job, the console displays only the presets that
specify a container that is valid for the output group. 5. Choose your output settings.

For more information about each setting, choose the **Info**
link located next to the setting or next to the heading for the group of
settings. 6. Choose the **Create** button at the bottom of the page.
