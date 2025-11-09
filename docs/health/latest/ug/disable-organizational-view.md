# Disabling organizational view

If you don't want to aggregate events for your organization, you can turn off this feature
from the management account or you can disable organizational view by using the [DisableHealthServiceAccessForOrganization](../APIReference/API_DisableHealthServiceAccessForOrganization.md "../APIReference/API_DisableHealthServiceAccessForOrganization.md") API operation.

Disabling organizational view events (Console)
AWS Health stops aggregating events for all other accounts in your
organization. You can continue to view previous events from your organization
until they're deleted.

###### To disable organizational view

1. Open your AWS Health Dashboard at [https://health.aws.com/health/home](https://health.aws.com/health/ "https://health.aws.com/health/").
2. In the navigation pane, under **Your organization
   health**, choose
   **Configurations**.
3. On the **Enable organizational view** page, choose
   **Disable organizational view**.

After you turn off this feature, AWS Health no longer aggregates events from
your organization. However, the service-linked role remains in the
management account until you delete it through the AWS Identity and Access Management (IAM) console,
IAM API, or AWS Command Line Interface (AWS CLI). For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

Disabling organizational view events (CLI)
The following AWS CLI command disables this feature from your
account.

```
aws health disable-health-service-access-for-organization --region us-east-1
```

###### Note

You can also disable the organizational feature by using the Organizations [DisableAWSServiceAccess](../../../organizations/latest/APIReference/API_DisableAWSServiceAccess.md "../../../organizations/latest/APIReference/API_DisableAWSServiceAccess.md") API operation. After you call this
operation, AWS Health stops aggregating events for all other accounts in
your organization. If you call the AWS Health API operations for
organizational view, AWS Health returns an error. AWS Health continues to
aggregate health events for your AWS account.

After you disable this feature, AWS Health no longer aggregates events from
your organization. However, the service-linked role remains in the
management account until you delete it through the AWS Identity and Access Management (IAM) console,
IAM API, or AWS CLI. For more information, see [Deleting a service-linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.
