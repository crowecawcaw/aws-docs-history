

# Create a VPC Endpoint Policy for SageMaker AI MLflow
<a name="mlflow-private-link-policy"></a>

You can attach an Amazon VPC endpoint policy to the interface VPC endpoints that you use to connect to SageMaker AI MLflow. The endpoint policy controls access to MLflow. You can specify the following:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed. 

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html).

The following example of a VPC endpoint policy specifies that all users that have access to the endpoint are allowed to access to the MLflow tracking server that you specify. Access to other tracking servers is denied.

```
{
    "Statement": [
        {
            "Action": "sagemaker-mlflow:*",
            "Effect": "Allow",
            "Principal": "*",
            "Resource": "arn:aws:sagemaker:{{AWS Region}}:{{111122223333}}:mlflow-tracking-server/*"
        }
    ]
}
```

For an MLflow App, use the `sagemaker:CallMlflowAppApi` action and the MLflow App resource ARN. Use the following example to grant access to the MLflow App that you specify. The policy denies access to all other MLflow Apps.

```
{
    "Statement": [
        {
            "Action": "sagemaker:CallMlflowAppApi",
            "Effect": "Allow",
            "Principal": "*",
            "Resource": "arn:aws:sagemaker:{{AWS Region}}:{{111122223333}}:mlflow-app/*"
        }
    ]
}
```