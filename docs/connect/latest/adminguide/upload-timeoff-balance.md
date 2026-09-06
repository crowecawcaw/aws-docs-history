

# Import an agent's time off balance to Connect Customer
<a name="upload-timeoff-balance"></a>

You can import or export a .csv file of an agent's time off balance. For example, you might download the time off balance from your HR system and then upload it to Connect Customer. 

Connect Customer uses the time off balance to automatically approve or decline time off requests based on the agent's available net balance. 

For the maximum file size that you can upload, see *File size per upload of agent time off data* in [Forecasting, capacity planning, and scheduling feature specifications](feature-limits.md#forecasting-cap-planning-scheduling-specs). 

**Tip**  
**IT admins**: For the endpoints to add to your proxy exception list for this feature, see [Allow upload of time-off balances and allowances in Connect Customer scheduling](ccp-networking.md#endpoints-scheduling). 

1. Log in to the Connect Customer admin website with an account that has security profile permissions for **Scheduling**, **Schedule manager - Edit**, or **Scheduling**, **Time off balance - Edit**. 

   For more information, see [Assign permissions](required-optimization-permissions.md). 

1. On the Connect Customer navigation menu, select **Analytics and optimization**, **Scheduling**.

1. On the **Scheduling** page, choose the **Staff Rules** tab.

1. Choose **Download template** and store the .csv file on your desktop. It looks similar to the following image.  
![The timeoff balance file for individuals.](http://docs.aws.amazon.com/connect/latest/adminguide/images/schedule-timeoff-balance-ic.png)

1. Add data or make changes to the .csv file as needed and then save to your desktop with a new file name. 
**Tip**  
To delete an agent's time-off balance, upload a blank value in the time-off balance hours column for that agent. 

1. Choose **Upload data** to upload the .csv file. Connect Customer does the following: 
   + Validates the data and provides details if there are errors.
   + Prompts you for confirmation that you want to upload the data.
   + Uploads the file and displays a confirmation message when complete.

After the .csv file is successfully uploaded, Connect Customer checks the available time off balance when time off requests are submitted. If there is enough time off balance it approves the request. Otherwise, the request is declined.
+ The time off balance for the requested time off type must be equal to or greater than the duration of the requested time off.

## Download snapshot
<a name="download-timeoff-snapshot"></a>

Choose **Download snapshot** to download the full set of the last uploaded time off balance and the net time off balance as of the time of download.

## How the system calculates time off deductions
<a name="how-system-calculates-time-off-deductions"></a>

When a staff's time off is approved, the following logic is used to calculate how many hours are deducted from both the staff's time off balance and the group allowance balance:
+ If the approved time off period overlaps with one or more staff shifts, then:
  + The system derives the deductible time off hours by taking the total number of overlapped hours for shift activities that have the setting **Deduct from time off balance** as **Yes**.
+ If the approved time off period does not have staff shifts that overlap because the schedule for that time period has not been published yet, then:
  + The system would check if the staff is scheduled to work on that day based on the shift profile **Day** (check-box) setting.
    + If the staff is not scheduled to work on this day, or if the approved time off is outside of the configured shift profile time window, then no time off hours will be deducted.
    + If the staff is scheduled to work on that specific day, the system determines the effective shift length based on the configured shift profile. If the shift length is not explicitly set in the profile, the system defaults to the minimum value between the maximum working hours defined in the **Staff Rules** for that staff and the shift window duration specified in the shift profile, effectively setting the effective shift length. In the event that there is no **Maximum working hours** defined for the staff, the system resorts to the shift window duration assigned within the staff's specific shift profile.
    + Based on this effective shift duration, the system would then determine which shift activity group would be used to schedule shifts, and then subtract the duration of all shift activities in this group which have the setting **Deduct from time off balance** as **Yes**.

## Time off deduction logic examples
<a name="timeoff-deduction-examples"></a>

Workforce managers and supervisors can specify which shift activities, in addition to default work activities, will be counted towards their agents' time-off balance. The following highlights an example of this feature:

**There are two time offs configured:**
+ Vacation time - activity name: VACAY\_SK
+ Sick time - activity name: SICK\_SK

Agent 1 has a vacation (VACAY\_SK) balance of 30 hours.

Agent 2 has a sick (SICK\_SK) balance of 12 hours.

Agent 3 has a vacation (VACAY\_SK) balance of 15 hours.

Agent 1, 2 and 3 have a 6-hour shift. In these shifts, there is a 30 minute **Break** activity for which **Deduct from time off balance** is set to **No**.

**Scenarios**
+ Agent 1 requested an all-day time off (VACAY\_SK). Once time off is approved, the system will deduct 5 hours 30 minutes from the current time off balance of 30 hours. 30 minutes for the **Break** activity will not be deducted because the shift activity flag **Deduct from time off balance** is set to **No**. The net balance after time off deduction will become 24 hours and 30 minutes.
+ Agent 2 requested time off outside of their shift hours (between **9:15 am** – **10:15 am**). In this case, given the request is outside of the planned schedule, the system will not deduct from the agent's time off balance.
+ Agent 3 requested time off between **2 am** to **4am**, partially outside of their shift and partially overlapping the shift. The **Deduct from time off balance** **Break** activity falls within the time off request. In this scenario, the system will deduct 1 hour 15 minutes for the duration between **2:45 am** to **4:00 am**. The vacation balance for agent 3 would now be 13 hours and 45 minutes.

![The image displays how the 3 agents are configured for time off using vacation time and sick time.](http://docs.aws.amazon.com/connect/latest/adminguide/images/timeoff-deduction-examples.png)
