# Reviewing and analyzing Macie findings

Amazon Macie generates findings when it detects potential policy violations or issues with the
security or privacy of your Amazon Simple Storage Service (Amazon S3) general purpose buckets or it detects sensitive
data in S3 objects. A _finding_ is a detailed report of a
potential issue or sensitive data that Macie found. Each finding provides a severity rating,
information about the affected resource, and additional details, such as when and how Macie
found the issue or data. Macie stores your policy and sensitive data findings for 90
days.

You can review, analyze, and manage findings in the following ways.

Amazon Macie console

The **Findings** pages on the Amazon Macie console list your findings and
provide detailed information for individual findings. These pages also provide
options for grouping, filtering, and sorting findings, and for creating and
managing suppression rules. Suppression rules can help you streamline your
analysis of findings.

Amazon Macie API

With the Amazon Macie API, you can query and retrieve findings data by using an AWS command
line tool or an AWS SDK, or by sending HTTPS requests directly to Macie. To
query the data, you submit a request to the Amazon Macie API and use supported
parameters to specify which findings you want to retrieve. After you submit your
request, Macie returns the results in a JSON response. You can then pass the
results to another service or application for deeper analysis, long-term
storage, or reporting. For more information, see the [Amazon Macie API Reference](../APIReference/welcome.md "../APIReference/welcome.md").

Amazon EventBridge

To further support integration with other services and systems, such as monitoring or
event management systems, Macie publishes findings to Amazon EventBridge as events. EventBridge,
formerly Amazon CloudWatch Events, is a serverless event bus service that can deliver a stream
of real-time data from your own applications, software as a service (SaaS)
applications, and AWS services such as Macie. It can route that data to
targets such as AWS Lambda functions, Amazon Simple Notification Service topics, and Amazon Kinesis streams for
additional, automated processing. Use of EventBridge also helps ensure longer-term
retention of findings data. To learn more about EventBridge, see the [Amazon EventBridge
User Guide](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

Macie automatically publishes events to EventBridge for new findings. It also publishes events
automatically for subsequent occurrences of existing policy findings. Because
the findings data is structured as EventBridge events, you can more easily monitor,
analyze, and act upon findings by using other services and tools. For example,
you might use EventBridge to automatically send specific types of new findings to an
AWS Lambda function that, in turn, processes and sends the data to your security
incident and event management (SIEM) system. If you integrate AWS User Notifications with
Macie, you can also use the events to be notified of findings automatically
through delivery channels that you specify. To learn about using EventBridge events to
monitor and process findings, see [Processing findings with
Amazon EventBridge](findings-monitor-events-eventbridge.md "findings-monitor-events-eventbridge.md").

AWS Security Hub

For additional, broader analysis of your organization's security posture, you can also
publish findings to AWS Security Hub. Security Hub is a service that collects security data
from AWS services and supported AWS Partner Network security solutions to provide you
with a comprehensive view of your security state across your AWS environment.
Security Hub also helps you check your environment against security industry standards
and best practices. To learn more about Security Hub, see the [AWS Security Hub User
Guide](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md"). To learn about using Security Hub to evaluate and process findings,
see [Evaluating findings with
AWS Security Hub](securityhub-integration.md "securityhub-integration.md").

In addition to findings, Macie creates sensitive data discovery results for S3 objects that
it analyzes to discover sensitive data. A _sensitive data discovery
result_ is a record that logs details about the analysis of an object. This
includes objects that Macie doesn't find sensitive data in, and therefore don't produce
findings, and objects that Macie can't analyze due to errors or issues. Sensitive data
discovery results provide you with analysis records that can be helpful for data privacy and
protection audits or investigations. You can't access sensitive data discovery results
directly on the Amazon Macie console or with the Amazon Macie API. Instead, you configure Macie to
store the results in an S3 bucket. You can then optionally access and query the results in
that bucket. To learn how to configure Macie to store the results, see [Storing and retaining
sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md").

###### Topics

- [Types of findings](findings-types.md "findings-types.md")
- [Severity scoring for findings](findings-severity.md "findings-severity.md")
- [Working with sample findings](findings-samples.md "findings-samples.md")
- [Reviewing findings](findings-view.md "findings-view.md")
- [Filtering findings](findings-filter-overview.md "findings-filter-overview.md")
- [Investigating sensitive data with
  findings](findings-investigate-sd.md "findings-investigate-sd.md")
- [Suppressing findings](findings-suppression.md "findings-suppression.md")
