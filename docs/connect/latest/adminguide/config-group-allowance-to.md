

# Set group allowance for time off in Connect Customer
<a name="config-group-allowance-to"></a>

Managers can set the maximum time off hours that agents combined can take within the Forecast Group: by hour, for each calendar day, for specific time off activities. 

You use a .csv file to quickly specify time off allowances at a hourly level, for up to 27 months. For example, you might specify Vacation, Personal time off, Casual, and other time off types that you specified when you [created shift activities](scheduling-create-shift-activities.md). 

**Tip**  
**IT admins**: For the endpoints to add to your proxy exception list for this feature, see [Allow upload of time-off balances and allowances in Connect Customer scheduling](ccp-networking.md#endpoints-scheduling). 

**Topics**
+ [Download the time off csv template](#timeoff-csv-template)
+ [Download time off for a forecast group](#download-timeoff-csv)
+ [Import group allowance .csv file](#upload-timeoff-csv)
+ [Example of using the time off allowances feature](#example-to-feature)

## Download the time off .csv template
<a name="timeoff-csv-template"></a>

1. On the **Scheduling** page, choose the **Time off** tab.

1. On the **Download** dropdown menu, choose **Download template**.

   The following image shows an example .csv template that contains valid data.  
![A sample csv file with time off allowances.](http://docs.aws.amazon.com/connect/latest/adminguide/images/group-allowance-csv.png)

1. When you add your time off data to the template, note the following:
   + Do not change the top row of the .csv file template.
   + In the **Time off activities** column, separate multiple activities with two pipes **\|\|**.
   + The **Start time** and **End time** must have a one-hour duration and set as multiples of 15 minutes. If they do not meet these criteria, the validation will fail when you attempt to upload your .csv file. The following example shows the error message that you might encounter: 

     `Column START_TIME value [2023-08-15T05:01:00] is not a multiple of 15 minutes from top of the hour, such as HH:00, HH:15, HH:30 and HH:45`

## Download time off for a forecast group
<a name="download-timeoff-csv"></a>

1. On the **Scheduling** page, choose the **Time off** tab.

1. Choose one or more forecast groups that you want in the download csv file.

1. On the **Download** dropdown menu, choose **Current group allowance balance**, as shown in the following image.  
![The scheduling page, the time off tab, the download menu.](http://docs.aws.amazon.com/connect/latest/adminguide/images/schedule-timeoff-download.png)

   The .csv file includes the data that was last uploaded to Connect Customer. For example, the following image shows the download time off allowance .csv file. 
   + **LAST\_UPLOADED\_GROUP\_ALLOWANCE\_IN\_HOURS**: The last upload for Group 1 was 4.4 hours of vacation.
   + **GROUP\_ALLOWANCE\_IN\_HOURS** shows they have 2.4 hours remaining in their allowance, they've already used 2 hours.  
![The timeoff allowance csv file.](http://docs.aws.amazon.com/connect/latest/adminguide/images/schedule-timeoff-allowance.png)

## Import group allowance .csv file
<a name="upload-timeoff-csv"></a>

You can upload multiple csv files for group allowance, Connect Customer will combine them into a single csv file when you download it. If the same combination of forecast group, time off activities, and datetime exists in multiple files, most recent uploaded file will override the data from previous uploads. For example, you can upload one csv file with group allowance for all of 2026 that has non-zero allowance until June 2026 and zero allowance from July to December 2026. This will prevent all time-off bookings for second half of 2026. Then at a later date you can upload another csv file that contains non-zero allowances for July to December 2026, thus opening up these dates for agents to request time-offs.

For the maximum file size that you can upload, see *File size per upload of time off group allowance data* in [Forecasting, capacity planning, and scheduling feature specifications](feature-limits.md#forecasting-cap-planning-scheduling-specs). 

1. On the **Scheduling** page, choose the **Time off** tab.

1. Choose the Forecast group the group allowance applies to, and then choose **Upload group allowance**. Connect Customer does the following:
   + Validates the data and provides details if there are errors.
   + Prompts you for confirmation that you want to upload the data.
   + Uploads the file and displays a confirmation message when complete.

## Example of using the time off allowances feature
<a name="example-to-feature"></a>

For example, your business provides time off in December. Here's how you might use the time off allowances feature:
+ Managers can allow a group of agents to take *casual leave* and *regular P.T.O* that add up to a maximum of 12 hours on December 20th, from 9AM to 9PM.
+ They can automatically decline those types of time off requests on December 22nd by giving a value of `0` - Zero hours.
+ Adding value `0` allows them to specify blocked days. Connect Customer ignores a group allowance check if no value is specified.

This allows the workforce managers to balance an agent's personal time off needs with business headcount needs. 