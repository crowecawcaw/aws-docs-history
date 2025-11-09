# Monitor Amazon Bedrock Guardrails using CloudWatch metrics

The following table describes runtime metrics provided by Amazon Bedrock Guardrails that you can monitor
with Amazon CloudWatch metrics.

**Runtime metrics**

| Metric name            | Unit         | Description                                                                                                 |
| ---------------------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| Invocations            | SampleCount  | Number of requests to the `ApplyGuardrail` API<br>operation                                                 |
| InvocationLatency      | MilliSeconds | Latency of the invocations                                                                                  |
| InvocationClientErrors | SampleCount  | Number of invocations that result in client-side errors                                                     |
| InvocationServerErrors | SampleCount  | Number of invocations that result in AWS server-side errors                                                 |
| InvocationThrottles    | SampleCount  | Number of invocations that the system throttled. Throttled requests don't<br>count as invocations or errors |
| TextUnitCount          | SampleCount  | Number of text units consumed by the guardrails policies                                                    |
| InvocationsIntervened  | SampleCount  | Number of invocations where the guardrails intervened                                                       |
| FindingCounts          | SampleCount  | Counts for each type of finding from InvokeAutomatedReasoningCheck                                          |
| TotalFindings          | SampleCount  | Counts number of findings produced for each InvokeAutomatedReasoningCheck request                           |
| Invocations            | SampleCount  | Number of requests to InvokeAutomatedReasoningCheck                                                         |
| Latency                | MilliSeconds | Latency of verification using automated reasoning policy                                                    |

You can view guardrail dimensions in the CloudWatch console based on the table below:

**Dimension**

| Dimension name                                | Dimension values                                                                                                | Available for the following metrics                                                                                                                                 |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Operation                                     | ApplyGuardrail                                                                                                  | • Invocations<br>• InvocationLatency<br>• InvocationClientErrors<br>• InvocationServerErrors<br>• InvocationThrottles<br>• InvocationsIntervened<br>• TextUnitCount |
| GuardrailContentSource                        | • Input<br>• Output                                                                                             | • Invocations<br>• InvocationLatency<br>• InvocationClientErrors<br>• InvocationServerErrors<br>• InvocationThrottles<br>• InvocationsIntervened<br>• TextUnitCount |
| GuardrailPolicyType                           | • ContentPolicy<br>• TopicPolicy<br>• WordPolicy<br>• SensitiveInformationPolicy<br>• ContextualGroundingPolicy | • InvocationsIntervened<br>• TextUnitCount                                                                                                                          |
| GuardrailArn, GuardrailVersion                | • Guardrail ARN<br>• Guardrail Version number or DRAFT                                                          | • Invocations<br>• InvocationLatency<br>• InvocationClientErrors<br>• InvocationServerErrors<br>• InvocationThrottles<br>• InvocationsIntervened<br>• TextUnitCount |
| FindingType + PolicyArn + PolicyVersion       | FindingType + PolicyArn + PolicyVersion                                                                         | • FindingCounts                                                                                                                                                     |
| FindingType + GuardrailArn + GuardrailVersion | FindingType + GuardrailArn + GuardrailVersion                                                                   | • FindingCounts                                                                                                                                                     |
| PolicyArn + PolicyVersion                     | PolicyArn + PolicyVersion                                                                                       | • TotalFindings<br>• Invocations<br>• Latency                                                                                                                       |
| GuardrailArn + GuardrailVersion               | GuardrailArn + GuardrailVersion                                                                                 | • TotalFindings                                                                                                                                                     |

**Get CloudWatch metrics for guardrails**

You can get metrics for guardrails with the AWS Management Console, the AWS CLI,
or the CloudWatch API. You can use the CloudWatch API through one of the AWS Software Development
Kits (SDKs) or the CloudWatch API tools.

The namespace for guardrail metrics in CloudWatch is `AWS/Bedrock/Guardrails`.

###### Note

You must have the appropriate CloudWatch permissions to monitor guardrails
with CloudWatch. For more information, see [Authentication and Access Control for CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md")
in the CloudWatch User Guide.

**View guardrails metrics in the CloudWatch console**

1. Sign in to the AWS Management Console and open the CloudWatch console at
   https://console.aws.amazon.com/cloudwatch/.
2. Choose the `AWS/Bedrock/Guardrails` namespace.
