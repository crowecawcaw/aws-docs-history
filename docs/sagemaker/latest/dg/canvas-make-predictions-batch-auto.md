# Make automatic batch predictions

###### Note

Time series forecasting models don't support automatic batch predictions.

To set up a schedule for automatic batch predictions, do the
following:

1. In the left navigation pane of Canvas, choose **My models**.
2. Choose your model.
3. Choose the **Predict**
   tab.
4. Choose **Batch
   prediction**.
5. For **Generate predictions**,
   choose **Automatic**.
6. The **Automate batch
   predictions** dialog box pops up. Choose **Select dataset** and choose the dataset
   for which you want to automate predictions. Note that you can
   only select a dataset that was imported through local upload or
   Amazon S3.
7. After selecting a dataset, choose **Set
   up**.
   Canvas runs a batch predictions job for the dataset after
   you set up the configuration. Then, every time you [Update a dataset](canvas-update-dataset.md "canvas-update-dataset.md"),
   either manually or automatically, another
   batch predictions job runs.

After the prediction job finishes running, on the **Run predictions** page, you
see an output dataset listed under **Predictions**. This dataset contains your results, and
if you select the **More options** icon (
![Vertical ellipsis icon representing a menu or more options.](images/studio/canvas/more-options-icon.png)
), you can choose
**Preview** to preview the output data. You can see the input
data matched to the prediction and the probability that the prediction is
correct. Then, you can choose **Download** to download the results.

The following sections describe how to view, update, and delete your automatic batch
prediction configuration through the **Datasets** page
in the Canvas application. You can only set up a maximum of 20 automatic configurations in Canvas.
For more information about viewing your automated
batch predictions job history or making changes to your automatic configuration through
the **Automations** page, see [How to manage automations](canvas-manage-automations.md "canvas-manage-automations.md").
