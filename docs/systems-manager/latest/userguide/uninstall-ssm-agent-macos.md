

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Uninstall SSM Agent from macOS instances
<a name="uninstall-ssm-agent-macos"></a>

macOS doesn't natively support uninstallation of `PKG` files. To uninstall SSM Agent from an Amazon EC2 instance for macOS, use the AWS managed script from the following location.

 [`https://github.com/aws/amazon-ssm-agent/blob/mainline/Tools/src/update/darwin/uninstall.sh`](https://github.com/aws/amazon-ssm-agent/blob/mainline/Tools/src/update/darwin/uninstall.sh) 