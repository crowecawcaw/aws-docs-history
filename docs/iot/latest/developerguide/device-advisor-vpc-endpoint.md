

# Device Advisor VPC endpoints (AWS PrivateLink)
<a name="device-advisor-vpc-endpoint"></a>

You can establish a private connection between your VPC and the AWS IoT Core Device Advisor test endpoint (data plane) by creating an *interface VPC endpoint*. You can use this endpoint to validate AWS IoT devices for reliable and secure connectivity with AWS IoT Core before deploying devices to production. Device Advisor's pre-built tests helps you validate your device software against best practices for usage of [TLS](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html), [MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html), [Device Shadow](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html), and [AWS IoT Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html). 

[AWS PrivateLink](http://aws.amazon.com/privatelink) powers the interface endpoints used with your IoT devices. This service helps you access the AWS IoT Core Device Advisor test endpoint privately without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC that send TCP and MQTT packets don't need public IP addresses to communicate with AWS IoT Core Device Advisor test endpoints. Traffic between your VPC and AWS IoT Core Device Advisor doesn't leave AWS Cloud. Any TLS and MQTT communication between IoT devices and Device Advisor test cases stay within the resources in your AWS account. 

Each interface endpoint is represented by one or more [elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets.

To learn more about using interface VPC endpoints, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

## Considerations for AWS IoT Core Device Advisor VPC endpoints
<a name="vpc-considerations"></a>

Review the [ interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide* before setting up interface VPC endpoints. Consider the following before you continue: 
+ AWS IoT Core Device Advisor currently supports making calls to Device Advisor test endpoint (data plane) from your VPC. A message broker uses data plane communications to send and receive data. It does this with the help of TLS and MQTT packets. VPC endpoints for AWS IoT Core Device Advisor connect your AWS IoT device to Device Advisor test endpoints. [Control plane API actions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/index.html) aren't used by this VPC endpoint. To create or run a test suite or other control plane APIs, use the console, an AWS SDK, or AWS Command Line Interface over the public internet. 
+ The following AWS Regions support VPC endpoints for AWS IoT Core Device Advisor:
  + US East (N. Virginia)
  + US West (Oregon)
  + Asia Pacific (Tokyo)
  + Europe (Ireland)
+  Device Advisor supports MQTT with X.509 client certificates and RSA server certificates. 
+ [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) aren't supported at this time. 
+ Check VPC endpoint [prerequisites ](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#prerequisites-interface-endpoints) for instructions on how to [create resources ](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) that connect VPC endpoints. You must create a VPC and private subnets to use AWS IoT Core Device Advisor VPC endpoints. 
+ There are quotas on your AWS PrivateLink resources. For more information, see [AWS PrivateLink quotas](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-limits-endpoints.html). 
+ VPC endpoints support only IPv4 traffic. 

## Create an interface VPC endpoint for AWS IoT Core Device Advisor
<a name="vpc-interface"></a>

To get started with VPC endpoints, [ create an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html). Next, select AWS IoT Core Device Advisor as the AWS service. If you are using the AWS CLI, call [describe-vpc-endpoint-services](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoint-services.html) to confirm that AWS IoT Core Device Advisor is present in an Availability Zone in your AWS Region. Confirm that the security group attached to the endpoint allows [TCP protocol communication](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html) for MQTT and TLS traffic. For example, in the US East (N. Virginia) Region, use the following command: 

```
aws ec2 describe-vpc-endpoint-services --service-name com.amazonaws.us-east-1.deviceadvisor.iot
```

You can create a VPC endpoint for AWS IoT Core using the following service name: 
+ com.amazonaws.*region*.deviceadvisor.iot

By default, private DNS is turned on for the endpoint. This ensures that use of the default test endpoint stays within your private subnets. To get your account or device level endpoint, use the console, AWS CLI or an AWS SDK. For example, if you run [ get-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/get-endpoint.html) within a public subnet or on the public internet, you can get your endpoint and use it to connect to Device Advisor. For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*. 

To connect MQTT clients to the VPC endpoint interfaces, the AWS PrivateLink service creates DNS records in a private hosted zone attached to your VPC. These DNS records direct the AWS IoT device’s requests to the VPC endpoint. 

## Controlling access to AWS IoT Core Device Advisor over VPC endpoints
<a name="vpc-controlling-access"></a>

You can restrict device access to AWS IoT Core Device Advisor and allow access only through VPC endpoints by using VPC [condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html). AWS IoT Core supports the following VPC related context keys: 
+  [SourceVpc](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcevpc) 
+  [SourceVpce](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcevpce) 
+  [VPCSourcelp](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-vpcsourceip) 

**Note**  
 AWS IoT Core Device Advisor doesn't support [ VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies) at this time. 

The following policy grants permission to connect to AWS IoT Core Device Advisor using a client ID that matches the thing name. It also publishes to any topic prefixed by the thing name. The policy is conditional on the device connecting to a VPC endpoint with a particular VPC endpoint ID. This policy denies connection attempts to your public AWS IoT Core Device Advisor test endpoint. 

****  

```
{
"Version":"2012-10-17",		 	 	 
    "Statement": [
        {
"Effect": "Allow",
            "Action": [
                "iot:Connect"
            ],
            "Resource": [
                "arn:aws:iot:us-east-1:123456789012:client/${iot:Connection.Thing.ThingName}"
            ],
            "Condition": {
"StringEquals": {
"aws:SourceVpce": "vpce-1a2b3c4d"
            }
        }
            
        },
        {
"Effect": "Allow",
            "Action": [
                "iot:Publish"
            ],
            "Resource": [
                "arn:aws:iot:us-east-1:123456789012:topic/${iot:Connection.Thing.ThingName}/*"
            ]
        }
    ]
}
```