

# Download a capacity plan in Connect Customer
<a name="download-capacity-plan"></a>

When you download a capacity plan file, it downloads as a .csv file type with multiple tabs. It's helpful to open this file using Excel. The following image shows an example of what a capacity plan file looks like in Excel. 

**Note**  
The multi-tab workbook format described in this section applies to Hiring plans only. For information about downloading a Scheduling plan, see [Download a Scheduling plan](#download-scheduling-capacity-plan).

![A downloaded capacity plan file opened with Excel showing multiple tabs for metrics, capacity plan details.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-capacity-planning-download1.png)


Following is a description of each worksheet:
+ **Metrics**: When you download the Monthly view, the capacity plan output shows Monthly and Daily granularities. When you download the Weekly view, it shows Weekly and Daily granularities.
+ **Capacity Plan**: The capacity plan metadata, such as name, starting date, and ending date of the plan.
+ **Scenario**: The input defined for the capacity plan. 
+ **Generation Details**: The metadata indicating when someone last changed the capacity plan.

## How to download capacity plan results
<a name="howto-download-capacity-plan"></a>

1. Log in to the Connect Customer admin website with an account that has security profile permissions for **Analytics**, **Capacity planning - Edit**. 

   For more information, see [Assign permissions](required-optimization-permissions.md). 

1. On the Connect Customer navigation menu, select **Analytics and optimization**, **Capacity Planning**.

1. On the **Capacity Plans** tab, choose the plan. 

1. On the detailed page for the capacity plan, choose **Actions**, **Download capacity plan**. 

## Download a Scheduling plan
<a name="download-scheduling-capacity-plan"></a>

You can download a Scheduling plan as a single .csv file. The file has one row per interval (15 or 30 minutes). The columns match the [Scheduling plan data](capacity-planning-review-output.md#capacity-planning-scheduling-plan-data-table) table on the plan detail page.

The download runs in the background. You can leave the page while it runs. When the export finishes, you receive a notification and the file is ready to download.

The following image shows a downloaded Scheduling plan .csv file opened in a spreadsheet application.

![A downloaded Scheduling plan .csv file with one row per interval and per-channel metric columns.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-capacity-planning-scheduling-download-csv.png)


**Note**  
The file can span a large date range with rows every 15 or 30 minutes. The export might take a few minutes.

### How to download Scheduling plan results
<a name="howto-download-scheduling-capacity-plan"></a>

1. Log in to the Connect Customer admin website with an account that has security profile permissions for **Analytics**, **Capacity planning - Edit**.

   For more information, see [Assign permissions](required-optimization-permissions.md).

1. On the navigation menu, choose **Analytics and optimization**, **Capacity Planning**.

1. On the **Capacity Plans** tab, choose the Scheduling plan.

1. Choose **Actions**, **Download**.