# Resilience testing in S3 Express One Zone

Amazon S3 Express One Zone storage class supports resilience testing with AWS Fault Injection Service (AWS FIS), a fully managed service for performing fault injection experiments on your AWS workloads. With AWS FIS, you can simulate connectivity disruptions to your directory buckets, causing Zonal (object level, or data plane) endpoint API operations to timeout as would occur during an Availability Zone disruption.

These experiments can help you:

- Verify your monitoring systems can detect S3 Express One Zone access issues
- Test and strengthen recovery processes
- Validate that application failover mechanisms work as expected
- Ensure your application recovery time meets your organization's service level objectives (SLOs) and service level agreements (SLAs)
  By testing your application's response to simulated disruptions, you can better prepare for the unlikely event of an actual Availability Zone outage that affects access to your data in S3 Express One Zone.

## How it works

The test uses the `aws:network:disrupt-connectivity` action with scope set to `S3 Express`. This action disrupts network connectivity to S3 Express One Zone endpoints, causing requests to directory buckets to timeout.

You can target subnets where your applications are running or Gateway VPC endpoints used to access S3 Express One Zone. For more information, see [AZ Availability: Power Interruption](../../../fis/latest/userguide/az-availability-power-interruption.md "../../../fis/latest/userguide/az-availability-power-interruption.md") in the _AWS Fault Injection Service User Guide_.

To test the resilience of applications that store data in S3 Express One Zone, see [Simulate a connectivity event](../../../fis/latest/userguide/fis-tutorial-disrupt-connectivity.md "../../../fis/latest/userguide/fis-tutorial-disrupt-connectivity.md") in the _AWS Fault Injection Service User Guide_.

## Considerations and limitations

Keep in mind the following considerations and limitations for disrupting connectivity in Amazon S3 Express One Zone storage class:

### Considerations

- **IAM Permissions:** To use AWS FIS with S3 Express One Zone, you must configure an IAM role with appropriate permissions. For more information on AWS FIS roles, see [Create an IAM role for AWS FIS](../../../fis/latest/userguide/getting-started-iam-service-role.md "../../../fis/latest/userguide/getting-started-iam-service-role.md") in the _AWS Fault Injection Service User Guide_. We recommend scoping these permissions to only the necessary resources.
- **Target Resolution:** Targets are resolved at the beginning of the experiment. If a target subnet or gateway VPC endpoint is deleted during the experiment, the experiment will fail.
- **Shared Resources Impact:** If multiple applications share the same subnets or gateway VPC endpoints, all traffic to S3 Express One Zone from these applications will be affected during the experiment.
- **Rollback Behavior:** When the AWS FIS action ends, connectivity is automatically restored and requests will resume the expected operation without manual intervention.
- **Stop Conditions:** Configure appropriate CloudWatch alarms as stop conditions to automatically terminate experiments if unexpected impacts occur.

### Limitations

- **Target Selection:** You can't target specific S3 directory buckets. The action affects all directory buckets accessed through the targeted networking components.
- **Maximum Targets:** There is a maximum number of subnets you can target per AWS FIS action. For more information, see [Service quotas for AWS Fault Injection Service](../../../fis/latest/userguide/fis-quotas.md "../../../fis/latest/userguide/fis-quotas.md") in the _AWS FIS User Guide_.
- **Access Methods:** The AWS FIS action only affects requests made through the internet or gateway virtual private cloud (VPC) endpoints. Requests from interface VPC endpoints (AWS PrivateLink) aren't supported.
- **Regional Availability:** This feature is available only in [AWS Regions where S3 Express One Zone is supported](s3-express-Endpoints.md "s3-express-Endpoints.md").
