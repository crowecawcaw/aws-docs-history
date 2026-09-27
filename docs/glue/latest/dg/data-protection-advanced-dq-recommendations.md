

# Data protection for advanced data quality rule recommendations
<a name="data-protection-advanced-dq-recommendations"></a>

For an `ADVANCED` run, Athena samples rows from the source table. AWS Glue does not exclude any table column from the sample.

AWS Glue sends the table metadata and sampled rows to Amazon Bedrock. Amazon Bedrock uses this data to generate Data Quality Definition Language (DQDL) rules.

Amazon Bedrock does not retain the model inputs or outputs after it processes the request. AWS and third-party model providers do not use these inputs or outputs to train models.

For more information about data protection in Amazon Bedrock, see [Data protection in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html).

For more information about retention and model training, see [Data retention policies for model inference](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html) and [Amazon Bedrock FAQs](https://aws.amazon.com/bedrock/faqs/).

For more information about recommendation modes, see [Recommendation modes](data-quality-getting-started.md#data-quality-recommendation-modes).

## Encryption in transit
<a name="advanced-dq-encryption-in-transit"></a>

Advanced recommendation runs use [geographic cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html). Amazon Bedrock can process your request in another AWS Region within the geographic boundary of the inference profile.

Your sampled content and the generated response can move outside the Region where you start the run. AWS encrypts this content in transit over the AWS network.

## Encryption at rest
<a name="advanced-dq-encryption-at-rest"></a>

By default, Athena stores query results in the `aws-glue-dataquality-sampling-{{account-id}}-{{region}}` bucket in your account. AWS Glue adds a lifecycle rule that expires objects after 14 days.

AWS Glue uses the `glue-dataquality-sampling` Athena workgroup. If the workgroup does not exist, AWS Glue creates it.

If you specify `DataQualitySecurityConfiguration`, Athena encrypts the query results with the customer managed AWS KMS key from that configuration.

## Key management
<a name="advanced-dq-key-management"></a>

If you specify a customer managed AWS KMS key, your recommendation role needs permissions for query result encryption and AWS Glue Data Quality asset encryption. The key policy must also allow these operations for your role.

For more information about the required recommendation role permissions, see [Minimum permissions to get advanced data quality rule recommendations](data-quality-authorization.md#example-policy-get-advanced-dq-rule-recommendations).