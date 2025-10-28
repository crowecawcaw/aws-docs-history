# Deleting access points

When you delete an access point, any clients that are using the access point lose access
to the Amazon EFS file system that it's configured for.

1. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. In the left navigation pane, choose **Access points** to open the
   **Access points** page.
3. Select the access point to delete.
4. Choose **Delete**.
5. Choose **Confirm** to confirm the action and delete the access point.
   In the following example, the `delete-access-point` CLI command deletes the
   specified access point. The equivalent API command is [DeleteAccessPoint](API_DeleteAccessPoint.md "API_DeleteAccessPoint.md"). If the command is successful,
   the service returns an HTTP 204 response with an empty HTTP body.

```
aws efs delete-access-point --access-point-id fsap-092e9f80b3fb5e6f3 --client-token 010102020-3
```
