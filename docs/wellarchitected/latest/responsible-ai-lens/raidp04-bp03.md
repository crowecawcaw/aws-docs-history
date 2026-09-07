

# RAIDP04-BP03 Protect data from being manipulated or accessed for unintended purposes
<a name="raidp04-bp03"></a>

 Implement the principle of least privilege, only providing access to relevant data to those who really need it for both automated systems and human users accessing your datasets. Consider scanning datasets for unwanted content, including adversarial prompts, disinformation, malware, or other data poisoning attempts that could affect downstream system behavior. Establish access controls and audit trails that track who accesses datasets and what modifications are made. Use cryptographic verification methods where appropriate to detect unauthorized changes to critical datasets, particularly those used for evaluation or system operation. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation considerations
<a name="implementation-considerations-58"></a>

1.  Build permission systems that align access controls with specific role requirements, assisting to reduce broad access to data. 

1.  Set up scanning tools that look for unwanted content like adversarial prompts, fake information, or suspicious patterns before a dataset gets used. These scanners should automatically flag potential data poisoning attempts or embedded malware that could affect your models. 

1.  Create detailed logs that track who looked at which datasets, when they accessed them, and what changes they made to the data. Your audit trail should be detailed enough that you can reconstruct exactly what happened during dataset operations. 

1.  Use checksums or digital signatures on your most important datasets so you can tell immediately they were changed without permission. This is especially important for evaluation datasets and operational data that your system relies on. 

1.  Plan out what your team will do when security problems happen, including how to quickly isolate manipulated datasets and figure out which models or evaluations might be affected. 

## Resources
<a name="resources-55"></a>

 **Related best practice:** 
+  RAISP02-BP02 Privacy: Build privacy-preserving mechanisms into the core AI system 
+  RAISP03-BP02 Security: Implement security safeguards to block AI-specific threats 

 **Related documents:** 
+  [Security control recommendations for protecting data](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-controls-by-caf-capability/data-controls.html) 
+  [Onboarding data in Amazon SageMaker AI Unified Studi](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/data-onboarding.html)o 
+  [Data and model quality monitoring with Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) 
+  [Detect and filter harmful content by using Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) 
+  [Monitor model invocation using CloudWatch Logs and Amazon S3](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) 
+  [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.7.3 Acquisition of data 
+  [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.7.5 Data provenance 

 **Related videos:** 
+  [Data protection strategies for the cloud - AWS Online Tech Talks:](https://www.youtube.com/watch?v=4PgoBjqpm8U) 
+  [AWS re:Inforce 2023 - Using AWS data protection services for innovation and automation (DAP305)](https://www.youtube.com/watch?v=jpT45GrbWGE) 
+  [AWS re:Invent 2024 - Achieve seamless and secure data sharing (ANT325)](https://www.youtube.com/watch?v=VFQjR2JQCQM) 

 **Related examples:** 
+  [Amazon SageMaker AI Lakehouse now supports attribute-based access control](https://aws.amazon.com/blogs/big-data/amazon-sagemaker-lakehouse-now-supports-attribute-based-access-control/) 

 **Related tools:** 
+  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) 
+  [AWS Lake Formation](https://aws.amazon.com/lake-formation/) 
+  [Amazon S3 Access Grants](https://aws.amazon.com/s3/features/access-grants/) 
+  [AWS Identity and Access Management](https://aws.amazon.com/iam/) 
+  [AWS Key Management Service](https://aws.amazon.com/kms/) 