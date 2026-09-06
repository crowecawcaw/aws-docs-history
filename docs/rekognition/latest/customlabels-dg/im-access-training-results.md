

# Accessing evaluation metrics (Console)
<a name="im-access-training-results"></a>

During testing, the model is evaluated for its performance against the test dataset. The labels in the test dataset are considered 'ground truth' as they represent what the actual image represents. During testing, the model makes predictions using the test dataset. The predicted labels are compared with the ground truth labels and the results are available in the console evaluation page.

The Amazon Rekognition Custom Labels console shows summary metrics for the entire model and metrics for individual labels. The metrics available in the console are precision recall, F1 score, confidence, and confidence threshold. For more information, see [Improving a trained Amazon Rekognition Custom Labels model](improving-model.md).

You can use the console to focus on individual metrics. For example, to investigate precision issues for a label, you can filter the training results by label and by *false positive* results. For more information, see [Metrics for evaluating your model](im-metrics-use.md).

After training, the training dataset is read-only. If you decide to improve the model, you can copy the training dataset to a new dataset. You use the copy of the dataset to train a new version of the model. 

In this step, you use the console to access the training results in the console. 

**To access evaluation metrics (console)**

1. Open the Amazon Rekognition console at [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/).

1. Choose **Use Custom Labels**.

1. Choose **Get started**. 

1. In the left navigation pane, choose **Projects**.

1. In the **Projects** page, choose the project that contains the trained model that you want to evaluate.

1. In the **Models**, choose the model that you want to evaluate. 

1. Choose the **Evaluation** tab to see the evaluation results. For information about evaluating a model, see [Improving a trained Amazon Rekognition Custom Labels model](improving-model.md).

1. Choose **View test results** to see the results for individual test images. For more information, see [Metrics for evaluating your model](im-metrics-use.md). The following screenshot of the model evaluation summary shows the F1 score, average precision, and overall recall for 6 labels with test results and performance metrics. Details on using the trained model are also provided.   
![Model evaluation summary showing F1 score, average precision, and overall recall.](http://docs.aws.amazon.com/rekognition/latest/customlabels-dg/images/get-started-training-results.jpg)

1. After viewing the test results, choose the project name to return to the model page. The test results page shows images with predicted labels and confidence scores for a machine learning model trained on backyard and front yard image categories. Two example images are displayed.   
![The test results page shows images with predicted labels and confidence scores.](http://docs.aws.amazon.com/rekognition/latest/customlabels-dg/images/get-started-image-test-results.jpg)

1. Use the metrics to evaluate the performance of the model. For more information, see [Improving an Amazon Rekognition Custom Labels model](tr-improve-model.md). 