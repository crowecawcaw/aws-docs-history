# Attach your custom image to your

domain

This page provides instructions on how to attach your custom image to your domain. Use
the following procedure to use the Amazon SageMaker AI console to navigate to your domain and start
the **Attach image** process.

The following instructions assume that you have pushed an image to a Amazon ECR repository in
the same AWS Region as your domain. If you have not already done so, see [Create a custom image and push to
Amazon ECR](studio-updated-byoi-how-to-prepare-image.md "studio-updated-byoi-how-to-prepare-image.md").

When you choose to attach an image, you will have two options:

- Attach a **New image**: This option will create an image and image
  version in your SageMaker AI image store and then attach it to your domain.

###### Note

If you are continuing the BYOI process, from [Create a custom image and push to
Amazon ECR](studio-updated-byoi-how-to-prepare-image.md "studio-updated-byoi-how-to-prepare-image.md"), use the **New
image** option.

- Attach an **Existing image**: If you have already created your
  intended custom image in the SageMaker AI image store, use this option. This option attaches an
  existing custom image to your domain. To view your custom images in the SageMaker AI image
  store, see [View custom image details
  (console)](studio-updated-byoi-view-images.md#studio-updated-byoi-view-images-console "studio-updated-byoi-view-images.md#studio-updated-byoi-view-images-console").

New image

###### To attach a new image to your domain

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
2. Expand the **Admin configurations** section, if not already
   done so.
3. Under **Admin configurations**, choose
   **Domains**.
4. From the list of **Domains**, select the domain you want to
   attach the image to.

###### Note

If you are attaching the image to a SageMaker Unified Studio project and you need clarification
on which domain to use, see [View the SageMaker AI domain details associated with your project](../../../sagemaker-unified-studio/latest/userguide/view-project-details.md#view-project-details-smai-domain "../../../sagemaker-unified-studio/latest/userguide/view-project-details.md#view-project-details-smai-domain"). 5. Open the **Environment** tab. 6. In the **Custom images for personal Studio apps** section,
choose **Attach image**. 7. For the **Image source**, choose **New
image**. 8. Include your Amazon ECR image URI. The format is as follows.

```
`account-id`.dkr.ecr.`aws-region`.amazonaws.com/`repository-name`:`tag`
```

    1. To obtain your Amazon ECR image URI, navigate to your [Amazon ECR private repositories](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories")
     page.
    2. Choose your repository name link.
    3. Choose the **Copy URI** icon that corresponds to your image
     version (**Image tag**).

9. Follow the rest of the instructions to attach your custom image.

###### Note

Ensure that you are using the application type consistent with your
`Dockerfile`. For more information, see [Dockerfile samples](studio-updated-byoi-specs.md#studio-updated-byoi-specs-dockerfile-templates "studio-updated-byoi-specs.md#studio-updated-byoi-specs-dockerfile-templates").

Once the image has been successfully attached to your domain, you will be able
to view it in the **Environment** tab.

Existing image

###### To attach an existing image to your domain

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
2. Expand the **Admin configurations** section, if not already
   done so.
3. Under **Admin configurations**, choose
   **Domains**.
4. From the list of **Domains**, select the domain you want to
   attach the image to.

###### Note

If you are attaching the image to a SageMaker Unified Studio project and you need clarification
on which domain to use, see [View the SageMaker AI domain details associated with your project](../../../sagemaker-unified-studio/latest/userguide/view-project-details.md#view-project-details-smai-domain "../../../sagemaker-unified-studio/latest/userguide/view-project-details.md#view-project-details-smai-domain"). 5. Open the **Environment** tab. 6. In the **Custom images for personal Studio apps** section,
choose **Attach image**. 7. For the **Image source**, choose **Existing
image**. 8. Choose an existing image and image version from the SageMaker AI image store.

If you are unable to view your image version, you may need to create an image
version. For more information, see [View custom image details
(console)](studio-updated-byoi-view-images.md#studio-updated-byoi-view-images-console "studio-updated-byoi-view-images.md#studio-updated-byoi-view-images-console"). 9. Follow the rest of the instructions to attach your custom image.

###### Note

Ensure that you are using the application type consistent with your
`Dockerfile`. For more information, see [Dockerfile samples](studio-updated-byoi-specs.md#studio-updated-byoi-specs-dockerfile-templates "studio-updated-byoi-specs.md#studio-updated-byoi-specs-dockerfile-templates").

Once the image has been successfully attached to your domain, you will be able
to view it in the **Environment** tab.

Once your image has been successfully attached to your domain, the domain users
can choose the image for their application. For more information, see [Launch a custom image in
Studio](studio-updated-byoi-how-to-launch.md "studio-updated-byoi-how-to-launch.md").

###### Note

If you have attached a custom image to your SageMaker Unified Studio project, you will need to launch
the application from within SageMaker Unified Studio. For more information, see [Launch
your custom image](../../../sagemaker-unified-studio/latest/userguide/byoi-launch-custom-image.md "../../../sagemaker-unified-studio/latest/userguide/byoi-launch-custom-image.md") in the _Amazon SageMaker Unified Studio User Guide_.
