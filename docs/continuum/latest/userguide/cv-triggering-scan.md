

# Triggering a scan
<a name="cv-triggering-scan"></a>

When you create an environment, AWS Continuum starts the first scan, even if you select **Manual only**. Use the scan frequency to control recurring scans. By default, AWS Continuum scans your code every day. If you select **Manual only**, AWS Continuum doesn't run automatic recurring scans. You can also queue a scan manually from the console.

To change the scan frequency, do the following.

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/).

1. In the navigation pane, choose **Environments**, and then choose the environment name.

1. Choose the **Scans** tab.

1. Choose **Configure scan frequency**.

1. For **Scan frequency**, select one of the following values:
   + **Every day**
   + **Every 2 days**
   + **Every 7 days**
   + **Manual only**

1. Choose **Save**.

To queue a manual scan, do the following. You can't cancel a scan after you queue it.

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/).

1. In the navigation pane, choose **Environments**, and then choose the environment name.

1. Choose the **Scans** tab.

1. Choose **Queue scan**.

1. In the **Queue scan?** dialog, choose **Queue scan**.

1. Choose the **Refresh scans** icon. Check the scan's status in the **Status** column.

If a failure reason is available for a failed scan, choose **Failed** in the **Status** column. The **Failure reason** popover shows the explanation.

After a scan reaches **Succeeded** status, AWS Continuum might continue processing issues and generating patches. To view available results, see [Viewing discovered issues](cv-viewing-issues.md) and [Viewing generated patches](cv-viewing-patches.md).