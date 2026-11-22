

# Create overtime slots for contact center agents in Connect Customer

You can create overtime slots for specific activities. This feature applies to activities that aren't the **Work** sub-type. Activities with the **Work** sub-type are not available in the Activity list dropdown where a user requests overtime. 

For example, the following image shows three different **Productive** shifts: Overtime, Training, and Work. The activity named Work has the sub-type **Work**.

![The Scheduling page, the shift-activities tab, the sub-type Work.](https://docs.aws.amazon.com/connect/latest/adminguide/images/overtime-slots-1.png)


The following image shows that while requesting Overtime, in the Activity dropdown, only Overtime and Training activities are shown. The productive activity Work with the sub-type **Work** is not shown. 

![The Request Overtime pane, the Activity dropdown list.](https://docs.aws.amazon.com/connect/latest/adminguide/images/overtime-slots-2.png)


**To create overtime slots**

1. Choose the **Make Request** button in the **Published schedule calendar** UI and select **OT**.

1. A supervisor or manager enters the date and time range for overtime.

1. Select the productive activity from the Activity list.

1. Choose **By Staffing group** or **By Staff**.
   + **By Staffing group** – Creates overtime slots and notifies all agents in the selected staffing groups that the slots are available. Agents accept or decline the slots in their schedule calendar, and slots are filled on a first come, first served basis. For more information, see [Contact center agent ability to accept or decline overtime in Connect Customer](agent-accept-decline-ot.md).
   + **By Staff** – Applies overtime directly to the published schedules of the agents that you select. Agents don't receive an offer, and there is no accept or decline step.
**Important**  
When you choose **By Staff**, Connect Customer adds the overtime to the selected agents' published schedules as soon as you choose **Request**. Before you submit a **By Staff** request, make sure that the selected agents have agreed to the overtime.

1. Select the number of required overtime slots.

1. Provide the reason for requesting overtime in the **Reason** text box. For **By Staffing group** requests, agents can view the reason before they accept or decline the overtime slot.

1. Choose **Request**.

After you submit a **By Staff** request, the overtime appears as accepted in the published schedule calendar. The shift details show an accepted timestamp that matches the time the request was submitted, and no agent name. This is expected behavior: Connect Customer applied the overtime, so it didn't record an agent action.