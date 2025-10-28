# Customizing Outputs

With Amazon Textract document analysis, you can customize the model output through
adapters trained on your own documents. Adapters are components that plug in to the
Amazon Textract pre-trained deep learning model, customizing its output for your business
specific documents. You create an adapter for your specific use case by
annotating/labeling your sample documents and training the adapter on the annotated
samples. When using this process, the Adapter used is similar to the use of queries,
and as such this feature is referred to as Custom Queries

After you create an adapter, Amazon Textract provides you with an AdapterId. You can have
multiple adapter versions within a single adapter. You can provide the AdapterId, along
with an AdapterVersion, to an operation to specify that you want to use the adapter that
you created. For example, you provide the two parameters to the [AnalyzeDocument](API_AnalyzeDocument.md "API_AnalyzeDocument.md") API for
synchronous document analysis, or the [StartDocumentAnalysis](API_StartDocumentAnalysis.md "API_StartDocumentAnalysis.md") operation for asynchronous analysis.
Providing the AdapterId as part of the request will automatically integrate the adapter
into the analysis process and use it to enhance predictions for your documents. This
way, you can leverage the capabilities of AnalyzeDocument while customizing the model to
fit your own use case.

For more information on creating and using adapters, see [Customizing your Queries Responses](textract-using-adapters.md "textract-using-adapters.md"). For a
tutorial on how to create, train, and use adapters with the AWS Management Console, see [Custom Queries tutorial](textract-adapters-tutorial.md "textract-adapters-tutorial.md").
