# Managing Amazon EBS volumes on

managed instances

[Amazon Elastic Block Store](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md") (Amazon EBS) provides block level storage volumes for use with
Amazon Elastic Compute Cloud (EC2) instances. EBS volumes behave like raw, unformatted block devices. You
can mount these volumes as devices on your instances.

You can use Fleet Manager, a tool in AWS Systems Manager, to manage Amazon EBS volumes on your managed
instances. For example, you can initialize an EBS volume, format a partition, and mount
the volume to make it available for use.

###### Note

Fleet Manager currently supports Amazon EBS volume management for Windows Server instances
only.

## View EBS volume details

###### To view details for an EBS volume with Fleet Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the managed instance for which you want to view
   EBS volume details.
4. Choose **View details**.
5. Choose **Tools, EBS volumes**.
6. To view details for an EBS volume, choose its ID in the **Volume
   ID** column.

## Initialize and format an EBS

volume

###### To initialize and format an EBS volume with Fleet Manager

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the button next to the managed instance for which you want to
   initialize, format, and mount an EBS volume. You can only initialize an EBS
   volume if its disk is empty.
4. Choose **View details**.
5. In the **Tools** menu, choose **EBS
   volumes**.
6. Choose the button next to the EBS volume you want to initialize and
   format.
7. Choose **Initialize and format**.
8. In **Partition style**, choose the partition style you
   want to use for the EBS volume.
9. (Optional) Choose a **Drive letter** for the
   partition.
10. (Optional) Enter a **Partition name** to identify the
    partition.
11. Choose the **File system** to use to organize files and
    data stored in the partition.
12. Choose **Confirm** to make the EBS volume available for
    use. You can't change the partition configuration from the AWS Management Console after
    confirming, however, you can use SSH or RDP to log into the instance to
    change the partition configuration.
