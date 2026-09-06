

# Mounting EFS file systems from another VPC
<a name="mount-fs-different-vpc"></a>

When you use a VPC peering connection or transit gateway to connect VPCs, Amazon EC2 instances that are in one VPC can access EFS file systems in another VPC, even if the VPCs belong to different accounts. 

You can't use DNS name resolution for EFS mount points in another VPC. To mount your EFS file system, use the IP address of the mount points in the corresponding Availability Zone.

Alternatively, you can use Amazon Route 53 as your DNS service. In Route 53, you can resolve the EFS mount target IP addresses from another VPC by creating a private hosted zone and resource record set. For more information on how to do so, see [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) in the *Amazon Route 53 Developer Guide*.

## Prerequisites
<a name="mount-fs-different-vpc-prerequisites"></a>

Before using the following the procedure, take these steps:
+ Install the Amazon EFS client, part of the `amazon-efs-utils` set of utilities on the compute instance you're mounting the EFS file system on. You use the EFS mount helper, which is included in `amazon-efs-utils`, to mount the file system. For instructions on installing `amazon-efs-utils`, see [Installing the Amazon EFS client](using-amazon-efs-utils.md).
+ Allow the `ec2:DescribeAvailabilityZones` action in the IAM policy for the IAM role you attached to the instance. We recommend that you attach the AWS managed policy `AmazonElasticFileSystemsUtils` to an IAM entity to provide the necessary permissions for the entity.
+ When mounting from another AWS account, update the file system resource policy to allow the `elasticfilesystem:DescribeMountTarget` action for the principal ARN of other AWS account. For example:

  ```
  {
      "Id": "access-point-example03",
      "Statement": [
          {
              "Sid": "access-point-statement-example03",
              "Effect": "Allow",
              "Principal": {"AWS": "arn:aws:iam::555555555555:root"},
              "Action": "elasticfilesystem:DescribeMountTargets",
              "Resource": "arn:aws:elasticfilesystem:us-east-2:111122223333:file-system/fs-12345678"
          }
      ]
  }
  ```

  For more information about EFS file system resource policies, see [Resource-based policies within Amazon EFS](security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies).
+ Install botocore. The EFS client uses botocore to retrieve the mount target IP address when the file system DNS name cannot be resolved when mounting a file system in another VPC. For more information, see [Install botocore](https://github.com/aws/efs-utils#Install-botocore) in the `amazon-efs-utils` README file.
+ Set up either a VPC peering connection or a VPC transit gateway. 

  You connect the client's VPC and your EFS file system's VPC using either a VPC peering connection or a VPC transit gateway. When you use a VPC peering connection or transit gateway to connect VPCs, Amazon EC2 instances that are in one VPC can access EFS file systems in another VPC, even if the VPCs belong to different accounts.

  A *transit gateway *is a network transit hub that you can use to interconnect your VPCs and on-premises networks. For more information about using VPC transit gateways, see [Getting Started with transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html) in the *Amazon VPC Transit Gateways Guide*.

  A *VPC peering connection* is a networking connection between two VPCs. This type of connection enables you to route traffic between them using private Internet Protocol version 4 (IPv4) or Internet Protocol version 6 (IPv6) addresses. You can use VPC peering to connect VPCs within the same AWS Region or between AWS Regions. For more information on VPC peering, see [What is VPC Peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) in the *Amazon VPC Peering Guide*.

To ensure high availability of your file system, we recommend that you always use an EFS mount target IP address that is in the same Availability Zone as your NFS client. If you're mounting an EFS file system that is in another account, ensure that the NFS client and EFS mount target are in the same Availability Zone ID. This requirement applies because AZ names can differ from one account to another.

**To mount an EFS file system in another VPC using IAM or an access point**

1. Connect to your EC2 instance. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) in the *Amazon EC2 User Guide*.

1. Create a directory for mounting the file system using the following command.

   ```
   $ sudo mkdir /mnt/efs
   ```

1. To mount the file system using IAM authorization, use the following command:

   ```
   $ sudo mount -t efs -o tls,iam {{file-system-dns-name}} /mnt/efs/
   ```

   For more information about using IAM authorization with EFS, see [Using IAM to control access to file systems](iam-access-control-nfs-efs.md).

   To mount the file system using an EFS access point, use the following command:

   ```
   $ sudo mount -t efs -o tls,accesspoint={{access-point-id}} {{file-system-dns-name}} /mnt/efs/
   ```

   For more information about EFS access points, see [Working with access points](efs-access-points.md).

## Mounting EFS file systems from a different AWS Region
<a name="mount-different-region-vpc"></a>

If you are mounting your EFS file system from another VPC that is in a different AWS Region than the file system, you will need to edit the `efs-utils.conf` file. In `/dist/efs-utils.conf`, locate the following lines:

```
#region = us-east-1
```

Uncomment the line, and replace the value for the ID of the region in which the file system is located, if it is not in `us-east-1`.