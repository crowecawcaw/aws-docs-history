# View and continue an open

investigation

Use the steps in this section to view and continue and existing investigation

###### To view and continue an investigation

1. If you aren't already on the page for the investigation, do the
   following:
   1. Open the CloudWatch console at
      [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
   2. In the left navigation pane, choose **AI
      Operations**, **Investigations**.
   3. Choose the name of the investigation.

2. The **Feed** section displays the items that have been added
   to the investigation findings, including the metric or alarm that was originally
   selected to start the investigation with.

The pane on the right includes tabs. Choose the
**Suggestions** tab. 3. The **Suggestions** tab displays
_observations_ of other telemetry that CloudWatch investigations has found
that might be related to the investigation. It might also include
_hypotheses_, which are possible reasons or root causes
that CloudWatch investigations has found for the situation.

Both observations and hypotheses are written in natural language by
CloudWatch investigations.

You have several options:

    * For each suggestion, you can choose **Accept** or
     **Discard**.


    When you choose **Accept**, the suggestion is added
     to the **Feed** section, and CloudWatch investigations uses this information
     to direct further scanning and suggestions.


    If you choose **Discard**, the suggestion is moved to
     the **Discarded** tab.
    * For each observation-type suggestion, you can choose to expand the
     graph in the **Suggestions** tab, or open it in the
     CloudWatch console to see more details about it.
    * Some of the observations might be results of CloudWatch Logs Insights queries
     that CloudWatch investigations ran as part of the investigation. When an observation is a
     CloudWatch Logs Insights query result, the query itself is displayed as part of
     the observation. You can edit the query and re-run it. To do so, choose
     the vertical ellipsis menu icon
    ![An example of a CloudWatch overview home page, showing alarms and their current state, and examples of other metrics graph widgets that might appear on the overview home page.](/images/AmazonCloudWatch/latest/monitoring/images/vmore.png)
     by the results, and then choose **Open in
     Logs Insights**. For more information, see [Analyzing
     log data with CloudWatch Logs Insights](../logs/AnalyzingLogData.md "../logs/AnalyzingLogData.md").
    * If you know of telemetry in an AWS service that might apply to this
     investigation, you can go to that service's console and add the
     telemetry to the investigation. For example, to add a Lambda metric to
     the investigation, you can do the following:




    	1. Open the Lambda console.
    	2. In the **Monitor** section, find the
    	 metric.
    	3. Open the vertical ellipsis context menu
    	![An example of a CloudWatch overview home page, showing alarms and their current state, and examples of other metrics graph widgets that might appear on the overview home page.](/images/AmazonCloudWatch/latest/monitoring/images/vmore.png)
    	 for the metric, choose
    	 **Investigate**, **Add to
    	 investigation** Then, in the
    	 **Investigate** pane, select the name of
    	 the investigation.
    * When you view a hypothesis in the **Suggestions**
     tab, you can choose **Show reasoning** to display the
     data that CloudWatch investigations used to generate the hypothesis. For hypotheses involving
     multiple resources, you may also see a visual representation showing the
     causal relationships between the resources as connected nodes.
    * You can choose the **Discarded** tab and view the
     suggestions that have been previously discarded. To add one of them to
     the findings, choose **Restore to findings**.
    * To add notes to the findings, choose **New note** in
     the **Feed** pane. Then enter your notes and choose
     **Add**.

4. When you add a hypothesis to the **Feed** area, it might
   display **Show suggested actions**. If so, choosing this
   displays possible actions that you can take, assuming that hypothesis is correct
   about the issue. Possible actions include the following:
   - **Documentation suggestions** are links to AWS
     documentation that can help you understand the issue that you are
     working on, and how to solve it. To view suggested documentation, choose
     its **Review** link
   - **Runbook suggestions** are suggestions that leverage
     the pre-defined _runbooks_ in Systems Manager
     Automation. Each runbook defines a number of steps for performing a task
     on an AWS resource. For information about continuing with a runbook
     action, see [Reviewing and executing suggested
     runbook remediations for CloudWatch investigations](suggested-investigation-actions.md "suggested-investigation-actions.md").

   ###### Important

   There is a charge for executing an Automation runbook. However,
   CloudWatch investigations provides you with a preview of actions that a suggested runbook
   takes, giving you an opportunity to better evaluate whether to
   execute the runbook. For information about Automation pricing, see
   [AWS Systems Manager pricing for
   Automation](https://aws.amazon.com/systems-manager/pricing/#Automation "https://aws.amazon.com/systems-manager/pricing/#Automation").

5. (Optional) Choose **Incident report** to create a
   comprehensive incident analysis document. For
   more information, see [Generate incident reports](Investigations-Incident-Reports.md "Investigations-Incident-Reports.md").
6. When you are ready to end an investigation, choose **End
   investigation** and then optionally add final notes. The
   investigation status changes to **Archived**. You can restart
   archived investigations by opening the investigation page and choosing
   **Restart investigation**.

###### Note

At some point, you might see **Completed the analysis. Finished with the
investigation.** displayed above the **Feed** area. If
you then add more telemetry to the findings, this message changes and CloudWatch investigations begins
scanning your telemetry again, based on the new data that you added to the
findings.
