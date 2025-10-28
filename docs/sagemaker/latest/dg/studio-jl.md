# JupyterLab Versioning in Amazon SageMaker Studio Classic

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

The Amazon SageMaker Studio Classic interface is based on JupyterLab, which is a web-based interactive
development environment for notebooks, code, and data. Studio Classic only supports using JupyterLab 3.

If you created your domain and user profile using the AWS Management Console before 08/31/2022 or using
the AWS Command Line Interface before 02/22/23, then your Studio Classic instance defaulted to JupyterLab 1. After
07/01/2024, you cannot create any Studio Classic applications that run JupyterLab 1.

## JupyterLab 3

JupyterLab 3 includes the following features that are not available in previous versions. For
more information about these features, see [JupyterLab 3.0 is released!](https://blog.jupyter.org/jupyterlab-3-0-is-out-4f58385e25bb "https://blog.jupyter.org/jupyterlab-3-0-is-out-4f58385e25bb").

- Visual debugger when using the Base Python 2.0 and Data Science 2.0 kernels.
- File browser filter
- Table of Contents (TOC)
- Multi-language support
- Simple mode
- Single interface mode

### Important changes to JupyterLab 3

Consider the following when using JupyterLab 3:

- When setting the JupyterLab version using the AWS CLI, select the corresponding image
  for your Region and JupyterLab version from the image list in [From the AWS CLI](#studio-jl-set-cli "#studio-jl-set-cli").
- In JupyterLab 3, you must activate the `studio` conda environment before
  installing extensions. For more information, see [Installing JupyterLab and Jupyter Server extensions](#studio-jl-install "#studio-jl-install").
- Debugger is only supported when
  using the following images:
  - Base Python 2.0
  - Data Science 2.0
  - Base Python 3.0
  - Data Science 3.0

## Restricting default JupyterLab version using an IAM policy condition

key

You can use IAM policy condition keys to restrict the version of JupyterLab that your users
can launch.

The following policy shows how to limit the JupyterLab version at the domain level.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BlockJupyterLab3DomainLevelAppCreation",
 "Effect": "Deny",
 "Action": [
 "sagemaker:CreateDomain",
 "sagemaker:UpdateDomain"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:ArnLike": {
 "sagemaker:ImageArns": "arn:aws:sagemaker:us-east-1:`111122223333`:image/jupyter-server-3"
 }
 }
 }
 ]
}`

```

The following policy shows how to limit the JupyterLab version at the user profile level.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BlockUsersFromCreatingJupyterLab3Apps",
 "Effect": "Deny",
 "Action": [
 "sagemaker:CreateUserProfile",
 "sagemaker:UpdateUserProfile"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:ArnLike": {
 "sagemaker:ImageArns": "arn:aws:sagemaker:us-east-1:`111122223333`:image/jupyter-server-3"
 }
 }
 }
 ]
}`

```

The following policy shows how to limit the JupyterLab version at the application level.
The `CreateApp` request must include the image ARN for this policy to apply.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BlockJupyterLab3AppLevelAppCreation",
 "Effect": "Deny",
 "Action": "sagemaker:CreateApp",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:ArnLike": {
 "sagemaker:ImageArns": "arn:aws:sagemaker:us-east-1:`111122223333`:image/jupyter-server-3"
 }
 }
 }
 ]
}`

```

## Setting a default JupyterLab

version

The following sections show how to set a default JupyterLab version for Studio Classic using
either the console or the AWS CLI. 

### From the console

You can select the default JupyterLab version to use on either the domain or user profile
level during resource creation. To set the default JupyterLab version using the console, see
[Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md"). 

### From the AWS CLI

You can select the default JupyterLab version to use on either the domain or user profile
level using the AWS CLI. 

To set the default JupyterLab version using the AWS CLI, you must include the ARN of the
desired default JupyterLab version as part of an AWS CLI command. This ARN differs based on
the version and the Region of the SageMaker AI domain. 

The following table lists the ARNs of the available JupyterLab versions for each
Region:

| Region
| JL3
|
| --- | --- |
| us-east-1 | arn:aws:sagemaker:us-east-1:081325390199:image/jupyter-server-3 |
| us-east-2 | arn:aws:sagemaker:us-east-2:429704687514:image/jupyter-server-3 |
| us-west-1 | arn:aws:sagemaker:us-west-1:742091327244:image/jupyter-server-3 |
| us-west-2 | arn:aws:sagemaker:us-west-2:236514542706:image/jupyter-server-3 |
| af-south-1 | arn:aws:sagemaker:af-south-1:559312083959:image/jupyter-server-3 |
| ap-east-1 | arn:aws:sagemaker:ap-east-1:493642496378:image/jupyter-server-3 |
| ap-south-1 | arn:aws:sagemaker:ap-south-1:394103062818:image/jupyter-server-3 |
| ap-northeast-2 | arn:aws:sagemaker:ap-northeast-2:806072073708:image/jupyter-server-3 |
| ap-southeast-1 | arn:aws:sagemaker:ap-southeast-1:492261229750:image/jupyter-server-3 |
| ap-southeast-2 | arn:aws:sagemaker:ap-southeast-2:452832661640:image/jupyter-server-3 |
| ap-northeast-1 | arn:aws:sagemaker:ap-northeast-1:102112518831:image/jupyter-server-3 |
| ca-central-1 | arn:aws:sagemaker:ca-central-1:310906938811:image/jupyter-server-3 |
| eu-central-1 | arn:aws:sagemaker:eu-central-1:936697816551:image/jupyter-server-3 |
| eu-west-1 | arn:aws:sagemaker:eu-west-1:470317259841:image/jupyter-server-3 |
| eu-west-2 | arn:aws:sagemaker:eu-west-2:712779665605:image/jupyter-server-3 |
| eu-west-3 | arn:aws:sagemaker:eu-west-3:615547856133:image/jupyter-server-3 |
| eu-north-1 | arn:aws:sagemaker:eu-north-1:243637512696:image/jupyter-server-3 |
| eu-south-1 | arn:aws:sagemaker:eu-south-1:592751261982:image/jupyter-server-3 |
| eu-south-2 | arn:aws:sagemaker:eu-south-2:127363102723:image/jupyter-server-3 |
| sa-east-1 | arn:aws:sagemaker:sa-east-1:782484402741:image/jupyter-server-3 |
| cn-north-1 | arn:aws-cn:sagemaker:cn-north-1:390048526115:image/jupyter-server-3 |
| cn-northwest-1 | arn:aws-cn:sagemaker:cn-northwest-1:390780980154:image/jupyter-server-3 | #### Create or update domain You can set a default JupyterServer version at the domain level by invoking [CreateDomain](../APIReference/API_CreateDomain.md "../APIReference/API_CreateDomain.md") or [UpdateDomain](../APIReference/API_UpdateDomain.md "../APIReference/API_UpdateDomain.md") and passing the `UserSettings.JupyterServerAppSettings.DefaultResourceSpec.SageMakerImageArn` field. The following shows how to create a domain with JupyterLab 3 as the default, using the AWS CLI: ``aws --region `<REGION>` \ sagemaker create-domain \ --domain-name `<NEW_DOMAIN_NAME>` \ --auth-mode `<AUTHENTICATION_MODE>` \ --subnet-ids `<SUBNET-IDS>` \ --vpc-id `<VPC-ID>` \ --default-user-settings '{ "JupyterServerAppSettings": { "DefaultResourceSpec": { "SageMakerImageArn": "arn:aws:sagemaker:`<REGION>`:`<ACCOUNT_ID>`:image/jupyter-server-3", "InstanceType": "system" } } }'`` The following shows how to update a domain to use JupyterLab 3 as the default, using the AWS CLI: ``aws --region `<REGION>` \ sagemaker update-domain \ --domain-id `<YOUR_DOMAIN_ID>` \ --default-user-settings '{ "JupyterServerAppSettings": { "DefaultResourceSpec": { "SageMakerImageArn": "arn:aws:sagemaker:`<REGION>`:`<ACCOUNT_ID>`:image/jupyter-server-3", "InstanceType": "system" } } }'`` #### Create or update user profile You can set a default JupyterServer version at the user profile level by invoking [CreateUserProfile](../APIReference/API_CreateUserProfile.md "../APIReference/API_CreateUserProfile.md") or [UpdateUserProfile](../APIReference/API_UpdateUserProfile.md "../APIReference/API_UpdateUserProfile.md") and passing the `UserSettings.JupyterServerAppSettings.DefaultResourceSpec.SageMakerImageArn` field. The following shows how to create a user profile with JupyterLab 3 as the default on an existing domain, using the AWS CLI: ``aws --region `<REGION>` \ sagemaker create-user-profile \ --domain-id `<YOUR_DOMAIN_ID>` \ --user-profile-name `<NEW_USERPROFILE_NAME>` \ --query UserProfileArn --output text \ --user-settings '{ "JupyterServerAppSettings": { "DefaultResourceSpec": { "SageMakerImageArn": "arn:aws:sagemaker:`<REGION>`:`<ACCOUNT_ID>`:image/jupyter-server-3", "InstanceType": "system" } } }'`` The following shows how to update a user profile to use JupyterLab 3 as the default, using the AWS CLI: ``aws --region `<REGION>` \ sagemaker update-user-profile \ --domain-id `<YOUR_DOMAIN_ID>` \ --user-profile-name `<EXISTING_USERPROFILE_NAME>` \ --user-settings '{ "JupyterServerAppSettings": { "DefaultResourceSpec": { "SageMakerImageArn": "arn:aws:sagemaker:`<REGION>`:`<ACCOUNT_ID>`:image/jupyter-server-3", "InstanceType": "system" } } }'`` ## View and update the JupyterLab version of an application from the console The following shows how to view and update the JupyterLab version of an application. 1. Navigate to the SageMaker AI **domains** page. 2. Select a domain to view its user profiles. 3. Select a user to view their applications. 4. To view the JupyterLab version of an application, select the application's name. 5. To update the JupyterLab version, select **Action**. 6. From the dropdown menu, select **Change JupyterLab version**. 7. From the **Studio Classic settings** page, select the JupyterLab version from the dropdown menu. 8. After the JupyterLab version for the user profile has been successfully updated, restart the JupyterServer application to make the version changes effective. For more information about restarting a JupyterServer application, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md "studio-tasks-update-studio.md"). ## Installing JupyterLab and Jupyter Server extensions In JupyterLab 3, you must activate the `studio` conda environment before installing extensions. The method for this differs if you're installing the extensions from within Studio Classic or using a lifecycle configuration script. ### Installing Extension from within Studio Classic To install extensions from within Studio Classic, you must activate the `studio` environment before you install extensions. ``# Before installing extensions conda activate studio # Install your extensions pip install `<JUPYTER_EXTENSION>` # After installing extensions conda deactivate`` ### Installing Extensions using a lifecycle configuration script If you're installing JupyterLab and Jupyter Server extensions in your lifecycle configuration script, you must modify your script so that it works with JupyterLab 3. The following sections show the code needed for existing and new lifecycle configuration scripts. #### Existing lifecycle configuration script If you're reusing an existing lifecycle configuration script that must work with both versions of JupyterLab, use the following code in your script: ``# Before installing extension export AWS_SAGEMAKER_JUPYTERSERVER_IMAGE="${AWS_SAGEMAKER_JUPYTERSERVER_IMAGE:-'jupyter-server'}" if [ "$AWS_SAGEMAKER_JUPYTERSERVER_IMAGE" = "jupyter-server-3" ] ; then eval "$(conda shell.bash hook)" conda activate studio fi; # Install your extensions pip install `<JUPYTER_EXTENSION>` # After installing extension if [ "$AWS_SAGEMAKER_JUPYTERSERVER_IMAGE" = "jupyter-server-3" ]; then conda deactivate fi;`` #### New lifecycle configuration script If you're writing a new lifecycle configuration script that only uses JupyterLab 3, you can use the following code in your script: ``# Before installing extension eval "$(conda shell.bash hook)" conda activate studio # Install your extensions pip install `<JUPYTER_EXTENSION>` conda deactivate``
