# Create a Model Group

A Model Group contains different versions of a model. You can create a Model Group
that tracks all of the models that you train to solve a particular problem. Create a
Model Group by using either the AWS SDK for Python (Boto3) or the Amazon SageMaker Studio console.

## Create a Model Group

(Boto3)

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

To create a Model Group by using Boto3, call the
`create_model_package_group` API operation and specify a name and
description as parameters. The following example shows how to create a Model
Group. The response from the `create_model_package_group` call is the
Amazon Resource Name (ARN) of the new Model Group.

First, import the required packages and set up the SageMaker AI Boto3 client.

```
import time
import os
from sagemaker import get_execution_role, session
import boto3

region = boto3.Session().region_name

role = get_execution_role()

sm_client = boto3.client('sagemaker', region_name=region)
```

Now create the Model Group.

```
import time
model_package_group_name = "scikit-iris-detector-" + str(round(time.time()))
model_package_group_input_dict = {
 "ModelPackageGroupName" : model_package_group_name,
 "ModelPackageGroupDescription" : "Sample model package group"
}

create_model_package_group_response = sm_client.create_model_package_group(**model_package_group_input_dict)
print('ModelPackageGroup Arn : {}'.format(create_model_package_group_response['ModelPackageGroupArn']))
```

## Create a Model Group

(Studio or Studio Classic)

To create a Model Group in the Amazon SageMaker Studio console, complete the following
steps based on whether you use Studio or Studio Classic.

Studio

1. Open the SageMaker Studio console by following the
   instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose
   **Models**.
3. Choose the **Registered models** tab, if
   not selected already.
4. Immediately below the **Registered
   models** tab label, choose **Model
   Groups**, if not selected already.
5. Choose **Register**, then choose
   **Model group**.
6. In the **Register model group** dialog
   box, enter the following information:
   - The name of the new Model Group in the
     **Model group name**
     field.
   - (Optional) A description for the Model Group in
     the **Description** field.
   - (Optional) Any key-value pairs you want to
     associate with the Model Group in the
     **Tags** field. For information
     about using tags, see [Tagging
     AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the
     _AWS General Reference_.

7. Choose **Register model group**.
8. (Optional) In the **Models** page, choose
   the **Registered models** tab, then choose
   **Model Groups**. Confirm your
   newly-created Model Group appears in the list of Model
   Groups.

Studio Classic

1. Sign in to Amazon SageMaker Studio Classic. For more information, see
   [Launch
   Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. In the left navigation pane, choose the
   **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Choose **Models**, and then
   **Model registry**.
4. Choose **Actions**, then choose
   **Create model group**.
5. In the **Create model group** dialog box,
   enter the following information:
   - Enter the name of the new Model Group in the
     **Model group name**
     field.
   - (Optional) Enter a description for the Model Group
     in the **Description**
     field.
   - (Optional) Enter any key-value pairs you want to
     associate with the Model Group in the
     **Tags** field. For information
     about using tags, see [Tagging
     AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the
     _AWS General Reference_.
   - (Optional) Choose a project with which to
     associate the Model Group in the
     **Project** field. For
     information about projects, see [MLOps Automation With SageMaker Projects](sagemaker-projects.md "sagemaker-projects.md").

6. Choose **Create model group**.
