# How to manage Amazon EMR Service Quotas

Service Quotas is an AWS feature that you can use to view and manage your Amazon EMR service
quotas or limits from a central location, using the AWS Management Console, the API
or the AWS CLI. To learn more about viewing quotas and requesting increases, see [AWS service
quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the _Amazon Web Services General Reference_.

###### Important

Service quotas can be enforced independent of each other and at times their effects can overlap. Some are scoped to specific APIs, and other quotas enforce
limits at the account level. Specifically, the following quotas are applied at the account level:

- _The maximum rate at which your bucket replenishes for all EMR operations_
- _The maximum number of API requests that you can make per second_
  Note that if you successfully request a specific quota increase and you continue to see throttling, for example for API
  requests, it's possible that one of these account-level quotas are continuing to limit API call rates. For
  troubleshooting, you can use the Service quotas console, which is available at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"), to check quota limits and request increases. If you
  make requests for increases and continue to see throttling, contact support. You can also find default limits and descriptions
  for EMR [Service quotas](../../../general/latest/gr/emr.md#limits_emr "../../../general/latest/gr/emr.md#limits_emr")
  in the **AWS General Reference** _Reference guide_.

For some APIs, setting up a CloudWatch event might be a better option than increasing
service quotas. You can also save time by using CloudWatch to set alarms and trigger
increase requests proactively, before you reach the service quota. For more details,
see [When to set up EMR events in CloudWatch](emr-service-limits-cloudwatch-events.md "emr-service-limits-cloudwatch-events.md").
