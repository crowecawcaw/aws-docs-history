# Set up IAM permissions for MLflow Apps

You must configure the necessary IAM service roles to get started with MLflow Apps in
Amazon SageMaker AI.

If you create a new Amazon SageMaker AI domain to access your experiments in Studio, you can
configure the necessary IAM permissions during domain setup. For more information, see [Set up MLflow IAM
permissions when creating a new domain](mlflow-create-tracking-server-iam.md#mlflow-create-tracking-server-iam-role-manager "mlflow-create-tracking-server-iam.md#mlflow-create-tracking-server-iam-role-manager").

To set up permissions using the IAM console, see [Create necessary IAM service roles in the IAM console](mlflow-create-tracking-server-iam.md#mlflow-create-tracking-server-iam-service-roles "mlflow-create-tracking-server-iam.md#mlflow-create-tracking-server-iam-service-roles").

You must configure authorization controls for `sagemaker-mlflow` actions. You
can optionally define more granular authorization controls to govern action-specific MLflow
permissions. For more information, see [Create action-specific
authorization controls](#mlflow-create-app-update-iam-actions "#mlflow-create-app-update-iam-actions").

## Set up MLflow IAM

permissions when creating a new domain

When setting up a new Amazon SageMaker AI domain for your organization, you can configure IAM
permissions for your domain service role through the **Users and ML Activities**
settings.

1. Set up a new domain using the SageMaker AI console. On the **Set up SageMaker AI
   domain** page, choose **Set up for organizations**. For
   more information, see [Custom setup using the console](onboard-custom.md#onboard-custom-instructions-console "onboard-custom.md#onboard-custom-instructions-console").
2. When setting up **Users and ML Activities**, choose from the
   following ML activities for MLflow: **Use MLflow**, **Manage
   MLflow Apps**, and **Access required to AWS Services for
   MLflow**. For more information about these activities, see the explanations
   that follow this procedure.
3. Complete the setup and creation of your new domain.

The following MLflow ML activities are available in Amazon SageMaker Role Manager:

- **Use MLflow**: This ML activity grants the domain service role
  permission to call MLflow REST APIs in order to manage experiments, runs, and models in
  MLflow.
- **Manage MLflow Apps**: This ML activity grants the domain service role permission to
  create, update, and delete MLflow Apps.
- **Access required to AWS services for MLflow Apps**: This ML activity provides
  the domain service role permissions needed to access Amazon S3 and the SageMaker AI Model
  Registry. This allows you to use the domain service role as the tracking server
  service role.

For more information about ML activities in Role Manager, see [ML activity reference](role-manager-ml-activities.md "role-manager-ml-activities.md").

## Create necessary IAM service roles in the IAM console

If you did not create or update your domain service role, you must instead create the following service roles in the IAM console
in order to create and use an MLflow Apps:

- An MLflow App IAM service role that the App can use to
  access SageMaker AI resources
- A SageMaker AI IAM service role that SageMaker AI can use to create and manage
  MLflow resources

### IAM policies for

the MLflow App IAM service role

The MLflow App IAM service role is used by the app to access the resources it
needs such as Amazon S3 and the SageMaker Model Registry.

When creating the app IAM service role, use the following IAM trust
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

In the IAM console, add the following permissions policy to your app
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

The SageMaker AI service role is used by the client accessing the MLflow App and needs
permissions to call MLflow REST APIs. The SageMaker AI service role also needs SageMaker API permissions to create, view
update, and delete apps.

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
permissions that your users have on an MLflow Apps.

###### Note

The following steps assume that you have an ARN for an MLflow Apps already
available.

### Data Plane IAM actions supported for

MLflow Apps

The following SageMaker AI MLflow actions are supported for authorization access
control:

- sagemaker:CallMlflowAppApi
