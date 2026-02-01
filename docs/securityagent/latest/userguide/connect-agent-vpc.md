# Connect agent to private VPC resources

If the application you want to run a penetration test on is not available on the public internet, you need to provide AWS Security Agent with a VPC configuration. AWS Security Agent will use this VPC configuration, including a VPC, subnet, and security groups, to access the application.

You grant AWS Security Agent general access to a VPC from the AWS Management Console. In the Security Agent web app, users select the specific configuration for a penetration test.
== To add a VPC in the Agent Space

1. Navigate to the Agent Space overview page
2. Select **Actions** and then **Edit penetration test configuration**
3. Under the **VPC** heading, specify the **VPC**, **Subnets**, and **Security groups**
   You can add up to 5 VPCs.

## To select a specific VPC configuration for a penetration test in the Security Agent web app

1. Navigate to the Penetration Tests overview page
2. Select the penetration test that you need to add VPC configuration for, and then choose **Modify pentest details**
3. Select **Next** at the bottom of the page to reach the **VPC Resources** section
4. Select the **VPC**, **Subnet**, and **Security groups**
5. Select **Next** to reach the last section and **Save** the penetration test

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
6. Navigate to the Penetration Tests overview page on the AWS Security Agent web app
7. Select the penetration test that you need to add VPC configuration for, and then choose **Modify pentest details**
8. Update the penetration test to use the shared VPC resources
