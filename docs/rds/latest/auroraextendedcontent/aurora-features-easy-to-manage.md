

# Easy to manage
<a name="aurora-features-easy-to-manage"></a>

**Topics**
+ [Quick create and connect](#aurora-features-quick-create)
+ [Monitoring and metrics](#aurora-features-monitoring)
+ [Amazon RDS blue/green deployments](#aurora-features-blue-green)
+ [Automatic software patching](#aurora-features-patching)
+ [Upgrade rollout policies](#aurora-features-upgrade-rollout)
+ [Event notifications](#aurora-features-event-notifications)
+ [Database cloning](#aurora-features-cloning)
+ [Stop and start](#aurora-features-stop-start)

## Quick create and connect
<a name="aurora-features-quick-create"></a>

You can [create and connect](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.html) to an Aurora PostgreSQL database in seconds with two clicks. Pre-configured with an Aurora serverless cluster, you can get started without worrying about database configuration. You also get a new internet gateway that fully supports the Postgres wire protocol, enabling secure connections from your favorite tools and IDEs outside of AWS infrastructure — no VPN or AWS Direct Connect required.

## Monitoring and metrics
<a name="aurora-features-monitoring"></a>

Aurora provides multiple options for monitoring and optimizing database performance. [CloudWatch metrics for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) tracks key operational metrics such as compute, memory, storage, query throughput, cache hit ratio, and active connections. You can set [CloudWatch alarms](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/creating_alarms.html) for specific metrics over a specified time period, and perform actions based on customizable thresholds.

[CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) consolidates logs and metrics from your applications, your databases, and the operating systems on which they run into a unified view in the console. Using its pre-built dashboards, recommended alarms, and automated telemetry collection, you can monitor the health of your database fleets and use a guided troubleshooting experience to drill down to individual instances for root-cause analysis. Application developers can correlate application performance with database performance by drilling down from the context of their application performance view in [CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) to the specific dependent database in CloudWatch Database Insights. CloudWatch Database Insights inherits all the features of [RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/) along with additional features such as fleet-level monitoring, integration with application performance monitoring and correlation of database metrics with logs and events.

[Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring.OS.html) provides metrics in real time from the operating system instance running your database. You can view [all the system metrics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring-Available-OS-Metrics.html) and process information for your Aurora database instances on the console. Aurora delivers the metrics from Enhanced Monitoring to your CloudWatch Logs account. You can create metrics filters in CloudWatch from CloudWatch Logs and display the graphs on the CloudWatch dashboard.

Additionally, [DevOps Guru for RDS](https://aws.amazon.com/devops-guru/features/devops-guru-for-rds/), powered by machine learning, automatically identifies, diagnoses, and provides recommendations for database issues, including resource overuse and SQL query problems, all without requiring ML or deep database expertise. You can simply enable DevOps Guru for RDS in the RDS Console Management, Performance Insights, or DevOps Guru Console for comprehensive database monitoring.

## Amazon RDS blue/green deployments
<a name="aurora-features-blue-green"></a>

[RDS blue/green deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) let you make safer, simpler, and faster database updates with zero data loss. In a few steps, blue/green deployments create a staging environment that mirrors production and keeps the two environments in sync using logical replication. You can make changes – such as major/minor version upgrades, schema modifications, and parameter changes — without impacting your production workload. When promoting your staging environment, blue/green deployments blocks write to both the blue and green environments until switchover is complete. Blue/green deployments use built-in switchover guardrails that time out promotion if it exceeds your maximum tolerable downtime, detects replication errors, checks instance health, and more.

## Automatic software patching
<a name="aurora-features-patching"></a>

Aurora keeps your database up to date with the latest patches automatically. You control if and when your instance is patched through DB Engine Version Management. Aurora uses zero-downtime patching when possible: if a suitable time window appears, the instance is updated in place, application sessions are preserved and the database engine restarts while the patch is in progress, leading to only a transient (approximately five seconds) drop in throughput.

## Upgrade rollout policies
<a name="aurora-features-upgrade-rollout"></a>

AWS Organizations upgrade rollout policies let you centrally manage and stagger automatic minor version upgrades across multiple AWS accounts. You can upgrade your Aurora databases in a specified order (e.g., development before production), define upgrade sequences using account-level policies or resource tags, provide time between upgrade phases to validate changes, and monitor upgrade health notifications for each phase. To use upgrade rollout policies your AWS account must be part of an organization in AWS Organizations with upgrade rollout policy enabled. Additional information is available in [managing organization policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html) documentation.

## Event notifications
<a name="aurora-features-event-notifications"></a>

Aurora notifies you by email or SMS of important database events such as automated failovers. You can subscribe to over 40 different DB events using the [RDS Management Console](https://console.aws.amazon.com/rds/home), RDS API, or AWS CLI.

## Database cloning
<a name="aurora-features-cloning"></a>

Aurora supports quick, efficient cloning operations, where entire multi-terabyte database clusters can be cloned in minutes. Cloning is useful for a number of purposes including application development, testing, database updates, and running analytical queries. Immediate availability of data can significantly accelerate your software development and upgrade projects and make analytics more accurate. You can clone an Aurora database in only a few steps, and you don't incur any storage charges, except if you use additional space to store data changes.

## Stop and start
<a name="aurora-features-stop-start"></a>

You save costs by stopping your Aurora database when it is not in use, e.g., during development and test cycles. Stopping your database does not delete your data, and you can restart in a few steps. Additional information is available in the [start/stop](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-cluster-stop-start.html) documentation.