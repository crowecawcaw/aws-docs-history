

# AI-Enabled Audio Insight Processing Pipeline
<a name="ai-audio-insight-pipeline"></a>

Publication date: **June 20, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to use API-driven AI/ML services to process audio files. With a serverless architecture, you can create a pipeline for multi-language insights including transcription, translation, and natural language understanding.

## AI-Enabled Audio Insight Processing Pipeline
<a name="diagram1"></a>

![Architecture diagram showing an AI-enabled audio insight processing pipeline with Amazon Transcribe, Amazon Translate, and Amazon Comprehend.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ai-audio-insight-pipeline/images/ai-audio-insight-pipeline.png)


The following steps describe the architecture:

1. Upload an audio file to an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket.

1. The file upload creates an Amazon S3 event and initiates an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) transcribe job.

1. The Lambda transcribe job calls the [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html) API for transcription. Audio is converted to text and output is returned to the Lambda job.

1. The transcribed audio file is written to the Amazon S3 transcribed text bucket. The audio file name and metadata is written to the [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) table as a new entry.

1. A Lambda translate job is initiated by the Amazon S3 file upload. The [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html) API is called for translation.

1. Amazon Translate converts text from input language to output language. Translated text is returned to Lambda.

1. The translated audio file is written to the Amazon S3 translated text bucket. The DynamoDB table entry is updated to include translate metadata.

1. The Lambda text insights job is initiated by the Amazon S3 file upload.

1. The function calls the [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) API for document understanding inference. Amazon Comprehend runs inference on translated text and returns analysis. This includes entity recognition, sentiment analysis, and key phrase extraction.

1. The Lambda function updates the DynamoDB entry with Amazon Comprehend insights as additional metadata.

1. Your `HTTP GET` match API call is routed through [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).

1. API Gateway initiates the Lambda GET match function.

1. The Lambda GET match function queries [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) to find a file match from the translated text Amazon S3 bucket. The query returns matching file IDs. Lambda then uses these to query DynamoDB for insight metadata and returns the most suitable matches.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon Transcribe product page](https://aws.amazon.com/transcribe/)
+ [Amazon Kendra product page](https://aws.amazon.com/kendra/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | June 20, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.