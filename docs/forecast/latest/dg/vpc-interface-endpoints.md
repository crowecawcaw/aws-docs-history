Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Forecast and interface VPC endpoints

(AWS PrivateLink)

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can
establish a private connection between your VPC and Amazon Forecast. This connection allows Amazon Forecast to communicate with your resources on your VPC
without going through the public internet.

Amazon VPC is an AWS service that you use to launch AWS resources in a virtual private cloud (VPC) or virtual network that
you define. With a VPC, you have control over your network settings, such the IP address
range, subnets, route tables, and network gateways. With VPC endpoints, the AWS network
handles the routing between your VPC and AWS services.

To connect your VPC to Amazon Forecast, you define an interface VPC endpoint for Amazon Forecast. An
interface endpoint is an elastic network interface with a private IP address that serves as
an entry point for traffic destined to a supported AWS service. The endpoint provides
reliable, scalable connectivity to Amazon Forecast—and it doesn't require an internet
gateway, a network address translation (NAT) instance, or a VPN connection. For more
information, see [What is Amazon VPC](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in the
_Amazon VPC User Guide_.

Interface VPC endpoints are enabled by AWS PrivateLink. This AWS technology enables
private communication between AWS services by using an elastic network interface with
private IP addresses.

###### Note

All Amazon Forecast Federal Information Processing Standard (FIPS) endpoints are supported
by AWS PrivateLink.

## Considerations for Forecast VPC

endpoints

Before you set up an interface VPC endpoint for Forecast, ensure that you
review [Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

Forecast supports making calls to
all of its API actions from your VPC.

## Creating an interface VPC endpoint for

Forecast

You can create a VPC endpoint for the Forecast service with either the Amazon VPC console or
the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

You can create two types of VPC endpoints to use with Amazon Forecast:

- A VPC endpoint to use with Amazon Forecast operations. For most users, this is the most suitable
  type of VPC endpoint.
  - com.amazonaws.`region`.forecast
  - com.amazonaws.`region`.forecastquery

- A VPC endpoint for Amazon Forecast operations with endpoints that comply with the
  Federal Information Processing Standard (FIPS) Publication 140-2 US government
  standard (available in select regions, see [Amazon Forecast endpoints and quotas](../../../general/latest/gr/forecast.md#forecast_region "../../../general/latest/gr/forecast.md#forecast_region")).
  - com.amazonaws.`region`.forecast-fips
  - com.amazonaws.`region`.forecastquery-fips

If you enable private DNS for the endpoint, you can make API requests to Forecast using its
default DNS name for the Region, for example,
`forecast.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

Forecast

You can attach an endpoint policy to your VPC endpoint that controls access to
Forecast. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy allowing all Forecast actions and passRole

actions

When attached to an endpoint, this policy grants access to all Forecast actions and
passRole actions.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": [
                "`forecast`:*",
                "`iam`:`PassRole`"
            ],
            "Resource": "*"
        }
    ]
}
```

###### Example: VPC endpoint policy allowing Forecast ListDatasets actions

When attached to an endpoint, this policy grants access to the listed Forecast
ListDatasets actions.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": [
                "`forecast`:`ListDatasets`"
            ],
            "Resource": "*"
        }
    ]
}
```
