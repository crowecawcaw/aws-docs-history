# View your custom image details

The following page provides instructions on how to view your custom image details in the
SageMaker AI image store.

The following provides instructions on how to view your custom images using the
SageMaker AI console. In this section, you can view and edit your image details.

###### View your custom images (console)

1. Open the [SageMaker AI
   console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
2. Expand the **Admin configurations** section.
3. Under **Admin configurations**, choose
   **Images**.
4. From the list of **Custom images**, select the hyperlink
   of your image name.
   The following section shows an example on how to view your custom images using the
   AWS CLI.

```
aws sagemaker list-images \
       --region `aws-region`
```
