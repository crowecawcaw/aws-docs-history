

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Managing Amazon EBS volumes on managed instances
<a name="fleet-manager-manage-amazon-ebs-volumes"></a>

[Amazon Elastic Block Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) (Amazon EBS) provides block level storage volumes for use with Amazon Elastic Compute Cloud (EC2) instances. EBS volumes behave like raw, unformatted block devices. You can mount these volumes as devices on your instances.

You can use Fleet Manager to manage Amazon EBS volumes on your managed instances. For example, you can initialize an EBS volume, format a partition, and mount the volume to make it available for use.

**Note**  
Fleet Manager currently supports Amazon EBS volume management for Windows Server instances only.

## View EBS volume details
<a name="ebs-volume-management-details"></a>

**To view details for an EBS volume with Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Choose the button next to the managed instance for which you want to view EBS volume details.

1. Choose **View details**.

1. Choose **Tools, EBS volumes**.

1. To view details for an EBS volume, choose its ID in the **Volume ID ** column.

## Initialize and format an EBS volume
<a name="ebs-volume-management-format"></a>

**To initialize and format an EBS volume with Fleet Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Choose the button next to the managed instance for which you want to initialize, format, and mount an EBS volume. You can only initialize an EBS volume if its disk is empty.

1. Choose **View details**.

1. In the **Tools** menu, choose **EBS volumes**.

1. Choose the button next to the EBS volume you want to initialize and format.

1. Choose **Initialize and format**.

1. In **Partition style**, choose the partition style you want to use for the EBS volume.

1. (Optional) Choose a **Drive letter** for the partition.

1. (Optional) Enter a **Partition name** to identify the partition.

1. Choose the **File system** to use to organize files and data stored in the partition.

1. Choose **Confirm** to make the EBS volume available for use. You can't change the partition configuration from the AWS Management Console after confirming, however, you can use SSH or RDP to log into the instance to change the partition configuration.