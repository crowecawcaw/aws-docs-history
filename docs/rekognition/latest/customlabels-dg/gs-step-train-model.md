# Step 2: Train your model

In this step you train your model. The training and test datasets are automatically configured for you.
After training successfully completes, you can see the overall
evaluation results, and evaluation results for individual test images.
For more information, see [Training an Amazon Rekognition Custom Labels model](training-model.md "training-model.md").

###### To train your model

1. On the dataset page, choose the **Train model**. The following image shows
   the console with the train model button.

![Console interface for rooms dataset with the Train model button to begin training a model.](images/get-started-train-model.jpg) 2. On the **Train model** page, Choose **Train model**. The
image belows shows the **Train model** button,
notice that the Amazon Resource Name (ARN) for your project is in the
**Choose project** edit box.

![Train model page with project ARN input field and Train model button.](images/tutorial-train-model-page-train-model.jpg) 3. In the **Do you want to train your model?** dialog box, shown in the
following image, choose **Train model**.

![Dialog box to start model training with Cancel and Train model buttons.](images/tutorial-dialog-train-model.jpg) 4. After training completes, choose the model name. Training is finished when the model status is
**TRAINING_COMPLETED**, as demonstrated in the following
console screenshot.

![Model training interface showing completed status for model named "rooms_19.2021-07-13T10:36:30" with performance score 0.902 and status "TRAINING_COMPLETED".](images/get-started-choose-model.jpg) 5. Choose the **Evaluate** button to see the evaluation results.
For information about evaluating a model, see [Improving a trained Amazon Rekognition Custom Labels model](improving-model.md "improving-model.md"). 6. Choose **View test results** to see the results for individual test images.
As seen in the following screenshot, the evaluation dashboard shows metrics such
as F1 score, precision, and recall for each label along with number of test
images. Overall metrics like average, precision, and recall are also
displayed.

![Model evaluation results showing performance metrics across 10 labels.](images/get-started-training-results.jpg) 7. After viewing the test results, choose the model name to return to the model page. The
following screenshot of the performance dashboard where you can click to the
return to the model page.

![Two example images from test results with predicted labels and confidence scores, and a breadcrumb link to return to the model page.](images/get-started-image-test-results.jpg)
