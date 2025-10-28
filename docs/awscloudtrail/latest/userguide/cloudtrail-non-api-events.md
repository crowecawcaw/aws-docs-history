# Non-API events captured by CloudTrail

In addition to logging AWS API calls, CloudTrail captures other related events that might have
a security or compliance impact on your AWS account or that might help you troubleshoot
operational problems.

- [AWS service events](non-api-aws-service-events.md "non-api-aws-service-events.md") – CloudTrail supports logging non-API service events. These events are created by AWS
  services but are not directly triggered by a request to a public AWS API. For these
  events, the `eventType` field is `AwsServiceEvent`.
- [AWS Management Console
  sign-in events](cloudtrail-event-reference-aws-console-sign-in-events.md "cloudtrail-event-reference-aws-console-sign-in-events.md") – CloudTrail logs attempts to sign in to the AWS Management Console,
  the AWS Discussion Forums, and the AWS Support Center. All IAM user and
  root user sign-in events, as well as all federated user sign-in events, generate
  records in CloudTrail. For sign-in events, the `eventType` field is `AwsConsoleSignIn`.
