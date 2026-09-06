

# Encryption at rest
<a name="next-gen-encryption-at-rest"></a>

All Next generation Resilience Hub data is encrypted at rest.


| Data store | Encryption | 
| --- | --- | 
| DynamoDB tables | AWS-managed keys (default) or customer-managed AWS KMS keys | 
| S3 objects (topology, assessment results) | SSE-S3 (default) or SSE-KMS with customer-managed keys | 