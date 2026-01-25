# Create a trigger for a Region switch plan

If you want to automate recovery for your application in Region switch, you can create one or more triggers
for your Region switch plan. Triggers automatically start executing a Region switch plan, based on CloudWatch alarm conditions
that you choose.

# To create a trigger for a Region switch plan

1. After you create a plan, on the **Plan details** page, select the **Triggers** tab.
2. Choose **Manage triggers**.
3. Select the workflows that you want to automate execution for, and then choose **Add trigger**.
4. Provide a description for the trigger.
5. Select a CloudWatch alarm, and then select up to 10 CloudWatch alarms to create the conditions for the trigger.

When you select more than one condition, all conditions must be met before automated execution of the plan will start.
The trigger starts plan execution when a CloudWatch alarm transitions to meet the conditions for the trigger. When the trigger is added to the plan, if the conditions are already met, the plan does not execute, which prevents unintended failover events.
