• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Working with public parameters in

Parameter Store

Some AWS services publish information about common artifacts as AWS Systems Manager
_public_ parameters. For example, the Amazon Elastic Compute Cloud (Amazon EC2) service
publishes information about Amazon Machine Images (AMIs) as public parameters.

###### Topics in this guide

- [Discovering public
  parameters in Parameter Store](parameter-store-finding-public-parameters.md "parameter-store-finding-public-parameters.md")
- [Calling AMI public
  parameters in Parameter Store](parameter-store-public-parameters-ami.md "parameter-store-public-parameters-ami.md")
- [Calling the ECS optimized
  AMI public parameter in Parameter Store](parameter-store-public-parameters-ecs.md "parameter-store-public-parameters-ecs.md")
- [Calling the EKS optimized
  AMI public parameter in Parameter Store](parameter-store-public-parameters-eks.md "parameter-store-public-parameters-eks.md")
- [Calling
  public parameters for AWS services, Regions, endpoints, Availability Zones,
  local zones, and Wavelength Zones in Parameter Store](parameter-store-public-parameters-global-infrastructure.md "parameter-store-public-parameters-global-infrastructure.md")

**Related AWS blog posts**

- [Query for AWS Regions, Endpoints, and More Using
  AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/aws/new-query-for-aws-regions-endpoints-and-more-using-aws-systems-manager-parameter-store/ "https://aws.amazon.com/blogs/aws/new-query-for-aws-regions-endpoints-and-more-using-aws-systems-manager-parameter-store/")
- [Query for the latest Amazon Linux AMI IDs using
  AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/ "https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/")
- [Query for the Latest Windows AMI Using
  AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/mt/query-for-the-latest-windows-ami-using-systems-manager-parameter-store/ "https://aws.amazon.com/blogs/mt/query-for-the-latest-windows-ami-using-systems-manager-parameter-store/")
