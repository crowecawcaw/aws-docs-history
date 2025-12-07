# Connect agent to private VPC resources

If the application you want to run a penetration test on is not available on the public internet, you need to provide AWS Security Agent with a VPC configuration. AWS Security Agent will use this VPC configuration, including a VPC, subnet, and security groups, to access the application.

###### Note

For VPC penetration tests, VPC CIDR ranges that overlap with the 10.0.0.0/16 range are currently not supported. Additionally, if you have a VPC IP endpoint that falls within this CIDR range, it will also fail to resolve.

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
