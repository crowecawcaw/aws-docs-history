

# Create cost control rules for your Lightsail for Research virtual computers
<a name="create-cost-control-rules"></a>

Complete the following steps to create a rule for your Lightsail for Research virtual computer.

**Note**  
The only supported rule action at this time is to stop a virtual computer. CPU utilization is the only metric currently monitored by rules, and the only supported operation is *less than or equal to*.

1. Sign in to the [Lightsail for Research console](https://lfr.console.aws.amazon.com/ls/research).

1. Choose **Cost control** in the navigation pane.

1. Choose **Create rule**.

1. Select the resource to apply the rule to.

1. Specify the CPU utilization percentage and time period at which the rule should run.

   For example, you can specify 5 percent and 30 minutes. Lightsail for Research automatically stops the computer when its CPU utilization is less than or equal to 5 percent during a 30-minute period.

1. Choose **Create rule**.

1. Confirm that the information for your new rule is correct, and then choose **Confirm**.