

# Generative AI data handling
<a name="next-gen-genai-data-handling"></a>

Failure mode assessments use Amazon Bedrock for AI inference. The following data handling practices apply:
+ Customer data is processed in the same AWS Region as the service
+ Data is not used to train or improve foundation models
+ Assessment inputs and outputs are stored in Next generation Resilience Hub-owned S3 buckets encrypted at rest
+ Customers can opt out of generative AI features entirely