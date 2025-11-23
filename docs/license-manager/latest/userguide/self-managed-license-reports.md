# Self-managed license reports

Self-managed license reports provide periodic snapshots of your license usage. You can set up multiple usage reports to track different license types in your environment with automated publishing to Amazon S3 buckets.

**Self-managed license summary report**

Contains information on the number of consumed licenses and details about self-managed license configurations, including license count, license rules, and distribution across resource types.

**Resource usage report**

Provides details about tracked resources and their license consumption, listing each resource with license ID, status, and AWS account ID information.

###### To create a self-managed license usage report

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. From the navigation panel choose **Usage reports** (under License analytics).
3. Choose **Create usage report**, then define the parameters:
   1. Enter a **Name** and optional **Description** for your usage report.
   2. Select a self-managed license type from the drop-down list.
   3. Choose the report types to generate.
   4. Choose the frequency: **Once every 24 hours**, **Once every 7 days**, or **Once every 30 days**.
   5. (Optional) Add **Tags** to track the usage report resource.

4. Select **Create usage report**.

###### To create a self-managed license report using CLI

- Use the `create-license-manager-report-generator` command:

```
aws license-manager create-license-manager-report-generator \
    --report-generator-name "Daily License Usage Report" \
    --type LicenseUsageReport \
    --report-context '{
      "licenseConfigurationArns": [
        "arn:aws:license-manager:region:account:license-configuration/lic-config-id"
      ]
    }' \
    --report-frequency '{
      "value": 1,
      "period": "DAY"
    }' \
    --client-token unique-token
```
