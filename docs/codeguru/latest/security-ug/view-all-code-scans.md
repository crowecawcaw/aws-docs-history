On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# View all code scans

You can view a list of all your code scans on the **Scans** page in the [CodeGuru Security console](https://console.aws.amazon.com/codeguru/security/Scans "https://console.aws.amazon.com/codeguru/security/Scans"). The
table lists the name, the status, the number of open findings, and the date of the last scan run
for each scan in your account.

Scans run in Amazon Inspector, JupyterLab, and Amazon SageMaker AI Studio do not appear in the console.

To customize the view of the Scans table, choose the gear icon on the upper right side of
the Scans table. In the **Preferences** window that appears, you can select
page size, display settings, and which columns you want to see.

## View scans with the AWS CLI or AWS SDKs

To get a list of all code scans in your account with the AWS CLI or AWS SDKs, use the
[`ListScans`](../security-api/API_ListScans.md "../security-api/API_ListScans.md") operation. For more information, see the [Amazon CodeGuru Security API Reference](../security-api.md "../security-api.md").
