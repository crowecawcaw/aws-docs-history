# Integrating AWS Security Hub in Jira Service Management Cloud

AWS Security Hub enables users to view security Findings from AWS services such as Amazon
Guard Duty and Amazon Inspector, as well as AWS Partner solutions.

If you use both [AWS Security Hub](https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc "https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc") and [Jira Service Management](https://www.atlassian.com/software/jira/service-management "https://www.atlassian.com/software/jira/service-management"), the AWS Service Management Connector for
Jira Service Management allows you to create an automated, bidirectional integration between Security Hub
and Jira Service Management. This two-way integration synchronizes your Security Hub Findings and
Jira Issues.

Specifically, as a Jira administrator, you can use this integration to automatically
create Jira Issues from AWS Security Hub Findings. When you update those tickets in Jira, the changes are
automatically replicated back to the original Security Hub Findings. For example, when you resolve the issue in
Jira, the workflow status of the Security Hub finding also changes to `RESOLVED`.
This action ensures that Security Hub always has up-to-date information about your security posture.

###### Note

If you are aggregating your Security Hub findings to a single management AWS account and have onboarded management to the connector,
internal customers and Jira agents updates on the Finding issue will **not** be synched to the finding in
Security Hub.
