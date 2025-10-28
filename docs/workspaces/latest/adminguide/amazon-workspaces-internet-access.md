# Provide internet access for WorkSpaces Personal

Your WorkSpaces must have access to the internet so that you can install updates to the
operating system and deploy applications. You can use one of the following options to allow
your WorkSpaces in a virtual private cloud (VPC) to access the internet.

###### Options

- Launch your WorkSpaces in private subnets and configure a NAT gateway in a public
  subnet in your VPC.
- Launch your WorkSpaces in public subnets and automatically or manually assign public
  IP addresses to your WorkSpaces.
  For more information about these options, see the corresponding sections in [Configure a VPC for WorkSpaces Personal](amazon-workspaces-vpc.md "amazon-workspaces-vpc.md").

With any of these options, you must ensure that the security group for your WorkSpaces
allows outbound traffic on ports 80 (HTTP) and 443 (HTTPS) to all destinations
(`0.0.0.0/0`).

###### Amazon Linux extras library

If you are using the Amazon Linux repository, your Amazon Linux WorkSpaces must either have internet
access or you must configure VPC endpoints to this repository and to the main Amazon Linux
repository. For more information, see the _Example: Enabling Access to the Amazon Linux
AMI Repositories_ section in [Endpoints for Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md "../../../vpc/latest/userguide/vpc-endpoints-s3.md"). The Amazon Linux
AMI repositories are Amazon S3 buckets in each Region. If you want instances in your VPC
to access the repositories through an endpoint, create an endpoint policy that enables
access to these buckets. The following policy allows access to the Amazon Linux
repositories.

```
{
  "Statement": [
    {
        "Sid": "AmazonLinux2AMIRepositoryAccess",
        "Principal": "*",
        "Action": [
            "s3:GetObject"
        ],
        "Effect": "Allow",
        "Resource": [
            "arn:aws:s3:::amazonlinux.*.amazonaws.com/*"
        ]
    }
  ]
}
```
