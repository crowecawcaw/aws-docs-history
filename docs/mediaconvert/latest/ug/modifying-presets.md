# Modifying a preset

You can adjust the settings and field values in your custom presets. You can't change system
presets, but you can duplicate them and modify the duplicate, as described in [Creating a preset, based on a system preset](create-custom-preset-from-system-preset.md "create-custom-preset-from-system-preset.md").

After you modify a preset, jobs that use the preset will run with the new settings,
including the following:

- Jobs that directly specify the custom preset.
- Jobs that you create based on a template that uses the custom preset.
- Jobs that you duplicate from your job history that use the custom preset. The original job
  used the settings in the preset as they were at the time; the new job uses the
  current settings.

###### To modify a custom output preset

1. Open the [Output presets](https://console.aws.amazon.com/mediaconvert/home#/presets/list "https://console.aws.amazon.com/mediaconvert/home#/presets/list") page in the MediaConvert console.
2. Choose the name of the custom preset that you want to modify.
3. Adjust the settings.
4. Choose **Save**.
