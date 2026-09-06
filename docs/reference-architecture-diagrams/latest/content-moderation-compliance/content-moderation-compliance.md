

# Content Moderation and Compliance Using AWS AI Services
<a name="content-moderation-compliance"></a>

Publication date: **October 28, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to build customizable serverless workflows for reliable and scalable AI-based content moderation. With AWS AI services, you can automate content analysis across multiple media types.

## Content Moderation and Compliance Using AWS AI Services
<a name="diagram1"></a>

![Architecture diagram showing content moderation and compliance by using AWS AI services.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/content-moderation-compliance/images/content-moderation-compliance.png)


The following steps describe the architecture:

1. End users upload their content into the AWS Cloud.

1. [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html) and [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) process the audio streams within video streams. They extract content moderation categories by using simple APIs.

1. Workflows, publisher/subscription patterns, and custom code moderate the content.

1. Content securely persists into an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket or another data store.

1. Amazon Transcribe converts audio into text. [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) provides natural language processing (NLP) for analysis.

1. [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) extracts content from documents. Amazon Comprehend NLP moderates the extracted content.

1. [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) Ground Truth integrates human workforces to customize model vocabularies and image labels.

1. [Amazon Augmented AI (Amazon A2I)](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html) brings humans into the loop for scenarios that are not fully automatable.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon Rekognition product page](https://aws.amazon.com/rekognition/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | October 28, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.