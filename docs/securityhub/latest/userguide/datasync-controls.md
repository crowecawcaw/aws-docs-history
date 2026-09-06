

# Security Hub CSPM controls for AWS DataSync
<a name="datasync-controls"></a>

These Security Hub CSPM controls evaluate the AWS DataSync service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [DataSync.1] DataSync tasks should have logging enabled
<a name="datasync-1"></a>

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::DataSync::Task`

**AWS Config rule:** [datasync-task-logging-enabled](https://docs.aws.amazon.com/config/latest/developerguide/datasync-task-logging-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS DataSync task has logging enabled. The control fails if the task doesn't have logging enabled.

Audit logs track and monitor system activities. They provide a record of events that can help you detect security breaches, investigate incidents, and comply with regulations. Audit logs also enhance the overall accountability and transparency of your organization.

### Remediation
<a name="datasync-1-remediation"></a>

For information about configuring logging for AWS DataSync tasks, see [Monitoring data transfers with Amazon CloudWatch Logs](https://docs.aws.amazon.com/datasync/latest/userguide/configure-logging.html) in the *AWS DataSync User Guide*.

## [DataSync.2] DataSync tasks should be tagged
<a name="datasync-2"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::DataSync::Task`

**AWS Config rule:** [datasync-task-tagged](https://docs.aws.amazon.com/config/latest/developerguide/datasync-task-tagged.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| requiredKeyTags | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions). | No default value | 

This control checks whether an AWS DataSync task has the tag keys specified by the `requiredKeyTags` parameter. The control fails if the task doesn't have any tag keys, or it doesn't have all the keys specified by the `requiredKeyTags` parameter. If you don't specify any values for the `requiredKeyTags` parameter, the control checks only for the existence of a tag key and fails if the task doesn't have any tag keys. The control ignores system tags, which are applied automatically and have the `aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of a required tag key and an optional tag value. You can use tags to categorize resources by purpose, owner, environment, or other criteria. They can help you identify, organize, search for, and filter resources. They can also help you track resource owners for actions and notifications. You can also use tags to implement attribute-based access control (ABAC) as an authorization strategy. For more information about ABAC strategies, see [Define permissions based on attributes with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. For more information about tags, see the [Tagging AWS Resources and Tag Editor User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

**Note**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation
<a name="datasync-2-remediation"></a>

For information about adding tags to an AWS DataSync task, see [Tagging your AWS DataSync tasks](https://docs.aws.amazon.com/datasync/latest/userguide/tagging-tasks.html) in the *AWS DataSync User Guide*.