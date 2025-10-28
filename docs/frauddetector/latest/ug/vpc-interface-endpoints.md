Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Amazon Fraud Detector and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and Amazon Fraud Detector by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access Amazon Fraud Detector APIs without an internet gateway, NAT device, VPN
connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to communicate with Amazon Fraud Detector APIs. Traffic between your VPC and Amazon Fraud Detector
does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for Amazon Fraud Detector VPC

endpoints

Before you set up an interface VPC endpoint for Amazon Fraud Detector, ensure that you
review [Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

Amazon Fraud Detector supports making calls to
all of its API actions from your VPC.

VPC endpoint policies are supported for Amazon Fraud Detector. By default, full access to
Amazon Fraud Detector is allowed through the endpoint. For more information, see [Controlling access to services with
VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

## Creating an interface VPC endpoint for

Amazon Fraud Detector

You can create a VPC endpoint for the Amazon Fraud Detector service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for Amazon Fraud Detector using the following service name:

- com.amazonaws.`region`.frauddetector

If you enable private DNS for the endpoint, you can make API requests to Amazon Fraud Detector using
its default DNS name for the Region, for example,
`frauddetector.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for Amazon Fraud Detector

You can create a policy for interface VPC endpoints for Amazon Fraud Detector to specify the following:

- The principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

For more information, see [Controlling Access to Services with VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the
_Amazon VPC User Guide_.

The following example VPC endpoint policy specifies that all users who have access to the VPC interface endpoint are allowed to access the Amazon Fraud Detector detector named `my_detector`.

```
{
  "Statement": [
      {
          "Action": "frauddetector:*Detector",
          "Effect": "Allow",
          "Resource": "arn:aws:frauddetector:us-east-1:123456789012:detector/my_detector",
          "Principal": "*"
      }
  ]
}

```

In this example, the following are denied:

- Other Amazon Fraud Detector API actions
- Invoking Amazon Fraud Detector `GetEventPrediction` API

###### Note

In this example, users can still take other Amazon Fraud Detector API actions from outside the VPC. For information about how to restrict API calls to those from within the VPC, see [Amazon Fraud Detector
identity-based policies](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies").
