

# Set up shift exchange in Connect Customer
<a name="shift-exchange"></a>

You can set up Connect Customer to allow agents to exchange shifts with each other. Agents can initiate shift trades directly from their agent calendar. They don't need to send emails their manager. This self-service functionality enables agents to manage unexpected life events and achieve better work-life balance.

Managers can approve shift exchange requests manually from their **Published schedule calendar**. Or, approvals can be automatic if the request meets certain criteria that you specify. 

Before completing the steps in this topic, you need to [create a shift trade group](scheduling-create-shift-trade-groups.md). A *shift trade group* is a list of agents in the same forecast group who can trade shifts with each other.

**Tip**  
Want to watch a video that shows how to set up shift exchange? See [How Schedulers Configure the Shift Exchange Feature](https://www.youtube.com/watch?v=skhoJqb4hzY) on the Connect Customer Enablement channel on YouTube.

**To define how shift exchange will work for the agents in a shift trade group**

1. Log in to the Connect Customer admin website with an account that has security profile permissions for **Scheduling**, **Schedule manager - Edit**. 

   For more information, see [Assign permissions](required-optimization-permissions.md). 

1. On the Connect Customer navigation menu, select **Analytics and optimization**, **Scheduling**.

1. On the **Scheduling** page, choose the **Shift activities** tab, choose the shift activity you want to edit, and choose **Edit**.

1. On the **Edit shift activities** page, in the **Trade behavior** box, choose one of the following values:
   + **Do not trade shift**: This is the default. Choose this option to block the trade if this shift activity exists. 
**Important**  
For for the system-created activity **Work**, the default configuration is **Keep activity with shift**. 
   + **Keep activity with shift**: Choose this option to move the activity together with the shift. 
   + **Remove from shift**: Choose this option to remove the activity from the shift. 

   The following image shows the **Trade behavior** dropdown list.  
![The Edit shift activities page, the Trade behavior dropdown list.](http://docs.aws.amazon.com/connect/latest/adminguide/images/shiftexchange-tradebehavior.png)

1. Choose **Save**.

1. On the **Scheduling** page, choose **Staff rules**. In the **Eligible to trade shifts** box, choose **Yes** to allow agents to trade shift with each other. Default = Yes.

   The **Eligible to trade shifts** dropdown box is shown in the following image.   
![The Scheduling page, the Staff rules tab, the Eligible to trade shift dropdown list.](http://docs.aws.amazon.com/connect/latest/adminguide/images/shiftexchange-shiftrules.png)