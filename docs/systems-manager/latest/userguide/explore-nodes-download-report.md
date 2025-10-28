# Downloading or exporting a managed node

report

You can use the Systems Manager **Explore nodes** feature to view filtered or
unfiltered lists of managed nodes for your AWS organization or account in the Systems Manager
console. For cases where you want to view the data offline or process it in another
application, you can save the report as a `CSV` or `JSON`
file.

Depending on the size of the report, you're prompted to download the report to your
local machine or export it to an Amazon S3 bucket. Reports are saved to S3 buckets in
`CSV` format only.

###### To download or export a managed node report

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Explore nodes**.
3. (Optional) Follow the steps in [Choosing a filter view for managed node
   summaries](explore-nodes-filter-view.md "explore-nodes-filter-view.md") to refine the list of managed
   nodes displayed for your organization or account.
4. Choose **Report** (
   ![The download report icon](images/download-arrow-icon.png)
   ).
5. If the **Download report** dialog box is displayed, do the
   following:
   1. For **File name**, enter a name for the file. We
      recommend specifying a name that represents the scope of the report,
      such as `all-organization-nodes` or
      `ec2-instances-out-of-date-agent`.
   2. For **Included columns**, specify whether to include
      columns for all available node details, or only those you've selected
      for your current display.

   ###### Tip

   For information about managing the columns in your report display,
   see [Managing node report content and
   appearance](explore-nodes-manage-report-display.md "explore-nodes-manage-report-display.md"). 3. For **File format**, select **CSV**
   or **JSON**, depending on how you will use the
   file. 4. For **Spreadsheet heading**, to include a column
   headings row in a `CSV` file, select **Include row of
   column names**. 5. Choose **Download**.The report is saved to the default download location according to your
   browser's settings.

6. If the **Export to Amazon S3** dialog box is displayed, do the
   following:
   1. For **S3 URI**, enter the URI for the bucket to
      export the report to.

   ###### Tip

   To view a list of your buckets in the Amazon S3 console, choose
   **View**. To select from a list of buckets in
   your account, choose **Browse S3**. 2. For **Authorization method**, specify the service
   role to use to provide permissions for exporting the report to the
   bucket.

   If you choose to let Systems Manager create the role for you, it provides all
   needed permissions and trust statements for the operation.

   If you want to use or create your own role, the role must include the
   required permissions and trust statements. For information about
   creating this role, see [Creating a custom service role to export
   diagnosis reports to S3](create-s3-export-role.md "create-s3-export-role.md"). 3. Choose **Submit**.
