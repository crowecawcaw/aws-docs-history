

# Quotas and considerations for Wavelength Zones
<a name="wavelength-quotas"></a>

Consider the following as you get started with AWS Wavelength.

**Topics**
+ [Networking considerations](#networking-considerations)
+ [Amazon EC2 considerations](#ec2-considerations)
+ [Amazon EBS considerations](#ebs)
+ [Amazon Elastic Kubernetes Service considerations](#eks-considerations)
+ [Amazon VPC considerations](#vpc-considerations)
+ [Service quotas for Amazon VPC](#quotas)

## Networking considerations
<a name="networking-considerations"></a>

Consider the following network information.

### Multiple Wavelength Zone considerations
<a name="multiple-wavelength-zones"></a>

EC2 instances that are in two different Wavelength Zones in the same VPC are not allowed to communicate with each other. If you need communication from one Wavelength Zone to another Wavelength Zone, we recommend that you use multiple VPCs, one for each Wavelength Zone. You can use a transit gateway to connect the VPCs. This configuration enables communication between instances in the Wavelength Zones. For information about how to configure multiple Wavelength Zones, see [Subnets in Wavelength](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-wavelength.html) in the *Amazon VPC User Guide*.

The following controls are enabled by the carrier gateway for internet flows by default and cannot be removed:


| Protocol | Between EC2 instance and the internet | Between EC2 instance and a device on the carrier network | 
| --- | --- | --- | 
| TCP | + Africa-based Wavelength Zones (parent region eu-west-3): Allowed<br />+ All other Wavelength Zones: Outbound and the response  | Allowed | 
| UDP | + Africa-based Wavelength Zones (parent region eu-west-3): Allowed<br />+ All other Wavelength Zones: Denied  | Allowed | 
| ICMP | Allowed | Allowed | 
+ TCP is allowed for outbound and response in most cases
+ UDP from the internet is denied

  UDP traffic from a device on the carrier network is allowed to route to an Amazon EC2 instance in a Wavelength Zone.
+ ICMP is allowed

In addition, inbound routing from the carrier network is optimized for devices in the location of the Wavelength Zone. For example, a Wavelength Zone in the San Francisco Bay area allows low latency access only from devices that are in that metro area and carrier network.

## Amazon EC2 considerations
<a name="ec2-considerations"></a>

Take the following information into consideration when you launch EC2 instances in Wavelength Zones:
+ You cannot use Dedicated Instances or Dedicated Hosts.
+ EC2 quotas are controlled by the quotas for the home Region.
+ The following instance types are supported:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wavelength/latest/developerguide/wavelength-quotas.html)

## Amazon EBS considerations
<a name="ebs"></a>

Take the following information into consideration when you use Amazon Elastic Block Store for EC2 instances that are in Wavelength Zones:
+ Snapshots of EBS volumes and AMIs are stored in the AWS Region.
+ You can only use `gp2` volumes.
+ There is a limit for `gp2` storage.

  For more information see [Quotas for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-resource-quotas.html) in the *Amazon EBS User Guide*.

## Amazon Elastic Kubernetes Service considerations
<a name="eks-considerations"></a>

Take the following information into consideration when you run an Amazon EKS cluster:
+ You must run Kubernetes 1.17 or later.
+ When you create your Amazon EKS cluster, you must select an Availability Zone in the VPC, and not a Wavelength Zone.
+ When you create your Amazon EKS cluster for private subnets only, you need to add VPC endpoints for Amazon ECR and Amazon Simple Storage Service. For more information, see [Amazon VPC considerations](#vpc-considerations).
+ To create node groups in Wavelength Zones for your Amazon EKS cluster, see [Launching self-managed Amazon Linux nodes](https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html) in the *Amazon EKS User Guide*.
+ To apply the `aws-auth` ConfigMap to your Amazon EKS cluster, see [Grant IAM users access to Kubernetes with a ConfigMap](https://docs.aws.amazon.com/eks/latest/userguide/auth-configmap.html) in the *Amazon EKS User Guide*.

## Amazon VPC considerations
<a name="vpc-considerations"></a>

Take the following information into consideration when you run Amazon VPC:
+ To use VPC endpoints, you must create the endpoint in an Availability Zone in the VPC. You cannot create the endpoint in a Wavelength Zone.
+ You cannot assign IPv6 addresses to subnets that are in Wavelength Zones.

## Service quotas for Amazon VPC
<a name="quotas"></a>

Wavelength VPCs and Wavelength subnets count toward your Amazon VPC service quotas. For more information about Amazon VPC quotas, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) in the *Amazon VPC User Guide*.

For more information about how to view your service quotas, see [Viewing service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html) in the *Service Quotas User Guide*.