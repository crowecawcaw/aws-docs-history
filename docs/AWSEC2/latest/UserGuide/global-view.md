

# View resources across Regions using AWS Global View
<a name="global-view"></a>

AWS Global View enables you to view some of your resources across a single AWS Region, or across multiple Regions in a single console. AWS Global View also provides *global search* functionality that lets you search for specific resources or specific resource types across multiple Regions simultaneously. 

AWS Global View does not let you modify resources in any way.

**Supported resources**  
Using AWS Global View, you can view a global summary of the following resources across all of the Regions for which your AWS account is enabled.
+ Auto Scaling groups
+ Availability Zones
+ Capacity Reservations and Capacity Blocks
+ DB clusters
+ DB instances
+ DHCP option set
+ Amazon Elastic Container Service (Amazon ECS) clusters
+ ECS services
+ ECS tasks
+ Egress-only internet gateways
+ Elastic IPs
+ Endpoint services
+ Instances
+ Internet gateways
+ Managed prefix lists
+ NAT gateways
+ Network ACLs
+ Network interfaces
+ Outposts
+ Route tables
+ S3 buckets
+ Security groups
+ Subnets
+ Volumes
+ VPCs
+ VPC endpoints
+ VPC peering connections

**Required permissions**  
A user must have the following permissions to use AWS Global View.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
  {
    "Effect": "Allow",
    "Action": [
      "autoscaling:DescribeAutoScalingGroups",
      "ec2:DescribeRegions",
      "ec2:DescribeCapacityReservations",
      "ec2:DescribeDhcpOptions",
      "ec2:DescribeEgressOnlyInternetGateways",
      "ec2:DescribeAddresses",
      "ec2:DescribeVpcEndpointServices",
      "ec2:DescribeInstances",
      "ec2:DescribeInternetGateways",
      "ec2:DescribePrefixLists",
      "ec2:DescribeNatGateways",
      "ec2:DescribeNetworkAcls",
      "ec2:DescribeNetworkInterfaces",
      "ec2:DescribeRouteTables",
      "ec2:DescribeSecurityGroups",
      "ec2:DescribeSubnets",
      "ec2:DescribeVolumes",
      "ec2:DescribeVpcs",
      "ec2:DescribeVpcEndpoints",
      "ec2:DescribeVpcPeeringConnections",
      "ec2:DescribeAvailabilityZones",
      "ec2:DescribeVpcEndpointServiceConfigurations",
      "ec2:DescribeManagedPrefixLists",
      "ecs:ListClusters",
      "ecs:DescribeServices",
      "ecs:ListTasks",
      "outposts:ListOutposts",
      "rds:DescribeDBInstances",
      "rds:DescribeDBClusters",
      "s3:ListAllMyBuckets"
  ],
  "Resource": "*"
  }]
}
```

------

**To use AWS Global View**  
Sign in to the [AWS Global View console](https://console.aws.amazon.com/ec2globalview/home#RegionsAndZones).

**Important**  
You cannot use a private window in Firefox to access AWS Global View.

The console consists of the following:
+ **Region explorer** – This page includes the following sections:
  + **Summary** – Provides a high-level overview of your resources across all Regions.

    Expand **Show all resource summary** indicates the number of Regions for which your AWS account is enabled. The remaining fields indicate the number of resources that you currently have in those Regions. Choose any of the links to view the resources of that type across all Regions. For example, if the link below the **Instances** label is **29 in 10 Regions**, it indicates that you currently have `29` instances across `10` Regions. Choose the link to view a list of all 29 instances.
  + **Region explorer** – Lists all of the AWS Regions (including those for which your account is not enabled) and provides totals for each resource type for each Region.

    Choose a Region name to view all resources of all types for that specific Region. For example, choose **Africa (Cape Town) af-south-1** to view all VPCs, subnets, instances, security groups, volumes, and Auto Scaling groups in that Region. Alternatively, select a Region and choose **View resources for selected Region**.

    Choose the value for a specific resource type in a specific Region to view only resources of that type in that Region. For example, choose the value for Instances for **Africa (Cape Town) af-south-1** to view only the instances in that Region.
+ **Global search** – This page enables you to search for specific resources or specific resource types across a single Region or across multiple Regions. It also enables you to view details for a specific resource.

  To search for resources, enter the search criteria in the field preceding the grid. You can search by Region, by resource type, and by the tags assigned to resources.

  To view the details for a specific resource, select it in the grid. You can also choose the resource ID of a resource to open it in its respective console. For example, choose an instance ID to open the instance in the Amazon EC2 console, or choose a subnet ID to open the subnet in the Amazon VPC console.
+ **Regions and Zones** – This page allows you to view and manage all available Regions, Availability Zones, Local Zones, and Wavelength Zones. You can switch between **List view** and **Map view** using the **List view**/**Map view** toggle. Your view preference persists across sessions.
  + **Map view** – Displays all Regions and Zones on an interactive world map, colored by status. To see details for a location, point to it or choose it. Choose a location to take action – you can enable a Region, enable a Zone, or open its detail page. You can also filter the map to show only specific statuses. The map and the detail list stay synchronized – selecting a location on one highlights it on the other.
  + **List view** – Displays Regions and Zones in a table. From the **Regions** tab, you can view all AWS Regions. The **Status** column shows the Regions that are enabled for your AWS account.

  From this page, you can select a Region to:
  + View details of the Region such as the Region code, Geography, and number of each type of Zone.

    You can also view the list of Availability Zones, Local Zones, and Wavelength Zones and the list of your resources in the Region.
  + Enable or disable the Region.

  From each zone tab, you can view the list of that zone type. From the **Local Zones** tab, you can opt-in to a Local Zone.

**Tip**  
If you only use specific Regions or resource types, you can customize AWS Global View to display only those Regions and resource types. To customize the displayed Regions and resource types, in the navigation panel, choose **Settings**, and then on the **Resources** and **Regions** tabs, select the Regions and resource types that you do not want to be displayed in AWS Global View.