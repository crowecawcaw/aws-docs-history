• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Adding

related resources to an OpsItem

Each OpsItem includes a **Related resources** section that lists the
Amazon Resource Name (ARN) of the related resource. A _related
resource_ is the impacted AWS resource that needs to be
investigated.

If Amazon EventBridge creates the OpsItem, the system automatically populates the OpsItem with the
ARN of the resource. You can manually specify ARNs of related resources. For certain
ARN types, OpsCenter automatically creates a deep link that displays details about
the resource directly in the OpsCenter console. For example, if you specify the ARN
of an Amazon Elastic Compute Cloud (Amazon EC2) instance as a related resource, then OpsCenter pulls in
details about that EC2 instance. This allows you to view detailed information about
your impacted AWS resources without having to leave OpsCenter.

###### To view and add related resources to an OpsItem

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **OpsCenter**.
3. Choose the **OpsItems** tab.
4. Choose an OpsItem ID.

![A new OpsItem on the OpsCenter Overview page.](images/OpsItems_working_scenario_1.png) 5. To view information about the impacted resource, choose the
**Related resources details** tab.

![Viewing the Related resource details tab for an OpsItem.](images/OpsItems_working_scenario_1_5.png)

This tab displays information about the resource from several
AWS services. Expand the **Resource details** section to
view information about this resource as provided by the AWS service that
hosts it. You can also toggle through other related resources associated
with this OpsItem by using the **Related resources**
list. 6. To add additional related resources, choose the
**Overview** tab. 7. In the **Related resources** section, choose
**Add**. 8. For **Resource type**, choose a resource from the
list. 9. For **Resource ID**, enter either the ID or the Amazon
Resource Name (ARN). The type of information you choose depends on the
resource that you chose in the previous step.

###### Note

You can manually add the ARNs of additional related resources. Each OpsItem can
list a maximum of 100 related resource ARNs.

The following table lists the resource types that automatically create deep links
to related resources.

| Supported resource types                                           | Resource name                                                                                                             | ARN format |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------- |
| AWS Certificate Manager certificate                                | ``<br>arn:aws:acm:`region`:`account-id`:certificate/`certificate-id`<br>``                                                |
| Amazon EC2 Auto Scaling group                                      | ``<br>arn:aws:autoscaling:`region`:`account-id`:autoScalingGroup:`groupid`:autoScalingGroupName/`groupfriendlyname`<br>`` |
| Amazon CloudFront distribution                                     | ``<br>arn:aws:cloudfront::`account-id`:*<br>``                                                                            |
| AWS CloudFormation stack                                           | ``<br>arn:aws:cloudformation:`region`:`account-id`:stack/`stackname`/`additionalidentifier`<br>``                         |
| Amazon CloudWatch alarm                                            | ``<br>arn:aws:cloudwatch:`region`:`account-id`:alarm:`alarm-name`<br>``                                                   |
| AWS CloudTrail trail                                               | ``<br>arn:aws:cloudtrail:`region`:`account-id`:trail/`trailname`<br>``                                                    |
| AWS CodeBuild project                                              | ``<br>arn:aws:codebuild:`region`:`account-id`:`resourcetype`/`resource`<br>``                                             |
| AWS CodePipeline                                                   | ``<br>arn:aws:codepipeline:`region`:`account-id`:`resource-specifier`<br>``                                               |
| Amazon DevOps Guru insight                                         | ``<br>arn:aws:devops-guru:`region`:`account-id`:insight/`proactive or reactive`/`resource-id`<br>``                       |
| Amazon DynamoDB table                                              | ``<br>arn:aws:dynamodb:`region`:`account-id`:table/`tablename`<br>``                                                      |
| Amazon Elastic Compute Cloud (Amazon EC2) customer gateway         | ``<br>arn:aws:ec2:`region`:`account-id`:customer-gateway/`cgw-id`<br>``                                                   |
| Amazon EC2 elastic IP                                              | ``<br>arn:aws:ec2:`region`:`account-id`:eip/`eipalloc-id`<br>``                                                           |
| Amazon EC2 Dedicated Host                                          | ``<br>arn:aws:ec2:`region`:`account-id`:dedicated-host/`host-id`<br>``                                                    |
| Amazon EC2 instance                                                | ``<br>arn:aws:ec2:`region`:`account-id`:instance/`instance-id`<br>``                                                      |
| Amazon EC2 internet gateway                                        | ``<br>arn:aws:ec2:`region`:`account-id`:internet-gateway/`igw-id`<br>``                                                   |
| Amazon EC2 network access control list (network ACL)               | ``<br>arn:aws:ec2:`region`:`account-id`:network-acl/`nacl-id`<br>``                                                       |
| Amazon EC2 network interface                                       | ``<br>arn:aws:ec2:`region`:`account-id`:network-interface/`eni-id`<br>``                                                  |
| Amazon EC2 route table                                             | ``<br>arn:aws:ec2:`region`:`account-id`:route-table/`route-table-id`<br>``                                                |
| Amazon EC2 security group                                          | ``<br>arn:aws:ec2:`region`:`account-id`:security-group/`security-group-id`<br>``                                          |
| Amazon EC2 subnet                                                  | ``<br>arn:aws:ec2:`region`:`account-id`:subnet/`subnet-id`<br>``                                                          |
| Amazon EC2 volume                                                  | ``<br>arn:aws:ec2:`region`:`account-id`:volume/`volume-id`<br>``                                                          |
| Amazon EC2 VPC                                                     | ``<br>arn:aws:ec2:`region`:`account-id`:vpc/`vpc-id`<br>``                                                                |
| Amazon EC2 VPN connection                                          | ``<br>arn:aws:ec2:`region`:`account-id`:vpn-connection/`vpn-id`<br>``                                                     |
| Amazon EC2 VPN gateway                                             | ``<br>arn:aws:ec2:`region`:`account-id`:vpn-gateway/`vgw-id`<br>``                                                        |
| AWS Elastic Beanstalk application                                  | ``<br>arn:aws:elasticbeanstalk:`region`:`account-id`:application/`applicationname`<br>``                                  |
| Elastic Load Balancing (Classic Load Balancer)                     | ``<br>arn:aws:elasticloadbalancing:`region`:`account-id`:loadbalancer/`name`<br>``                                        |
| Elastic Load Balancing (Application Load Balancer)                 | ``<br>arn:aws:elasticloadbalancing:`region`:`account-id`:loadbalancer/app/`load-balancer-name`/`load-balancer-id`<br>``   |
| Elastic Load Balancing (Network Load Balancer)                     | ``<br>arn:aws:elasticloadbalancing:`region`:`account-id`:loadbalancer/net/`load-balancer-name`/`load-balancer-id`<br>``   |
| AWS Identity and Access Management (IAM) group                     | ``<br>arn:aws:iam::`account-id`:group/`group-name`<br>``                                                                  |
| IAM policy                                                         | ``<br>arn:aws:iam::`account-id`:policy/`policy-name`<br>``                                                                |
| IAM role                                                           | ``<br>arn:aws:iam::`account-id`:role/`role-name`<br>``                                                                    |
| IAM user                                                           | ``<br>arn:aws:iam::`account-id`:user/`user-name`<br>``                                                                    |
| AWS Lambda function                                                | ``<br>arn:aws:lambda:`region`:`account-id`:function:`function-name`<br>``                                                 |
| Amazon Relational Database Service (Amazon RDS) cluster            | ``<br>arn:aws:rds:`region`:`account-id`:cluster:`db-cluster-name`<br>``                                                   |
| Amazon RDS database instance                                       | ``<br>arn:aws:rds:`region`:`account-id`:db:`db-instance-name`<br>``                                                       |
| Amazon RDS subscription                                            | ``<br>arn:aws:rds:`region`:`account-id`:es:`subscription-name`<br>``                                                      |
| Amazon RDS security group                                          | ``<br>arn:aws:rds:`region`:`account-id`:secgrp:`security-group-name`<br>``                                                |
| Amazon RDS cluster snapshot                                        | ``<br>arn:aws:rds:`region`:`account-id`:cluster-snapshot:`cluster-snapshot-name`<br>``                                    |
| Amazon RDS subnet group                                            | ``<br>arn:aws:rds:`region`:`account-id`:subgrp:`subnet-group-name`<br>``                                                  |
| Amazon Redshift cluster                                            | ``<br>arn:aws:redshift:`region`:`account-id`:cluster:`cluster-name`<br>``                                                 |
| Amazon Redshift parameter group                                    | ``<br>arn:aws:redshift:`region`:`account-id`:parametergroup:`parameter-group-name`<br>``                                  |
| Amazon Redshift security group                                     | ``<br>arn:aws:redshift:`region`:`account-id`:securitygroup:`security-group-name`<br>``                                    |
| Amazon Redshift cluster snapshot                                   | ``<br>arn:aws:redshift:`region`:`account-id`:snapshot:`cluster-name`/`snapshot-name`<br>``                                |
| Amazon Redshift subnet group                                       | ``<br>arn:aws:redshift:`region`:`account-id`:subnetgroup:`subnet-group-name`<br>``                                        |
| Amazon Simple Storage Service (Amazon S3) bucket                   | ``<br>arn:aws:s3:::`bucket_name`<br>``                                                                                    |
| AWS Config recording of AWS Systems Manager managed node inventory | ``<br>arn:aws:ssm:`region`:`account-id`:managed-instance-inventory/`node_id`<br>``                                        |
| Systems Manager State Manager association                          | ``<br>arn:aws:ssm:`region`:`account-id`:association/`association_ID`<br>``                                                |
