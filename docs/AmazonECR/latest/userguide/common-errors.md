# Troubleshooting Amazon ECR error messages

In some cases, an API call that you have initiated through the Amazon ECR console or the
AWS CLI exits with an error message. Some common error messages and potential solutions
are explained below.

## HTTP 429: Too Many Requests or

ThrottleException

You may receive a `429: Too Many Requests` error or a
`ThrottleException` error from one or more Amazon ECR actions or API
calls. This indicates that you are calling a single endpoint in Amazon ECR repeatedly
over a short interval, and that your requests are getting throttled. Throttling
occurs when calls to a single endpoint from a single user exceed a certain threshold
over a period of time.

Each API operations in Amazon ECR has a rate throttles associated with it. For example,
the throttle for the [`GetAuthorizationToken`](../APIReference/API_GetAuthorizationToken.md "../APIReference/API_GetAuthorizationToken.md") action is 20 transaction per
second (TPS), with up to a 200 TPS burst allowed. In each region, each account
receives a bucket that can store up to 200 `GetAuthorizationToken`
credits. These credits are replenished at a rate of 20 per second. If your bucket
has 200 credits, you could achieve 200 `GetAuthorizationToken` API
transactions per second for one second, and then sustain 20 transactions per second
indefinitely. For more information on the rate limits for Amazon ECR APIs, see [Amazon ECR service quotas](service-quotas.md "service-quotas.md").

To handle throttling errors, implement a retry function with incremental backoff
into your code. For more information, see [Retry behavior](../../../general/latest/gr/api-retries.md "../../../general/latest/gr/api-retries.md") in the _AWS SDKs and Tools Reference
Guide_. Another option is to request a rate limit increase, which you
can do using the Service Quotas console. For more information, see
[Managing your Amazon ECR service quotas in the
AWS Management Console](service-quotas.md#service-quotas-console "service-quotas.md#service-quotas-console")..

## HTTP 403: "User [arn] is not authorized to

perform [operation]"

You may receive the following error when attempting to perform an action with
Amazon ECR:

```
$ `aws ecr get-login-password`
A client error (AccessDeniedException) occurred when calling the GetAuthorizationToken operation:
    User: arn:aws:iam::`account-number`:user/`username` is not authorized to perform:
    ecr:GetAuthorizationToken on resource: *
```

This indicates that your user does not have permissions granted to use Amazon ECR, or
that those permissions are not set up correctly. In particular, if you are
performing actions against an Amazon ECR repository, verify that the user has been
granted permissions to access that repository. For more information about creating
and verifying permissions for Amazon ECR, see [Identity and Access Management for Amazon Elastic Container Registry](security-iam.md "security-iam.md").

## HTTP 404: "Repository Does Not Exist"

error

If you specify a Docker Hub repository that does not currently exist, Docker Hub
creates it automatically. With Amazon ECR, new repositories must be explicitly created
before they can be used. This prevents new repositories from being created
accidentally (for example, due to typos), and it also ensures that an appropriate
security access policy is explicitly assigned to any new repositories. For more
information about creating repositories, see [Amazon ECR private repositories](Repositories.md "Repositories.md").

## Error: Cannot perform an

interactive login from a non TTY device

If you receive the error `Cannot perform an interactive login from a non TTY
 device`, the following troubleshooting steps should help.

- Verify that you're using AWS CLI version 2 and that you don't have a
  conflicting version of AWS CLI version 1 on your system. For more information,
  see [Installing or
  updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- Verify that you've configured your AWS CLI with valid credentials. For more
  information, see [Installing or
  updating the latest version of the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").
- Verify that the syntax of your AWS CLI command is correct.
