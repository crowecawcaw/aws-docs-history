

# Service Quotas
<a name="plan-quotas"></a>

Review the service quotas below before deploying AVX. The defaults for new AWS accounts may require increases before reaching production-level load.

## Quota reference
<a name="plan-quotas-table"></a>


| Service | Quota | Default limit | Increase path | 
| --- | --- | --- | --- | 
| Amazon Bedrock — model invocation | Requests per minute (RPM) and tokens per minute (TPM) per model per region | Varies by model and region; Claude Sonnet and Nova 2 Sonic both have default quotas that may be insufficient for multi-tenant production load |  [Request a quota increase](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) in the Bedrock console under Service Quotas | 
| Amazon Bedrock AgentCore Runtime | Concurrent runtime invocations; invocations per second per runtime | Default concurrent invocations are modest; multi-tenant concurrent voice sessions may require increases |  [AgentCore quotas](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/quotas.html); request increases via the Service Quotas console | 
| Amazon Connect | Concurrent contacts per instance; contact flows per instance; queues per instance | New instances have conservative defaults; a multi-tenant production deployment with a chat queue and a callback queue per tenant may approach limits |  [Amazon Connect service quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html); request increases via Service Quotas or the Connect console | 
| AWS Lambda | Concurrent executions per region | 1,000 (default, adjustable) |  [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html); request increases via Service Quotas | 
| Amazon DynamoDB | Read/write capacity units (on-demand) or provisioned throughput | On-demand mode auto-scales; provisioned mode requires manual planning |  [DynamoDB quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html)  | 

**Tip**  
Request Bedrock model quota increases **before** onboarding a real workload — increases for Claude Sonnet and Nova 2 Sonic in your target region can take several business days to process. Plan for a two-week lead time for quota requests on high-demand models.

## Quota monitoring
<a name="plan-quotas-monitoring"></a>

AVX emits CloudWatch metrics for model invocation rates and AgentCore runtime invocations. Set [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) on these metrics at 80% of your quota thresholds to give advance warning before throttling affects customers. See the [Security](security.md) chapter for guidance on monitoring and audit logging.