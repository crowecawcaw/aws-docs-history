# Troubleshooting Parameter Store

Use the following information to help you troubleshoot problems with Parameter Store, a tool in AWS Systems Manager.

## Troubleshooting throughput issues

Use the following information to troubleshoot throughput issues in Parameter Store. For information about throughput quotas and why throttling occurs,
see [Optimizing throughput in Parameter Store](parameter-store-throughput.md#parameter-store-throughput-optimizing "parameter-store-throughput.md#parameter-store-throughput-optimizing").

### Application receives `ThrottlingException` or `RateExceeded` errors

**Problem**: Your application logs or CloudWatch Logs show an
error such as the following when calling `GetParameter`, `GetParameters`,
or `GetParametersByPath`:

```
An error occurred (ThrottlingException) when calling the GetParameters operation (reached max retries: 4): Rate exceeded
```

- **Solution**: This error means your combined call rate
  for these API actions exceeded your account throughput quota for the current
  AWS Region. Take one or more of the following actions:

  - Reduce how often your application calls Parameter Store. Cache parameter values in
    your application instead of retrieving them on every invocation or request.

  For more information, see [Parameters and Secrets Lambda Extension](ps-integration-lambda-extensions.md "ps-integration-lambda-extensions.md") and [Using the AWS Parameter and Secrets Lambda extension to cache parameters and secrets](https://aws.amazon.com/blogs/compute/using-the-aws-parameter-and-secrets-lambda-extension-to-cache-parameters-and-secrets/ "https://aws.amazon.com/blogs/compute/using-the-aws-parameter-and-secrets-lambda-extension-to-cache-parameters-and-secrets/").
  - Use `GetParameters` to retrieve multiple known parameter names in
    a single call, rather than issuing separate `GetParameter` calls or
    a `GetParametersByPath` call.
  - Stagger reads when many instances, containers, or functions start at the same
    time, such as during a deployment or a scaling event.
  - If your application uses efficient request patterns and continues to
    generate throttling errors, enable higher throughput for your account and
    AWS Region. You can enable and disable higher throughput at any time. The cost is determined by usage.
    For more information, see [AWS Systems Manager Pricing for Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store "https://aws.amazon.com/systems-manager/pricing/#Parameter_Store").

### Throttling occurs only on `DescribeParameters` calls

**Problem**: Your application receives a
`ThrottlingException` error on `DescribeParameters` calls, even though
your `GetParameter`, `GetParameters`, and `GetParametersByPath`
calls don't exceed the quota.

- **Solution**: `DescribeParameters` has a
  separate throughput limit from the other parameter retrieval actions: 3
  TPS by default, or 10 TPS with higher throughput enabled. Making fewer
  `GetParameter`, `GetParameters`, or
  `GetParametersByPath` calls doesn't affect this limit.

A common cause is calling `DescribeParameters` with a filter on an account
that has a large number of parameters. The API paginates over all parameters in the
account before applying the filter. Accounts with many parameters can exceed the
`DescribeParameters` quota even when the filtered result set is
small.

Where possible, use `GetParametersByPath` against a specific
hierarchy instead of `DescribeParameters` with a filter. You can also reduce the
frequency of `DescribeParameters` calls in scripts and automation that run
on a schedule.

### No throttling error, but latency increases during deployments

**Problem**: You don't see a `ThrottlingException`
error in your logs, but your application experiences elevated latency or intermittent failures during
deployments, restarts, or scaling events.

- **Solution**: If your application or SDK retries
  throttled requests automatically, a retry can succeed without ever surfacing a
  throttling error. If your latency increases, check the retry count in the
  logs or metrics of your SDK. A nonzero retry count on Parameter Store calls during these events indicates
  you're approaching your throughput quota, even without a failure. Apply the
  same optimization techniques described in [Optimizing throughput in Parameter Store](parameter-store-throughput.md#parameter-store-throughput-optimizing "parameter-store-throughput.md#parameter-store-throughput-optimizing") to reduce retries before
  they become failures.

## Troubleshooting `aws:ec2:image` parameter creation

Use the following information to help troubleshoot problems with creating
`aws:ec2:image` data type parameters.

### No permission to create an instance

**Problem**: You try to create an instance using
an `aws:ec2:image` parameter but receive an error message such as
"You are not authorized to perform this operation."

- **Solution**: You do not have all the
  permissions needed to create an EC2 instance using a parameter value,
  such as permissions for `ec2:RunInstances`,
  `ec2:DescribeImages`, and `ssm:GetParameter`,
  among others. Contact a user with administrator permissions in your
  organization to request the necessary permissions.

### EventBridge reports the failure message "Unable to Describe Resource"

**Problem**: You ran a command to create an
`aws:ec2:image` parameter, but parameter creation failed. You
receive a notification from Amazon EventBridge that reports the exception "Unable to
Describe Resource".

**Solution**: This message can indicate the
following:

- You do not have all the permissions needed for the
  `ec2:DescribeImages` API operation, or you lack
  permission to access the specific image referenced in the parameter.
  Contact a user with administrator permissions in your organization to
  request the necessary permissions.
- The Amazon Machine Image (AMI) ID you entered as a parameter value isn't valid.
  Make sure you're entering the ID of an AMI that is available in the
  current AWS Region and account you're working in.

### New `aws:ec2:image` parameter isn't available

**Problem**: You just ran a command to create an
`aws:ec2:image` parameter and a version number was reported, but
the parameter isn't available.

- **Solution**: When you run the command to
  create a parameter that uses the `aws:ec2:image` data type, a
  version number is generated for the parameter right away, but the
  parameter format must be validated before the parameter is available.
  This process can take up to a few minutes. To monitor the parameter
  creation and validation process, you can do the following:

  - Use EventBridge to send you notifications about your
    `create` and `update` parameter
    operations. These notifications report whether a parameter
    operation was successful or not. For information about
    subscribing to Parameter Store events in EventBridge, see [Setting up notifications or triggering actions based on Parameter Store events](sysman-paramstore-cwe.md "sysman-paramstore-cwe.md").
  - In the Parameter Store section of the Systems Manager console, refresh the list
    of parameters periodically to search for the new or updated
    parameter details.
  - Use the **GetParameter** command to check for
    the new or updated parameter. For example, using the AWS Command Line Interface
    (AWS CLI):

  ```
  aws ssm get-parameter name `MyParameter`
  ```

  For a new parameter, a `ParameterNotFound` message
  is returned until the parameter is validated. For an existing
  parameter that you're updating, information about the new
  version isn't included until the parameter is validated.
  If you attempt to create or update the parameter again before the
  validation process is complete, the system reports that validation is
  still in process. If the parameter isn't created or updated, you can try
  again after 5 minutes have passed from the original attempt.
