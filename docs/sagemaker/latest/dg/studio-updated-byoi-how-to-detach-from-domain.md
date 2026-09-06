

# Detach and clean up custom image resources
<a name="studio-updated-byoi-how-to-detach-from-domain"></a>

The following page provides instructions on how to detach your custom images and clean up the related resources using the Amazon SageMaker AI console or the AWS Command Line Interface (AWS CLI). 

**Important**  
You must first detach your custom image from your domain before deleting the image from the SageMaker AI image store. If not, you may experience errors while viewing your domain information or attaching new custom images to your domain.   
If you are experiencing an error loading a custom image, see [Failure to load custom image](studio-updated-troubleshooting.md#studio-updated-troubleshooting-custom-image). 

## Detach and delete custom images (console)
<a name="studio-updated-byoi-how-to-detach-from-domain-console"></a>

The following provides instructions on how to detach your custom images from SageMaker AI and clean up your custom image resources using the console.

**Detach your custom image from your domain**

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker).

1. Expand the **Admin configurations** section.

1. Under **Admin configurations**, choose **Domains**.

1. From the list of **domains**, select a domain.

1. Open the **Environment** tab.

1. For **Custom images for personal Studio apps**, select the checkboxes for the images you want to detach.

1. Choose **Detach**.

1. Follow the instructions to detach.

**Delete your custom image**

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker).

1. Expand the **Admin configurations** section, if not already done so.

1. Under **Admin configurations**, choose **Images**.

1. From the list of **Images**, select an image you would like to delete.

1. Choose **Delete**.

1. Follow the instructions to delete your image and all its versions from SageMaker AI.

**Delete your custom images and repository from Amazon ECR**
**Important**  
This will also delete any container images and artifacts in this repository.

1. Open the [Amazon ECR console](https://console.aws.amazon.com/ecr).

1. If not already done so, expand the left navigation pane.

1. Under **Private registry**, choose **Repositories**.

1. Select the repositories you wish to delete.

1. Choose **Delete**.

1. Follow the instructions to delete.

## Detach and delete custom images (AWS CLI)
<a name="studio-updated-byoi-how-to-detach-from-domain-cli"></a>

The following section shows an example on how to detach your custom images using the AWS CLI.

1. First set your variables for the AWS CLI commands that follow.

   ```
   ACCOUNT_ID={{account-id}}
   REGION={{aws-region}}
   APP_IMAGE_CONFIG={{app-image-config}}
   SAGEMAKER_IMAGE_NAME={{custom-image-name}}
   ```
   + `{{aws-region}}` is the AWS Region of your Amazon SageMaker AI domain. You can find this at the top right of any AWS console page. 
   + `{{app-image-config}}` is the name of your application image configuration. Use the following AWS CLI command to list the application image configurations in your AWS Region.

     ```
     aws sagemaker list-app-image-configs \
            --region ${REGION}
     ```
   + `{{custom-image-name}}` is the custom image name. Use the following AWS CLI command to list the images in your AWS Region.

     ```
     aws sagemaker list-images \
            --region ${REGION}
     ```

1. To detach the image and image versions from your domain using these instructions, you will need to create or update a domain configuration json file.
**Note**  
If you followed the instructions in [Attach your custom image to your domain](studio-updated-byoi-how-to-attach-to-domain.md), you may have updated your domain using the file named `update-domain.json`.   
If you do not have that file, you can create a new json file instead.

   Create a file named `update-domain.json` that you will use to update your domain.

1. To delete the custom images, you will need to leave `CustomImages` blank, such that `"CustomImages": []`. Choose one of the following to view example configuration files for Code Editor or JupyterLab.

------
#### [ Code Editor: update domain configuration file example ]

   A configuration file example for Code Editor, using [`CodeEditorAppSettings`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CodeEditorAppSettings.html).

   ```
   {
       "DomainId": "{{domain-id}}",
       "DefaultUserSettings": {
           "CodeEditorAppSettings": {
               "CustomImages": [
               ]
           }
       }
   }
   ```

------
#### [ JupyterLab: update domain configuration file example ]

   A configuration file example for JupyterLab, using [`JupyterLabAppSettings`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_JupyterLabAppSettings.html).

   ```
   {
       "DomainId": "{{domain-id}}",
       "DefaultUserSettings": {
           "JupyterLabAppSettings": {
               "CustomImages": [
               ]
           }
       }
   }
   ```

------

   `{{domain-id}}` is the domain ID that your image is attached to. Use the following command to list your domains.

   ```
   aws sagemaker list-domains \
         --region ${REGION}
   ```

1. Save the file.

1. Call the [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html) AWS CLI using the update domain configuration file, `update-domain.json`.
**Note**  
Before you can update the custom images, you must delete all of the **applications** in your domain. You **do not** need to delete user profiles or shared spaces. For instructions on deleting applications, choose one of the following options.  
If you want to use the SageMaker AI console, see [Shut down SageMaker AI resources in your domain](sm-console-domain-resources-shut-down.md).
If you want to use the AWS CLI, use steps 1 through 3 of [Delete an Amazon SageMaker AI domain (AWS CLI)](gs-studio-delete-domain.md#gs-studio-delete-domain-cli).

   ```
   aws sagemaker update-domain \
       --cli-input-json file://update-domain.json \
       --region ${REGION}
   ```

1. Delete the app image config.

   ```
   aws sagemaker delete-app-image-config \
       --app-image-config-name ${APP_IMAGE_CONFIG}
   ```

1. Delete the custom image. This also deletes all of the image versions. This does not delete the Amazon ECR container image and image versions. To do so, use the optional steps below.

   ```
   aws sagemaker delete-image \
       --image-name ${SAGEMAKER_IMAGE_NAME}
   ```

1. (Optional) Delete your Amazon ECR resources. The following list provides AWS CLI commands to obtain your Amazon ECR resource information for the steps below.

   1. Set your variables for the AWS CLI commands that follow.

      ```
      ECR_REPO_NAME={{ecr-repository-name}}
      ```

      `{{ecr-repository-name}}` is the name of your Amazon Elastic Container Registry repository. 

      To list the details of your repositories, use the following command.

      ```
      aws ecr describe-repositories \
              --region ${REGION}
      ```

   1. Delete your repository from Amazon ECR. 
**Important**  
This will also delete any container images and artifacts in this repository.

      ```
      aws ecr delete-repository \
            --repository-name ${ECR_REPO_NAME} \
            --force \
            --region ${REGION}
      ```