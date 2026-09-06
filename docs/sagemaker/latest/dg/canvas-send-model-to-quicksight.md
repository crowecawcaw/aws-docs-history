

# Send your model to Quick
<a name="canvas-send-model-to-quicksight"></a>

If you use Quick and want to leverage SageMaker Canvas in your Quick visualizations, you can build an Amazon SageMaker Canvas model and use it as a *predictive field* in your Quick dataset. A *predictive field* is a field in your Quick dataset that can make predictions for a given column in your dataset, similar to how Canvas users make single or batch predictions with a model. To learn more about how to integrate Canvas predictive abilities into your Quick datasets, see [SageMaker Canvas integration](https://docs.aws.amazon.com/quicksight/latest/user/sagemaker-canvas-integration.html) in the [Quick User Guide](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).

The following steps explain how you can add a predictive field to your Quick dataset using a Canvas model:

1. Open the Canvas application and build a model with your dataset.

1. After building the model in Canvas, send the model to Quick. A schema file automatically downloads to your local machine when you send the model to Quick. You upload this schema file to Quick in the next step.

1. Open Quick and choose a dataset with the same schema as the dataset you used to build your model. Add a predictive field to the dataset and do the following:

   1. Specify the model sent from Canvas.

   1. Upload the schema file that was downloaded in Step 2.

1. Save and publish your changes, and then generate predictions for the new dataset. Quick uses the model to fill in the target column with predictions.

In order to send a model from Canvas to Quick, you must meet the following prerequisites:
+ You must have both Canvas and Quick set up. Your Quick account must be created in the same AWS Region as your Canvas application. If your Quick account’s home Region differs from your Canvas application’s Region, you must either [close](https://docs.aws.amazon.com/quicksight/latest/user/closing-account.html) and recreate your Quick account, or [set up a Canvas application](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-getting-started.html#canvas-prerequisites) in the same Region as your Quick account. Your Quick account must also contain the default namespace, which you set up when you first create your Quick account. Contact your administrator to help you get access to Quick. For more information, see [Setting up for Quick](https://docs.aws.amazon.com/quicksight/latest/user/setting-up.html) in the *Quick User Guide*.
+ Your user must have the necessary AWS Identity and Access Management (IAM) permissions to send your predictions to Quick. Your administrator can set up the IAM permissions for your user. For more information, see [Grant Your Users Permissions to Send Predictions to Quick](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-quicksight-permissions.html).
+ Quick must have access to the Amazon S3 bucket that you’ve specified for Canvas application storage. For more information, see [Configure your Amazon S3 storage](canvas-storage-configuration.md).