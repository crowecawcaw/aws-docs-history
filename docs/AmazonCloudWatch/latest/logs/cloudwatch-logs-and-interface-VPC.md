# Using CloudWatch Logs with interface VPC

endpoints

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private
connection between your VPC and CloudWatch Logs. You can use this connection to send logs to CloudWatch Logs
without sending them through the internet. CloudWatch Logs supports IPv4 VPC endpoints in all Regions, and supports IPv6 endpoints in
all Regions.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network that you define. With a VPC, you
have control over your network settings, such the IP address range, subnets, route tables, and network gateways. To connect
your VPC to CloudWatch Logs, you define an _interface VPC endpoint_ for CloudWatch Logs. This type of endpoint enables you to connect your VPC to AWS
services. The endpoint provides reliable, scalable connectivity to CloudWatch Logs without requiring an internet gateway, network
address translation (NAT) instance, or VPN connection. For more information, see [What is Amazon VPC](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in the
_Amazon VPC User Guide_.

Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that
enables private communication between AWS services using an elastic network interface with
private IP addresses. For more information, see [New – AWS PrivateLink for AWS Services](https://aws.amazon.com/blogs/aws/new-aws-privatelink-endpoints-kinesis-ec2-systems-manager-and-elb-apis-in-your-vpc/ "https://aws.amazon.com/blogs/aws/new-aws-privatelink-endpoints-kinesis-ec2-systems-manager-and-elb-apis-in-your-vpc/").

The following steps are for users of Amazon VPC. For more information, see [Getting Started](../../../vpc/latest/userguide/GetStarted.md "../../../vpc/latest/userguide/GetStarted.md") in the
_Amazon VPC User Guide_.

## Availability

CloudWatch Logs currently supports VPC endpoints in all AWS Regions, including the AWS GovCloud (US) Regions.

## Creating a VPC endpoint for CloudWatch Logs

To start using CloudWatch Logs with your VPC, create an interface VPC endpoint for CloudWatch Logs.
The
service to choose is **com.amazonaws.`Region`.logs**. To connect with a FIPS endpoint, the service to choose is `com.amazonaws.Region.logs-fips`.
You do not need to change any settings for CloudWatch Logs. For
more information, see [Creating an
Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint.html "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint.html") in the _Amazon VPC User Guide_.

Some CloudWatch Logs APIs, such as StartLiveTail and GetLogObject, are hosted under a different endpoint and VPC endpoint: `stream-logs.Region.amazonaws.com`.
To create an interface VPC endpoint for these APIs, the service to choose is **com.amazonaws.`Region`.stream-logs**. To connect with a FIPS endpoint, the service to choose is `com.amazonaws.Region.stream-logs-fips`.

## Testing the connection between your VPC and

CloudWatch Logs

After you create the endpoint, you can test the connection.

###### To test the connection between your VPC and your CloudWatch Logs endpoint

1. Connect to an Amazon EC2 instance that resides in your VPC. For information about connecting, see
   [Connect to Your Linux Instance](../../../AWSEC2/latest/UserGuide/vpce-interface.md#create-interface-endpoint.html "../../../AWSEC2/latest/UserGuide/vpce-interface.md#create-interface-endpoint.html") or
   [Connecting to Your Windows Instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the Amazon EC2 documentation.
2. From the instance, use the AWS CLI to create a log entry in one of your existing log groups.

First, create a JSON file with a log event. The timestamp must be specified as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

```
[
  {
    "timestamp": 1533854071310,
    "message": "VPC Connection Test"
  }
]
```

Then, use the `put-log-events` command to create the log entry:

```
aws logs put-log-events --log-group-name `LogGroupName` --log-stream-name `LogStreamName` --log-events file://`JSONFileName`
```

If the response to the command includes `nextSequenceToken`, the command has succeeded and your VPC endpoint is working.

## Controlling access to your CloudWatch Logs VPC

endpoint

A VPC endpoint policy is an IAM resource policy that you attach to an endpoint when
you create or modify the endpoint. If you don't attach a policy when you create an
endpoint, we attach a default policy for you that allows full access to the service. An
endpoint policy doesn't override or replace IAM policies or service-specific
policies. It's a separate policy for controlling access from the endpoint to the
specified service.

Endpoint policies must be written in JSON format.

For more information, see [Controlling Access to Services with
VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

The following is an example of an endpoint policy for CloudWatch Logs. This policy enables users connecting to CloudWatch Logs through
the VPC to create log streams and send logs to CloudWatch Logs, and
prevents them from performing other CloudWatch Logs actions.

```
{
  "Statement": [
    {
      "Sid": "PutOnly",
      "Principal": "*",
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}

```

###### To modify the VPC endpoint policy for CloudWatch Logs

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. If you have not already created the endpoint for CloudWatch Logs, choose **Create Endpoint**. Then select
   **com.amazonaws.`Region`.logs** and choose **Create endpoint**.
4. Select the **com.amazonaws.`Region`.logs** endpoint, and choose the **Policy** tab in the lower half of the screen.
5. Choose **Edit Policy** and make the changes to the policy.

## Support for VPC context keys

CloudWatch Logs supports the `aws:SourceVpc` and `aws:SourceVpce` context
keys that can limit access to specific VPCs or specific VPC endpoints. These keys work
only when the user is using VPC endpoints. For more information, see [Keys Available for Some Services](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-service-available "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-service-available") in the
_IAM User Guide_.
