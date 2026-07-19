# Sending capacity provider system logs to CloudWatch Logs

By default, Lambda automatically captures system logs for your capacity provider and sends them to CloudWatch Logs, provided your capacity provider's [operator role](lambda-managed-instances-operator-role.md "lambda-managed-instances-operator-role.md") has the necessary permissions. These logs are stored in a log group named `/aws/lambda/capacity-provider/`<capacity-provider-name>``. If needed, you can configure your capacity provider to send logs to a different log group using the Lambda console, AWS CLI, or Lambda API. For more information, see [Configuring CloudWatch log groups](lambda-managed-instances-cwl-configure.md "lambda-managed-instances-cwl-configure.md").

You can view logs for your capacity provider using the Lambda console, the CloudWatch console, the AWS Command Line Interface (AWS CLI), or the CloudWatch API. For more information, see [Viewing CloudWatch logs for capacity providers](lambda-managed-instances-cwl-view-logs.md "lambda-managed-instances-cwl-view-logs.md").

## Required IAM permissions

Your capacity provider's [operator role](lambda-managed-instances-operator-role.md "lambda-managed-instances-operator-role.md") needs the following permissions to upload logs to CloudWatch Logs:

- `logs:CreateLogGroup`
- `logs:CreateLogStream`
- `logs:PutLogEvents`

To learn more, see [Using identity-based policies (IAM policies) for CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.md "../../../AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.md") in the _Amazon CloudWatch User Guide_.

You can add these CloudWatch Logs permissions using the `AWSLambdaManagedEC2ResourceOperator` AWS managed policy provided by Lambda. To add this policy to your role, run the following command:

```
`aws iam attach-role-policy --role-name `your-role` --policy-arn arn:aws:iam::aws:policy/AWSLambdaManagedEC2ResourceOperator`
```

For more information, see [Lambda operator role for Lambda Managed Instances](lambda-managed-instances-operator-role.md "lambda-managed-instances-operator-role.md").

###### Important

If the operator role doesn't have the required permissions, Lambda does not deliver system logs and does not return an error. Make sure that your operator role has the correct permissions to avoid silent log delivery failures.

## Pricing

There is no additional charge for using capacity provider system logs; however, standard CloudWatch Logs charges apply. For more information, see [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
