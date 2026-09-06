

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Tag bulk update notes
<a name="ams-tags-bu-notes"></a>

These notes are for use with the [Tag \| Bulk Update](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-tag-bulk-update.html) and [Tag \| Bulk Update (Managed automation)](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-tag-bulk-update-review-required.html) change type example walkthroughs.

Notes on bulk update tags:
+ Supported services:
  + For [Tag \| Bulk Update (Managed automation)](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-tag-bulk-update-review-required.html): All.
  + For [Tag \| Bulk Update](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-tag-bulk-update.html):
    + Auto Scaling
    + Amazon EC2
    + Elastic Load Balancing
    + Amazon RDS
    + Amazon S3 buckets
+ To generate the comma-separated values (CSV) file, log in to **Resource Groups** > **Tag Editor** in the AWS console, find the resources you want to tag, and then export them to a CSV file. For more information, see [Export Results to CSV](https://docs.aws.amazon.com/ARG/latest/userguide/find-resources-to-tag.html#tagging-resources-csv).

  NOTE: We recommend using an S3 pre-signed URL for providing the CSV object location.
+ There must be columns with the headers **Service**, **Type**, and **Identifier**. These columns are mandatory.
+ Rename the column **Identifier** to **ID**.
+ The values for columns **Service**, **Type**, and **Identifier** (changed to **ID**) are as provided by the **Tag Editor** under **Resource Groups**.
+ If a resource to be tagged is not available under the **Tag Editor**, use the Amazon Resource Name (ARN) of the resource for the column **Identifier** (changed to **ID**) and keep **Service** and **Type** blank.
+ The column headers of the tags to be added or modified must have the format **Tag: {{TagKey}}**.
+ The column headers of the tags to be deleted must have the format **Untag: {{TagKey}}**.
+ Each row is for a resource to be tagged or untagged.
+ If a tag is to be added to a resource, specify the value of the tag under the appropriate **Tag: {{TagKey}}** column.
+ If a tag is to be deleted from a resource, specify **True** under the appropriate **Untag: {{TagKey}}** column.
+ If a **Tag: {{TagKey}} **or **Untag: {{TagKey}}** is not applicable for a resource, add a dash (-) to the respective column or keep it blank.

  NOTE: The Untag overrides the Tag - this is because, unlike Tag, Untag needs to be manually added to the CSV file, so we assume the intention was to remove, not modify, the tag.
+ Any additional columns that don't fit the criteria are ignored.

**Important**  
The Tag Editor export populates a matrix of all tags against all resources, missing tags are populated with a value of 'not tagged'. Re-using this export CSV as input to the RFC results in all the previously missing tags being created, with literal values of 'not tagged'.

![Spreadsheet showing AWS resource details including service types, regions, IDs, and tags.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/bulkUpdateTagCsvEx.png)


**Note**  
For information about exporting tags to a CSV file, see [ Find Resources to Tag -> Export Results to CSV](https://docs.aws.amazon.com/ARG/latest/userguide/find-resources-to-tag.html#tagging-resources-csv).