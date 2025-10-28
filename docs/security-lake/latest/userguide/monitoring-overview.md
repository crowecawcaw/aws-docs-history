# Monitoring Amazon Security Lake

Security Lake integrates with AWS CloudTrail, which is a service that provides a record of actions
that were taken in Security Lake by a user, a role, or another AWS service. This includes
actions from the Security Lake console and programmatic calls to Security Lake API operations. By
using the information collected by CloudTrail, you can determine which requests were made to
Security Lake. For each request, you can identify when it was made, the IP address from which it
was made, who made it, and additional details. For more information, see [Logging Security Lake API calls using CloudTrail](securitylake-cloudtrail.md "securitylake-cloudtrail.md").

Security Lake and Amazon CloudWatch are integrated, so you can collect, view, and analyze metrics for
logs that Security Lake collects. CloudWatch metrics for your Security Lake data lake
are automatically collected and pushed to CloudWatch at one-minute intervals. You can also set an alarm to
send you a notification if a
specified threshold is met for a Security Lake metric. For a list of all the metrics that Security Lake
sends to CloudWatch, see [Security Lake metrics and dimensions](cloudwatch-metrics.md#available-securitylake-metrics "cloudwatch-metrics.md#available-securitylake-metrics").
