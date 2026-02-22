# Monitor Amazon ECS container instance health

Amazon ECS provides container instance health monitoring. You can quickly determine whether
Amazon ECS has detected any problems that might prevent your container instances from running
containers. Amazon ECS performs automated checks on every running container instance with agent
version `1.57.0` or later to identify issues. For more information on verifying
the agent version an a container instance, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").

You must be using AWS CLI version `1.22.3` or later or AWS CLI version
`2.3.6` or later. For information about how to update the AWS CLI, see [Installing
or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide Version 2_.

To view the container instance health, run `describe-container-instances` with
the `CONTAINER_INSTANCE_HEALTH` option.

The `overallStatus` is determined by the individual health check statuses in the `details` array.
The most severe status takes precedence in the following order: `IMPAIRED`, `INSUFFICIENT_DATA`,
`INITIALIZING`, and `OK`.

The following are the valid values for `overallStatus`:

- `OK` – All health checks are passing.
- `IMPAIRED` – One or more health checks have failed.
- `INSUFFICIENT_DATA` – One or more health checks are unavailable.
- `INITIALIZING` – One or more health checks are being initialized.
  The following is an example of how to run `describe-container-instances`.

```
aws ecs describe-container-instances \
     --cluster `cluster_name` \
     --container-instances `47279cd2cadb41cbaef2dcEXAMPLE` \
     --include CONTAINER_INSTANCE_HEALTH
```

The following is an example of the health status object in the output.

```
"healthStatus": {
	"overallStatus": "OK",
	"details": [{
		"type": "CONTAINER_RUNTIME",
		"status": "OK",
		"lastUpdated": "2021-11-10T03:30:26+00:00",
		"lastStatusChange": "2021-11-10T03:26:41+00:00"
	}]
}
```

## Container instance-health issues

When the `overallStatus` any status other than `OK`, try the
following:

- Wait, and then run `describe-container-instances`
- View your container instance health in the EC2 console or by using the
  CLI.
- Review the CloudWatch metrics. For more information, see [Monitor Amazon ECS using CloudWatch](cloudwatch-metrics.md "cloudwatch-metrics.md")
- Check the AWS Health Dashboard to see if there are any issues with the service.
