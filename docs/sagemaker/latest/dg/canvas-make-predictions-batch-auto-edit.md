

# Edit your automatic batch prediction configuration
<a name="canvas-make-predictions-batch-auto-edit"></a>

You might want to make changes to your auto update configuration for a dataset, such as changing the frequency of the updates. You might also want to turn off your automatic update configuration to pause the updates to your dataset.

When you edit a batch prediction configuration, you can change the target dataset but not the frequency (since automatic batch predictions occur whenever the dataset is updated).

To edit your auto update configuration, do the following:

1. Go to the **Predict** tab of your model.

1. Under **Predictions**, choose the **Configuration** tab.

1. Find your configuration and choose the **More options** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/more-options-icon.png)).

1. From the dropdown menu, choose **Update configuration**.

1. The **Automate batch prediction** dialog box opens. You can select another dataset and choose **Set up** to save your changes.

Your automatic batch predictions configuration is now updated.

To pause your automatic batch predictions, turn off your automatic configuration by doing the following:

1. Go to the **Predict** tab of your model.

1. Under **Predictions**, choose the **Configuration** tab.

1. Find your configuration from the list and turn off the **Auto update** toggle.

Automatic batch predictions are now paused. You can turn the toggle back on at any time to resume the update schedule.