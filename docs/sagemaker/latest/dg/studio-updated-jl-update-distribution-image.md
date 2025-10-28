# Update the SageMaker

Distribution Image

###### Important

This topic assumes that you've created a space and given the user access to it.
For more information, see [Give your users access to
spaces](studio-updated-jl-admin-guide-permissions.md "studio-updated-jl-admin-guide-permissions.md").

Update the JupyterLab spaces that you've already created to use the latest version of
the SageMaker Distribution Image to access the latest features. You can use either the
Studio UI or the AWS Command Line Interface (AWS CLI) to update the image.

The following sections provide information about updating an image.

Updating the image involves restarting the JupyterLab space of your user. Use
the following procedure to update your user's JupyterLab space with the latest
image.

###### To update the image (UI)

1. Open Studio. For information about opening Studio, see [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. Choose **JupyterLab**.
3. Select the JupyterLab space of your user.
4. Choose **Stop space**.
5. For **Image**, select an updated version of the SageMaker AI
   Distribution Image. For the latest image, choose
   **Latest**.
6. Choose **Run space**.
   This section assumes that you have the AWS Command Line Interface (AWS CLI) installed. For
   information about installing the AWS CLI, see [Install or update to
   the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

To update the image, you must the do the following for your user's
space:

1. Delete the JupyterLab application
2. Update the space
3. Create the application

###### Important

You must have the following information ready before you start updating
the image:

- domain ID – The ID of your user's Amazon SageMaker AI domain.
- Application type – JupyterLab.
- Application name – default.
- Space name – The name specified for the space.
- Instance type – The Amazon EC2 instance type that you're using to
  run the application. For example, `ml.t3.medium`.
- SageMaker Image ARN – The Amazon Resource Name (ARN) of the SageMaker AI
  Distribution Image. You can provide the latest version of the SageMaker AI
  Distribution Image by specifying either
  `sagemaker-distribution-cpu` or
  `sagemaker-distribution-gpu` as the resource
  identifier.
  To delete the JupyterLab application, run the following command:

```
aws sagemaker delete-app \
--domain-id `your-user's-domain-id`
--app-type JupyterLab \
--app-name default \
--space-name `name-of-your-user's-space`
```

To update your user's space, run the following command:

```
aws sagemaker update-space \
--space-name `name-of-your-user's-space` \
--domain-id `your-user's-domain-id`
```

If you've updated the space successfully, you'll see the space ARN in the
response:

```
{
"SpaceArn": "arn:aws:sagemaker:`AWS Region`:`111122223333`:space/`your-user's-domain-id`/name-of-your-user's-space"
}
```

To create the application, run the following command:

```
aws sagemaker create-app \
--domain-id `your-user's-domain-id`  \
--app-type JupyterLab \
--app-name default \
--space-name `name-of-your-user's-space` \
--resource-spec "InstanceType=`instance-type`,SageMakerImageArn=arn:aws:sagemaker:`AWS Region`:`555555555555`:image/sagemaker-distribution-`resource-identifier`"
```
