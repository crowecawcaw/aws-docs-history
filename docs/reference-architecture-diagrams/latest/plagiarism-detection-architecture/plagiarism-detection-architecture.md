

# Plagiarism Detection Architecture
<a name="plagiarism-detection-architecture"></a>

Publication date: **July 26, 2021 ([Diagram history](#diagram-history))**

This architecture helps you create a plagiarism-detection service using AWS Step Functions, AWS Lambda, Amazon SageMaker AI, and OpenSearch Service.

## Plagiarism Detection Architecture Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how you can use AWS Step Functions, AWS Lambda, Amazon SageMaker AI, and OpenSearch Service services to create a plagiarism-detection service .](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/plagiarism-detection-architecture/images/plagiarism-detection-architecture.png)


1. Copy the document you’d like to run plagiarism detection on to **Amazon Simple Storage Service** (Amazon S3). 

1. **Amazon S3** event triggers start of **AWS Step Functions** workflow. 

1. **AWS Lambda** function extracts text from document using Tika (a content analysis toolkit that detects and extracts metadata and text from over a thousand different file types. 

1. For each paragraph in the document, text is passed to a pre-trained Bidirectional Encoder Representations from Transformers (BERT)-based model to extract word embedding vectors. 

1. For each word embedding vector, a K-Nearest Neighbor (KNN) search is run using a cosine-similarity algorithm. 

1. **Amazon OpenSearch Service** (OpenSearch Service) domain stores an index of pre-processed works that have been converted into word embedding vectors and indexed. 

1. Based on the configured similarity threshold that is compared against the **OpenSearch Service** query result score, an event bridge event is raised, specifying source document information that has possibly been plagiarized with reference to relevant works. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | July 26, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.