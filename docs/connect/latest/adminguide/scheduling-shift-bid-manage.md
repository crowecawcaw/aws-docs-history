

# Review and manage a shift bid
<a name="scheduling-shift-bid-manage"></a>

After you generate a shift bid, you review it, open it for agents to rank their preferences, close it, and then assign shifts.

1. After the bid is generated, the **Schedule Manager** page shows a **Schedule status** of **Bid generation success** and a **Bid status** of **Ready to open**.

1. Choose the schedule name to open the bid details.

1. On the **Overview** tab, you can open or close the bid, review the shift pattern summaries and metrics, and monitor agent preference submissions, as described in the following list:
   + Open or close the bid.  
![The Bid status control, showing the options to open or close the bid.](https://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-shift-bid-bid-status.png)
   + In the **Shift pattern summaries** table, view an overview of all shift patterns with their availability and assignment status, including the **Shift pattern**, **Shift profile**, **Time zone**, **Required agents**, and **Eligible agents**. You can edit the **Required agents** count as needed.  
![The Shift pattern summaries table with its columns for shift and staffing details.](https://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-shift-bid-shift-pattern-summaries.png)
   + View the shift pattern metrics, which show the projected service levels if all available slots are filled.
   + View the agents included in the bid, the status of each agent's preference submission, and the preferences that they submitted.

1. Open the bid. You can open it manually, or let Amazon Connect Customer open it automatically at the start of the bid date range.

1. After the bid is open, agents can rank their shift preferences. For more information, see [How agents enter shift preferences](scheduling-shift-bid-agents.md).

1. Close the bid. You can close it manually, or let Amazon Connect Customer close it automatically at the end of the bid date range. To close it manually, set **Bid status** to **Closed**, and then choose **Save**.
**Note**  
You can re-open a closed bid at any time before you start assignment. After assignment is complete, the bid can no longer be re-opened.

1. To assign shifts to agents, choose **Start assignment**.  
![The bid details page showing the Schedule details panel with the Bid status set to Closed, and the Start assignment button.](https://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-shift-bid-start-assignment.png)

1. After the assignment is complete, the **Schedule status** changes to **Generation success** and the **Bid status** changes to **Completed**.