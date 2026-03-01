# Deleting an image in Amazon ECR

If you're finished using an image, you can delete it from your repository. If you're
finished with a repository, you can delete the entire repository and all of the images
within it. For more information, see [Deleting a private repository in Amazon ECR](repository-delete.md "repository-delete.md").

As an alternative to deleting images manually, you can create repository lifecycle
policies which provide more control over the lifecycle management of images in your
repositories. Lifecycle policies automate this process for you. For more information,
see [Automate the cleanup of images by using lifecycle policies in Amazon ECR](LifecyclePolicies.md "LifecyclePolicies.md").

###### Note

If your repository has a mix of images, some of which were pushed before Amazon ECR
supported OCI v1.1, some signatures will have image indexes or manifest lists
pointing to them. As a result, when you delete a pre-OCI v1.1 image, you might need
to manually delete the manifest list that references the image in order to delete
the artifact.

###### To delete an image (AWS Management Console)

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the Region that contains the image to
   delete.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, choose the repository that
   contains the image to delete.
5. On the **Repositories: `repository_name`**
   page, select the box to the left of the image to delete and choose **Delete**.
6. In the **Delete image(s)** dialog box, verify that the
   selected images should be deleted and choose **Delete**.

###### To delete an image (AWS CLI)

1. List the images in your repository. Tagged images will have both an image
   digest as well as a list of associated tags. Untagged images will only have an
   image digest.

```
`aws ecr list-images \
 --repository-name `my-repo``
```

2. (Optional) Delete any unwanted tags for the image by specifying the tag
   associated with the image you want to delete. When the last tag is deleted from
   an image, the image is also deleted.

```
`aws ecr batch-delete-image \
 --repository-name `my-repo` \
 --image-ids imageTag=`tag1` imageTag=`tag2``
```

3. Delete a tagged or untagged image by specifying the image digest. When you
   delete an image by referencing its digest, the image and all of its tags are
   deleted.

```
`aws ecr batch-delete-image \
 --repository-name `my-repo` \
 --image-ids imageDigest=`sha256:4f70ef7a4d29e8c0c302b13e25962d8f7a0bd304EXAMPLE``
```

To delete multiple images, you can specify multiple image tags or image
digests in the request.

```
`aws ecr batch-delete-image \
 --repository-name `my-repo` \
 --image-ids imageDigest=`sha256:4f70ef7a4d29e8c0c302b13e25962d8f7a0bd304EXAMPLE` imageDigest=`sha256:f5t0e245ssffc302b13e25962d8f7a0bd304EXAMPLE``
```
