

# Analysis jobs for custom classification (API)
<a name="analysis-jobs-custom-class-api"></a>

After you [create and train](train-custom-classifier-api.md) a custom document classifier, you can use the classifier to run analysis jobs.

Use the [StartDocumentClassificationJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDocumentClassificationJob.html) operation to start classifying unlabeled documents. You specify the S3 bucket that contains the input documents, the S3 bucket for the output documents, and the classifier to use.

To achieve the highest level of accuracy in training a model, match the type of input to the classifier model type. The classifier job returns a warning if you submit native documents to a plain-text model, or plain text documents to a native document model. For more information, see [Training classification models](training-classifier-model.md).

 [StartDocumentClassificationJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDocumentClassificationJob.html) is asynchronous. Once you have started the job, use the [DescribeDocumentClassificationJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeDocumentClassificationJob.html) operation to monitor its progress. When the `Status` field in the response shows `COMPLETED`, you can access the output in the location that you specified.

**Topics**
+ [Using the AWS Command Line Interface](#get-started-api-customclass-cli)
+ [Using the AWS SDK for Java or SDK for Python](#get-started-api-customclass-java)

## Using the AWS Command Line Interface
<a name="get-started-api-customclass-cli"></a>

The following examples the `StartDocumentClassificationJob` operation, and other custom classifier APIs with the AWS CLI. 

The following examples use the command format for Unix, Linux, and macOS. For Windows, replace the backslash (\\) Unix continuation character at the end of each line with a caret (^).

Run a custom classification job using the `StartDocumentClassificationJob` operation.

```
aws comprehend start-document-classification-job \
     --region {{region}} \
     --document-classifier-arn arn:aws:comprehend:{{region}}:{{account number}}:document-classifier/testDelete \
     --input-data-config S3Uri=s3://{{S3Bucket}}/docclass/{{file name}},InputFormat=ONE_DOC_PER_LINE \
     --output-data-config S3Uri=s3://{{S3Bucket}}/output \
     --data-access-role-arn arn:aws:iam::{{account number}}:role/{{resource name}}
```

Get information on a custom classifier with the job id using the `DescribeDocumentClassificationJob` operation.

```
aws comprehend describe-document-classification-job \
     --region {{region}} \
     --job-id {{job id}}
```

List all custom classification jobs in your account using the `ListDocumentClassificationJobs` operation.

```
aws comprehend list-document-classification-jobs
     --region {{region}}
```

## Using the AWS SDK for Java or SDK for Python
<a name="get-started-api-customclass-java"></a>

For SDK examples of how to start a custom classifier job, see [Use `StartDocumentClassificationJob` with an AWS SDK or CLI](example_comprehend_StartDocumentClassificationJob_section.md).