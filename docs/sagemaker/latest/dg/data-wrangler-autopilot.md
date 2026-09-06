

# Automatically Train Models on Your Data Flow
<a name="data-wrangler-autopilot"></a>

You can use Amazon SageMaker Autopilot to automatically train, tune, and deploy models on the data that you've transformed in your data flow. Amazon SageMaker Autopilot can go through several algorithms and use the one that works best with your data. For more information about Amazon SageMaker Autopilot, see [SageMaker Autopilot](autopilot-automate-model-development.md).

When you train and tune a model, Data Wrangler exports your data to an Amazon S3 location where Amazon SageMaker Autopilot can access it.

You can prepare and deploy a model by choosing a node in your Data Wrangler flow and choosing **Export and Train** in the data preview. You can use this method to view your dataset before you choose to train a model on it.

You can also train and deploy a model directly from your data flow.

The following procedure prepares and deploys a model from the data flow. For Data Wrangler flows with multi-row transforms, you can't use the transforms from the Data Wrangler flow when you're deploying the model. You can use the following procedure to process the data before you use it to perform inference.

To train and deploy a model directly from your data flow, do the following.

1. Choose the **\+** next to the node containing the training data.

1. Choose **Train model**.

1. (Optional) Specify a AWS KMS key or ID. For more information about creating and controlling cryptographic keys to protect your data, see [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).

1. Choose **Export and train**.

1. After Amazon SageMaker Autopilot trains the model on the data that Data Wrangler exported, specify a name for **Experiment name**.

1. Under **Input data**, choose **Preview** to verify that Data Wrangler properly exported your data to Amazon SageMaker Autopilot.

1. For **Target**, choose the target column.

1. (Optional) For **S3 location** under **Output data**, specify an Amazon S3 location other than the default location.

1. Choose **Next: Training method**.

1. Choose a training method. For more information, see [Training modes](autopilot-model-support-validation.md#autopilot-training-mode).

1. (Optional) For **Auto deploy endpoint**, specify a name for the endpoint.

1. For **Deployment option**, choose a deployment method. You can choose to deploy with or without the transformations that you've made to your data.
**Important**  
You can't deploy an Amazon SageMaker Autopilot model with the transformations that you've made in your Data Wrangler flow. For more information about those transformations, see [Export to an Inference Endpoint](data-wrangler-data-export.md#data-wrangler-data-export-inference).

1. Choose **Next: Review and create**.

1. Choose **Create experiment**.

For more information about model training and deployment, see [Create Regression or Classification Jobs for Tabular Data Using the AutoML API](autopilot-automate-model-development-create-experiment.md). Autopilot shows you analyses about the best model's performance. For more information about model performance, see [View an Autopilot model performance report](autopilot-model-insights.md).