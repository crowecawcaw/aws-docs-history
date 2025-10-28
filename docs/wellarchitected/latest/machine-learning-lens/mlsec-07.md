# MLSEC-07: Keep only relevant data

Preserve data across computing environments (such as development
and staging) and only store use-case relevant data to reduce
data exposure risks. Implement mechanisms to enforce a lifecycle
management process across the data. Decide when to automatically
remove stale data.

## Implementation plan

- **Establish a data lifecycle
  plan** - Understand usage patterns and
  requirements for debugging and operational tasks.
  Establish a data lifecycle plan to reduce data sprawl over
  time.
- **Design for privacy** - Remove sensitive elements that are not needed for the ML workflow. Detect and redact personally identifiable information (PII), while maintaining data usability. Determine what features are required to solve the business problem and valuable for future iterations.

## Documents

- [Reference
  Guide: Extract More Value from your Data](https://pages.awscloud.com/data-lifecycle-reference-guide.html?sc_channel=bl&sc_campaign=datalifecycleandanalyticsintheawscloud&sc_geo=mult&sc_country=global&sc_outcome=multi "https://pages.awscloud.com/data-lifecycle-reference-guide.html?sc_channel=bl&sc_campaign=datalifecycleandanalyticsintheawscloud&sc_geo=mult&sc_country=global&sc_outcome=multi")

## Blogs

- [Building
  a data analytics practice across the data lifecycle](https://aws.amazon.com/blogs/publicsector/building-a-data-analytics-practice-across-the-data-lifecycle/ "https://aws.amazon.com/blogs/publicsector/building-a-data-analytics-practice-across-the-data-lifecycle/")
- [Detecting
  and redacting PII using Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/detecting-and-redacting-pii-using-amazon-comprehend/ "https://aws.amazon.com/blogs/machine-learning/detecting-and-redacting-pii-using-amazon-comprehend/")
- [Now
  available in Amazon Transcribe: Automatic Redaction of
  Personally Identifiable Information](https://aws.amazon.com/blogs/aws/now-available-in-amazon-transcribe-automatic-redaction-of-personally-identifiable-information/ "https://aws.amazon.com/blogs/aws/now-available-in-amazon-transcribe-automatic-redaction-of-personally-identifiable-information/")
- [Machine
  learning models that act on encrypted data](https://www.amazon.science/blog/machine-learning-models-that-act-on-encrypted-data "https://www.amazon.science/blog/machine-learning-models-that-act-on-encrypted-data")
- [Redacting
  sensitive information with user-defined functions in Amazon Athena](https://aws.amazon.com/blogs/big-data/redacting-sensitive-information-with-user-defined-functions-in-amazon-athena/ "https://aws.amazon.com/blogs/big-data/redacting-sensitive-information-with-user-defined-functions-in-amazon-athena/")

## Videos

- [AWS re:Invent 2020: Privacy-preserving machine learning](https://www.youtube.com/watch?v=ZQkB9XRqdnc "https://www.youtube.com/watch?v=ZQkB9XRqdnc")
- [AWS re:Invent 2019: Best practices for Amazon S3](https://youtu.be/HT3QiuzgjZg?t=524 "https://youtu.be/HT3QiuzgjZg?t=524")

## Examples

- [Field
  Notes: Redacting Personal Data from Connected Cars Using
  Amazon Rekognition](https://aws.amazon.com/blogs/architecture/field-notes-redacting-personal-data-from-connected-cars-using-amazon-rekognition/ "https://aws.amazon.com/blogs/architecture/field-notes-redacting-personal-data-from-connected-cars-using-amazon-rekognition/")
- [How
  to Create a Modern CPG Data Architecture with Data
  Mesh](https://aws.amazon.com/blogs/industries/how-to-create-a-modern-cpg-data-architecture-with-data-mesh/ "https://aws.amazon.com/blogs/industries/how-to-create-a-modern-cpg-data-architecture-with-data-mesh/")
