

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Using the Audit Manager dashboard
<a name="dashboard"></a>



With the Audit Manager dashboard, you can visualize non-compliant evidence in your active assessments. It's a convenient and fast way to monitor your assessments, stay informed, and remediate issues proactively. By default, the dashboard provides a top-down, aggregated view of all your active assessments. Using this view, you can visually identify issues in your assessments without first needing to sift through vast amounts of individual evidence. 

The dashboard is the first screen that you see when you sign in to the Audit Manager console. It contains two widgets that show the data and key performance indicators (KPIs) that are most relevant to you. Using an assessment filter, you can refine this data to focus on the KPIs for a specific assessment. From there, you can review control domain groupings to identify which controls have the most non-compliant evidence. Then, you can explore the underlying controls to examine and remediate issues.

**Note**  
If you’re a first-time Audit Manager user or you don’t have any active assessments, no data is displayed in the dashboard. To get started, [create an assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-assessments.html). This starts the ongoing collection of evidence. After a 24-hour period, aggregated evidence data will start to appear in the dashboard. You can read the following sections to learn how to understand and interpret this data.

This page covers the following topics:

**Topics**
+ [Dashboard concepts and terminology](#dashboard-concepts-terminology)
+ [Dashboard elements](#dashboard-elements)
+ [Next steps](#dashboard-next-steps)
+ [Additional resources](#dashboard-troubleshooting)

## Dashboard concepts and terminology
<a name="dashboard-concepts-terminology"></a>

This section covers important things to know about the Audit Manager dashboard before you get started using it.

**Permissions and visibility**  
Both [audit owners](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#audit-owner) and [delegates](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#delegate-persona) have access to the dashboard. This means that both of these personas can see the metrics and aggregates for all active assessments in your AWS account. Having access to the same information enables all of your team to focus on the same KPIs and goals. 

**Filters**  
Audit Manager provides a page-level [Assessment filter](#dashboard-assessment-filters) that you can apply to all of the widgets on your dashboard. 

**Non-compliant evidence**  
The dashboard highlights the controls in your assessments that have [compliance check evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#evidence) with a *non-compliant* conclusion. Compliance check evidence relates to controls that use AWS Config or AWS Security Hub CSPM as a data source type. For this evidence type, Audit Manager reports the result of a compliance check directly from those services. If Security Hub CSPM reports a *Fail* result, or if AWS Config reports a *Non-compliant* result, Audit Manager classes the evidence as non-compliant. 

**Inconclusive evidence**  
Evidence is *inconclusive* if a compliance check isn’t available or applicable. As a result, no compliance evaluation can be made. This is the case if a control uses AWS Config or AWS Security Hub CSPM as a data source type but you didn’t enable those services. This is also the case if the control uses a data source type that doesn't support compliance checks, such as manual evidence, AWS API calls, or AWS CloudTrail. In the console, evidence with a compliance check status of *not applicable* is classified as *inconclusive* in the dashboard.  
You can use the inconclusive evidence to manually evaluate a control's compliance.   
Inconclusive evidence doesn't indicate failure, it signals that you should manually evaluate the evidence for compliance.

**Compliant evidence**  
Evidence is *compliant* if a compliance check reported no issues. This is the case if Security Hub CSPM reports a *Pass* result, or AWS Config reports a *Compliant* result.

**Control domains**  
The dashboard introduces the concept of a *control domain*. You can think of a control domain as a general category of controls that isn’t specific to any one framework. Control domain groupings are one of the most powerful features of the dashboard. Audit Manager highlights the controls in your assessments that have non-compliant evidence, and groups them by control domain. Using this feature, you can focus your remediation efforts on specific subject domains as you prepare for an audit.   
A control domain is different to a *control set*. A control set is a framework-specific grouping of controls that’s typically defined by a regulatory body. For example, the PCI DSS framework has a control set named *Requirement 8: Identify and authenticate access to system components*. This control set falls under the control domain of *Identity and access management*.

**Eventual consistency of data**  
The dashboard data is *eventually consistent*. This means that, when you read data from the dashboard, it might not instantly reflect the results of a recently completed write or update operation. If you check again within a few hours, the dashboard should reflect the latest data.

**Data from deleted and inactive assessments**  
The dashboard displays data from active assessments. If you delete an assessment or change its status to inactive on the same day that you view the dashboard, data is included for that assessment as follows.  
+ **Inactive assessments** – If Audit Manager collected evidence for your assessment before you changed it to inactive, that evidence data is included in the dashboard counts for that day. 
+ **Deleted assessments** – If Audit Manager collected evidence for your assessment before you deleted it, that evidence data isn’t included in the dashboard counts for that day.

## Dashboard elements
<a name="dashboard-elements"></a>

The following sections cover the different components of the dashboard.

**Topics**
+ [Assessment filter](#dashboard-assessment-filters)
+ [Daily snapshot](#dashboard-daily-snapshot)
+ [Controls with non-compliant evidence grouped by control domain](#dashboard-controls-by-domain)

### Assessment filter
<a name="dashboard-assessment-filters"></a>

You can use the assessment filter to focus on a specific active assessment.

By default, the dashboard displays aggregated data for all your active assessments. If you want to view data for a specific assessment, you apply an assessment filter. This is a page-level filter that applies to all widgets on the dashboard. 

![Screenshot of the assessment filter dropdown on the Audit Manager dashboard.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/dashboard-assessment_filter-console.png)


To apply the assessment filter, select an assessment from the drop-down list at the top of the dashboard. This list shows up to 10 of your active assessments. The most recently created assessments appear first. If you have many active assessments, you can start typing the name of an assessment to quickly find it. After you select an assessment, the dashboard displays data for that assessment only. 

### Daily snapshot
<a name="dashboard-daily-snapshot"></a>

This widget shows a snapshot of the current compliance status of your active assessments. 

The daily snapshot reflects the latest data that was collected on the date at the top of the dashboard. The date and time on the dashboard are represented in Coordinated Universal Time (UTC). It’s important to understand that these numbers are daily counts based on this timestamp. They aren't a total sum to date. 

By default, the daily snapshot shows the following data for all your active assessments:

1. **Controls with non-compliant evidence** - The total number of controls that are associated with non-compliant evidence. 

1. **Non-compliant evidence** - The total amount of compliance check evidence with a non-compliant conclusion. 

1. **Active assessments** - The total number of your active assessments. Choose this number to see links to these assessments.

![Screenshot of the daily snapshot widget on the Audit Manager dashboard.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/dashboard-daily_snapshot-console.png)


The daily snapshot data changes based on the [Assessment filter](#dashboard-assessment-filters) that you apply. When you specify an assessment, the data reflects the daily counts for that assessment only. In this case, the daily snapshot shows the name of the assessment that you specified. You can choose the name of the assessment to open it.

![Screenshot of the daily snapshot widget when an assessment filter is applied.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/dashboard-daily_snapshot_with_assessment_filter_applied-console.png)


### Controls with non-compliant evidence grouped by control domain
<a name="dashboard-controls-by-domain"></a>

You can use this widget to identify which controls have the most non-compliant evidence. 

By default, the widget shows the following data for all your active assessments:

1. **Control domain** – A list of the [control domains](#control-domain) that are associated with your active assessments. 

1. **Evidence breakdown** – A bar chart that shows a breakdown of the evidence compliance status.

![Screenshot of controls with non-compliant evidence grouped by domain.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/dashboard-controls_with_noncompliant_evidence_grouped_by_domain_collapsed-console.png)


To expand a control domain, choose the arrow next to its name. When expanded, the console shows up to 10 controls for each domain. These controls are ranked according to the highest total count of non-compliant evidence. 

The data in this widget changes based on the [Assessment filter](#dashboard-assessment-filters) that you apply. When you specify an assessment, you see data for that assessment only. In addition, you can also download a CSV file for each available control domain in the assessment. 

![Screenshot that shows the CSV download option for a control domain.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/dashboard-controls_with_noncompliant_evidence_grouped_by_domain-csv-console.png)


The .csv file includes the full list of controls in the domain that are associated with non-compliant evidence. The following example shows the CSV data columns with fictionalized values.

![Screenshot of a sample .csv file that shows a list of controls that have non-compliant evidence.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/dashboard-csv-file.png)


Lastly, when you apply an assessment filter, the control names under each domain are hyperlinked. Choose any control to open the control details page in the specified assessment. 

![Screenshot of controls with non-compliant evidence grouped by domain and filtered by assessment.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/dashboard-controls_with_noncompliant_evidence_grouped_by_domain-console.png)


**Tip**  
Using the control details page as your starting point, you can move from one level of detail to the next.   
**Control details page** - On this page, the [Evidence folders tab](review-controls.md#review-evidence-folders) lists daily folders of evidence that Audit Manager collected for that control. For more detail, choose a folder.
**Evidence folder -** Next, you can review an [Evidence folder summary](review-evidence-folders-detail.md#review-evidence-folders-summary-summary) and a list of the evidence in that folder. For more detail, choose an individual evidence item. 
**Individual evidence** - Lastly, you can explore [individual evidence details](https://docs.aws.amazon.com/audit-manager/latest/userguide/review-evidence.html). This is the most granular level of evidence data. 

## Next steps
<a name="dashboard-next-steps"></a>

Here are some next steps that you can take after reviewing the dashboard.
+ **Download a CSV file** – Find the assessment and control domain that you want to focus on, and [download the full list of related controls with non-compliant evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/dashboard.html#dashboard-csv).
+ **Review a control** – After you identify a control that needs remediation, you can [review the control](https://docs.aws.amazon.com/audit-manager/latest/userguide/review-controls.html). 
+ **Delegate a control for review** – If you need assistance reviewing a control, you can [delegate a control set for review](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-audit-owners-delegating-a-control-set.html).
+ **Edit your assessment** – If you want to change the scope of an active assessment, you can [edit the assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-assessment.html).
+ **Update the status of your assessment** – If you want to stop collecting evidence for an assessment, you can [change the assessment status to inactive](https://docs.aws.amazon.com/audit-manager/latest/userguide/change-assessment-status-to-inactive.html).

## Additional resources
<a name="dashboard-troubleshooting"></a>

To find answers to common questions and issues, see [Troubleshooting dashboard issues](dashboard-issues.md) in the *Troubleshooting* section of this guide.