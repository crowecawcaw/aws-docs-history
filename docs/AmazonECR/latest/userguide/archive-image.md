# Archiving an image

You can archive images manually using the Amazon ECR console or AWS CLI, or automatically
using lifecycle policies. When an image is archived:

- The image is moved to the archival storage class.
- Archived images cannot be pulled. Requests to pull the archived image will fail with a 404 error.
- While the image cannot be pulled, it can still be described using the **describe-images** command, or listed using the **list-images**
  command. The image status will be shown as `ARCHIVED`.
- Archived images have a minimum storage duration of 90 days. You cannot configure lifecycle policies that delete images that have been in archive for less than 90 days. If you must delete images that have been archived for less than 90 days, you need to use the **batch-delete-image** API, but you will be charged for the 90-day minimum storage duration.
- The image appears in an **Archived images** tab in the
  repository view (this tab will appear only if at least one image is archived in the repository).
- The image can be restored as an active image by manually selecting it to
  be restored or by re-pushing the image to the repository.
- The image will be deleted if the repository has lifecycle policies that
  delete the image with criteria such as time in archive.

AWS Management Console

###### To archive an image

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the Region that contains the repository
   with the image you want to archive.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, choose the repository
   containing the image you want to archive.
5. Select the image you want to archive. You will see Image Details.
6. To archive the image, select the **Archive** button and
   select **Confirm** when you are prompted.
7. If this is the first archived image in the repository, a new **Archived
   images** tab appears with the newly archived image. If there are
   other archived images, this image will be added to that tab.

AWS CLI

###### To archive an image

- Use the **update-image-storage-class** command to archive an
  image by updating its storage class to `ARCHIVE`:

```
`aws ecr update-image-storage-class \
 --repository-name `my-repository` \
 --image-id imageDigest=`sha256:4f70ef7a4d29e8c0c302b13e25962d8f7a0bd304EXAMPLE` \
 --target-storage-class ARCHIVE`
```

###### To archive an image using lifecycle policies

- You can configure archive rules for your repositories using lifecycle policies
  to automatically archive images. Lifecycle policies allow you to automatically archive
  images based on criteria such as:

      + Time since the image was pushed
      + Time since the image was last pulled
      + Maximum number of images to keep active

  You can also configure lifecycle policies to permanently delete images after
  they've been archived for a specified period. For more information and examples of
  lifecycle policies with archive actions, see [Automate the cleanup of images by using lifecycle
  policies in Amazon ECR](LifecyclePolicies.md "LifecyclePolicies.md").

###### Note

Archived images have a minimum storage duration of 90 days. You cannot configure lifecycle policies that delete images that have been in archive for less than 90 days. If you must delete images that have been archived for less than 90 days, you need to use the **batch-delete-image** API, but you will be charged for the 90-day minimum storage duration.
When you describe images using the **describe-images** command,
archived images have an `image-status` of `ARCHIVED`. You can filter
images by `image-status` to view only archived images or only active images.
