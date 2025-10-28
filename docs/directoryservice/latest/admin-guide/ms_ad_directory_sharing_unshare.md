# Unsharing your directory

Use the following procedure to unshare an AWS Managed Microsoft AD directory.

###### To unshare your directory

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, under **Active Directory**, select
   **Directories**.
2. Choose the directory ID of the AWS Managed Microsoft AD directory that you want to unshare.
3. On the **Directory details** page, do one of the following:
   - If you have multiple Regions showing under **Multi-Region replication**,
     select the Region where you want to unshare your directory, and then choose the
     **Scale & share** tab. For more information,
     see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   - If you do not have any Regions showing under **Multi-Region replication**,
     choose the **Scale & share** tab.

4. In the **Shared directories** section, select the shared directory you want to unshare, choose **Actions**, and then choose **Unshare**.
5. In the **Unshare directory** dialog box, choose **Unshare**.
