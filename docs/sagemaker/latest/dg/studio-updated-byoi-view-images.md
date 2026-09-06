

# View your custom image details
<a name="studio-updated-byoi-view-images"></a>

The following page provides instructions on how to view your custom image details in the SageMaker AI image store.

## View custom image details (console)
<a name="studio-updated-byoi-view-images-console"></a>

The following provides instructions on how to view your custom images using the SageMaker AI console. In this section, you can view and edit your image details.

**View your custom images (console)**

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker).

1. Expand the **Admin configurations** section.

1. Under **Admin configurations**, choose **Images**.

1. From the list of **Custom images**, select the hyperlink of your image name.

## View custom image details (AWS CLI)
<a name="studio-updated-byoi-view-images-cli"></a>

The following section shows an example on how to view your custom images using the AWS CLI.

```
aws sagemaker list-images \
       --region {{aws-region}}
```