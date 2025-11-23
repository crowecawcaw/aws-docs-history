# Restoring an image

When you restore an archived image, it is moved from the ECR Archive storage class
back to the ECR Standard storage class. Restored images are charged at the standard storage rates.
The restore process performs similar actions that occur when a new image is created:

- The image becomes available for pulling when the restore is complete.
  Restore typically takes up to 20 minutes, though it may complete faster.
- If scan on push is enabled for the repository, the restored image will be
  scanned. Note that previous scan results from before the image was archived
  will not be available.
- If replication is configured for the repository, the restored image will
  be replicated if replication was enabled at the time of restore.
- The restored image appears in the active images list.
  Restoring an image typically takes up to 20 minutes, though it may complete
  faster. During the restore process, the image remains in the archived state and
  cannot be pulled until the restore completes.

AWS Management Console

###### To restore an archived image

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the Region that contains the repository
   with the archived image you want to restore.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, choose the repository
   containing the archived image.
5. Choose the **Archived images** tab.
6. Select the archived image you want to restore.
7. Choose **Restore** and confirm the restore action.
8. Wait for the restore to complete. The image will appear in the active
   images list once restoration is complete.

AWS CLI

###### To restore an archived image

- Use the **update-image-storage-class** command to restore an
  archived image by updating its storage class to `STANDARD`:

```
`aws ecr update-image-storage-class \
 --repository-name `my-repository` \
 --image-id imageDigest=`sha256:4f70ef7a4d29e8c0c302b13e25962d8f7a0bd304EXAMPLE` \
 --target-storage-class STANDARD`
```

When you describe images using the **describe-images** command,
images that are being restored have an `image-status` of `ACTIVATING`.
You can filter images by `image-status` with the value `ACTIVATING`
to view images that are currently being restored.

An alternative method to restore an archived image is to re-push the image to the
repository. When you push an image that is currently archived, that image will be
immediately restored and removed from the archive.
