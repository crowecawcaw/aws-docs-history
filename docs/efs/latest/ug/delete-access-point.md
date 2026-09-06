

# Deleting access points
<a name="delete-access-point"></a>

When you delete an access point, any clients that are using the access point lose access to the Amazon EFS file system that it's configured for.

## Using the console
<a name="delete-ap-console"></a>

1. Open the Amazon Elastic File System console at [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).

1. In the left navigation pane, choose **Access points** to open the **Access points** page.

1. Select the access point to delete.

1. Choose **Delete**.

1. Choose **Confirm** to confirm the action and delete the access point.

## Using the AWS CLI
<a name="delete-ap-cli"></a>

In the following example, the `delete-access-point` CLI command deletes the specified access point. The equivalent API command is [DeleteAccessPoint](https://docs.aws.amazon.com/efs/latest/APIReference/API_DeleteAccessPoint.html). If the command is successful, the service returns an HTTP 204 response with an empty HTTP body.

```
aws efs delete-access-point --access-point-id fsap-092e9f80b3fb5e6f3 --client-token 010102020-3
```