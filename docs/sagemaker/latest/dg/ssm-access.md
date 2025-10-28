# Access containers through SSM

Amazon SageMaker AI allows you to securely connect to the Docker containers on which your models are deployed on
for Inference using AWS Systems Manager (SSM). This gives you shell level access to the container so that you
can debug the processes running within the container and log commands and responses with Amazon CloudWatch. You
can also set up an AWS PrivateLink connection to the ML instances that host your containers for accessing the
containers via SSM privately.

###### Warning

Enabling SSM access can impact the performance of your endpoint. We recommend using this feature with your
dev or test endpoints and not with the endpoints in production. Also, SageMaker AI automatically applies security
patches, and replaces or terminates faulty endpoint instances within 10 minutes. However for endpoints with
SSM enabled production variants, SageMaker AI delays security patching and replacing or terminating faulty
endpoint instances by a day, to allow you to debug.

The following sections detail how you can use this feature.

## Allowlist

You have to contact customer support, and get your account allowlisted, to use this feature. You cannot
create an endpoint with SSM access enabled, if your account is not allow listed for this access.

## Enable SSM access

To enable SSM access for an existing container on an endpoint, update the endpoint with a new endpoint
configuration, with the `EnableSSMAccess` parameter set to `true` The following
example provides a sample endpoint configuration.

```
{
    "EndpointConfigName": `"endpoint-config-name"`,
    "ProductionVariants": [
        {
            "InitialInstanceCount": 1,
            "InitialVariantWeight": 1.0,
            "InstanceType": "ml.t2.medium",
            "ModelName": `model-name`,
            "VariantName": `variant-name`,
            "EnableSSMAccess": true,
        },
    ]
}

```

For more information on enabling SSM access, see [EnableSSMAccess](../APIReference/API_ProductionVariant.md#API_EnableSSMAccess "../APIReference/API_ProductionVariant.md#API_EnableSSMAccess").

## IAM configuration

### Endpoint IAM permissions

If you have enabled SSM access for an endpoint instance, SageMaker AI starts and manages the [SSM agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") when it
initiates the endpoint instance. To allow the SSM agent to communicate with the SSM services, add
the following policy to the execution role that the endpoint runs under.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssmmessages:CreateControlChannel",
 "ssmmessages:CreateDataChannel",
 "ssmmessages:OpenControlChannel",
 "ssmmessages:OpenDataChannel"
 ],
 "Resource": "*"
 }
 ]
 }`

```

### User IAM permissions

Add the following policy to give an IAM user SSM session permissions to connect to a SSM target.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession",
 "ssm:TerminateSession"
 ],
 "Resource": "*"
 }
 ]
}`

```

You can restrict the endpoints that an IAM user can connect to, with the following
policy. Replace the `italicized placeholder text` with your own information.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession",
            ],
            "Resource": [
                "`sagemaker-endpoint-arn`"
            ]
        }
    ]
}


```

## SSM access with AWS PrivateLink

If your endpoints run within a virtual private cloud (VPC) that is not connected to the public internet, you
can use AWS PrivateLink to enable SSM. AWS PrivateLink restricts all network traffic between your endpoint
instances, SSM, and Amazon EC2 to the Amazon network. For more information on how to setup SSM access with
AWS PrivateLink, see [Set up a VPC
endpoint for Session Manager](../../../systems-manager/latest/userguide/session-manager-getting-started-privatelink.md "../../../systems-manager/latest/userguide/session-manager-getting-started-privatelink.md").

## Logging with Amazon CloudWatch Logs

For SSM access enabled endpoints, you can log errors from the SSM agent with Amazon CloudWatch Logs. For more
information on how to log errors with CloudWatch Logs, see [Logging session activity](../../../systems-manager/latest/userguide/session-manager-logging.md "../../../systems-manager/latest/userguide/session-manager-logging.md"). The
log is available at the SSM log stream,
``variant-name`/`ec2-instance-id`/ssm`, under
 the endpoint log group `/aws/sagemaker/endpoints/`endpoint-name``. For
more information on how to view the log, see [View log data
sent to CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#ViewingLogData "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#ViewingLogData").

Production variants behind your endpoint can have multiple model containers. The log for each model
container is recorded in the log stream. Each log is preceded by `[sagemaker ssm
 logs][container-name]`, where `container-name` is either the name that you gave to the
container, or the default name, such as `container_0`, and `container_1`.

## Accessing model containers

To access a model container on your endpoint instance, you need its target ID. The target ID is in one of
the following formats:

- `sagemaker-endpoint:`endpoint-name`_`variant-name`_`ec2-instance-id``
  for containers on single container endpoints
- `sagemaker-endpoint:`endpoint-name`_`variant-name`_`ec2-instance-id`_`container-name``
  for containers on multi-container endpoints

The following example shows how you can use the AWS CLI to access a model container using its target ID.

```
aws ssm start-session --target sagemaker-endpoint:prod-image-classifier_variant1_i-003a121c1b21a90a9_container_1

```

If you enable logging, as mentioned in [Logging with Amazon CloudWatch Logs](#ssm-access-logging "#ssm-access-logging"), you can find the target IDs for all the containers listed at the
beginning of the SSM log stream.

###### Note

- You cannot connect to 1P algorithm containers or containers of models obtained from SageMaker AI
  MarketPlace with SSM. However you can connect to deep learning containers (DLCs) provided by
  AWS or any custom container that you own.
- If you have enabled network isolation for a model container that prevents it from making
  outbound network calls, you cannot start an SSM session for that container.
- You can only access one container from one SSM session. To access another container, even if
  it is behind the same endpoint, start a new SSM session with the target ID of that endpoint.
