# Deleting a service-linked role for MediaTailor

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the MediaTailor service is using the role when you try to clean up the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To clean up MediaTailor resources used by the AWSServiceRoleForMediaTailor

- Before you can delete the service-linked role created by MediaTailor for the log
  configuration, you must first _deactivate_ all of the log
  configurations in your account. To deactivate a log configuration, set the
  **percent enabled** value to **0**. This turns off all
  session logging the corresponding playback configuration. For more information, see [Deactivating a log
  configuration](log-configuration.md#deactivating-logging-configuration "log-configuration.md#deactivating-logging-configuration").
  **To manually delete the service-linked role using
  IAM**

Use the IAM console, the AWS Command Line Interface (AWS CLI), or the AWS API to delete the AWSServiceRoleForMediaTailor
service-linked role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
