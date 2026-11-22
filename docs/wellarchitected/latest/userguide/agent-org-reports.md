

AWS Well-Architected Agent is in preview release and is subject to change.

# Organization reports

Organization reports are filterable, customizable reports of AWS Well-Architected Agent recommendations across AWS accounts monitored in your organizational agent profile.

**Note**  
Organization reports depend on an organizational profile and on trusted access with AWS Organizations being enabled. For more information, see [Trusted access with AWS Organizations](agent-preferences.md#agent-preferences-trusted-access).

The **Organization reports** dialog in the AWS Well-Architected sidebar lists the reports you have created. For each report in the list, you can do the following:
+ **Download a report:** Download the report directly.
+ **Deliver to an Amazon S3 bucket:** Deliver the report to an S3 bucket that you specify.
+ **Delete a report:** Remove the report.

## Creating a report
<a name="agent-org-reports-create"></a>

**To create a report**

1.  In the top right corner, choose **Create report**. 

1.  Enter a **Report name**. 

1.  Choose any **Recommendation filteres** to filter the report's recommendations by pillar, type, priority, or status. 

1.  In **Report scope**, choose which organizational units and accounts to include either by selecting an OU, individual accounts, or searching in the search field. You can select multiple accounts at once to add into the report. 

1.  When you're finished, choose **Create report**. 

## Report details
<a name="agent-org-reports-details"></a>

Choose a completed report to open its report details. Report details show the following:
+ Any filters that were applied when the report was created.
+ The overall coverage of the report, including recommendations broken down by pillar and by priority.

From the report overview, you can download the report directly, deliver it to an S3 bucket, or delete the report.