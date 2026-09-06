

# Select and deploy text classification models
<a name="jumpstart-text-classification-deploy"></a>

Deploy two text classification models for comparison: DistilBERT Base Cased and BERT Base Uncased. You'll see the differences between these models and deploy them using the optimal instance configuration.

## Why these two models
<a name="w2aac37c15c21b5"></a>

These models show the typical choice customers face in production between performance and cost:
+ **BERT Base Uncased**: Larger, more accurate, but slower and more resource-intensive.
+ **DistilBERT Base Cased**: Smaller, faster, more cost-effective, but potentially less accurate.

This comparison helps you choose the right model for your specific needs.

## Understanding model names in the catalog
<a name="w2aac37c15c21b7"></a>

Text classification model names in the catalog include these components:
+ BERT: Bidirectional Encoder Representations from Transformers.
+ L-X\_H-Y\_A-Z: Model structure where:
  + L-X: Number of layers (X).
  + H-Y: Hidden size (Y).
  + A-Z: Number of attention heads (Z).
+ Small/Base/Large: Model size and complexity.
+ Uncased/Cased - Case sensitivity setting.

Example: `Small BERT L-2_H-128_A-2` indicates a small BERT model with:
+ 2 layers.
+ 128 hidden units.
+ 2 attention heads.

## Access the JumpStart model catalog
<a name="w2aac37c15c21b9"></a>

Navigate to the text classification models in JumpStart catalog.

1. Open SageMaker AI Studio

1. In the left navigation pane, choose **JumpStart**.

1. On the JumpStart page, choose **Hugging Face**.

1. Choose **Text Classification**.

You should see a list of available text classification models in the catalog, including DistilBERT and BERT variants.

## Deploy DistilBERT Base Cased
<a name="w2aac37c15c21c11"></a>

Deploy the DistilBERT model using the default configuration.

1. In the model list, find and choose **DistilBERT Base Cased** (by distilbert).

1. On the model details page, keep the default instance type.

1. Keep all other default settings and choose **Deploy**.

1. Wait 5-10 minutes for deployment to complete.

1. To verify deployment success, go to **Deployments** then **Endpoints**.

1. Confirm the DistilBERT endpoint shows `InService` status.

## Deploy BERT Base Uncased
<a name="w2aac37c15c21c13"></a>

Deploy the BERT model for comparison with DistilBERT.

1. Return to the Hugging Face text classification models in JumpStart.

1. Find and choose **BERT Base Uncased** (by google-bert).

1. Keep the default instance type and choose **Deploy**.

1. To confirm both deployments, check that both endpoints show `InService` status in the endpoints list.

Both models appear in your endpoints list with `InService` status.

**Important**  
Copy and save the endpoint names. You'll need them for the evaluation process.

## Troubleshooting
<a name="w2aac37c15c21c15"></a>

If you encounter deployment issues:
+ For instance type errors, verify that you're using the default instance type, not CPU instances like `ml.m5.large`.
+ If you can't find models, search using the exact model names, including the publisher in parentheses.
+ For failed deployments, check the service health in your Region or try a different Region.

After your model shows `InService` status, continue to [Evaluate and compare model performance](jumpstart-text-classification-evaluate.md) to evaluate your deployed model.