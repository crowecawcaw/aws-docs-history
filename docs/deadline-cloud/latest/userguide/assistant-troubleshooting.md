

# Troubleshooting
<a name="assistant-troubleshooting"></a>

This section describes common issues you might encounter when using the Deadline Cloud assistant and how to resolve them.

## Assistant returns errors or is slow to respond
<a name="assistant-ts-errors"></a>

The assistant displays error messages or takes a long time to generate responses.

### Common cause
<a name="assistant-ts-errors-cause"></a>

Errors or slow responses typically occur when your Amazon Bedrock service quotas are exceeded or when the monitor user role is missing required permissions.

### Resolution
<a name="assistant-ts-errors-resolution"></a>
+ Check your Amazon Bedrock service quotas in your Region. See [Amazon Bedrock quotas for the Deadline Cloud assistant](deadline-cloud-quotas.md#assistant-bedrock-quotas) for details on checking and increasing your quotas.
+ If you receive throttling errors, request a service quota increase for Amazon Bedrock in your Region.
+ Verify that your monitor user role has the required permissions listed in [Required permissions](assistant-permissions.md).

## Assistant cannot access Amazon CloudWatch logs
<a name="assistant-ts-logs"></a>

The assistant cannot retrieve or analyze log data from CloudWatch.

### Common cause
<a name="assistant-ts-logs-cause"></a>

The assistant cannot retrieve logs when the queue role or fleet role lacks the required CloudWatch Logs read permissions.

### Resolution
<a name="assistant-ts-logs-resolution"></a>

The assistant assumes the queue role (by using `deadline:AssumeQueueRoleForRead`) to read task logs and the fleet role (by using `deadline:AssumeFleetRoleForRead`) to read worker logs. Verify that these roles have CloudWatch Logs read permissions.