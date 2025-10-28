# Deleting a service-linked role for WorkSpaces Secure Browser

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the WorkSpaces Secure Browser service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete WorkSpaces Secure Browser resources used by the AWSServiceRoleForAmazonWorkSpacesWeb

- Choose from one of the following options:

      + If you use the console, delete all of your portals on the console.
      + If you use the CLI or API, disassociate all of your resources (including browser
       settings, network settings, user settings,
       trust
       stores, and user
       access logging settings) from your portals, delete these resources,
       and then delete the portals.

  **To manually delete the service-linked role using
  IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonWorkSpacesWeb
service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
