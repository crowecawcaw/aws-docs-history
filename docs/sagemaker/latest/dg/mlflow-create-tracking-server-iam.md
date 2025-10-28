# Set up IAM permissions for MLflow

You must configure the necessary IAM service roles to get started with MLflow in
Amazon SageMaker AI.

If you create a new Amazon SageMaker AI domain to access your experiments in Studio, you can
configure the necessary IAM permissions during domain setup. For more information, see [Set up MLflow IAM
permissions when creating a new domain](#mlflow-create-tracking-server-iam-role-manager "#mlflow-create-tracking-server-iam-role-manager").

To set up permissions using the IAM console, see [Create necessary IAM service roles in the IAM console](#mlflow-create-tracking-server-iam-service-roles "#mlflow-create-tracking-server-iam-service-roles").

You must configure authorization controls for `sagemaker-mlflow` actions. You
can optionally define more granular authorization controls to govern action-specific MLflow
permissions. For more information, see [Create action-specific
authorization controls](#mlflow-create-tracking-server-update-iam-actions "#mlflow-create-tracking-server-update-iam-actions").

## Set up MLflow IAM

permissions when creating a new domain

When setting up a new Amazon SageMaker AI domain for your organization, you can configure IAM
permissions for your domain service role through the **Users and ML Activities**
settings.

###### To configure IAM permissions for using MLflow with SageMaker AI when setting up a new

domain

1. Set up a new domain using the SageMaker AI console. On the **Set up SageMaker AI
   domain** page, choose **Set up for organizations**. For
   more information, see [Custom setup using the console](onboard-custom.md#onboard-custom-instructions-console "onboard-custom.md#onboard-custom-instructions-console").
2. When setting up **Users and ML Activities**, choose from the
   following ML activities for MLflow: **Use MLflow**, **Manage
   MLflow Tracking Servers**, and **Access required to AWS Services for
   MLflow**. For more information about these activities, see the explanations
   that follow this procedure.
3. Complete the setup and creation of your new domain.

The following MLflow ML activities are available in Amazon SageMaker Role Manager:

- **Use MLflow**: This ML activity grants the domain service role
  permission to call MLflow REST APIs in order to manage experiments, runs, and models in
  MLflow.
- **Manage MLflow Tracking Servers**: This ML activity grants the domain service role permission to
  create, update, start, stop, and delete tracking servers.
- **Access required to AWS Services for MLflow**: This ML activity provides
  the domain service role permissions needed to access Amazon S3 and the SageMaker AI Model
  Registry. This allows you to use the domain service role as the tracking server
  service role.

For more information about ML activities in Role Manager, see [ML activity reference](role-manager-ml-activities.md "role-manager-ml-activities.md").

## Create necessary IAM service roles in the IAM console

If you did not create or update your domain service role, you must instead create the following service roles in the IAM console
in order to create and use an MLflow Tracking Server:

- A tracking server IAM service role that the tracking server can use to
  access SageMaker AI resources
- A SageMaker AI IAM service role that SageMaker AI can use to create and manage
  MLflow resources

### IAM policies for

the tracking server IAM service role

The tracking server IAM service role is used by the tracking server to access the resources it
needs such as Amazon S3 and the SageMaker Model Registry.

When creating the tracking server IAM service role, use the following IAM trust
policy:

JSON

```
`{
 "Version":"2012-10-17",
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
 }`

```

In the IAM console, add the following permissions policy to your tracking server
service role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:Get*",
 "s3:Put*",
 "s3:List*",
 "sagemaker:AddTags",
 "sagemaker:CreateModelPackageGroup",
 "sagemaker:CreateModelPackage",
 "sagemaker:UpdateModelPackage",
 "sagemaker:DescribeModelPackageGroup"
 ],
 "Resource": "`*`"
 }
 ]
}`

```

### IAM policy for the

SageMaker AI IAM service role

The SageMaker AI service role is used by the client accessing the MLflow Tracking Server and needs
permissions to call MLflow REST APIs. The SageMaker AI service role also needs SageMaker API permissions to create, view
update, start, stop, and delete tracking servers.

You can create a new role or update an existing role. The SageMaker AI service role needs the following
policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker-mlflow:*",
 "sagemaker:CreateMlflowTrackingServer",
 "sagemaker:ListMlflowTrackingServers",
 "sagemaker:UpdateMlflowTrackingServer",
 "sagemaker:DeleteMlflowTrackingServer",
 "sagemaker:StartMlflowTrackingServer",
 "sagemaker:StopMlflowTrackingServer",
 "sagemaker:CreatePresignedMlflowTrackingServerUrl"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Create action-specific

authorization controls

You must set up authorization controls for `sagemaker-mlflow`, and can
optionally configure action-specific authorization controls to govern more granular MLflow
permissions that your users have on an MLflow Tracking Server.

###### Note

The following steps assume that you have an ARN for an MLflow Tracking Server already
available. To learn how to create a tracking server, see [Create a tracking server using Studio](mlflow-create-tracking-server-studio.md "mlflow-create-tracking-server-studio.md") or [Create a tracking server using the AWS CLI](mlflow-create-tracking-server-cli.md "mlflow-create-tracking-server-cli.md").

The following command creates a file called `mlflow-policy.json` that
provides your tracking server with IAM permissions for all available SageMaker AI MLflow actions.
You can optionally limit the permissions a user has by choosing the specific actions you
want that user to perform. For a list of available actions, see [IAM actions supported for
MLflow](#mlflow-create-tracking-server-iam-actions "#mlflow-create-tracking-server-iam-actions").

```
# Replace "Resource":"*" with "Resource":"TrackingServerArn"
# Replace "sagemaker-mlflow:*" with specific actions

printf '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "`sagemaker-mlflow:*`",
            "Resource": "`*`"
        }
    ]
}' > mlflow-policy.json
```

Use the `mlflow-policy.json` file to create an IAM policy using the AWS CLI.

```
aws iam create-policy \
  --policy-name `MLflowPolicy` \
  --policy-document `file://mlflow-policy.json`
```

Retrieve your account ID and attach the policy to your IAM role.

```
# Get your account ID
aws sts get-caller-identity

# Attach the IAM policy using your exported role and account ID
aws iam attach-role-policy \
  --role-name `$role_name` \
  --policy-arn arn:aws:iam::`123456789012`:policy/`MLflowPolicy`
```

### IAM actions supported for

MLflow

The following SageMaker AI MLflow actions are supported for authorization access
control:

- sagemaker-mlflow:AccessUI
- sagemaker-mlflow:CreateExperiment
- sagemaker-mlflow:SearchExperiments
- sagemaker-mlflow:GetExperiment
- sagemaker-mlflow:GetExperimentByName
- sagemaker-mlflow:DeleteExperiment
- sagemaker-mlflow:RestoreExperiment
- sagemaker-mlflow:UpdateExperiment
- sagemaker-mlflow:CreateRun
- sagemaker-mlflow:DeleteRun
- sagemaker-mlflow:RestoreRun
- sagemaker-mlflow:GetRun
- sagemaker-mlflow:LogMetric
- sagemaker-mlflow:LogBatch
- sagemaker-mlflow:LogModel
- sagemaker-mlflow:LogInputs
- sagemaker-mlflow:SetExperimentTag
- sagemaker-mlflow:SetTag
- sagemaker-mlflow:DeleteTag
- sagemaker-mlflow:LogParam
- sagemaker-mlflow:GetMetricHistory
- sagemaker-mlflow:SearchRuns
- sagemaker-mlflow:ListArtifacts
- sagemaker-mlflow:UpdateRun
- sagemaker-mlflow:CreateRegisteredModel
- sagemaker-mlflow:GetRegisteredModel
- sagemaker-mlflow:RenameRegisteredModel
- sagemaker-mlflow:UpdateRegisteredModel
- sagemaker-mlflow:DeleteRegisteredModel
- sagemaker-mlflow:GetLatestModelVersions
- sagemaker-mlflow:CreateModelVersion
- sagemaker-mlflow:GetModelVersion
- sagemaker-mlflow:UpdateModelVersion
- sagemaker-mlflow:DeleteModelVersion
- sagemaker-mlflow:SearchModelVersions
- sagemaker-mlflow:GetDownloadURIForModelVersionArtifacts
- sagemaker-mlflow:TransitionModelVersionStage
- sagemaker-mlflow:SearchRegisteredModels
- sagemaker-mlflow:SetRegisteredModelTag
- sagemaker-mlflow:DeleteRegisteredModelTag
- sagemaker-mlflow:DeleteModelVersionTag
- sagemaker-mlflow:DeleteRegisteredModelAlias
- sagemaker-mlflow:SetRegisteredModelAlias
- sagemaker-mlflow:GetModelVersionByAlias
- sagemaker-mlflow:FinalizeLoggedModel
- sagemaker-mlflow:GetLoggedModel
- sagemaker-mlflow:DeleteLoggedModel
- sagemaker-mlflow:SearchLoggedModels
- sagemaker-mlflow:SetLoggedModelTags
- sagemaker-mlflow:DeleteLoggedModelTag
- sagemaker-mlflow:ListLoggedModelArtifacts
- sagemaker-mlflow:LogLoggedModelParams
- sagemaker-mlflow:LogOutputs
