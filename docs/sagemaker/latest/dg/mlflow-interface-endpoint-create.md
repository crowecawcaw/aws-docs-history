# Create a VPC Endpoint

You can create an interface endpoint to connect to SageMaker AI MLflow. For instructions, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint"). Make sure that you create interface endpoints for all of
the subnets in your VPC from which you want to connect to SageMaker AI MLflow.

When you create an interface endpoint, ensure that the security groups on your
endpoint allow inbound and outbound access for HTTPS traffic. For more information, see [Control access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoints-security-groups "../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoints-security-groups").

###### Note

In addition to creating an interface endpoint to connect to SageMaker AI MLflow,
create an interface endpoint to connect to the Amazon SageMaker API. When users call [CreatePresignedMlflowTrackingServerUrl](../APIReference/API_CreatePresignedMlflowTrackingServerUrl.md "../APIReference/API_CreatePresignedMlflowTrackingServerUrl.md") (for an MLflow
tracking server) or [CreatePresignedMlflowAppUrl](../APIReference/API_CreatePresignedMlflowAppUrl.md "../APIReference/API_CreatePresignedMlflowAppUrl.md") (for an MLflow App) to get the
URL to connect to SageMaker AI MLflow, the call goes through the interface endpoint. This
endpoint is the one used to connect to the SageMaker API.

When you create the interface endpoint, specify the service name that corresponds to
your MLflow offering:

- For an MLflow tracking server, specify
  `aws.sagemaker.`AWS Region`.experiments`
  as the service name.
- For an MLflow App, specify
  `aws.sagemaker.`AWS Region`.mlflow`
  as the service name.
  After you create the interface endpoint, enable private DNS for your endpoint. When
  you connect to SageMaker AI MLflow from within the VPC using the SageMaker Python SDK, you connect
  through the interface endpoint instead of the public internet.

Within the AWS Management Console, you can use the following procedure to create an endpoint.

###### To create an endpoint

1. Navigate to the [Amazon Virtual Private Cloud console](https://console.aws.amazon.com/vpcconsole "https://console.aws.amazon.com/vpcconsole").
2. Navigate to **Endpoints**.
3. Choose **Create endpoint**.
4. (Optional) For **Name (tag)**, specify a name for the endpoint.
5. In the search bar under **Services**, specify
   **experiments** (for an MLflow tracking server) or
   **mlflow** (for an MLflow App).
6. Select the endpoint that you're creating.
7. For **VPC**, specify the name of the VPC.
8. Choose **Create endpoint**.
