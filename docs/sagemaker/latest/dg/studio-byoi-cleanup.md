# Clean Up Resources for Custom Images in Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

The following sections show how to clean up the resources you created in the previous
sections from the SageMaker AI console or AWS CLI. You perform the following steps to clean up the resources:

- Detach the image and image versions from your domain.
- Delete the image, image version, and app image config.
- Delete the container image and repository from Amazon ECR. For more information, see
  [Deleting a repository](../../../AmazonECR/latest/userguide/repository-delete.md "../../../AmazonECR/latest/userguide/repository-delete.md").

## Clean up resources from the SageMaker AI console

The following section shows how to clean up resources from the SageMaker AI console.

When you detach an image from a domain, all versions of the image are detached. When an
image is detached, all users of the domain lose access to the image versions. A running
notebook that has a kernel session on an image version when the version is detached,
continues to run. When the notebook is stopped or the kernel is shut down, the image version
becomes unavailable.

###### To detach an image

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **Images**.
4. Under **Custom SageMaker Studio Classic images attached to domain**, choose
   the image and then choose **Detach**.
5. (Optional) To delete the image and all versions from SageMaker AI, select
   **Also delete the selected images ...**. This does not delete the
   associated container images from Amazon ECR.
6. Choose **Detach**.

## Clean up resources from the AWS CLI

The following section shows how to clean up resources from the AWS CLI.

###### To clean up resources

1. Detach the image and image versions from your domain by passing an empty custom image
   list to the domain. Open the `default-user-settings.json` file you
   created in [Attach the SageMaker image to your
   current domain](studio-byoi-attach.md#studio-byoi-sdk-attach-current-domain "studio-byoi-attach.md#studio-byoi-sdk-attach-current-domain"). To detach the image and
   image version from a shared space, open the
   `default-space-settings.json` file.
2. Delete the custom images and then save the file.

```
"DefaultUserSettings": {
  "KernelGatewayAppSettings": {
     "CustomImages": [
     ],
     ...
  },
  ...
}
```

3. Use the domain ID and default user settings file to update your domain. To update your
   shared space, use the default space settings file.

```
aws sagemaker update-domain \
    --domain-id `<d-xxxxxxxxxxxx>` \
    --cli-input-json file://default-user-settings.json
```

The response should look similar to the following.

```
{
    "DomainArn": "arn:aws:sagemaker:us-east-2:acct-id:domain/d-xxxxxxxxxxxx"
}
```

4. Delete the app image config.

```
aws sagemaker delete-app-image-config \
    --app-image-config-name custom-image-config
```

5. Delete the SageMaker image, which also deletes all image versions. The container images
   in ECR that are represented by the image versions are not deleted.

```
aws sagemaker delete-image \
    --image-name custom-image
```
