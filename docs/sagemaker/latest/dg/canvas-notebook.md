# Download a model notebook

###### Note

The model notebook feature is available for quick build and standard build
tabular models, and fine-tuned foundation models. Model notebooks aren't supported
for image prediction, text prediction, or time series forecasting models.

If you'd like to generate a model notebook for a tabular model built before this
feature was launched, you must rebuild the model to generate a notebook.

For eligible models that you successfully build in Amazon SageMaker Canvas, a Jupyter notebook containing a report of all
the model building steps is generated. This Jupyter notebook contains
Python code that you can run locally or run in an environment like Amazon SageMaker Studio Classic to
replicate the steps necessary to build your model. The notebook can be useful if you’d like
to experiment with the code or see the backend details of how Canvas builds
models.

To access the model notebook, do the following:

1.  Open the SageMaker Canvas application.
2.  In the left navigation pane, choose **My models**.
3.  Choose the model and version that you built.
4.  On the model version’s page, choose the **More options** icon (
    ![Vertical ellipsis icon representing a menu or more options.](images/studio/canvas/more-options-icon.png)
    ) in the header.
5.  From the dropdown menu, choose **View Notebook**.
6.  A popup appears with the notebook content. You can choose
    **Download** and then do one of the following:

        1. Choose **Download** to save the notebook content to your
         local device.
        2. Choose **Copy S3 URI** to copy the Amazon S3 location where
         the notebook is stored. The notebook is stored in the Amazon S3 bucket specified
         in your **Canvas storage configuration**, which is configured
         in the [Prerequisites for setting up Amazon SageMaker Canvas](canvas-getting-started.md#canvas-prerequisites "canvas-getting-started.md#canvas-prerequisites") section.

    You should now be able to view the notebook either locally or as an object in Amazon S3.
    You can upload the notebook to an IDE to edit and run the code, or you can share the
    notebook with others in your organization to review.
