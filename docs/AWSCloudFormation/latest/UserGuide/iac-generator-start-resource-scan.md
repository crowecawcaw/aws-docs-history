# Start a resource scan with
 CloudFormation IaC generator

Before you create a template from existing resources, you first must initiate a
 resource scan to discover your current resources and their relationships.

You can start a resource scan using one of the following options. For first-time users
 of IaC generator, we recommend the first option.


* Scan all resources (full scan) – Scans
 all existing resources in the current account and Region. This scanning process
 can take up to 10 minutes for 1,000 resources.
* Scan specific resources (partial scan) –
 Manually select which resource types to scan in the current account and Region.
 This option provides a faster and more focused scanning process, making it ideal
 for iterative template development.
After the scan completes, you can choose which resources and their related resources
 to include when generating your template. When using partial scanning, related resources
 will only be available during template generation if either:


* You specifically selected them before starting the scan, or
* They were required to discover your selected resource types.
For example, if you select `AWS::EKS::Nodegroup` without selecting
 `AWS::EKS::Cluster`, IaC generator automatically includes
 `AWS::EKS::Cluster` resources in the scan because discovering the node
 group requires discovering the cluster first. In all other cases, the scan will only
 include the resources you specifically select.

###### Note

Before you continue, confirm that you have the permissions required to work with
 IaC generator. For more information, see [IAM permissions required for scanning
 resources](generate-IaC.md#iac-generator-permissions "generate-IaC.md#iac-generator-permissions").

###### Topics

* [Start a resource scan
 (console)](#start-resource-scan-console "#start-resource-scan-console")
* [Start a resource scan (AWS CLI)](#start-resource-scan-cli "#start-resource-scan-cli")

## Start a resource scan
 (console)


###### To start a resource scan of all resource types (full scan)

1. Open the [IaC
 generator page](https://console.aws.amazon.com/cloudformation/home?#iac-generator "https://console.aws.amazon.com/cloudformation/home?#iac-generator") of the CloudFormation console.
2. On the navigation bar at the top of the screen, choose the AWS Region
 that contains the resources to scan.
3. From the **Scans** panel, choose **Start a new
 scan** and then choose **Scan all resources**.

###### To start a resource scan of specific resource types (partial scan)

1. Open the [IaC
 generator page](https://console.aws.amazon.com/cloudformation/home?#iac-generator "https://console.aws.amazon.com/cloudformation/home?#iac-generator") of the CloudFormation console.
2. On the navigation bar at the top of the screen, choose the AWS Region
 that contains the resources to scan.
3. From the **Scans** panel, choose **Start a new
 scan** and then choose **Scan specific
 resources**.
4. In the **Start partial scan** dialog box, select up to
 100 resource types, and then choose **Start scan**.

## Start a resource scan (AWS CLI)


###### To start a resource scan of all resource types (full scan)


Use the following [start-resource-scan](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/start-resource-scan.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/start-resource-scan.html") command. Replace
 `us-east-1` with the AWS Region that
 contains the resources to scan.



```
aws cloudformation start-resource-scan --region `us-east-1`
```

If successful, this command returns the ARN of the scan. Note the ARN in the
 `ResourceScanId` property. You need it to create your
 template.



```
{
    "ResourceScanId":
      "arn:aws:cloudformation:`region`:`account-id`:resourceScan/`0a699f15-489c-43ca-a3ef-3e6ecfa5da60`"
}
```

###### To start a resource scan of specific resource types (partial scan)

1. Use the following [cat](https://en.wikipedia.org/wiki/Cat_(Unix) "https://en.wikipedia.org/wiki/Cat_(Unix)") command to store the resource types you want to scan in a
 JSON file named `config.json` in your home directory. The
 following is an example scanning configuration that scans for Amazon EC2
 instances, security groups, and all Amazon S3 resources.



```
$ cat > `config.json`
[
  {
    "Types":[
      "`AWS::EC2::Instance`",
      "`AWS::EC2::SecurityGroup`",
      "`AWS::S3::*`"
    ]
  }
]
```
2. Use the [start-resource-scan](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/start-resource-scan.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/start-resource-scan.html") command with the
 `--scan-filters` option, along with the
 `config.json` file you created, to start the partial scan.
 Replace `us-east-1` with the
 AWS Region that contains the resources to scan.



```
aws cloudformation start-resource-scan --scan-filters `file://config.json` --region `us-east-1`
```

If successful, this command returns the ARN of the scan. Note the ARN in
 the `ResourceScanId` property. You need it to create your
 template.



```
{
    "ResourceScanId":
      "arn:aws:cloudformation:`region`:`account-id`:resourceScan/`0a699f15-489c-43ca-a3ef-3e6ecfa5da60`"
}
```

###### To monitor the progress of a resource scan


Use the [describe-resource-scan](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-resource-scan.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-resource-scan.html") command. For the
 `--resource-scan-id` option, replace the sample ARN with the
 actual ARN.



```
aws cloudformation describe-resource-scan --region `us-east-1` \
  --resource-scan-id `arn:aws:cloudformation:us-east-1:123456789012:resourceScan/0a699f15-489c-43ca-a3ef-3e6ecfa5da60`
```

If successful, this command returns output similar to the following: 



```
{
    "ResourceScanId": "arn:aws:cloudformation:`region`:`account-id`:resourceScan/`0a699f15-489c-43ca-a3ef-3e6ecfa5da60`",
    "Status": "COMPLETE",
    "StartTime": "2023-08-21T03:10:38.485000+00:00",
    "EndTime": "2023-08-21T03:20:28.485000+00:00",
    "PercentageCompleted": 100.0,
    "ResourceTypes": [
        "AWS::CloudFront::CachePolicy",
        "AWS::CloudFront::OriginRequestPolicy",
        "AWS::EC2::DHCPOptions",
        "AWS::EC2::InternetGateway",
        "AWS::EC2::KeyPair",
        "AWS::EC2::NetworkAcl",
        "AWS::EC2::NetworkInsightsPath",
        "AWS::EC2::NetworkInterface",
        "AWS::EC2::PlacementGroup",
        "AWS::EC2::Route",
        "AWS::EC2::RouteTable",
        "AWS::EC2::SecurityGroup",
        "AWS::EC2::Subnet",
        "AWS::EC2::SubnetCidrBlock",
        "AWS::EC2::SubnetNetworkAclAssociation",
        "AWS::EC2::SubnetRouteTableAssociation",
        ...
    ],
    "ResourcesRead": 676
}
```

For a partial scan, the output will look similar to the following: 



```
{
    "ResourceScanId": "arn:aws:cloudformation:`region`:`account-id`:resourceScan/`0a699f15-489c-43ca-a3ef-3e6ecfa5da60`",
    "Status": "COMPLETE",
    "StartTime": "2025-03-06T18:24:19.542000+00:00",
    "EndTime": "2025-03-06T18:25:23.142000+00:00",
    "PercentageCompleted": 100.0,
    "ResourceTypes": [
        "AWS::EC2::Instance",
        "AWS::EC2::SecurityGroup",
        "AWS::S3::Bucket",
        "AWS::S3::BucketPolicy"
    ],
    "ResourcesRead": 65,
    "ScanFilters": [
        {
            "Types": [
                "AWS::EC2::Instance",
                "AWS::EC2::SecurityGroup",
                "AWS::S3::*"
            ]
        }
    ]
}
```

For a description of the fields in the output, see [DescribeResourceScan](../APIReference/API_DescribeResourceScan.md "../APIReference/API_DescribeResourceScan.md") in the
 *AWS CloudFormation API Reference*.
