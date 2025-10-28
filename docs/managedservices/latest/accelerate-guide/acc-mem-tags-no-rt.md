# Accelerate tags without Resource Tagger

The tag-based Alarm Manager manages the lifecycle of per-resource CloudWatch alarms; however,
it requires that the managed resources have specific tags defined by AMS Accelerate. AMS Accelerate provides a
default configuration profile that assumes that your tags have been applied by Resource Tagger.

If you want to use an alternate method of applying tags to your resources, such as AWS CloudFormation
or Terraform, and not Resource Tagger, you need to disable the Resource Tagger so that it doesn’t apply tags to your
resources and compete with your chosen tagging method. For instructions on changing your custom Resource Tagger configuration profile
to enable read-only mode, see [Preventing Resource Tagger from modifying resources](acc-rt-using.md#acc-rt-preventing-rt-changes "acc-rt-using.md#acc-rt-preventing-rt-changes").

After the Resource Tagger has been set to read-only mode, and the configuration profile is deployed, use your chosen
tagging method to apply tags to your resources according to the following guidelines:

| Resource type                                     | Tag key                               | Tag value                 |
| ------------------------------------------------- | ------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------- |
| All supported resources (described in this table) | ams:rt:ams-monitoring-policy          | ams-monitored             |
| EC2 instances (Linux)                             | ams:rt:ams-monitoring-policy-platform | ams-monitored-linux       |
| EC2 instances (Windows)                           | ams:rt:ams-monitoring-policy-platform | ams-monitored-windows     |
| OpenSearch Domain with KMS                        | ams:rt:ams-monitoring-with-kms        | ams-monitored-with-kms    |
| OpenSearch Domain with Dedicated Master Node      | ams:rt:ams-monitoring-with-master     | ams-monitored-with-master | Resources that have these tag keys and values are managed by the AMS Accelerate Alarm Manager. |
