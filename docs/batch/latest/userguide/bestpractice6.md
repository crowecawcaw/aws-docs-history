# Use Amazon EC2 Spot best practices for AWS Batch

When you choose Amazon Elastic Compute Cloud (EC2) Spot instances, you likely can optimize your workflow to
save costs, sometimes significantly. For more information, see [Best practices
for Amazon EC2 Spot](../../../AWSEC2/latest/UserGuide/spot-best-practices.md#be-instance-type-flexible "../../../AWSEC2/latest/UserGuide/spot-best-practices.md#be-instance-type-flexible").

To optimize your workflow to save costs, consider the following Amazon EC2 Spot best practices
for AWS Batch:

- Choose the `SPOT_CAPACITY_OPTIMIZED` allocation strategy –
  AWS Batch chooses Amazon EC2 instances from the deepest Amazon EC2 Spot capacity pools. If you’re concerned about
  interruptions, this is a suitable choice. For more information, see [Instance type allocation strategies for AWS Batch](allocation-strategies.md "allocation-strategies.md").
- Diversify instance types – To diversify your instance types, consider
  compatible sizes and families, then let AWS Batch choose based on price or availability. For example, consider
  `c5.24xlarge` as an alternative to `c5.12xlarge` or `c5a`, `c5n`,
  `c5d`, `m5`, and `m5d` families. For more information, see [Be
  flexible about instance types and Availability Zones](../../../AWSEC2/latest/WindowsGuide/spot-best-practices.md#be-instance-type-flexible "../../../AWSEC2/latest/WindowsGuide/spot-best-practices.md#be-instance-type-flexible").
- Reduce job runtime or checkpoint – We advise against
  running jobs that take an hour or more when using Amazon EC2 Spot instances to avoid interruptions.
  If you divide or checkpoint your jobs into smaller parts that consist of 30 minutes or less,
  you can significantly reduce the possibility of interruptions.
- Use automated retries – To avoid disruptions to AWS Batch jobs, set
  automated retries for jobs. Batch jobs can be disrupted for any of the following reasons: a non-zero exit code is
  returned, a service error occurs, or an instance reclamation occurs. You can set up to 10 automated retries. For a
  start, we recommend that you set at least 1-3 automated retries. For information about tracking Amazon EC2 Spot
  interruptions, see [Spot Interruption
  Dashboard](https://github.com/aws-samples/ec2-spot-interruption-dashboard "https://github.com/aws-samples/ec2-spot-interruption-dashboard").

For AWS Batch, if you set the retry parameter, the job is placed at the front of the job queue. That is, the job
is given priority. When you create the job definition or you submit the job in the AWS CLI, you can configure a retry
strategy. For more information, see [submit-job](../../../goto/aws-cli/batch-2016-08-10/SubmitJob.md "../../../goto/aws-cli/batch-2016-08-10/SubmitJob.md").

```
`$` `aws batch submit-job --job-name MyJob \
 --job-queue MyJQ \
 --job-definition MyJD \
 --retry-strategy attempts=2`
```

- Use custom retries – You can configure a job retry strategy to a
  specific application exit code or instance reclamation. In the following example, if the host causes the failure,
  the job can be retried up to five times. However, if the job fails for a different reason, the job exits and the
  status is set to `FAILED`.

```
"retryStrategy": {
    "attempts": 5,
    "evaluateOnExit":
    [{
        "onStatusReason" :"Host EC2*",
        "action": "RETRY"
    },{
      "onReason" : "*",
        "action": "EXIT"
    }]
}
```

- Use the Spot Interruption Dashboard – You can use the
  Spot Interruption Dashboard to track Spot interruptions. The application provides metrics on
  Amazon EC2 Spot instances that are reclaimed and which Availability Zones that Spot instances are
  in. For more information, see [Spot Interruption
  Dashboard](https://github.com/aws-samples/ec2-spot-interruption-dashboard "https://github.com/aws-samples/ec2-spot-interruption-dashboard")
