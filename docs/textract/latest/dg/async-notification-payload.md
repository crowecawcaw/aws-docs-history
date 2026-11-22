

# Amazon Textract Core results notification

Amazon Textract Core sends the status of an analysis request to an Amazon SNS topic. To get the notification from an Amazon SNS topic, use an Amazon SQS queue or an AWS Lambda function. For more information, see [Calling Amazon Textract Core asynchronous operations](api-async.md). For an example, see [Detecting or analyzing text in a multipage document](async-analyzing-with-sqs.md).

The status message sent by Amazon SNS to Amazon SQS has the following JSON format:

```
{
  "JobId": "String",
  "Status": "String",
  "API": "String",
  "JobTag": "String",
  "Timestamp": Number,
  "DocumentLocation": {
    "S3ObjectName": "String",
    "S3Bucket": "String"
  }
}
```

This table describes the different parameters within an Amazon SNS status:


| **Parameter** | **Description** | 
| --- | --- | 
| JobId | The unique identifier that Amazon Textract Core assigns to the job. It matches a job identifier that's returned from a `Start` operation, such as [StartDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentTextDetection.html). | 
| Status | The status of the job. Valid values are SUCCEEDED, FAILED, or ERROR. | 
| API | The Amazon Textract Core operation used to analyze the input document, such as [StartDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentTextDetection.html) or [StartDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentAnalysis.html). | 
| JobTag | The user-specified identifier for the job. You specify `JobTag` in a call to the `Start` operation, such as [StartDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentTextDetection.html). | 
| Timestamp | The Unix timestamp that indicates when the job finished, returned in milliseconds. | 
| DocumentLocation | Details about the document that was processed. Includes the file name and the Amazon S3 bucket that the file is stored in. | 

If the value of "Status" in the Amazon SNS notification is "FAILED", this indicates something has gone wrong with your analysis job. In this case, check for an error message returned by the Amazon Textract Core API operation and ensure your document matches the quotas specified by [Set quotas in Amazon Textract Core](limits-document.md).