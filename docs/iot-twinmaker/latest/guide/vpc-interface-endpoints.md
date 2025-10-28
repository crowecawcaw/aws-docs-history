# AWS IoT TwinMaker and interface VPC

endpoints (AWS PrivateLink)

You can establish a private connection between your virtual private cloud (VPC) and
AWS IoT TwinMaker by creating an _interface VPC endpoint_. Interface endpoints
are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), which you
can use to privately access AWS IoT TwinMaker APIs without an internet gateway, network address
translation (NAT) device, VPN connection, or AWS Direct Connect connection. AWS IoT TwinMaker supports both IPv4 and IPv6 (dual-stack) through its interface endpoints.
Instances in your VPC don't need public IP addresses to communicate
with AWS IoT TwinMaker APIs. Traffic between your VPC and AWS IoT TwinMaker doesn't leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for AWS IoT TwinMaker VPC

endpoints

Before you set up an interface VPC endpoint for AWS IoT TwinMaker, review [Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

AWS IoT TwinMaker supports making calls to all of its API actions from your VPC.

- For data plane API operations, use the following endpoint:

```
data.iottwinmaker.`region`.amazonaws.com
```

The data plane API operations include the following:

    + [GetPropertyValue](../apireference/API_GetPropertyValue.md "../apireference/API_GetPropertyValue.md")
    + [GetPropertyValueHistory](../apireference/API_GetPropertyValueHistory.md "../apireference/API_GetPropertyValueHistory.md")
    + [BatchPutPropertyValues](../apireference/API_BatchPutPropertyValues.md "../apireference/API_BatchPutPropertyValues.md")

- For the control plane API operations, use the following endpoint:

```
api.iottwinmaker.`region`.amazonaws.com
```

The supported control plane API operations include the following:

    + [CreateComponentType](../apireference/API_CreateComponentType.md "../apireference/API_CreateComponentType.md")
    + [CreateEntity](../apireference/API_CreateEntity.md "../apireference/API_CreateEntity.md")
    + [CreateScene](../apireference/API_CreateScene.md "../apireference/API_CreateScene.md")
    + [CreateWorkspace](../apireference/API_CreateWorkspace.md "../apireference/API_CreateWorkspace.md")
    + [DeleteComponentType](../apireference/API_DeleteComponentType.md "../apireference/API_DeleteComponentType.md")
    + [DeleteEntity](../apireference/API_DeleteEntity.md "../apireference/API_DeleteEntity.md")
    + [DeleteScene](../apireference/API_DeleteScene.md "../apireference/API_DeleteScene.md")
    + [DeleteWorkspace](../apireference/API_DeleteWorkspace.md "../apireference/API_DeleteWorkspace.md")
    + [GetComponentType](../apireference/API_GetComponentType.md "../apireference/API_GetComponentType.md")
    + [GetEntity](../apireference/API_GetEntity.md "../apireference/API_GetEntity.md")
    + [GetScene](../apireference/API_GetScene.md "../apireference/API_GetScene.md")
    + [GetWorkspace](../apireference/API_GetWorkspace.md "../apireference/API_GetWorkspace.md")
    + [ListComponentTypes](../apireference/API_ListComponentTypes.md "../apireference/API_ListComponentTypes.md")
    + [ListComponentTypes](../apireference/API_ListComponentTypes.md "../apireference/API_ListComponentTypes.md")
    + [ListEntities](../apireference/API_ListEntities.md "../apireference/API_ListEntities.md")
    + [ListScenes](../apireference/API_ListScenes.md "../apireference/API_ListScenes.md")
    + [ListTagsForResource](../apireference/API_ListTagsForResource.md "../apireference/API_ListTagsForResource.md")
    + [ListWorkspaces](../apireference/API_ListWorkspaces.md "../apireference/API_ListWorkspaces.md")
    + [TagResource](../apireference/API_TagResource.md "../apireference/API_TagResource.md")
    + [UntagResource](../apireference/API_UntagResource.md "../apireference/API_UntagResource.md")
    + [UpdateComponentType](../apireference/API_UpdateComponentType.md "../apireference/API_UpdateComponentType.md")
    + [UpdateEntity](../apireference/API_UpdateEntity.md "../apireference/API_UpdateEntity.md")
    + [UpdateScene](../apireference/API_UpdateScene.md "../apireference/API_UpdateScene.md")
    + [UpdateWorkspace](../apireference/API_UpdateWorkspace.md "../apireference/API_UpdateWorkspace.md")

## Creating an interface VPC endpoint for

AWS IoT TwinMaker

You can create a VPC endpoint for the AWS IoT TwinMaker service by using either the Amazon VPC
console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for AWS IoT TwinMaker that uses the following service name.

- For data plane API operations, use the following service name:

```
com.amazonaws.`region`.iottwinmaker.data
```

- For control plane API operations, use the following service name:

```
com.amazonaws.`region`.iottwinmaker.api
```

If you enable private DNS for the endpoint, you can make API requests to AWS IoT TwinMaker by
using its default DNS name for the Region, for example,
`iottwinmaker.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

AWS IoT TwinMaker PrivateLink is supported in the following regions:

- **us-east-1**

The ControlPlane service is supported in the following availability zones: `use1-az1`, `use1-az2`, and `use1-az6`.

The DataPlane service is supported in the
following availability zones: `use1-az1`, `use1-az2`, and `use1-az4`.

- **us-west-2**

The ControlPlane and DataPlane services are supported in the following
availability zones: `usw2-az1`, `usw2-az2`, and
`usw2-az3`.

- **eu-west-1**
- **eu-central-1**
- **ap-southeast-1**
- **ap-southeast-2**

For more information on availability zones, see [Availability Zone IDs for your AWS resources - AWS Resource Access Manager](../../../ram/latest/userguide/working-with-az-ids.md "../../../ram/latest/userguide/working-with-az-ids.md").

## Accessing AWS IoT TwinMaker through an interface VPC

endpoint

When you create an interface endpoint, AWS IoT TwinMaker generates endpoint-specific DNS hostnames
that you can use to communicate with AWS IoT TwinMaker. The private DNS option is enabled by
default. For more information, see [Using private hosted
zones](../../../vpc/latest/userguide/vpc-dns.md#vpc-private-hosted-zones "../../../vpc/latest/userguide/vpc-dns.md#vpc-private-hosted-zones") in the _Amazon VPC User Guide_.

If you enable private DNS for the endpoint, you can make API requests to AWS IoT TwinMaker
through one of the following VPC endpoints.

- For the data plane API operations, use the following endpoint. Replace `region` with your AWS
  Region.

```
data.iottwinmaker.`region`.amazonaws.com
```

- For the control plane API operations, use the following endpoint. Replace `region` with your AWS
  Region.

```
api.iottwinmaker.`region`.amazonaws.com
```

If you disable private DNS for the endpoint, you must do the following to access AWS IoT TwinMaker
through the endpoint:

- Specify the VPC endpoint URL in API requests.
  - For the data plane API operations, use the following endpoint URL.
    Replace `vpc-endpoint-id` and `region`
    with your VPC endpoint ID and
    Region.

  ```
  `vpc-endpoint-id`.data.iottwinmaker.`region`.vpce.amazonaws.com
  ```

  - For the control plane API operations, use the following endpoint URL.
    Replace `vpc-endpoint-id` and `region`
    with your VPC endpoint ID and
    Region.

  ```
  `vpc-endpoint-id`.api.iottwinmaker.`region`.vpce.amazonaws.com
  ```

- Disable host prefix injection. The AWS CLI and AWS SDKs prepend the service
  endpoint with various host prefixes when you call each API operation. This
  causes the AWS CLI and AWS SDKs to produce invalid URLs for AWS IoT TwinMaker when you
  specify a VPC endpoint.

###### Important

You can't disable host prefix injection in AWS CLI or AWS Tools for PowerShell. This
means that if you've disabled private DNS, you won't be able to use AWS CLI
or AWS Tools for PowerShell to access AWS IoT TwinMaker through the VPC endpoint. If
you want to use these tools to access AWS IoT TwinMaker through the endpoint, enable
private DNS.

For more information about how to disable host prefix injection in the AWS
SDKs, see the following documentation sections for each SDK:

    + [AWS SDK for C++](https://sdk.amazonaws.com/cpp/api/LATEST/struct_aws_1_1_client_1_1_client_configuration.html#a3579c1a2f2e1c9d54e99c59d27643499 "https://sdk.amazonaws.com/cpp/api/LATEST/struct_aws_1_1_client_1_1_client_configuration.html#a3579c1a2f2e1c9d54e99c59d27643499")
    + [AWS SDK for Go](../../../sdk-for-go/api/aws.md#Config.WithDisableEndpointHostPrefix "../../../sdk-for-go/api/aws.md#Config.WithDisableEndpointHostPrefix")
    + [AWS SDK for Go
     v2](../../../sdk-for-go/v2/developer-guide/configure-endpoints.md#migration "../../../sdk-for-go/v2/developer-guide/configure-endpoints.md#migration")
    + [AWS SDK for Java](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.md#setDisableHostPrefixInjection-boolean- "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.md#setDisableHostPrefixInjection-boolean-")
    + [AWS SDK for Java 2.x](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/config/SdkAdvancedClientOption.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/config/SdkAdvancedClientOption.html")
    + [AWS SDK for JavaScript](../../../AWSJavaScriptSDK/latest/AWS/Config.md#hostPrefixEnabled-property "../../../AWSJavaScriptSDK/latest/AWS/Config.md#hostPrefixEnabled-property")
    + [AWS SDK for .NET](../../../sdkfornet/v4/apidocs/items/Runtime/TClientConfig.md "../../../sdkfornet/v4/apidocs/items/Runtime/TClientConfig.md")
    + [AWS SDK for PHP](../../../aws-sdk-php/v3/api/class-Aws.md#___construct "../../../aws-sdk-php/v3/api/class-Aws.md#___construct")
    + [AWS SDK for Python (Boto3)](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html "https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html")
    + [AWS SDK for Ruby](../../../sdk-for-ruby/v3/api/Aws/IoTSiteWise/Client.md#initialize-instance_method "../../../sdk-for-ruby/v3/api/Aws/IoTSiteWise/Client.md#initialize-instance_method")

For more information, see [Accessing a
service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for AWS IoT TwinMaker

You can attach an endpoint policy to your VPC endpoint that controls access to
AWS IoT TwinMaker. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for AWS IoT TwinMaker actions

The following is an example of an endpoint policy for AWS IoT TwinMaker. When attached to an
endpoint, this policy grants access to the listed AWS IoT TwinMaker actions for the IAM user
`iottwinmakeradmin` in the AWS account `123456789012` on
all resources.

```
{
   "Statement":[
      {
        "Principal": {
            "AWS": "arn:aws:iam::123456789012:user/role"
                },
         "Resource": "*",
         "Effect":"Allow",
         "Action":[
            "`iottwinmaker`:`CreateEntity`",
            "`iottwinmaker`:`GetScene`",
            "`iottwinmaker`:`ListEntities`"
         ]
        }
    ]
}
```
