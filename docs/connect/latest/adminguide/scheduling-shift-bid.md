

# Shift bidding
<a name="scheduling-shift-bid"></a>

With shift bidding, you let agents influence their schedules by ranking the shifts they prefer, rather than assigning shifts to them directly. As a scheduler, you define the parameters for a shift bid, such as the forecast group, bidding window, scheduling period, and agent ranking. Amazon Connect Customer then generates shift patterns from the shift profiles assigned to agents and opens the bid automatically for a set period. While the bid is open, agents rank the available shift patterns from their calendar in the agent workspace. After the bid closes, Amazon Connect Customer assigns shifts based on each agent's ranked preferences and their assigned rank. This gives agents a better chance of getting the shifts they want, while your contact center still meets its forecasted demand and service level goals.

**To configure shift bidding**
+ Assign additional shift profiles to the agents who will participate in the bid. Amazon Connect Customer uses these profiles to generate the shift patterns that agents rank. You assign them by using the **Additional shift profiles** option in either of the following ways:
  + For all agents in a staffing group, on the **Staffing group details** page.
  + For an individual agent, on the **Staff rules** page.

  You can take one of the following approaches when you assign profiles:
  + **A single flexible profile** – For example, a 9-hour shift anywhere between 6 AM and 10 PM. Amazon Connect Customer uses the forecasted demand to determine the shift patterns within that window.  
![The Edit staffing group page with a single flexible profile added under Additional shift profiles.](https://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-shift-bid-staffing-group-flexible-profile.png)
  + **Multiple working profiles**, where each profile is a fixed working window – for example, Monday-Friday 8 AM-5 PM, Tuesday-Saturday 8 AM-5 PM. Amazon Connect Customer generates shift patterns from the fixed windows that you define.  
![The Edit staffing group page with multiple fixed working profiles added under Additional shift profiles.](https://docs.aws.amazon.com/connect/latest/adminguide/images/wfm-shift-bid-staffing-group-fixed-profiles.png)