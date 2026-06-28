# Revising using the console

1. If you want to add a feature (an output), make sure that you have room in
   the [enabled outputs quota](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas") for Elemental Inference. The list of quotas is sorted
   alphabetically. Look for quotas that don't start with "Request rate for".
2. Open the Elemental Inference console at [https://console.aws.amazon.com/elemental-inference/](https://console.aws.amazon.com/elemental-inference/ "https://console.aws.amazon.com/elemental-inference/").
3. In the left navigation bar, choose **Feeds**. On the
   **Feeds** page, select the feed. The feed details page
   appears.
4. Take the appropriate action, as follows.

| Action                         | Description                                                                                                                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| To change output properties    | In the section for the output, choose the edit icon and<br>make any changes. Then choose *_Save_<br>• on the<br>dialog.                                                                             |
| To enable or disable an output | In the section for the output, choose the edit icon and change<br>the *_Status_<br>• field. Then choose<br>*_Save_<br>• on the dialog.                                                              |
| To add an output               | In the *_Feed outputs_<br>• tab, choose<br>Add output.<br>In the dialog that appears, enter a name and optional description,<br>then choose the feature type. Then choose **Add**<br>on the dialog. |
| To remove an output            | In the section for that output, choose the delete icon on the<br>right side of the section.                                                                                                         |
