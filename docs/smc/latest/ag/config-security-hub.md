# Configuring AWS Security Hub

Integration

AWS Security Hub enables users to view security findings from AWS services,
such as Amazon Guard Duty, Amazon Inspector, as well as AWS Partner
solutions.

If you use both [AWS Security Hub](https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc "https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc") and [Jira
Service Management](https://www.atlassian.com/software/jira/service-management "https://www.atlassian.com/software/jira/service-management") (JSM), the AWS Service Management Connector
for JSM allows you to create an automated, bidirectional integration
between Security Hub and JSM. This two-way integration synchronizes your Security
Hub findings and Jira issues.

Specifically, as a Jira administrator, you can use this integration to
automatically create Jira issues from Security Hub findings. When you update
those tickets in Jira, the changes are automatically replicated back to
the original Security Hub findings. For example, when you resolve the issue in
Jira, the workflow status of the Security Hub finding also changes to
`RESOLVED`. This action ensures Security Hub always has up-to-date
information about your security posture.

###### To configure AWS Security Hub integration features

1. Enable AWS Security Hub. For more information, see [Accessing Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md#securityhub-get-started "../../../securityhub/latest/userguide/what-is-securityhub.md#securityhub-get-started").
2. Set up an SQS queue to receive updated Findings. Name the queue
   **AwsSmcJsmSecurityHubQueue** to align
   with the default name in the JSM Connector Settings for the AWS Security Hub
   integration. For more information, see [Getting started with Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md").
3. Set up a Amazon EventBridge rule to detect changes to Findings and
   push these to the queue. For more information, see [Getting started with Amazon EventBridge.](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md")

The CloudWatch rule should have the following event pattern and
should point to the SQS queue created in Step 2.

```
"EventPattern": {

       "source": [

        "aws.securityhub"

        ]
}
```

4. You can also customize this CloudWatch Events rule to only pull in
   Security Hub findings that have specific finding types, severity labels,
   workflow statuses, or compliance statuses. For details about how to
   filter the event pattern, see [Configuring an EventBridge rule for automatically sent
   findings](../../../securityhub/latest/userguide/securityhub-cwe-all-findings.md "../../../securityhub/latest/userguide/securityhub-cwe-all-findings.md") in the _AWS Security Hub
   User Guide_.

###### Note

You can use the available AWS CloudFormation templates for the JSM connector
to configure your AWS account to enable AWS Service Catalog integration. For more
information, see [Baseline Permissions](jsd-baseline-permissions.md "jsd-baseline-permissions.md").

## Video: Bidirectional integration with Atlassian Jira Service

Management

This video (8:40) describes how to set up a bidirectional
integration with Atlassian Jira Service Management. This feature makes
it easier for AWS Security Hub users to automatically create and update issues
in Jira Service Management from AWS Security Hub findings and ensure that
updates to those tickets are synced with the findings.
