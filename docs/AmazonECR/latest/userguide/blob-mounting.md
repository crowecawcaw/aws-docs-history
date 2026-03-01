# Blob mounting in Amazon ECR

Amazon ECR supports a capability called blob mounting to share common image layers across repositories within a registry.
When enabled, repositories within a single registry can reference layers from other repositories within the same registry
instead of storing duplicate copies.

When registry blob mounting is enabled, Amazon ECR checks for existing layers in your registry during push operations when mounting parameters are included.
If a layer already exists in another repository within the same registry, Amazon ECR will mount the existing
layer instead of uploading a duplicate.

###### Note

OCI clients automatically include mounting parameters if they detect a blob may already exist in a different repository. Amazon ECR attempts mounting only when these parameters are present in the client's POST request.

## Blob mounting concepts

- Blob mounting only works within the same registry (same account and region).
- Repositories must use identical encryption type and keys.
- Blob mounting is not supported for images created via pull through cache.
- If you decide to disable blob mounting, existing images that were pushed with blob
  mounting configured will continue to work and layers will remain mounted.

## Blob mounting configuration

You can use the AWS Management Console or AWS CLI to configure blob mounting for your registry.

###### Note

Users need `ecr:GetDownloadUrlForLayer` IAM permission on a repository to mount layers from it.

AWS Management Console
Use the following steps to update your registry's blob mounting configuration
using the AWS Management Console.

###### Turn on the blob mounting configuration for your private registry

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/private-registry/repositories](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories")
2. From the navigation bar, choose the Region.
3. In the navigation pane, choose **Private
   registry**, **Feature &
   Settings**, and then choose **Blob mounting**.
4. On the **Blob mounting** page, choose **Enable**.

A banner displays indicating that the blob mounting configuration
has been updated to be enabled.

AWS CLI
Use the following command to update your registry's blob mounting configuration using the AWS CLI.

- ```
  `aws ecr put-account-setting --name BLOB_MOUNTING --value ENABLED`
  ```

```

```
