

# Backfill cost allocation tags
<a name="cost-allocation-backfill"></a>

Management account users can request a backfill of cost allocation tags for up to twelve months. When you request a backfill, the current **activation status** of the tags are backfilled for the duration of your choice.

For example, the `Project` tag was associated to an AWS Resources in June 2023 and activated in November 2023. On December 2023, you request to backfill the tag from January 2023. As a result, the `Project` tag is retroactively activated for the prior months from January to December 2023. The tag values associated to the `Project` tag will be available with the cost data from June 2023 to December 2023. However, January 2023 to May 2023 will not have tag values associated because the `Project` tag was not present in the AWS Resources.

Backfill can also be used to deactivate tags for alignment. For example, a `Team` tag was active in prior months, but currently is set to `inactive` status. Backfilling will result in the `Team` tag being deactivated and removed from the cost data for previous months.

**Note**  
The resource tag must be historically assigned to the AWS Resource for the backfilled cost data to be available.
You can't submit a new backfill request when there is a backfill in progress.
You can only submit a new backfill request once every 24 hours.

**To request a cost allocation tag backfill**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost allocation tags**.

1. At the top right of the page, choose **Backfill tags**.

1. In the **Backfill tags** dialog box, choose the month you want the backfill to start from.

1. Choose **Confirm**.

## Updating your AWS Cost Management services with backfill
<a name="cost-allocation-backfill-ce"></a>

Backfill will update your Cost Explorer, Data Exports, and AWS Cost and Usage Report automatically. Because these services refresh your data once every 24 hours, your backfill won't update as soon as it succeeds. For more information, see the following resources in their corresponding guides:
+ [Analyzing your costs with Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) in the *AWS Cost Management User Guide*
+ [What is Data Exports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) in the *AWS Data Exports user guide*