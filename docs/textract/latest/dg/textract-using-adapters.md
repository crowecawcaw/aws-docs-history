# Customizing your Queries Responses

Amazon Textract lets you customize the output of its pretrained Queries feature using
adapters. You can use the [Amazon Textract
Console](https://console.aws.amazon.com/textract/ "https://console.aws.amazon.com/textract/") to create an adapter. This adapter can then be referenced when calling
the [AnalyzeDocument](API_AnalyzeDocument.md "API_AnalyzeDocument.md") and [StartDocumentAnalysis](API_StartDocumentAnalysis.md "API_StartDocumentAnalysis.md")
operations.

When you create an adapter using the console, you upload your own documents for the
purposes of training the adapter and testing its performance. You also add queries to your
documents and then annotate your documents by linking these queries to the correct response
elements in your documents. Once you have created an adapter and annotated your documents,
you can train the adapter, check its performance, and then use it when analyzing
documents.

Adapters are modular components are added to the existing Amazon Textract deep learning
model, extending its capabilities for the tasks it’s trained on. By fine-tuning a deep
learning model with adapters, you can customize the output for document analysis tasks
related to your specific use case.

To create and use an adapter, you must:

- Upload sample documents for training
- Designate the train and test datasets
- Annotate your documents with queries and responses
- Train the adapter
- Get the AdapterId
- Use the adapter when calling `AnalyzeDocument`
  **Uploading sample documents**

To train the adapter, you must upload a set of sample documents representative of your
use case. You can upload documents directly from your computer or an Amazon S3 bucket. For best
results, provide as many documents for training as possible (up to a maximum of 2,500 pages
training documents and 1000 test documents). Make sure that the documents represent all
aspects of your use case. You must upload a minimum of five training and five testing
documents.

**Designating training and test sets**

You must divide all of your documents into training and test sets. The training set is
used to train the adapter. The adapter learns the patterns contained in these annotated
documents. The test set is used to evaluate the adapter performance.

For more information on training and testing data, see [Preparing training and testing
datasets](textract-preparing-training-testing.md "textract-preparing-training-testing.md").

**Annotating documents with queries and responses**

When annotating your documents, you have two choices: You can auto-label your documents
using the pretrained Queries feature and then edit the labels where needed. Alternatively,
you can manually label responses for each of your document queries.

For more information on best practices for queries, see [Best
Practices for Queries](../../../en_us/textract/latest/dg/bestqueries.md "../../../en_us/textract/latest/dg/bestqueries.md").

**Train the adapter**

After you annotate the training data, you can initiate the training process for your
adapter. Amazon Textract trains an adapter that's tailored to your documents. The adapter
training takes 2-30 hours, depending on the size of the dataset and the AWS Region. When
the training is complete, you can view the training status in the adapter details page. If
the status is `training failed`, see [Debugging training
failures](textract-debugging-failures-adapters.md "textract-debugging-failures-adapters.md") to debug the failure.

**Evaluate the adapter**

After each round of adapter training, review the performance metrics in the AWS Management Console
to determine how close the adapter is to your desired level of performance. You can then
further improve your adapter’s accuracy for your documents by uploading a new batch of
training documents or by reviewing annotations for documents that have low accuracy scores.
After you create an improved version of the adapter, you can use the AWS Console to delete
any earlier adapter versions that you no longer need.

For more information on evaluation metrics, see [Evaluating and improving your
adapters](textract-evaluating-improving-adapters.md "textract-evaluating-improving-adapters.md").

**Get the AdapterId**

Once the adapter has been trained, you can get the unique ID for your adapter to use with
the Amazon Textract document analysis API operations. Retrieve the AdapterId by using the [ListAdapterVersions](API_ListAdapterVersions.md "API_ListAdapterVersions.md") API
operation, or by using the AWS Management Console.

**Call the AnalyzeDocument API operation**

To apply your custom adapter, provide its ID when calling the [AnalyzeDocument](API_AnalyzeDocument.md "API_AnalyzeDocument.md") or [StartDocumentAnalysis](API_StartDocumentAnalysis.md "API_StartDocumentAnalysis.md") API
operations. This enhances predictions on your documents. When calling API operations, you
can use up to one adapter per page.

**Video demonstration and tutorial**
