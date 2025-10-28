# Viewing CIS scan results

Amazon Inspector creates a scan job for every scan configuration that runs and collects results of a scan with a unique scan ID.
CIS scan results are available for 90 days.
You can view CIS scan results by its checks or scanned resources:

- **Scan results aggregated by checks** – Groups the results of a scan by each individual check performed during the scan.
  For each check, you get a report of how many resources failed, skipped, or passed.
- **Scan results aggregated by scanned resources** – Groups the results of a scan by each scanned resource the scan targets during the scan.
  For each resource, you get a report of how many checks that a resource failed, skipped, or passed.

This topic describes how to view results for a CIS scan.

###### To view scan results

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Use the AWS Region dropdown to select the AWS Region where you created your CIS scan configuration.
3. From the navigation pane, choose **On-demand scans**, and then choose **CIS scans**.
4. Choose the **Scan results** tab.
5. Under the **Scheduled by** column, choose the scan schedule ID you want to view.
   Or select the row with the scan schedule ID you want to view, and then choose **View details**.
6. Choose **Checks** to view each check that was performed performed or **Scanned resources** to view each scanned resource that was targeted during the scan.

You can also view details for scheduled CIS scans.

###### To view details for scheduled CIS scans

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Use the AWS Region dropdown to select the AWS Region where you created your CIS scan configuration.
3. From the navigation pane, choose **On-demand scans**, and then choose **CIS scans**.
4. Choose the **Scheduled** tab.
5. Under the **Scan configuration name** column, choose the name of the scan configuration you want to view.
   Or select the row with the scan configuration you want to view, and then choose **View details**.
