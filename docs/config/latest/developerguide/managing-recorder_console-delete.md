# Deleting your configuration

recorders

You must use the AWS CLI to delete the customer managed configuration recorder. You can use
AWS Config console or the AWS CLI to delete a service-linked configuration recorder.

To delete the customer managed configuration recorder (CLI)
Use the [`delete-configuration-recorder`](../../../cli/latest/reference/configservice/delete-configuration-recorder.md "../../../cli/latest/reference/configservice/delete-configuration-recorder.md") command:

```
$ **aws configservice delete-configuration-recorder --configuration-recorder-name `default`**
```

To delete a service-linked configuration recorder (Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Settings** in the navigation pane.
3. On the **Service-linked recorders** tab, choose a
   service-linked configuration recorders on the **Service-linked
   recorders** tab, and then choose **Delete**. When
   prompted, choose **Delete**.

To delete a service-linked configuration recorder (CLI)
Use the [`delete-service-linked-configuration-recorder`](../../../cli/latest/reference/configservice/delete-service-linked-configuration-recorder.md "../../../cli/latest/reference/configservice/delete-service-linked-configuration-recorder.md") command:

This command uses the `--service-principal` field.

```
$ **aws configservice delete-service-linked-configuration-recorder --service-principal "`The service principal of the AWS service for the service-linked configuration recorder that you want to delete`"**
```
