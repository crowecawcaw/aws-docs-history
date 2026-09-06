

# Regions, Availability Zones, and Local Zones
<a name="Concepts.RegionsAndAvailabilityZones"></a>

Amazon cloud computing resources are hosted in multiple locations world-wide. These locations are composed of AWS Regions, Availability Zones, and Local Zones. Each *AWS Region* is a separate geographic area. Each AWS Region has multiple, isolated locations known as *Availability Zones*.

**Note**  
For information about finding the Availability Zones for an AWS Region, see [Describe your Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#availability-zones-describe) in the Amazon EC2 documentation.

By using Local Zones, you can place resources, such as compute and storage, in multiple locations closer to your users. Amazon RDS enables you to place resources, such as DB instances, and data in multiple locations. Resources aren't replicated across AWS Regions unless you do so specifically.

Amazon operates state-of-the-art, highly-available data centers. Although rare, failures can occur that affect the availability of DB instances that are in the same location. If you host all your DB instances in one location that is affected by such a failure, none of your DB instances will be available.

![AWS Region.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/Con-AZ-Local.png)


It is important to remember that each AWS Region is completely independent. Any Amazon RDS activity you initiate (for example, creating database instances or listing available database instances) runs only in your current default AWS Region. The default AWS Region can be changed in the console, or by setting the [`AWS_DEFAULT_REGION`](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-region) environment variable. Or it can be overridden by using the `--region` parameter with the AWS Command Line Interface (AWS CLI). For more information, see [Configuring the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html), specifically the sections about environment variables and command line options. 

Amazon RDS supports special AWS Regions called AWS GovCloud (US). These are designed to allow US government agencies and customers to move more sensitive workloads into the cloud. The AWS GovCloud (US) Regions address the US government's specific regulatory and compliance requirements. For more information, see [What is AWS GovCloud (US)?](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/whatis.html) 

To create or work with an Amazon RDS DB instance in a specific AWS Region, use the corresponding regional service endpoint.

## AWS Regions
<a name="Concepts.RegionsAndAvailabilityZones.Regions"></a>

Each AWS Region is designed to be isolated from the other AWS Regions. This design achieves the greatest possible fault tolerance and stability.

When you view your resources, you see only the resources that are tied to the AWS Region that you specified. This is because AWS Regions are isolated from each other, and we don't automatically replicate resources across AWS Regions.

### Region availability
<a name="Concepts.RegionsAndAvailabilityZones.Availability"></a>

The following table shows the AWS Regions where Amazon RDS is currently available and the endpoint for each Region.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  rds.us-east-2.amazonaws.com <br /> rds-fips.us-east-2.api.aws <br /> rds.us-east-2.api.aws <br /> rds-fips.us-east-2.amazonaws.com  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  rds.us-east-1.amazonaws.com <br /> rds-fips.us-east-1.api.aws <br /> rds-fips.us-east-1.amazonaws.com <br /> rds.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (N. California) | us-west-1 |  rds.us-west-1.amazonaws.com <br /> rds.us-west-1.api.aws <br /> rds-fips.us-west-1.amazonaws.com <br /> rds-fips.us-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  rds.us-west-2.amazonaws.com <br /> rds-fips.us-west-2.amazonaws.com <br /> rds.us-west-2.api.aws <br /> rds-fips.us-west-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Africa (Cape Town) | af-south-1 |  rds.af-south-1.amazonaws.com <br /> rds.af-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  rds.ap-east-1.amazonaws.com <br /> rds.ap-east-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  rds.ap-south-2.amazonaws.com <br /> rds.ap-south-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  rds.ap-southeast-3.amazonaws.com <br /> rds.ap-southeast-3.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  rds.ap-southeast-5.amazonaws.com  | HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  rds.ap-southeast-4.amazonaws.com <br /> rds.ap-southeast-4.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  rds.ap-south-1.amazonaws.com <br /> rds.ap-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  rds.ap-southeast-6.amazonaws.com  | HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  rds.ap-northeast-3.amazonaws.com <br /> rds.ap-northeast-3.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  rds.ap-northeast-2.amazonaws.com <br /> rds.ap-northeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  rds.ap-southeast-1.amazonaws.com <br /> rds.ap-southeast-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  rds.ap-southeast-2.amazonaws.com <br /> rds.ap-southeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  rds.ap-east-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  rds.ap-southeast-7.amazonaws.com  | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  rds.ap-northeast-1.amazonaws.com <br /> rds.ap-northeast-1.api.aws  | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 |  rds.ca-central-1.amazonaws.com <br /> rds.ca-central-1.api.aws <br /> rds-fips.ca-central-1.api.aws <br /> rds-fips.ca-central-1.amazonaws.com  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Canada West (Calgary) | ca-west-1 |  rds.ca-west-1.amazonaws.com <br /> rds-fips.ca-west-1.amazonaws.com  | HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  rds.eu-central-1.amazonaws.com <br /> rds.eu-central-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Ireland) | eu-west-1 |  rds.eu-west-1.amazonaws.com <br /> rds.eu-west-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 |  rds.eu-west-2.amazonaws.com <br /> rds.eu-west-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Milan) | eu-south-1 |  rds.eu-south-1.amazonaws.com <br /> rds.eu-south-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Paris) | eu-west-3 |  rds.eu-west-3.amazonaws.com <br /> rds.eu-west-3.api.aws  | HTTPS<br />HTTPS | 
| Europe (Spain) | eu-south-2 |  rds.eu-south-2.amazonaws.com <br /> rds.eu-south-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Stockholm) | eu-north-1 |  rds.eu-north-1.amazonaws.com <br /> rds.eu-north-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Zurich) | eu-central-2 |  rds.eu-central-2.amazonaws.com <br /> rds.eu-central-2.api.aws  | HTTPS<br />HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  rds.il-central-1.amazonaws.com <br /> rds.il-central-1.api.aws  | HTTPS<br />HTTPS | 
| Mexico (Central) | mx-central-1 |  rds.mx-central-1.amazonaws.com  | HTTPS | 
| Middle East (Bahrain) | me-south-1 |  rds.me-south-1.amazonaws.com <br /> rds.me-south-1.api.aws  | HTTPS<br />HTTPS | 
| Middle East (UAE) | me-central-1 |  rds.me-central-1.amazonaws.com <br /> rds.me-central-1.api.aws  | HTTPS<br />HTTPS | 
| South America (São Paulo) | sa-east-1 |  rds.sa-east-1.amazonaws.com <br /> rds.sa-east-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  rds.us-gov-east-1.amazonaws.com <br /> rds.us-gov-east-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  rds.us-gov-west-1.amazonaws.com <br /> rds.us-gov-west-1.api.aws  | HTTPS<br />HTTPS | 

If you do not explicitly specify an endpoint, the US West (Oregon) endpoint is the default.

When you work with a DB instance using the AWS CLI or API operations, make sure that you specify its regional endpoint.

## Availability Zones
<a name="Concepts.RegionsAndAvailabilityZones.AvailabilityZones"></a>

When you create a DB instance, you can choose an Availability Zone or have Amazon RDS choose one for you randomly. An Availability Zone is represented by an AWS Region code followed by a letter identifier (for example, `us-east-1a`).

Use the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) Amazon EC2 command as follows to describe the Availability Zones within the specified Region that are enabled for your account.

```
aws ec2 describe-availability-zones --region {{region-name}}
```

For example, to describe the Availability Zones within the US East (N. Virginia) Region (us-east-1) that are enabled for your account, run the following command:

```
aws ec2 describe-availability-zones --region us-east-1
```

You can't choose the Availability Zones for the primary and secondary DB instances in a Multi-AZ DB deployment. Amazon RDS chooses them for you randomly. For more information about Multi-AZ deployments, see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.MultiAZ.md).

**Note**  
Random selection of Availability Zones by RDS doesn't guarantee an even distribution of DB instances among Availability Zones within a single account or DB subnet group. You can request a specific AZ when you create or modify a Single-AZ instance, and you can use more-specific DB subnet groups for Multi-AZ instances. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md) and [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).

## Local Zones
<a name="Concepts.RegionsAndAvailabilityZones.LocalZones"></a>

A *Local Zone* is an extension of an AWS Region that is geographically close to your users. You can extend any VPC from the parent AWS Region into Local Zones. To do so, create a new subnet and assign it to the AWS Local Zone. When you create a subnet in a Local Zone, your VPC is extended to that Local Zone. The subnet in the Local Zone operates the same as other subnets in your VPC.

When you create a DB instance, you can choose a subnet in a Local Zone. Local Zones have their own connections to the internet and support Direct Connect. Thus, resources created in a Local Zone can serve local users with very low-latency communications. For more information, see [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/).

A Local Zone is represented by an AWS Region code followed by an identifier that indicates the location, for example `us-west-2-lax-1a`.

**Note**  
A Local Zone can't be included in a Multi-AZ deployment.

**To use a Local Zone**

1. Enable the Local Zone in the Amazon EC2 console.

   For more information, see [Enabling Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#enable-zone-group) in the *Amazon EC2 User Guide.*

1. Create a subnet in the Local Zone.

   For more information, see [Creating a subnet in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#AddaSubnet) in the *Amazon VPC User Guide.*

1. Create a DB subnet group in the Local Zone.

   When you create a DB subnet group, choose the Availability Zone group for the Local Zone.

   For more information, see [Creating a DB instance in a VPC](USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.InstanceInVPC).

1. Create a DB instance that uses the DB subnet group in the Local Zone.

   For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md).

**Important**  
Currently, the only AWS Local Zone where Amazon RDS is available is Los Angeles in the US West (Oregon) Region.