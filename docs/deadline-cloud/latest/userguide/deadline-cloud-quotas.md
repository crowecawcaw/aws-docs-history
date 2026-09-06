# Service quotas and throttling for Deadline Cloud

AWS Deadline Cloud provides resources, such as farms, fleets, and queues, that you can use to
process jobs. When you create your AWS account, we set default quotas on these resources
for each AWS Region. Deadline Cloud also limits the rate of API requests. For more information,
see [API request throttling](#deadline-cloud-throttling "#deadline-cloud-throttling").

Service Quotas is a central location where you can view and manage your quotas for
AWS services. You can also request a quota increase for many of the resources that you
use.

To view the quotas for Deadline Cloud, open the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS services** and
select **Deadline Cloud**.

To request a quota increase, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_. If the quota is not yet
available in Service Quotas, use the [service quota increase
form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

Your AWS account has the following quotas related to Deadline Cloud.

The _associated members_ quotas count the memberships that you
assign to a farm, fleet, queue, or job. Each user grant and each group grant counts
as one membership, so a group counts as one member no matter how many users it
contains. Deadline Cloud doesn't limit the number of users in a group or the number of
groups that a user belongs to; the quotas for AWS IAM Identity Center apply instead. To grant
access to more users within the membership quota, assign groups instead of
individual users. For more information, see [How permissions work in Deadline Cloud](permissions-overview.md "permissions-overview.md").

Compute for service-managed fleets counts against the Deadline Cloud vCPU and GPU quotas in the
following table, not against your Amazon Elastic Compute Cloud (Amazon EC2) service quotas. For more information,
see [Quotas for related services](#related-service-quotas "#related-service-quotas").

The following table includes quotas for persistent storage volumes used by
service-managed fleets. For more information about persistent storage, see [Persistent storage for service-managed fleets](volumes.md "volumes.md").

| Name                                                             | Default                        | Adjustable                                                                                                                                                                           | Description                                                                                                                                                                                              |
| ---------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Associated members per farm                                      | Each supported Region: 75      | No                                                                                                                                                                                   | The maximum number of principals (users or groups) that can be associated to each farm in the current AWS Region. Each associated group counts as one member, regardless of how many users it contains.  |
| Associated members per fleet                                     | Each supported Region: 75      | No                                                                                                                                                                                   | The maximum number of principals (users or groups) that can be associated to each fleet in the current AWS Region. Each associated group counts as one member, regardless of how many users it contains. |
| Associated members per job                                       | Each supported Region: 75      | No                                                                                                                                                                                   | The maximum number of principals (users or groups) that can be associated to each job in the current AWS Region. Each associated group counts as one member, regardless of how many users it contains.   |
| Associated members per queue                                     | Each supported Region: 75      | No                                                                                                                                                                                   | The maximum number of principals (users or groups) that can be associated to each queue in the current AWS Region. Each associated group counts as one member, regardless of how many users it contains. |
| Budgets per farm                                                 | Each supported Region: 20      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-86C1F13E "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-86C1F13E") | The maximum number of budgets per farm in the current AWS Region                                                                                                                                         |
| Farms per region                                                 | Each supported Region: 2       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-2DEF7E07 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-2DEF7E07") | The maximum number of farms that can be created in the current AWS Region.                                                                                                                               |
| Fleets per farm                                                  | Each supported Region: 5       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-55A8E463 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-55A8E463") | The maximum number of fleets that can be created for each farm in the current AWS Region.                                                                                                                |
| Jobs per farm                                                    | Each supported Region: 100,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-5369B22C "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-5369B22C") | The maximum number of jobs per farm in the current AWS Region.                                                                                                                                           |
| License endpoints per region                                     | Each supported Region: 5       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-F0DF6BC2 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-F0DF6BC2") | The maximum number of license endpoints in the current AWS Region.                                                                                                                                       |
| License sessions per license endpoint                            | Each supported Region: 500     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-EFCAFDCA "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-EFCAFDCA") | The maximum number of license sessions per license endpoint in the current AWS Region.                                                                                                                   |
| Limits per farm                                                  | Each supported Region: 50      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-253A82CE "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-253A82CE") | The maximum number of limits that can be created for each farm in the current AWS Region.                                                                                                                |
| Monitors per region                                              | Each supported Region: 1       | No                                                                                                                                                                                   | The maximum number of monitors in the current AWS Region.                                                                                                                                                |
| OnDemand G instance GPUs per region                              | Each supported Region: 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-5D6BA491 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-5D6BA491") | The maximum number of on-demand G instance GPUs that can be provisioned across all service-managed fleets in the current AWS Region.                                                                     |
| OnDemand vCPUs per region                                        | Each supported Region: 50      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-3ED8FD3C "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-3ED8FD3C") | The maximum number of on-demand vCPUs that can be provisioned across all service-managed fleets in the current AWS Region.                                                                               |
| Queue environments per queue                                     | Each supported Region: 10      | No                                                                                                                                                                                   | The maximum number of queue environments that can be created for each queue in the current AWS Region.                                                                                                   |
| Queue fleet associations per farm                                | Each supported Region: 100     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-BF011D88 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-BF011D88") | The maximum number of queue fleet associations per farm in the current AWS Region                                                                                                                        |
| Queue limit associations per queue                               | Each supported Region: 10      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-55B7030C "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-55B7030C") | The maximum number of limits that can be associated with each queue in the current AWS Region.                                                                                                           |
| Queues per farm                                                  | Each supported Region: 20      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-5E4FD3A4 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-5E4FD3A4") | The maximum number of queues that can be created for each farm in the current AWS Region.                                                                                                                |
| Resource configurations per fleet                                | Each supported Region: 1       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-9F7AA0C8 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-9F7AA0C8") | The maximum number of VPC Lattice resource configurations that can be added to each fleet.                                                                                                               |
| Spot G Instance GPUs per region                                  | Each supported Region: 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-2CCF07BF "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-2CCF07BF") | The maximum number of spot G instance GPUs that can be provisioned across all service-managed fleets in the current AWS Region.                                                                          |
| Spot vCPUs per region                                            | Each supported Region: 50      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-F4A135EC "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-F4A135EC") | The maximum number of spot vCPUs that can be provisioned across all service-managed fleets in the current AWS Region.                                                                                    |
| Step consumers per step                                          | Each supported Region: 32      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-B38F4796 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-B38F4796") | The maximum number of steps that may declare a dependency on (consume) a single step within a job in the current AWS Region.                                                                             |
| Step dependencies per step                                       | Each supported Region: 128     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-3A262554 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-3A262554") | The maximum number of steps that a single step within a job may declare a dependency on in the current AWS Region.                                                                                       |
| Steps per job                                                    | Each supported Region: 200     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-BABD8718 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-BABD8718") | The maximum number of steps per job in the current AWS Region.                                                                                                                                           |
| Storage for General Purpose SSD (gp3) volumes, in TiB            | Each supported Region: 1       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-711C7611 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-711C7611") | The maximum aggregated amount of EBS storage, measured in TiB, that can be used across all fleets in the current AWS Region.                                                                             |
| Storage for persistent General Purpose SSD (gp3) volumes, in TiB | Each supported Region: 4       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-49CA2379 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-49CA2379") | The maximum aggregated amount of storage, in TiB, that can be provisioned across persistent General Purpose SSD (gp3) volumes in the current AWS Region.                                                 |
| Storage profiles per farm                                        | Each supported Region: 50      | No                                                                                                                                                                                   | The maximum number of storage profiles that can be created for each farm in the current AWS Region.                                                                                                      |
| Tasks per chunk                                                  | Each supported Region: 150     | No                                                                                                                                                                                   | The maximum number of tasks that can be combined into a single chunk when submitting a job.                                                                                                              |
| Tasks per job                                                    | Each supported Region: 10,000  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-CF66A041 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-CF66A041") | The maximum number of tasks per job in the current AWS Region.                                                                                                                                           |
| Tasks per step                                                   | Each supported Region: 10,000  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-3DE82FE6 "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-3DE82FE6") | The maximum number of tasks per step in the current AWS Region.                                                                                                                                          |
| Wait-and-save vCPUs per region                                   | Each supported Region: 50      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-B65B621C "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-B65B621C") | The maximum number of wait-and-save vCPUs that can be provisioned across all service-managed fleets in the current AWS Region.                                                                           |
| Workers per farm                                                 | Each supported Region: 7,500   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-48CC9B8E "https://console.aws.amazon.com/servicequotas/home/services/deadline/quotas/L-48CC9B8E") | The maximum number of workers per farm in the current AWS Region.                                                                                                                                        |

## API request throttling

Deadline Cloud limits the rate of API requests for each AWS account in each AWS Region.
The default request rates support large-scale workloads and usage. When your requests
exceed the allowed rate, Deadline Cloud rejects the request with an HTTP 429 status code and a
`ThrottlingException` error.

The AWS SDKs and the AWS CLI automatically retry throttled requests using
exponential backoff. Occasional throttling resolves without requiring changes to your
application. If you experience sustained throttling, contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to request higher request rates.

## Quotas for related services

Some Deadline Cloud features use other AWS services, and the quotas for those services
also apply.

### Amazon EC2 quotas for customer-managed fleets

Your Amazon Elastic Compute Cloud (Amazon EC2) quotas apply to [customer-managed
fleets](../developerguide/manage-cmf.md "../developerguide/manage-cmf.md"), because those workers run on instances in your own account.
Compute for service-managed fleets counts against the Deadline Cloud vCPU and GPU quotas in
the preceding table instead.

To view or increase your Amazon EC2 quotas, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home") and choose
**Amazon Elastic Compute Cloud**. For more information, see [Amazon EC2 service
quotas](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md") in the _Amazon EC2 User Guide_.

### Amazon Bedrock quotas for the Deadline Cloud assistant

The [Deadline Cloud assistant](deadline-cloud-assistant.md "deadline-cloud-assistant.md") uses Amazon Bedrock on-demand inference in
your AWS account, so your account's Amazon Bedrock service quotas apply. The two primary
constraints are:

- **Requests per minute (RPM)** – The
  number of model invocation requests allowed per minute.
- **Tokens per minute (TPM)** – The
  total number of input and output tokens processed per minute.

Default quotas vary by Region. Some Regions have lower default limits, as low as
20 RPM, which might result in throttling during heavy assistant usage. The
assistant uses [cross-region
inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md") profiles, which support a minimum of 200 RPM. Cross-region
inference can help alleviate throttling in Regions with lower single-Region limits.
If your Region uses cross-region inference, the service quotas in the destination
Regions also apply.

If you experience throttling errors when using the assistant, you can request an
Amazon Bedrock service quota increase:

###### To request a quota increase

1. Open the [Service Quotas
   console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2. In the navigation pane, choose **AWS services**, then
   choose **Amazon Bedrock**.
3. Find the quota for the model used by the assistant (look for quotas
   related to `InvokeModelWithResponseStream` for the relevant
   model).
4. Choose the quota name, then choose **Request increase at account
   level**.
5. Enter your desired quota value and submit the request.

You can monitor your Amazon Bedrock quota usage through CloudWatch metrics. Set up CloudWatch alarms
on Amazon Bedrock throttling metrics to identify when you are approaching your quota limits.
For more information, see [Monitoring
Amazon Bedrock](../../../bedrock/latest/userguide/monitoring-overview.md "../../../bedrock/latest/userguide/monitoring-overview.md") in the _Amazon Bedrock User Guide_.
