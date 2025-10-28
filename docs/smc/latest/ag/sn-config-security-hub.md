# AWS Security Hub in ServiceNow

AWS Security Hub enables users to view security Findings from AWS services such as Amazon
Guard Duty and Amazon Inspector, as well as AWS Partner solutions.

If you use both [AWS Security Hub](https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc "https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc") and ServiceNow ITSM, the AWS Service Management Connector for
ServiceNow allows you to create an automated, bidirectional integration between Security Hub
and ServiceNow ITSM. This two-way integration synchronizes your Security Hub findings and
ServiceNow tickets.

Specifically, as a ServiceNow administrator, you can use this integration to automatically
create ServiceNow incident or problem tickets from AWS Security Hub findings. When you
update those tickets in ServiceNow, the changes are automatically replicated back to the
original Security Hub findings. For example, when you resolve the ticket in ServiceNow, the
workflow status of the Security Hub finding also changes to `RESOLVED`. This action ensures that
Security Hub always has up-to-date information about your security posture.

View the following video, _AWS Security Hub -
Bidirectional integration with ServiceNow ITSM_, for an overview of the
AWS Security Hub integration to the Connector for ServiceNow.
