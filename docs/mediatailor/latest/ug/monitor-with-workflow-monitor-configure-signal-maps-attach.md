# Attaching alarm and event templates to the signal map of your AWS media workflow

After you have created alarm and event templates, you need to attach these to
a signal map. Any of the alarm and event templates you have created can be
attached to any discovered signal maps.

###### To attach alarm and event templates to your signal map

1. From the workflow monitor console's navigation pane, select **Signal
   maps** and select the signal map you want to work
   with.
2. In the upper-right of the signal map page, in the **CloudWatch
   alarm template groups** tab, select **Attach
   CloudWatch alarm template groups**.
   1. In the new section that opens, choose all of the alarm
      template groups that you want to apply to this signal map, then
      select **Add**. This will cause the selected
      alarm template groups to move to the **Attached CloudWatch
      alarm template groups** section.
   2. Selecting **Save** will save your changes and
      return you to the signal map page.

3. At the right of the signal map page, select the **EventBridge rule
   template groups** tab then select **Attach EventBridge
   rule template groups**.
   1. In the new section that opens, choose all of the event
      template groups that you want to apply to this signal map, then
      select **Add**. This will cause the selected
      rule template groups to move to the **Attached EventBridge rule
      template groups** section.
   2. Selecting **Save** will save your changes and
      return you to the signal map page.

4. You have assigned CloudWatch alarm and EventBridge rule templates to the signal
   map, but the monitoring is not yet deployed. The next section will cover
   the deployment of the monitoring resources.
