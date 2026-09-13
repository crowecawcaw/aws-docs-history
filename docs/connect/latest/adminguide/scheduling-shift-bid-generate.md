

# Generate a shift bid
<a name="scheduling-shift-bid-generate"></a>

To create a shift bid, you use the **Create shift bid** wizard, which walks you through four steps: **Configure schedule details**, **Configure shift bid details**, **Optimize schedule**, and **Review and create**.

1. Log in to the Connect Customer admin website with an account that has security profile permissions for **Scheduling**, **Schedule manager - Edit**. For more information, see [Assign permissions](required-optimization-permissions.md).

1. On the Amazon Connect Customer navigation menu, choose **Analytics and optimization**, **Scheduling**.

1. Choose the **Schedule Manager** tab, choose **Generate new**, and then choose **Shift bid**. The **Create shift bid** wizard opens.  
![The Generate new menu expanded, showing the Schedule and Shift bid options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-shift-bid-generate-new-menu.png)

## Step 1: Configure schedule details
<a name="scheduling-shift-bid-configure-schedule"></a>

On the **Configure schedule details** page, configure the basic details of the shift bid and schedule.

1. For **Bid name**, enter a name for the shift bid.

1. For **Forecast group**, choose the forecast group to use for the scheduling requirements.

1. (Optional) For **Description**, enter a description for the shift bid.

1. For **Bid date range**, specify the period during which agents can rank their shift preferences.

1. For **Schedule date range**, specify the period that the generated schedule covers.

1. Choose **Next**.

![The Configure schedule details page of the Create shift bid wizard.](https://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-shift-bid-configure-schedule-details.png)


## Step 2: Configure shift bid details
<a name="scheduling-shift-bid-configure-details"></a>

On the **Configure shift bid details** page, choose how to rank agents and select the agents to include in the bid.

1. Under **Staff ranking method**, choose one of the following:
   + **Upload CSV with staff/agent rankings** – Upload your own staff ranking in CSV format.
   + **Random ranking** – Assign a random ranking to all agents.

1. Choose **Generate staff ranking**. After the ranking is generated, each agent's rank appears in the **Staff in schedule** table.

1. In the **Staff in schedule** table, select the agents to include in the bid. For any agent who should receive a fixed schedule instead of participating in the bid, select **Auto-assigned schedule**. Only the agents you select are included in this schedule.

1. Choose **Next**.

![The Configure shift bid details page, showing the Staff ranking method options and the Staff in schedule table.](https://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-shift-bid-configure-details.png)


## Step 3: Optimize schedule
<a name="scheduling-shift-bid-optimize"></a>

On the **Optimize schedule** page, select the optimization goals for each channel in your forecast:
+ **Voice**: **Service level** or **Average speed of answer**
+ **Chat**: **Service level** or **Average speed of answer**
+ **Task**: **Service level** or **Average time to complete**
+ **Email**: **Service level** or **Average time to complete**

For Task and Email, use **Service level** when the work is done synchronously – for example, when a task is picked up within 5 minutes of arriving. Use **Average time to complete** when the work can be deferred and is completed over hours or days.

**Note**  
Backlog metrics are only available when **Average time to complete** is selected as the optimization goal.

Choose **Next**.

## Step 4: Review and create
<a name="scheduling-shift-bid-review-create"></a>

On the **Review and create** page, review your shift bid configuration. To change any section, choose **Edit**. When you're satisfied with the configuration, choose **Generate shift bid**.

![The Review and create page, showing summaries of the Configure schedule details, Configure shift bid details, and Optimize schedule steps, and the Generate shift bid button.](https://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-shift-bid-review-create.png)
