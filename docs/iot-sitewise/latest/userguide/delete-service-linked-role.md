# Delete a service-linked role for

AWS IoT SiteWise

If a feature or service requiring a service-linked role is no longer in use, it's
advisable to delete the associated role. This is to avoid having an inactive entity that isn't
being monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the AWS IoT SiteWise service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try again.

###### To delete AWS IoT SiteWise resources used by the AWSServiceRoleForIoTSiteWise

1. Disable logging for AWS IoT SiteWise. For more information, see [Change your logging level](monitor-cloudwatch-logs.md#change-logging-level "monitor-cloudwatch-logs.md#change-logging-level")
2. Delete any active SiteWise Edge gateways.
   **To manually delete the service-linked role using
   IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForIoTSiteWise service-linked
role. For more information, see [Delete roles or instance profiles](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#delete-service-linked-role "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#delete-service-linked-role") in the _IAM User Guide_.
