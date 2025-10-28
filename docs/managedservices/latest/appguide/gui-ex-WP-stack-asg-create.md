# Create an Auto Scaling Group Stack

Launch an Auto scaling group.

REQUIRED DATA:

- `VpcId`: The VPC you are using, this should be the same as the previously used VPC.
- `AMI-ID`: This value determines what kind of EC2 instances your Auto Scaling group (ASG) will spin up. Be sure to select an AMI in your account
  that starts with "customer-" and is of the operating system that you want. Find AMI IDs with the For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. operation (CLI: list-amis) or in
  the AMS Console VPCs -> VPCs details page. This walkthrough is for ASGs configured to use a Linux AMI.
- `ASGLoadBalancerNames`: The load balancer that you previously created--find the name by looking at the EC2 Console -> Load Balancers (in
  the left nav). Note this is not the "Name" that you specified when you created the ELB previously.

1. On the **Create RFC** page, select the category **Deployment**,
   subcategory **Advanced Stack Components**, item **Auto scaling group**, and click **Create**.
   Choose **Advanced** and accept all defaults (including those with no value) except those shown next.

###### Note

Specify the latest AMS AMI. Specify the previously-created ELB.

```

**Subject**:                              WP-ASG-RFC
**ASGSubnetIds**:                         `PRIVATE_AZ1
 PRIVATE_AZ2`
**ASGAmiId**:                             `AMI_ID`
**VpcId**:                                `VPC_ID`
**Name**:                                 WP_ASG
**ASGLoadBalancerNames**:                 `ELB_NAME`
**ASGUserData**:
#!/bin/bash
REGION=$(curl 169.254.169.254/latest/meta-data/placement/availability-zone/ | sed 's/[a-z]$//')
yum -y install ruby httpd
chkconfig httpd on
service httpd start
touch /var/www/html/status
cd /tmp
curl -O https://aws-codedeploy-$REGION.s3.amazonaws.com/latest/install
chmod +x ./install
./install auto
chkconfig codedeploy-agent on
service codedeploy-agent start
```

2. Click **Submit** when finished.
