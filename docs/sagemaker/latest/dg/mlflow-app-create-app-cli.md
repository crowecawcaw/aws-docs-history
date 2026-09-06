

# Create an app using the AWS CLI
<a name="mlflow-app-create-app-cli"></a>

You can create an app using the AWS CLI for more granular security customization.

## Prerequisites
<a name="mlflow-app-create-app-cli-prereqs"></a>

To create an app using the AWS CLI, you must have the following:
+ **Access to a terminal. **This can include local IDEs, an Amazon EC2 instance, or AWS CloudShell.
+ **Access to a development environment.** This can include local IDEs or a Jupyter notebook environment within Studio or Studio Classic.
+ **A configured AWS CLI installation**. For more information, see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html). 
+ **An IAM role with appropriate permissions**. The following steps require your environment to have `iam:CreateRole`, `iam:CreatePolicy`, `iam:AttachRolePolicy`, and `iam:ListPolicies` permissions. These permissions are needed on the role that is being used to run the steps in this user guide. The instructions in this guide create an IAM role that is used as the execution role of the MLflow App so that it can access data in your Amazon S3 buckets. Additionally, a policy is created to give the IAM role of the user that is interacting with the App via the MLflow SDK permission to call MLflow APIs. For more information, see [Modifying a role permissions policy (console) ](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-modify_permissions-policy). 

  If using a SageMaker Studio Notebook, update the service role for your Studio user profile with these IAM permissions. To update the service role, navigate to the SageMaker AI console and select the domain you are using. Then, under the domain, select the user profile you are using. You will see the service role listed there. Navigate to the IAM console, search for the service role under **Roles**, and update your role with a policy that allows the `iam:CreateRole`, `iam:CreatePolicy`, `iam:AttachRolePolicy`, and `iam:ListPolicies` actions. 

## Set up AWS CLI model
<a name="mlflow-app-create-app-cli-setup"></a>

Follow these command line steps within a terminal to set up the AWS CLI for Amazon SageMaker AI with MLflow.

1. Install an updated version of the AWS CLI. For more information, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS CLI User Guide*.

1. Verify that the AWS CLI is installed using the following command: 

   ```
   aws sagemaker help
   ```

   Press `q` to exit the prompt.

   For troubleshooting help, see [Troubleshoot common setup issues](mlflow-troubleshooting.md).

## Set up MLflow infrastructure
<a name="mlflow-create-app-cli-infra-setup"></a>

The following section shows you how to set up an MLflow App along with the Amazon S3 bucket and IAM role needed for the app.

### Create an S3 bucket
<a name="mlflow-infra-setup-s3-bucket"></a>

Within your terminal, use the following commands to create a general purpose Amazon S3 bucket: 

**Important**  
When you provide the Amazon S3 URI for your artifact store, ensure the Amazon S3 bucket is in the same AWS Region as your MLflow App. **Cross-region artifact storage is not supported**.

```
bucket_name={{bucket-name}}
  region={{valid-region}}
  
  aws s3api create-bucket \
    --bucket {{$bucket_name}} \
    --region {{$region}} \
    --create-bucket-configuration LocationConstraint={{$region}}
```

The output should look similar to the following:

```
{
      "Location": "/{{bucket-name}}"
  }
```

### Set up IAM trust policies
<a name="mlflow-app-create-app-cli-trust-policy"></a>

Use the following steps to create an IAM trust policy. For more information about roles and trust policies, see [Roles terms and concepts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) in the *AWS Identity and Access Management User Guide*.

1. Within your terminal, use the following command to create a file called `mlflow-trust-policy.json`.

   ```
   cat <<EOF > /tmp/{{mlflow-trust-policy.json}}
     {
          "Version": "2012-10-17",		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "Service": [                     
                           "sagemaker.amazonaws.com"
                      ]
                  },
                  "Action": "sts:AssumeRole"
              }
          ]
      }
     EOF
   ```

1. Within your terminal, use the following command to create a file called `custom-policy.json`.

   ```
   cat <<EOF > /tmp/custom-policy.json
     {
         "Version": "2012-10-17",		 	 	 
         "Statement": [
             {
                 "Effect": "Allow",
                 "Action": [
                     "s3:Get*",
                     "s3:Put*",
                     "sagemaker:AddTags",
                     "sagemaker:CreateModelPackageGroup",
                     "sagemaker:CreateModelPackage",
                     "sagemaker:DescribeModelPackageGroup",
                     "sagemaker:UpdateModelPackage",
                     "s3:List*"
                 ],
                 "Resource": "*"
             }
         ]
     }
     EOF
   ```

1. Use the trust policy file to create a role. Then, attach IAM role policies that allow MLflow to access Amazon S3 and SageMaker Model Registry within your account. MLflow must have access to Amazon S3 for your app's artifact store and SageMaker Model Registry for automatic model registration. 
**Note**  
If you are updating an existing role, use the following command instead: `aws iam update-assume-role-policy --role-name {{$role_name}} --policy-document {{file:///tmp/mlflow-trust-policy.json}}`.

   ```
   role_name={{role-name}}
     
     aws iam  create-role \
       --role-name {{$role_name}} \
       --assume-role-policy-document file:///tmp/{{mlflow-trust-policy.json}}
     
     aws iam put-role-policy \
       --role-name {{$role_name}} \
       --policy-name {{custom-policy}} \
       --policy-document file:///tmp/{{custom-policy.json
     }}
     role_arn=$(aws iam get-role --role-name  $role_name --query 'Role.Arn' --output text)
   ```

## Create MLflow App
<a name="mlflow-app-create-app-cli-create"></a>

Within your terminal, use the `create-mlflow-app` API to create an app in the AWS Region of your choice. This step normally takes approximately 2-3 minutes.

The following command creates a new app with automatic model registration enabled. To deactivate automatic model registration, specify `--no-automatic-model-registration`. 

After creating your app, you can launch the MLflow UI. For more information, see [Launch the MLflow UI using a presigned URL](mlflow-launch-ui.md).

**Note**  
It may take up to 2-3 minutes to complete app creation. If the app takes over 3 minutes to create, check that you have the necessary IAM permissions. When you successfully create an app, it automatically starts.

By default, the app that is created is the latest version and will be automatically updated.

```
app_name={{app-name}}
  region={{valid-region}}
  version={{valid-version}}        
  
  
  aws sagemaker create-mlflow-app \
   --name {{$app_name}} \
   --artifact-store-uri s3://{{$bucket_name}} \
   --role-arn {{$role_arn}} \
   {{--automatic-model-registration}} \
   --region {{$region}}
```

The output should be similar to the following: 

```
{
      "AppArn": "arn:aws:sagemaker:{{region}}:{{123456789012}}:mlflow-app/{{app-name}}"
  }
```

**Important**  
**Take note of the app ARN for later use.** You will also need the `$bucket_name` for clean up steps. 