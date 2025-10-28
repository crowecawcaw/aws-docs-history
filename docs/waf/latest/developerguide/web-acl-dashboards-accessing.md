**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Viewing the dashboards for a protection pack (web ACL)

Follow the procedure in this section to access the protection pack (web ACL) dashboards and set the data filtering criteria. If you recently associated a protection pack (web ACL) with an AWS resource, you might need to wait a few
minutes for data to become available in the dashboards.

The dashboards include the requests for all of the resources that you've associated with the protection pack (web ACL).

###### To view the **Traffic overview** dashboards for a protection pack (web ACL)

1.  Sign in to the AWS Management Console and open the AWS WAF console at
    [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2.  In the navigation pane, choose **protection packs (web ACLs)** and then search for the web
    ACL that you're interested in.
3.  Select the protection pack (web ACL). The console takes you to the protection pack (web ACL)'s page. The **Traffic
    overview** tab is selected by default.
4.  Change the **Data filters** settings as needed.

        * **Terminating rule actions** – Select the terminating actions to
         include in the dashboards. The dashboards summarize the metrics
         for the web requests that had one of the selected actions
         applied by the protection pack (web ACL) evaluation. If you select all of the
         available actions, the dashboards include all evaluated web
         requests. For information about the actions, see [How AWS WAF handles rule and rule group actions](web-acl-rule-actions.md "web-acl-rule-actions.md").
        * **Time range** – Select the time interval to view in the
         dashboards. You can choose to view a time frame relative to now, for
         example the last 3 hours or the last week, and you can select an
         absolute time range from a calendar.
        * **Time zone** – This setting applies when you specify an absolute time
         range. You can use your browser's local time zone or UTC
         (Coordinated Universal Time).

    Review the information in the tabs that you're interested in. The data filter
    selections apply to all of the dashboards. In the graph panes, you can hover the
    cursor over a data point or an area to see any additional details.

###### Count action rules

You can view information for count action matches in one of two places.

- In this **Traffic overview** tab, on the **All traffic**
  dashboard, find the **Top 10 rules** pane and toggle
  **Switch to count action**. With this toggle on,
  the pane shows count rule matches instead of terminating rule
  matches.
- In the protection pack (web ACL)'s **Sampled requests** tab, see a graph of all rule matches
  and actions for the time range that you've set on the **Traffic
  overview** tab. For information about the **Sampled
  requests** tab, see [Viewing a sample of web requests](web-acl-testing-view-sample.md "web-acl-testing-view-sample.md").

###### Amazon CloudWatch metrics

In the dashboard graph panes, you can access the CloudWatch metrics for the graphed data.
Choose the option at the top of the graph pane or from the
**⋮** (vertical ellipsis) dropdown menu inside the
pane.

###### Refreshing the dashboards

The dashboards don't refresh automatically. To update the display, choose the refresh
![Icon to refresh the dashboard graph](images/cloudwatch-refresh-icon.png)
icon.
