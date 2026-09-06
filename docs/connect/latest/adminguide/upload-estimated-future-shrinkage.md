

# Import estimated future shrinkage and available full-time employees in Connect Customer
<a name="upload-estimated-future-shrinkage"></a>

You can increase capacity planning accuracy by providing estimated future data for your existing forecast groups. You can import data for either plan type: Hiring plans use day-level Available FTE and shrinkage data, and Scheduling plans use interval-level available headcount and shrinkage data. Providing this data is optional. Connect Customer can generate a capacity plan without it, but providing it improves the accuracy of your plan.

## How to import data for Hiring plans
<a name="how-to-import-shrinkage-data"></a>

Use this procedure to import day-level Available FTE and shrinkage data for Hiring plans. To import interval-level data for Scheduling plans, see [Import headcount and shrinkage data for Scheduling plans](#upload-scheduling-headcount-shrinkage).

1. Log in to the Connect Customer admin website with an account that has security profile permissions for **Analytics**, **Capacity planning - Edit**. 

   For more information, see [Assign permissions](required-optimization-permissions.md). 

1. On the Connect Customer navigation menu, select **Analytics and optimization**, **Capacity Planning**.

1. On the **Import Data** tab, choose **Upload data**, and then choose **Hiring shrinkage and FTE**.

   The .csv file you upload must have the following headings: FORECAST\_GROUP, Date, AVAILABLE\_FTE, IN\_OFFICE\_SHRINKAGE\_OUT\_OFFICE\_SHRINKAGE. These are shown in the following image of a .csv file opened with Excel.  
![A Hiring plan csv file with correct headings.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-capacity-planning-csv-template.png)

1. Update values in this template, and then choose `Upload CSV` to upload it. Choose `Upload`.

It usually between 2 - 5 minutes for the .csv file to upload. If the upload fails, check if the `FORECAST_GROUP` name in the .csv file matches the name of the forecast group that you created.

## Important things to know about your Hiring plan .csv file
<a name="important-things-about-import-shrinkage-data"></a>

The following applies to the day-level .csv file for Hiring plans. For the interval-level file used by Scheduling plans, see [Import headcount and shrinkage data for Scheduling plans](#upload-scheduling-headcount-shrinkage).
+ FORECAST\_GROUP: Enter the EXACT name of the forecast group you created. You can add multiple forecast groups in this `.csv` file. 
+ Date: Each row is one day. In the previous image, row 2 is January 1, row 3 is January 2, row 4 is January 3, and so on. Use ISO 8601 format ending with Z. The time component of this field must represent midnight the time zone of the long term forecast. For example, if the long term forecast is in US/Pacific time, then the Date field should be as follows: 2024-05-30T07:00:00Z
+ AVAILABLE\_FTE: Based on your estimation, how many full-time agents will be available for working that day. For example, your contact center currently has 100 FTEs and you expect this number to be the same next year.

  In the previous image, 0 indicates no full-time agents are available on January 1 for the forecast group named **Forecast For Demo**. On January 3, 100 agents are available.
**Tip**  
Required FTE (the output) is how many full-time agents are required to meet the Service Level target. For example, if the Required FTE = 120 and Available FTE = 100 for next year, then that means a deficit = 20.
+ IN\_OFFICE\_SHRINKAGE: Percentage of agents in the office but not in production mode. For example, they might be in training or in meetings.
+ OUT\_OFFICE\_SHRINKAGE: Percentage of agents absent from work (for example, no show or personal time off).

**Note**  
The latest uploaded .csv file always overrides the previous one you updated. Make sure errors aren't introduced to the uploaded .csv file accidentally. For example, don't press **Enter** and add new rows to the end of the file. Otherwise, the data won't validate and an error message is displayed.

## Import headcount and shrinkage data for Scheduling plans
<a name="upload-scheduling-headcount-shrinkage"></a>

For Scheduling plans, you can import headcount and shrinkage data at the interval level. Each row covers a 15-minute or 30-minute interval, matching your short-term forecast. To upload this data, choose **Scheduling shrinkage and headcount** from the **Upload data** dropdown on the **Import Data** tab.

### To import headcount and shrinkage data for a Scheduling plan
<a name="how-to-import-scheduling-headcount-shrinkage"></a>

1. Log in to the Connect Customer admin website with an account that has security profile permissions for **Analytics**, **Capacity planning - Edit**.

   For more information, see [Assign permissions](required-optimization-permissions.md).

1. On the Connect Customer navigation menu, select **Analytics and optimization**, **Capacity Planning**.

1. Choose the **Import Data** tab.

1. Choose **Upload data**, and then choose **Scheduling shrinkage and headcount**.

1. In the **Import scheduling interval data** dialog, upload your `.csv` file, and then choose **Upload**.

The upload takes 2 to 5 minutes. If it fails, check that the `FORECAST_GROUP` value in your file matches the name of an existing forecast group.

### CSV field reference for Scheduling plan data
<a name="scheduling-headcount-shrinkage-csv-fields"></a>

Your `.csv` file must have the following columns in this order:
+ `START_INTERVAL_TIMESTAMP`: Required. The start of the interval. Use ISO 8601 format with a UTC offset. For example: `2026-01-01T00:00:00-08:00`.
+ `END_INTERVAL_TIMESTAMP`: Optional. Use the same format as the start. If you omit this field, the row covers one interval. If you include it, the row covers every interval in that range.
+ `FORECAST_GROUP`: Required. Enter the exact name of a forecast group you created. You can add multiple forecast groups in one `.csv` file.
+ `AVAILABLE_HC`: Required. Enter the number of agents available for that interval. Use zero or a positive number.
+ `IN_OFFICE_SHRINKAGE`: Required. Percentage of agents in the office but not in production mode. For example, they might be in training or meetings. Enter a value from 0 to 100.
+ `OUT_OFFICE_SHRINKAGE`: Required. Percentage of agents absent from work (for example, no-show or personal time off). Enter a value from 0 to 100.

**Note**  
The latest uploaded file always overrides the previous file. Check that your file has no errors before you upload it.