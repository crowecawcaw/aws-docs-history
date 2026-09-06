

# Revising using the console
<a name="modify-delete-feed-console"></a>

1. If you want to add a feature (an output), make sure that you have room in the [enabled outputs quota](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas) for Elemental Inference. The list of quotas is sorted alphabetically. Look for quotas that don't start with "Request rate for".

1. Open the Elemental Inference console at [https://console.aws.amazon.com/elemental-inference/](https://console.aws.amazon.com/elemental-inference/).

1. In the left navigation bar, choose **Feeds**. On the **Feeds** page, select the feed. The feed details page appears.

1. Take the appropriate action, as follows.


| Action | Description | 
| --- | --- | 
| To change output properties  | In the section for the output, choose the edit icon and make any changes. Then choose **Save** on the dialog. | 
| To enable or disable an output  | In the section for the output, choose the edit icon and change the **Status** field. Then choose **Save** on the dialog.  | 
| To add an output | In the **Feed outputs** tab, choose Add output. <br />In the dialog that appears, enter a name and optional description, then choose the feature type. Then choose **Add** on the dialog. | 
| To remove an output | In the section for that output, choose the delete icon on the right side of the section.  | 