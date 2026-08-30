# Service quotas for managed knowledge bases

Your AWS account has default quotas, formerly referred to as limits, for managed
Amazon Bedrock knowledge bases. To view service quotas for Amazon Bedrock, do one of the following:

- Follow the steps at [Viewing service
  quotas](../../../servicequotas/latest/userguide/gs-request-quota.md "../../../servicequotas/latest/userguide/gs-request-quota.md") and select **Amazon Bedrock** as the service.
- Refer to [Amazon Bedrock service
  quotas](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") in the AWS General Reference.
  The following quotas apply specifically to managed knowledge bases:

Managed knowledge base quotas| Quota | Default value | Adjustable |
| --- | --- | --- |
| Maximum managed knowledge bases per account, per Region | 10,000 | Yes |
| Maximum data sources per knowledge base | 200 | No |
| Maximum concurrent ingestion jobs per knowledge base | 50 | No |
| Maximum raw data storage per knowledge base | 10 TB | No |
| Maximum query input characters per `Retrieve` or<br>`AgenticRetrieveStream` request (English text) | 10,000 | No |
| Maximum `Retrieve` requests per minute (RPM), per knowledge base | 600 (supports burst of 25 requests per second (RPS)) | Yes |
| Maximum `AgenticRetrieveStream` requests per minute, per account | 300 | Yes |

To request adjustable quota increases, follow the steps at [Requesting a
quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md"), or contact your AWS account team.
