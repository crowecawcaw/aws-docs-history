# Amazon SageMaker Canvas

Amazon SageMaker Canvas gives you the ability to use machine learning to generate predictions without
needing to write any code. The following are some use cases where you can use SageMaker Canvas:

- Predict customer churn
- Plan inventory efficiently
- Optimize price and revenue
- Improve on-time deliveries
- Classify text or images based on custom categories
- Identify objects and text in images
- Extract information from documents
  With Canvas, you can chat with popular large language models (LLMs), access
  Ready-to-use models, or build a custom model trained on your data.

Canvas chat is a functionality that leverages open-source and Amazon LLMs to help you
boost your productivity. You can prompt the models to get assistance with tasks such as
generating content, summarizing or categorizing documents, and answering questions. To learn
more, see [Generative AI foundation models in SageMaker Canvas](canvas-fm-chat.md "canvas-fm-chat.md").

The [Ready-to-use models](canvas-ready-to-use-models.md "canvas-ready-to-use-models.md") in Canvas
can extract insights from your data for a variety of use cases. You don’t have to build a
model to use Ready-to-use models because they are powered by Amazon AI services, including
[Amazon Rekognition](../../../rekognition/latest/dg/what-is.md "../../../rekognition/latest/dg/what-is.md"),
[Amazon Textract](../../../textract/latest/dg/what-is.md "../../../textract/latest/dg/what-is.md"),
and [Amazon Comprehend](../../../comprehend/latest/dg/what-is.md "../../../comprehend/latest/dg/what-is.md"). You
only have to import your data and start using a solution to generate predictions.

If you want a model that is customized to your use case and trained with your data, you
can [build a model](canvas-custom-models.md "canvas-custom-models.md"). You can get predictions
customized to your data by doing the following:

1. Import your data from one or more data sources.
2. Build a predictive model.
3. Evaluate the model's performance.
4. Generate predictions with the model.
   Canvas supports the following types of custom models:

- Numeric prediction (also known as _regression_)
- Categorical prediction for 2 and 3+ categories (also known as _binary_ and _multi-class
  classification_)
- Time series forecasting
- Single-label image prediction (also known as _image
  classification_)
- Multi-category text prediction (also known as _multi-class
  text classification_)
  To learn more about pricing, see the [SageMaker Canvas pricing page](https://aws.amazon.com/sagemaker/canvas/pricing/ "https://aws.amazon.com/sagemaker/canvas/pricing/"). You can also see [Billing and cost in SageMaker Canvas](canvas-manage-cost.md "canvas-manage-cost.md") for more
  information.

SageMaker Canvas is currently available in the following Regions:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Europe (Stockholm)
- South America (São Paulo)

###### Topics

- [Are you a first-time SageMaker Canvas user?](#canvas-first-time-user "#canvas-first-time-user")
- [Getting started with using Amazon SageMaker Canvas](canvas-getting-started.md "canvas-getting-started.md")
- [Tutorial: Build an end-to-end machine
  learning workflow in SageMaker Canvas](canvas-end-to-end-machine-learning-workflow.md "canvas-end-to-end-machine-learning-workflow.md")
- [Amazon SageMaker Canvas setup and permissions management (for IT
  administrators)](canvas-setting-up.md "canvas-setting-up.md")
- [Generative AI assistance for solving ML problems in Canvas using Amazon Q Developer](canvas-q.md "canvas-q.md")
- [Data import](canvas-importing-data.md "canvas-importing-data.md")
- [Data preparation](canvas-data-prep.md "canvas-data-prep.md")
- [Generative AI foundation models in SageMaker Canvas](canvas-fm-chat.md "canvas-fm-chat.md")
- [Ready-to-use models](canvas-ready-to-use-models.md "canvas-ready-to-use-models.md")
- [Custom models](canvas-custom-models.md "canvas-custom-models.md")
- [Logging out of Amazon SageMaker Canvas](canvas-log-out.md "canvas-log-out.md")
- [Limitations and troubleshooting](canvas-limits.md "canvas-limits.md")
- [Billing and cost in SageMaker Canvas](canvas-manage-cost.md "canvas-manage-cost.md")

## Are you a first-time SageMaker Canvas user?

If you are a first-time user of SageMaker Canvas, we recommend that you begin by reading the
following sections:

- For IT administrators – [Amazon SageMaker Canvas setup and permissions management (for IT
  administrators)](canvas-setting-up.md "canvas-setting-up.md")
- For analysts and individual users – [Getting started with using Amazon SageMaker Canvas](canvas-getting-started.md "canvas-getting-started.md")
- For an example of an end to end workflow – [Tutorial: Build an end-to-end machine
  learning workflow in SageMaker Canvas](canvas-end-to-end-machine-learning-workflow.md "canvas-end-to-end-machine-learning-workflow.md")
