# Ready-to-use models

With Amazon SageMaker Canvas Ready-to-use models, you can make predictions on your data without writing a
single line of code or having to build a model—all you have to bring is your data. The
Ready-to-use models use pre-built models to generate predictions without requiring you to spend
the time, expertise, or cost required to build a model, and you can choose from a variety of use
cases ranging from language detection to expense analysis.

Canvas integrates with existing AWS services, such as [Amazon Textract](../../../textract/latest/dg/what-is.md "../../../textract/latest/dg/what-is.md"), [Amazon Rekognition](../../../rekognition/latest/dg/what-is.md "../../../rekognition/latest/dg/what-is.md"), and [Amazon Comprehend](../../../comprehend/latest/dg/what-is.md "../../../comprehend/latest/dg/what-is.md"), to analyze your data and make predictions
or extract insights. You can use the predictive power of these services from within the Canvas
application to get high quality predictions for your data.

Canvas supports the following Ready-to-use models types:

| Ready-to-use model             | Description                                                                                                                                                             | Supported data type                  |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| Sentiment analysis             | Detect sentiment in lines of text, which can be positive, negative, neutral, or<br>mixed. Currently, you can only do sentiment analysis for English language<br>text.   | Plain text or tabular (CSV, Parquet) |
| Entities extraction            | Extract entities, which are real-world objects such as people, places, and<br>commercial items, or units such as dates and quantities, from text.                       | Plain text or tabular (CSV, Parquet) |
| Language detection             | Determine the dominant language in text such as English, French, or<br>German.                                                                                          | Plain text or tabular (CSV, Parquet) |
| Personal information detection | Detect personal information that could be used to identify an individual, such as<br>addresses, bank account numbers, and phone numbers, from text.                     | Plain text or tabular (CSV, Parquet) |
| Object detection in images     | Detect objects, concepts, scenes, and actions in your images.                                                                                                           | Image (JPG, PNG)                     |
| Text detection in images       | Detect text in your images.                                                                                                                                             | Image (JPG, PNG)                     |
| Expense analysis               | Extract information from invoices and receipts, such as date, number, item prices,<br>total amount, and payment terms.                                                  | Document (PDF, JPG, PNG, TIFF)       |
| Identity document analysis     | Extract information from passports, driver licenses, and other identity<br>documentation issued by the US Government.                                                   | Document (PDF, JPG, PNG, TIFF)       |
| Document analysis              | Analyze documents and forms for relationships among detected text.                                                                                                      | Document (PDF, JPG, PNG, TIFF)       |
| Document queries               | Extract information from structured documents such as paystubs, bank statements,<br>W-2s, and mortgage application forms by asking questions using natural<br>language. | Document (PDF)                       |

## Get started

To get started with Ready-to-use models, review the following information.

**Prerequisites**

To use Ready-to-use models in Canvas, you must turn on the **Canvas
Ready-to-use models configuration** permissions when [setting up your
Amazon SageMaker AI domain](canvas-getting-started.md#canvas-prerequisites "canvas-getting-started.md#canvas-prerequisites"). The **Canvas Ready-to-use models configuration**
attaches the [AmazonSageMakerCanvasAIServicesAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess") policy to your Canvas user's AWS Identity and Access Management
(IAM) execution role. If you encounter any issues with granting permissions, see the topic
[Troubleshooting issues with granting permissions through the SageMaker AI console](canvas-limits.md#canvas-troubleshoot-trusted-services "canvas-limits.md#canvas-troubleshoot-trusted-services").

If you’ve already set up your domain, you can edit your domain settings and turn on
the permissions. For instructions on how to edit your domain settings, see [Edit
domain settings](domain-edit.md "domain-edit.md"). When editing the settings for your domain, go to the
**Canvas settings** and turn on the **Enable Canvas
Ready-to-use models** option.

**(Optional) Opt out of AI services data storage**

Certain AWS AI services store and use your data to make improvements to the service. You
can opt out of having your data stored or used for service improvements. To learn more about how
to opt out, see [AI services opt-out
policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") in the _AWS Organizations User Guide_.

**How to use Ready-to-use models**

To get started with Ready-to-use models, do the following:

1. **(Optional) Import your data.** You can import a tabular,
   image, or document dataset to generate batch predictions, or a dataset of predictions, with
   Ready-to-use models. To get started with importing a dataset, see [Create a data flow](canvas-data-flow.md "canvas-data-flow.md").
2. **Generate predictions.** You can generate single or batch
   predictions with your chosen Ready-to-use model. To get started with making predictions, see
   [Make predictions for text data](canvas-ready-to-use-predict-text.md "canvas-ready-to-use-predict-text.md").
