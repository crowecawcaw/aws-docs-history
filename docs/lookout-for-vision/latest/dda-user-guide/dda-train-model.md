Defect Detection App is in preview release and is subject to change.

# Training your model

After you have created your datasets and labeled the images, you can train your model.
Defect Detection App creates either a classification or segmentation model, depending on how you annotated the training images.
Optionally, you can choose to create a heatmap model using the classifications you make
in your dataset. For more information, see [Heatmap model](dda-components.md#dda-ud-image-segmentation-heatmap "dda-components.md#dda-ud-image-segmentation-heatmap").
As part of the training process, Defect Detection App uses a test dataset to evaluate the model. To create the
test dataset, the dataset is split into a test dataset and a training dataset.

After training is complete, you can evaluate the performance of the model and make any
necessary improvements. For more information, see [Evaluating your model](dda-evaluate-model.md "dda-evaluate-model.md").

To view the existing model versions in the project, choose **Model versions** tab on the
top navigation pane.

The following procedure shows you how to train your model.

###### To train your model

1. If you're not on the project details page, do the following:
   1. [Sign in](dda-signin-dda-web-app.md "dda-signin-dda-web-app.md") to the Defect Detection App Console.
   2. In the top navigation pane, choose **Projects**.
   3. On the projects page, choose the project. The console opens the project details page.

2. On the project details page, choose the **Model versions** tab
3. Choose **Train new model version**. The console raises a warning dialog box
   if your training or test dataset does not met the minimum requirements for training a model.
   Choose the **Training dataset** tab to review the requirements and add more images to your
   dataset.
4. If your datasets meet the requirements, the console opens the **Train new model version** dialog box.
5. Enter a **Model name** for the model.
6. If you want to create a model that generates a heatmap, choose **Generate defect heat maps**. For more information, see [Heatmap model](dda-components.md#dda-ud-image-segmentation-heatmap "dda-components.md#dda-ud-image-segmentation-heatmap").
7. (Optional) Expand **Advanced settings** to select a higher image resolution to apply during training.

Defect Detection App creates downscaled copies of your dataset images to use for training. Higher resolutions can result in better accuracy
when detecting small defects, but result in longer training times and higher inference latency. 8. Choose **Train** to start training the model. 9. In the **Model versions** tab, you can see that training has started and you can
see the current status in the `Status` column for the model.
Training a model takes a while to complete. 10. Next step: When training is finished, see [Evaluating your model](dda-evaluate-model.md "dda-evaluate-model.md").
