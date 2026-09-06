

# Create a VPC Endpoint
<a name="mlflow-interface-endpoint-create"></a>

You can create an interface endpoint to connect to SageMaker AI MLflow. For instructions, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint). Make sure that you create interface endpoints for all of the subnets in your VPC from which you want to connect to SageMaker AI MLflow. 

When you create an interface endpoint, ensure that the security groups on your endpoint allow inbound and outbound access for HTTPS traffic. For more information, see [Control access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoints-security-groups).

**Note**  
In addition to creating an interface endpoint to connect to SageMaker AI MLflow, create an interface endpoint to connect to the Amazon SageMaker API. When users call [CreatePresignedMlflowTrackingServerUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedMlflowTrackingServerUrl.html) (for an MLflow tracking server) or [CreatePresignedMlflowAppUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedMlflowAppUrl.html) (for an MLflow App) to get the URL to connect to SageMaker AI MLflow, the call goes through the interface endpoint. This endpoint is the one used to connect to the SageMaker API.

When you create the interface endpoint, specify the service name that corresponds to your MLflow offering:
+ For an MLflow tracking server, specify **aws.sagemaker.{{AWS Region}}.experiments** as the service name.
+ For an MLflow App, specify **aws.sagemaker.{{AWS Region}}.mlflow** as the service name.

After you create the interface endpoint, enable private DNS for your endpoint. When you connect to SageMaker AI MLflow from within the VPC using the SageMaker Python SDK, you connect through the interface endpoint instead of the public internet.

Within the AWS Management Console, you can use the following procedure to create an endpoint.

**To create an endpoint**

1. Navigate to the [Amazon Virtual Private Cloud console](https://console.aws.amazon.com/vpcconsole).

1. Navigate to **Endpoints**.

1. Choose **Create endpoint**.

1. (Optional) For **Name (tag)**, specify a name for the endpoint.

1. In the search bar under **Services**, specify **experiments** (for an MLflow tracking server) or **mlflow** (for an MLflow App).

1. Select the endpoint that you're creating.

1. For **VPC**, specify the name of the VPC.

1. Choose **Create endpoint**.