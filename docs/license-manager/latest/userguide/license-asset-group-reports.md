

# License asset group reports
<a name="license-asset-group-reports"></a>

License asset group reports provide on-demand, comprehensive reporting for software license compliance across multiple AWS regions and accounts within your organization. These reports offer detailed inventory of all resources discovered and mapped to a License asset group.

**To create a License asset group report**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. From the navigation panel choose **Usage reports** (under License analytics).

1. Choose **Create license asset group report**, then define the parameters:

   1. Enter a **Name** and optional **Description** for your report.

   1. Select a **License asset group** from the drop-down list.

   1. Choose the date range to list all resources within that range.

   1. (Optional) Add **Tags** to track the usage report resource.

1. Select **Create usage report**.

**To create a License asset group report using CLI**
+ Use the `create-license-manager-report-generator` command for on-demand reports with a specific time range:

  ```
  aws license-manager create-license-manager-report-generator \
      --report-generator-name "License asset group Report" \
      --type LicenseAssetGroupReport \
      --report-context '{
        "licenseAssetGroupArns": [
          "arn:aws:license-manager:region:account:license-asset-group/group-id"
        ],
        "startTime": "2024-01-01T00:00:00Z",
        "endTime": "2024-01-31T23:59:59Z"
      }' \
      --client-token unique-token
  ```
**Note**  
License asset group reports are generated on-demand for a specified time range and do not support periodic scheduling. Omit the `--report-frequency` parameter.