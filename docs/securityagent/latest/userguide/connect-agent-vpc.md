# Connect agent to private VPC resources

If the application you want to run a penetration test on is not available on the public internet, you need to provide AWS Security Agent with a VPC configuration. AWS Security Agent will use this VPC configuration, including a VPC, subnet, and security groups, to access the application.

###### Note

If a private endpoint presents a Transport Layer Security (TLS) certificate that is not publicly trusted, also provide the trust anchor. This applies when the certificate is issued by a private or internal certificate authority (CA), an intermediate CA, or a self-signed certificate. Endpoint validation uses the trust anchor to accept the certificate. For more information, see [Provide trusted CA certificates for a penetration test](provide-trusted-ca-certificates.md "provide-trusted-ca-certificates.md").

###### Note

When testing endpoints in a private VPC, only endpoints resolving to IPs in known private IP ranges are allowed (see [VPC CIDR blocks](../../../vpc/latest/userguide/vpc-cidr-blocks.md "../../../vpc/latest/userguide/vpc-cidr-blocks.md") for more information). The following IPv4 and IPv6 ranges are allowed:

```
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
fd00::/8
```

###### Note

When connecting to a subnet, AWS Security Agent will create an ENI ([Elastic Network Interface](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md")) in the subnet configured for the penetration test. This ENI does not have an associated public IP address, meaning that it cannot communicate with [VPC Internet Gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in public subnets. If your penetration test requires open internet access, please use a private subnet with an associated [VPC NAT Gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") instead

###### Tip

When testing against an endpoint that has an IP allowlist, you can add a private VPC configuration with an associated [VPC NAT Gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") to your penetration test. You can then use the NAT Gateway IP address to allowlist outbound traffic from the penetration test.

You grant AWS Security Agent general access to a VPC from the AWS Management Console. In the Security Agent web application, users select the specific configuration for a penetration test.

## To add a VPC in the Agent Space

1. Navigate to the Agent Space overview page
2. Select **Actions** and then **Edit penetration test configuration**
3. Under the **VPC** heading, specify the **VPC**, **Subnets**, and **Security groups**

You can add up to 5 VPCs.

## Required Agent Space service role permissions

To run a penetration test with a VPC, your Agent Space service role must include the following permissions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeNetworkInterfaceAttribute",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeVpcs",
        "ec2:ModifyNetworkInterfaceAttribute",
        "ec2:DeleteNetworkInterface"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "ec2:CreateNetworkInterfacePermission",
      "Resource": "arn:aws:ec2:{{region}}:{{accountId}}:network-interface/*",
      "Condition": {
        "ArnEquals": {
          "ec2:Subnet": [
            "arn:aws:ec2:{{region}}:{{accountId}}:subnet/[[subnetIds]]"
          ]
        }
      }
    }
  ]
}
```

## To select a specific VPC configuration for a penetration test in the Security Agent web application

1. Navigate to the Penetration Tests overview page
2. Select the penetration test that you need to add VPC configuration for, and then choose **Modify pentest details**
3. Select **Next** to reach the **VPC Resources** section
4. Select the **VPC**, **Subnet**, and **Security groups**
5. Select **Next** to reach the last section and **Save** the penetration test

###### Note

Cross-account penetration testing is currently supported for VPC resources (subnets and security groups) shared using AWS Resource Access Manager. Secrets Manager secrets and Lambda functions used for authentication credentials must be configured in the same AWS account as your AWS Security Agent setup.

## Running a penetration test against VPC resources in another AWS account

You can run penetration tests against VPC resources shared with your account using AWS Resource Access Manager. Both accounts must be part of the same AWS Organization.

1. (Optional) Enable automatic resource sharing for your AWS organization

```
aws ram enable-sharing-with-aws-organization
```

1. Using credentials from the AWS account that owns the VPC resources, share subnet and security group resources with the penetration test owner account

```
aws ram create-resource-share \
    --name SharePentestResources \
    --resource-arns <subnet ARN> <security group ARN> \
    --principals <penetration test owner account ID>
```

1. Navigate to the Agent Space overview page
2. Select **Penetration test** and locate **Service role name**
3. Verify that the IAM role grants access to the shared VPC resources
4. Select **Actions** and then **Edit penetration test configuration**
5. Under the **VPC** heading, specify the shared **VPC**, **Subnets**, and **Security groups** and save the updated configuration.
6. Navigate to the Penetration Tests overview page on the AWS Security Agent web application
7. Select the penetration test that you need to add VPC configuration for, and then choose **Modify pentest details**
8. Update the penetration test to use the shared VPC resources
