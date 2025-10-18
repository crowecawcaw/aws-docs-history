# Using CloudWatch, CloudWatch Synthetics, and CloudWatch Network
 Monitoring with interface VPC endpoints

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private
 connection between your VPC, CloudWatch, CloudWatch Synthetics, and CloudWatch Network Monitoring features. 
 You can use these connections to enable these services to communicate with resources in 
 your VPC without going through the public internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network
 that you define. With a VPC, you have control over your network settings, such the IP
 address range, subnets, route tables, and network gateways. To connect your VPC to CloudWatch
 services, you define an *interface VPC endpoint* for your
 VPC. The endpoint provides reliable, scalable connectivity to CloudWatch and supported CloudWatch
 services without requiring an internet gateway, network address translation (NAT)
 instance, or VPN connection. For more information, see [What is
 Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/ "https://docs.aws.amazon.com/vpc/latest/userguide/") in the *Amazon VPC User Guide*.

Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that enables
 private communication between AWS services using an elastic network interface with private
 IP addresses. For more information, see the following blog post: [New – AWS PrivateLink for AWS Services](https://aws.amazon.com/blogs/aws/new-aws-privatelink-endpoints-kinesis-ec2-systems-manager-and-elb-apis-in-your-vpc/ "https://aws.amazon.com/blogs/aws/new-aws-privatelink-endpoints-kinesis-ec2-systems-manager-and-elb-apis-in-your-vpc/")

The following steps are for users of Amazon VPC. For more information, see [Getting Started](https://docs.aws.amazon.com/vpc/latest/userguide/GetStarted.html "https://docs.aws.amazon.com/vpc/latest/userguide/GetStarted.html") in the
 *Amazon VPC User Guide*.


## CloudWatch VPC endpoints


CloudWatch currently supports VPC endpoints, including IPv6-only and dual stack enabled endpoints, in all AWS Regions, including the AWS GovCloud (US) Regions. For information on endpoints URL, see [CloudWatch endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cw_region.html "https://docs.aws.amazon.com/general/latest/gr/cw_region.html") .


### Creating a VPC endpoint for CloudWatch


To start using CloudWatch with your VPC, create an interface VPC endpoint for CloudWatch. The
 service name to choose is
 `com.amazonaws.`region`.monitoring`. For
 more information, see [Creating
 an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint.html "https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint.html") in the
 *Amazon VPC User Guide*.


You do not need to change the settings for CloudWatch. CloudWatch calls
 other AWS services using either public endpoints or private interface VPC endpoints, whichever are in use. 
 For example, if you create an interface VPC endpoint for CloudWatch, and you already have metrics flowing
 to CloudWatch from resources located on your VPC, these metrics begin flowing through the interface VPC endpoint by default.


### Controlling access to your CloudWatch VPC
 endpoint


A VPC endpoint policy is an IAM resource policy that you attach to an endpoint when you create or modify
 the endpoint. If you don't attach a policy when you create an endpoint, Amazon VPC 
 attaches a default policy for you that allows full access to the service. An endpoint policy doesn't
 override or replace user policies or service-specific policies. It's a separate policy for
 controlling access from the endpoint to the specified service. 


Endpoint policies must be written in JSON format. 


For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html") 
 in the *Amazon VPC User Guide*.


The following is an example of an endpoint policy for CloudWatch. This policy allows users
 connecting to CloudWatch through the VPC to send metric data to CloudWatch and prevents them
 from performing other CloudWatch actions.



```
{
  "Statement": [
    {
      "Sid": "PutOnly",
      "Principal": "*",
      "Action": [
        "cloudwatch:PutMetricData"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

###### To edit the VPC endpoint policy for CloudWatch

1. Open the Amazon VPC console at
 [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. If you have not already created the endpoint for CloudWatch, choose **Create
 endpoint**. Select
 **com.amazonaws.`region`.monitoring**,
 and then choose **Create endpoint**.
4. Select the **com.amazonaws.`region`.monitoring**
 endpoint, and then choose the **Policy** tab.
5. Choose **Edit policy**, and then make your changes.

## CloudWatch Synthetics VPC endpoint


CloudWatch Synthetics currently supports VPC endpoints in the following AWS Regions:



* US East (Ohio)
* US East (N. Virginia)
* US West (N. California)
* US West (Oregon)
* Asia Pacific (Hong Kong)
* Asia Pacific (Mumbai)
* Asia Pacific (Seoul)
* Asia Pacific (Singapore)
* Asia Pacific (Sydney)
* Asia Pacific (Tokyo)
* Canada (Central)
* Europe (Frankfurt)
* Europe (Ireland)
* Europe (London)
* Europe (Paris)
* South America (São Paulo)

### Creating a VPC endpoint for CloudWatch
 Synthetics


To start using CloudWatch Synthetics with your VPC, create an interface VPC endpoint for
 CloudWatch Synthetics. The service name to choose is
 `com.amazonaws.`region`.synthetics`.
 For more information, see [Creating
 an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint.html "https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint.html") in the
 *Amazon VPC User Guide*.


You do not need to change the settings for CloudWatch Synthetics. CloudWatch Synthetics
 communicates with other AWS services using either public endpoints or private
 interface VPC endpoints, whichever are in use. For example, if you create an
 interface VPC endpoint for CloudWatch Synthetics, and you already have an interface
 endpoint for Amazon S3, CloudWatch Synthetics begins communicating with Amazon S3 through the
 interface VPC endpoint by default.


### Controlling access to your CloudWatch
 Synthetics VPC endpoint


A VPC endpoint policy is an IAM resource policy that you attach to an endpoint when
 you create or modify the endpoint. If you don't attach a policy when you create an
 endpoint, we attach a default policy for you that allows full access to the service. An
 endpoint policy doesn't override or replace user policies or service-specific
 policies. It's a separate policy for controlling access from the endpoint to the
 specified service. 


Endpoint policies affect canaries that are managed privately by VPC. They are not needed for 
 canaries that run on private subnets.


Endpoint policies must be written in JSON format. 


For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html") 
 in the *Amazon VPC User Guide*.


The following is an example of an endpoint policy for CloudWatch Synthetics. 
 This policy enables users
 connecting to CloudWatch Synthetics through the VPC to view information about canaries and 
 their runs, but not to create, modify, or delete canaries.



```
{
    "Statement": [
        {
            "Action": [
                "synthetics:DescribeCanaries",
                "synthetics:GetCanaryRuns"
            ],
            "Effect": "Allow",
            "Resource": "*",
            "Principal": "*"
        }
    ]
}
```

###### To edit the VPC endpoint policy for CloudWatch Synthetics

1. Open the Amazon VPC console at
 [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. If you have not already created the endpoint for CloudWatch Synthetics, choose **Create
 endpoint**. Select
 **com.amazonaws.`region`.synthetics**
 and then choose **Create endpoint**.
4. Select the **com.amazonaws.`region`.synthetics**
 endpoint, and then choose the **Policy** tab.
5. Choose **Edit policy**, and then make your changes.

## CloudWatch Network Monitoring feature VPC endpoints


CloudWatch Network Monitoring includes the following features: Network Flow Monitor, Internet Monitor, and Network Synthetic Monitor. These features each support VPC endpoints in 
 the AWS Regions where the Network Monitoring feature is supported.


To see a list of supported Regions for each Network Monitoring feature, see the following topics:



* **Network Flow Monitor:** [Supported AWS Regions for Network Flow Monitor](CloudWatch-NetworkFlowMonitor-Regions.md "CloudWatch-NetworkFlowMonitor-Regions.md")
* **Internet Monitor:** [Supported AWS Regions for Internet Monitor](CloudWatch-InternetMonitor.md "CloudWatch-InternetMonitor.md")
* **Network Synthetic Monitor:** [Supported AWS Regions for Network Synthetic Monitor](nw-monitor-regions.md "nw-monitor-regions.md")

### Creating a VPC endpoint for a CloudWatch
 Network Monitoring feature


To start using CloudWatch Network Monitoring features with your VPC, create an interface VPC endpoint for
 the feature that you want to use. For Network Monitoring, the following service names are available:



* `com.amazonaws.`region`.networkflowmonitor`
* `com.amazonaws.`region`.networkflowmonitorreports`
* `com.amazonaws.`region`.internetmonitor`
* `com.amazonaws.`region`.internetmonitor-fips`
* `com.amazonaws.`region`.networkmonitor`

For more information, see [Creating
 an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint.html "https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint.html") in the *Amazon VPC User Guide*.


You don't need to change the settings for Network Monitoring services. Network Monitoring services
 communicate with other AWS services using either public endpoints or private
 interface VPC endpoints, whichever are being used. For example, if you create an
 interface VPC endpoint for a Network Monitoring service, and you already have metrics flowing to the
 service from resources located on your VPC, the metrics begin flowing through the interface VPC endpoint by default.


### Controlling access to your CloudWatch
 Network Monitoring feature VPC endpoints


A VPC endpoint policy is an IAM resource policy that you attach to an endpoint when you create or modify
 the endpoint. An endpoint policy doesn't
 override or replace user policies or service-specific policies. It's a separate policy for
 controlling access from the endpoint to the specified service. 


If you don't attach a policy when you create an endpoint, Amazon VPC attaches a default policy for you that allows full access and does not restrict access
 to a specific service. For additional security, you can attach a policy to the endpoint to specifically limit access to the feature. For example, for
 Internet Monitor, you could allow full access to just Internet Monitor by attaching the AWS managed policy that enables full access to the feature, [CloudWatchInternetMonitorFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchInternetMonitorFullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchInternetMonitorFullAccess.html").
 Or, you can further limit permissions to just specific actions for the endpoint.


For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html") 
 in the *Amazon VPC User Guide*.


The following is an example of an endpoint policy that you could create for Network Flow Monitor to limit actions for the endpoint. This policy allows requests to
 Network Flow Monitor through the VPC to use only the `Publish` action, which enables requests to publish metrics to Network Flow Monitor backend ingestion.



```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "networkflowmonitor:Publish",
            "Resource": "*"
        }
    ]
}
```

If you want to use a specific VPC endpoint policy with an interface VPC endpoint for
 a Network Monitoring feature, use steps similar to the following example for adding a policy for Network Flow Monitor.


###### To edit a VPC endpoint policy for Network Flow Monitor

1. Open the Amazon VPC console at
 [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. If you have not already created the endpoint for Internet Monitor, choose **Create endpoint**.
4. Select **com.amazonaws.`region`.networkflowmonitor**,
 and then choose **Create endpoint**.
5. Select the **com.amazonaws.`region`.networkflowmonitor**
 endpoint, and then choose the **Policy** tab.
6. Choose **Edit policy**, and then make your changes.
