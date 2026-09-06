

# Using AWS services
<a name="using-services"></a>

## AWS Identity and Access Management
<a name="aws-identity-and-access-management"></a>

 Using an IAM role to access AWS services, and being specific in the IAM policy attached to it, is a best practice that provides only the users in WorkSpaces Applications sessions have access without managing additional credentials. Follow the [*best practices for using IAM Roles with WorkSpaces Applications*](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html#best-practices-for-using-iam-role-with-streaming-instances). 

 Create [*IAM policies to protect Amazon S3 buckets*](https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy.html) that are created to persist user data in both home folders and application settings persistence. This [*prevents non-WorkSpaces Applications administrators*](https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy.html#s3-iam-policy-restricted-access) from access. 

## VPC endpoints
<a name="vpc-endpoints-1"></a>

 A VPC endpoint enables private connections between your VPC and supported AWS services and VPC endpoint services powered by AWS PrivateLink. AWS PrivateLink is a technology that enables you to privately access services by using private IP addresses. Traffic between your VPC and the other service does not leave the Amazon network. If public internet access is required only for AWS services, VPC endpoints remove the requirement for NAT gateways and internet gateways altogether. 

 In environments where automation routines or developers require making API calls for WorkSpaces Applications, [*create an interface VPC endpoint for WorkSpaces Applications API operations*](https://docs.aws.amazon.com/appstream2/latest/developerguide/access-api-cli-through-interface-vpc-endpoint.html). For example, if there are EC2 instances in private subnets without public internet access, a VPC endpoint for WorkSpaces Applications API can be used to call AppStream 2.0 API operations such as [*CreateStreamingURL*](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html). The following diagram shows an example setup where WorkSpaces Applications API and streaming VPC endpoints are consumed by Lambda functions and EC2 instances. 

![A reference architecture diagram for VPC endpoint](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/vpc-endpoint.jpeg)


 *VPC endpoint* 

 The streaming VPC endpoint allows you to stream sessions through a VPC endpoint. The streaming interface endpoint maintains the streaming traffic within your VPC. Streaming traffic includes pixel, USB, user input, audio, clipboard, file upload and download, and printer traffic. To use the VPC endpoint, the VPC endpoint setting must be enabled at the WorkSpaces Applications stack. This serves as an alternative to streaming user sessions over the public internet from locations that have limited internet access and would benefit from accessing through a Direct Connect instance. Streaming user sessions through a VPC endpoint require the following: 
+  The Security Groups that are associated with the interface endpoint must allow inbound access to port `443` (TCP) and ports `1400–1499` (TCP) from the IP address range from which your users connect. 
+  The Network Access Control List for the subnets must allow outbound traffic from ephemeral network ports `1024-65535` (TCP) to the IP address range from which your users connect. 
+  Internet connectivity is required to authenticate users and deliver the web assets that WorkSpaces Applications requires to function. 

 To learn more about restricting traffic to AWS services with WorkSpaces Applications, see the administration guide for [*creating and streaming from VPC endpoints*](https://docs.aws.amazon.com/appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.html). 

 When full public internet access is required, it’s a best practice to disable Internet Explorer Enhanced Security Configuration (ESC) on the Image Builder. For more information, see the WorkSpaces Applications administration guide to [*disable Internet Explorer enhanced security configuration*](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets.html#customize-fleets-disable-ie-esc). 

## Configuring the Instance Metadata Service (IMDS) on your instances
<a name="configuring-imds"></a>

This topic describes the Instance Metadata Service (IMDS).

*Instance metadata* is data that's related to an Amazon Elastic Compute Cloud (Amazon EC2) instance that applications can use to configure or manage the running instance. The instance metadata service (IMDS) is an on-instance component that code on the instance uses to securely access instance metadata. For more information, see [Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon EC2 User Guide*.

Code can access instance metadata from a running instance using one of two methods: Instance Metadata Service Version 1 (IMDSv1) or Instance Metadata Service Version 2 (IMDSv2). IMDSv2 uses session-oriented requests and mitigates several types of vulnerabilities that could be used to try to access the IMDS. For information about these two methods, see [Configuring the instance metadata service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the *Amazon EC2 User Guide*.

### Resource support for IMDS
<a name="imds-resource-support"></a>

Always-On, On-Demand, Single-Session, and Multi-Session Fleets, and all Image Builders support both IMDSv1 and IMDSv2 when running WorkSpaces Applications images with the agent version or managed image update released on or after January 16, 2024.

Elastic Fleets and AppBlock Builders instances also support both IMDSv1 and IMDSv2.

### Example of IMDS attribute settings
<a name="imds-examples"></a>

Below are two examples of choosing the IMDS method:

#### Java v2 SDK example
<a name="java-sdk-example"></a>

Below example request disable IMDSv1 using `disableIMDSV1` attributes

```
CreateFleetRequest request = CreateFleetRequest.builder()
 .name("TestFleet")
 .imageArn("arn:aws:appstream:us-east-1::image/TestImage")
 .instanceType("stream.standard.large")
 .fleetType(FleetType.ALWAYS_ON)
 .computeCapacity(ComputeCapacity.builder()
 .desiredInstances(5)
 .build())
 .description("Test fleet description")
 .displayName("Test Fleet Display Name")
 .enableDefaultInternetAccess(true)
 .maxUserDurationInSeconds(3600)
 .disconnectTimeoutInSeconds(900)
 .idleDisconnectTimeoutInSeconds(600)
 .iamRoleArn("arn:aws:iam::123456789012:role/TestRole")
 .streamView(StreamView.APP)
 .platform(PlatformType.WINDOWS)
 .maxConcurrentSessions(10)
 .maxSessionsPerInstance(2)
 .tags(tags)
 .disableIMDSV1(true)
 .build();
```

Set **disableIMDSV1** to true to disable IMDSv1 and enforce IMDSv2.

Set **disableIMDSV1** to false to enable both IMDSv1 and IMDSv2.

#### CLI Example
<a name="cli-example"></a>

Below example request disable IMDSv1 using `--disable-imdsv1` attributes

```
aws appstream create-fleet --name test-fleet --image-arn "arn:aws:appstream:us-east-1::image/test-image" --disable-imdsv1 --instance-type stream.standard.small --compute-capacity DesiredInstances=2 --max-user-duration-in-seconds 57600 --disconnect-timeout-in-seconds 57600 --region us-east-1
```

Set `--disable-imdsv1` to true to disable IMDSv1 and enforce IMDSv2.

Set `--no-disable-imdsv1` to false to enable both IMDSv1 and IMDSv2.