# Alarms and tagging

_Tags_ are key-value pairs that can help you organize and categorize
your resources. You can also use them to scope user permissions by granting a user permission
to access or change only resources with certain tag values. For more general information about
tagging resources, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md")

The following list explains some details about how tagging works with CloudWatch alarms.

- To be able to set or update tags for a CloudWatch resource, you must be signed on to an
  account that has the `cloudwatch:TagResource` permission. For example, to
  create an alarm and set tags for it, you must have the `cloudwatch:TagResource`
  permission in addition to the `the cloudwatch:PutMetricAlarm` permission. We
  recommend that you make sure anyone in your organization who will create or update CloudWatch
  resources has the `cloudwatch:TagResource` permission.
- Tags can be used for tag-based authorization control. For example, IAM user or role
  permissions can include conditions to limit CloudWatch calls to specific resources based on
  their tags. However, keep in mind the following
  - Tags with names that start with `aws:` can't be used for tag-based
    authorization control.
  - Composite alarms do not support tag-based authorization control.
