# Update the product

Research and Engineering Studio (RES) has two methods of updating the product which depend on if the version update
is major or minor.

RES uses a date-based versioning scheme. A major release uses the year and month, and a
minor release adds a sequence number when necessary. For example, version 2024.01 was released
in January 2024 as a major release; version 2024.01.01 was a minor release update of that version.

###### Topics

- [Major version updates](#major-version-update "#major-version-update")
- [Minor version updates](#minor-version-updates "#minor-version-updates")

## Major version updates

Research and Engineering Studio uses snapshots to support migration from a previous RES environment to the latest
without losing your environment settings. You can also use this process to test and verify
updates to your environment before onboarding users.

###### To update your environment with the latest version of RES:

1. Create a snapshot of your current environment. See [Create a snapshot](create-snapshot.md "create-snapshot.md").
2. Redeploy RES with the new version. See [Step 1: Launch the product](launch-the-product.md "launch-the-product.md").
3. Apply the snapshot to your updated environment. See [Apply a snapshot](apply-snapshot.md "apply-snapshot.md").
4. Verify all data migrated successfully to the new environment.

## Minor version updates

###### Warning

Upgrading from RES version 2025.06 to 2025.06.01 requires using the [Major version updates](#major-version-update "#major-version-update") process.

For minor version updates to RES, a new install is not required. You can update
the existing RES stack by updating its CloudFormation template. Check the version of your
current RES environment in CloudFormation before deploying the update. You can find the
version number at the beginning of the template.

For example: `"Description": "RES_2024.1"`

###### To make a minor version update:

1. Download the latest CloudFormation template in [Step 1: Launch the product](launch-the-product.md "launch-the-product.md").
2. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. From **Stacks**, find and select the primary stack. It should
   appear as `<stack-name>`.
4. Choose **Update**.
5. Choose **Replace current template**.
6. For **Template source**, choose **Upload a template
   file**.
7. Choose **Choose file** and upload the template you downloaded.
8. On **Specify stack details**, choose **Next**.
   You do not need to update the parameters.
9. On **Configure stack options**, choose **Next**.
10. On **Review <stack-name>**, choose **Submit**.
