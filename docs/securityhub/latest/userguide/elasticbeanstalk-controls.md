# Security Hub CSPM controls for Elastic Beanstalk

These AWS Security Hub CSPM controls evaluate the AWS Elastic Beanstalk service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [ElasticBeanstalk.1] Elastic Beanstalk environments should have enhanced health reporting enabled

**Related requirements:** NIST.800-53.r5 CA-7,NIST.800-53.r5 SI-2

**Category:** Detect > Detection services > Application
monitoring

**Severity:** Low

**Resource type:**
`AWS::ElasticBeanstalk::Environment`

**AWS Config rule:**
[`beanstalk-enhanced-health-reporting-enabled`](../../../config/latest/developerguide/beanstalk-enhanced-health-reporting-enabled.md "../../../config/latest/developerguide/beanstalk-enhanced-health-reporting-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether enhanced health reporting is enabled for your AWS Elastic Beanstalk
environments.

Elastic Beanstalk enhanced health reporting enables a more rapid response to changes in the health of
the underlying infrastructure. These changes could result in a lack of availability of the
application.

Elastic Beanstalk enhanced health reporting provides a status descriptor to gauge the severity of the
identified issues and identify possible causes to investigate. The Elastic Beanstalk health agent, included
in supported Amazon Machine Images (AMIs), evaluates logs and metrics of environment EC2
instances.

For additional information, see [Enhanced health reporting and
monitoring](../../../elasticbeanstalk/latest/dg/health-enhanced.md "../../../elasticbeanstalk/latest/dg/health-enhanced.md") in the _AWS Elastic Beanstalk Developer Guide_.

### Remediation

For instructions on how to enable enhanced health reporting, see [Enabling enhanced health reporting using the Elastic Beanstalk console](../../../elasticbeanstalk/latest/dg/health-enhanced-enable.md#health-enhanced-enable-console "../../../elasticbeanstalk/latest/dg/health-enhanced-enable.md#health-enhanced-enable-console") in the _AWS Elastic Beanstalk Developer Guide_.

## [ElasticBeanstalk.2] Elastic Beanstalk managed platform updates should be enabled

**Related requirements:** NIST.800-53.r5 SI-2,NIST.800-53.r5 SI-2(2),NIST.800-53.r5 SI-2(4),NIST.800-53.r5 SI-2(5), PCI DSS v4.0.1/6.3.3

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** High

**Resource type:**
`AWS::ElasticBeanstalk::Environment`

**AWS Config rule:**
[`elastic-beanstalk-managed-updates-enabled`](../../../config/latest/developerguide/elastic-beanstalk-managed-updates-enabled.md "../../../config/latest/developerguide/elastic-beanstalk-managed-updates-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter     | Description          | Type | Allowed custom values | Security Hub CSPM default value |
| ------------- | -------------------- | ---- | --------------------- | ------------------------------- |
| `UpdateLevel` | Version update level | Enum | `minor`, `patch`      | No default value                |

This control checks whether managed platform updates are enabled for an Elastic Beanstalk
environment. The control fails if no managed platform updates are enabled. By default, the control passes if any
type of platform update is enabled. Optionally, you can provide a custom parameter value to require a specific update level.

Enabling managed platform updates ensures that the latest available platform fixes,
updates, and features for the environment are installed. Keeping up to date with patch
installation is an important step in securing systems.

### Remediation

To enable managed platform updates, see [To configure managed platform updates under Managed platform updates](../../../elasticbeanstalk/latest/dg/environment-platform-update-managed.md "../../../elasticbeanstalk/latest/dg/environment-platform-update-managed.md") in the _AWS Elastic Beanstalk Developer Guide_.

## [ElasticBeanstalk.3] Elastic Beanstalk should stream logs to CloudWatch

**Related requirements:** PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** High

**Resource type:**
`AWS::ElasticBeanstalk::Environment`

**AWS Config rule:**
[`elastic-beanstalk-logs-to-cloudwatch`](../../../config/latest/developerguide/elastic-beanstalk-logs-to-cloudwatch.md "../../../config/latest/developerguide/elastic-beanstalk-logs-to-cloudwatch.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                         | Type | Allowed custom values                                                                                              | Security Hub CSPM default value |
| ----------------- | --------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| `RetentionInDays` | Number of days to keep log events before expiration | Enum | `1`, `3`, `5`, `7`, `14`, `30`,<br>`60`, `90`, `120`, `150`, `180`, `365`<br>, `400`, `545`, `731`, `1827`, `3653` | No default value                |

This control checks whether an Elastic Beanstalk environment is configured to send logs to CloudWatch Logs. The control fails if an
Elastic Beanstalk environment isn't configured to send logs to CloudWatch Logs. Optionally, you can provide a custom value for the
`RetentionInDays` parameter if you want the control to pass only if logs are retained for the specified number of days before expiration.

CloudWatch helps you collect and monitor various metrics for your applications and infrastructure resources. You can also
use CloudWatch to configure alarm actions based on specific metrics. We recommend integrating Elastic Beanstalk with CloudWatch to get
increased visibility into your Elastic Beanstalk environment. Elastic Beanstalk logs include the eb-activity.log, access logs from the
environment nginx or Apache proxy server, and logs that are specific to an environment.

### Remediation

To integrate Elastic Beanstalk with CloudWatch Logs, see [Streaming instance logs to CloudWatch Logs](../../../elasticbeanstalk/latest/dg/AWSHowTo.md#AWSHowTo.cloudwatchlogs.streaming "../../../elasticbeanstalk/latest/dg/AWSHowTo.md#AWSHowTo.cloudwatchlogs.streaming") in the _AWS Elastic Beanstalk Developer Guide_.
