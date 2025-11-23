# How Amazon EC2 High Availability for SQL Server works

Upon registration, Amazon EC2 High Availability for SQL Server (SQL HA) automatically monitors your Amazon EC2 instances running
Windows SQL Server License Included AMIs and classifies them as either active or standby based on
their current role in your SQL Server deployment. For High Availability configurations containing an
active SQL Server instance, one standby failover instance in the same cluster may receive a SQL Server
licensing fee waiver, meaning you pay only the Windows Server licensing fee. You can monitor
your current SQL HA status through the Amazon EC2 console, which displays the latest records of
which instances are receiving license savings and historical status changes.

SQL HA continuously monitors your enabled SQL Server instances to determine their active
or standby status. Using AWS Systems Manager (SSM) commands, it collects metadata from your SQL Server
installations and applies classification logic to identify which instances are actively
serving traffic and which are functioning as standby failover nodes.

Standby instances are billed as Windows instances rather than Windows SQL Server instances,
providing license cost savings. Billing changes take effect when an SQL HA standby
detection enabled instance is classified as standby and eligible for the benefit, with
no manual intervention required. This classification adapts to changes in your environment,
such as failover events where a standby instance becomes active. The system detects these
transitions and updates billing accordingly.
