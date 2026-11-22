

# Plagiarism detection on AWS

Publication date: **July 26, 2021 ([Diagram history](diagram-history.md))**

This architecture helps you create a plagiarism-detection service using [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/), and [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/).

## Plagiarism detection on AWS diagram
<a name="plagiarism-detection-architecture-diagram"></a>

![A document uploaded to Amazon S3 triggers a Step Functions workflow that scores it for plagiarism.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/education/images/plagiarism-detection-architecture.png)


The following steps describe the architecture:

1. Copy the document you'd like to run plagiarism detection on to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3). 

1. Amazon S3 event triggers start of Step Functions workflow. 

1. Lambda function extracts text from document using Tika (a content analysis toolkit that detects and extracts metadata and text from over a thousand different file types). 

1. For each paragraph in the document, text is passed to a pre-trained Bidirectional Encoder Representations from Transformers (BERT)-based model to extract word embedding vectors. 

1. For each word embedding vector, a K-Nearest Neighbor (KNN) search is run using a cosine-similarity algorithm. 

1. Amazon OpenSearch Service (OpenSearch Service) domain stores an index of pre-processed works that have been converted into word embedding vectors and indexed. 

1. Based on the configured similarity threshold that is compared against the OpenSearch Service query result score, an [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) event is raised, specifying source document information that has possibly been plagiarized with reference to relevant works. 

## Further reading
<a name="plagiarism-detection-architecture-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 