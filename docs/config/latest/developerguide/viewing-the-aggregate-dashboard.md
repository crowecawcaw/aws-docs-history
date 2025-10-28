# Viewing Compliance and Inventory Data in the Aggregator

Dashboard for AWS Config

The dashboard on the **Aggregators** page displays the configuration data
of your aggregated AWS resources. It provides an overview of your rules, conformance packs, and their
compliance
states.

The dashboard provides the total resource count of AWS resources. The resource types and
source accounts are ranked by the highest number of resources. It also provides a count of
compliant and noncompliant rules and conformance packs. The noncompliant rules are ranked by
highest number of noncompliant resources. The noncompliant conformance packs and source
accounts are ranked by the highest number of noncompliant rules.

After setting up AWS Config, it starts aggregating data from the specified source accounts
into an aggregator. It might take a few minutes for the compliance status of rules to
display.

## Using the Aggregator Dashboard

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Navigate to the **Aggregators** page.
   You can view:
   - Your rules and their compliance states.
   - Your conformance packs and their compliance states.
   - Your AWS resources and their configuration
     data.

3. Choose an aggregator from the dashboard. Filter through your aggregators
   by aggregator name. You can view the following widgets:
   - **Resource inventory**

   View the top 10
   resource types from the selected aggregator, in descending order
   by the resource count.
   Choose
   the total number of resources for the selected aggregator, displayed in
   parentheses after **Resource inventory**,
   to
   go to the aggregated **Resources** page, where you can
   view all the resources for an aggregator. Alternatively, choose a
   resource type in the widget to go to the aggregated **Resources**
   page, filtered using the specified resource type.
   - **Accounts by resource count**

   View
   the top five accounts from the selected aggeregator in the descending
   order by the resource count. Choose an account in the widget
   to go to the **Resources** page, filtered using the
   specified account.
   - **Noncompliant rules**

   View the top five
   noncompliant rules from the selected Aggregator, in descending order
   by the number of noncompliant resources.
   Choose
   a rule in the widget to go to the details page for the specified rule.
   Choose **View all noncompliant rules** to go to the
   aggregated **Rules** page, where you can view all
   the rules for an aggregator.
   - **Accounts by noncompliant rules**

   View the
   top five accounts from the selected aggregator, in descending order
   by the number of noncompliant rules. Choose an account in the
   widget to go to the aggregated **Rules** page, where
   you can view all the rules for an aggregator filtered using the
   specified account.
   - **Accounts by noncompliant conformance packs**

   View the top five accounts from the selected aggregagtor, in
   descending order by the number of noncompliant conformance
   packs.
   Choose
   an account in the widget to go to the aggregated **Conformance
   Pack** page, where you can view all conformance packs for
   an aggregagtor filtered using the specified account.

4. In the left navigation pane, choose one of the following options from the
   dropdown menu:
   - **Compliance dashboard**

   View automated compliance dashboards by using the widgets that
   summarize insights about resource compliance within your aggregator. You
   can see data such as the top 10 resource types by noncompliant
   resources, and top 10 account level conformance packs by noncompliant
   rules. For information about these graphs and charts, see [Compliance dashboards](viewing-the-aggregate-dashboard.md#aggregate-compliance-dashboard "viewing-the-aggregate-dashboard.md#aggregate-compliance-dashboard").
   - **Conformance packs**

   View all conformance packs that are created and linked to the
   different AWS accounts within your aggregator. The **Conformance Pack** page displays a table that
   lists the name, Region, account ID, and compliance status of each
   conformance pack. From this page, you can choose a conformance pack and
   **View details** for more information about its
   rules and resources and their compliance status.
   - **Rules**

   View all rules that are created and linked to the different AWS
   accounts within your aggregator. The **Rules** page displays a table that lists the name,
   compliance status, Region, and account of each rule. From this page, you
   can choose a rule and **View details** for information,
   such as its aggregator, Region, account ID, and resources in
   scope.
   - **Inventory dashboard**

   View automated inventory dashboards by using the widgets that
   summarize insights about resource configuration data within your
   aggregator. You can see data such as the top 10 resource types by
   resource count, and the top 10 accounts by resource count. For
   information about these graphs and charts, see [Inventory dashboards](viewing-the-aggregate-dashboard.md#aggregate-resource-dashboard "viewing-the-aggregate-dashboard.md#aggregate-resource-dashboard").
   - **Resources**

   View all resources that are recorded and linked to the different AWS
   accounts within your aggregator. From the **Resource** page, choose a resource and **View
   details** to view its details, the rules associated with
   it, and the current resource configuration. You can also see information
   about the resource, such as its aggregator, Region, account ID, resource
   name, resource type, and resource ID.
   - **Authorizations**

   View
   and manage all accounts currently authorized or pending authorization.
   From the **Authorizations** page, choose **Add
   authorization** to provide access to another account.
   Choose **Delete authorization** to revoke access from
   an account ID.

###### Note

**Troubleshooting**

You might see the **Data collection from all source accounts and regions is
incomplete** message displayed in the aggregated view for the following
reasons:

- The transfer of
  noncompliant
  AWS Config rules and configuration data of AWS resources is in progress.
- AWS Config can't find rules to match the filter that you applied.
  Select
  the appropriate account or Region, and
  try
  again.
  You might see this message display in the aggregated view:
  **Data
  collection from your organization is incomplete. You can view the below data
  only for 24 hours.** It displays for the following reasons:

- AWS Config can't access your organization details because of an IAM role that
  is not valid. If the IAM role remains not valid for more than 24 hours,
  AWS Config deletes the data for the entire organization.
- AWS Config service access is disabled in your organization.

## Compliance Dashboard

View automated compliance dashboards by using widgets that summarize insights about
resource compliance within your aggregator This dashboard displays only rules with compliance
results.

###### Note

**Limitations**

The insights in the compliance dashboard are provided by the Advanced Queries feature of AWS Config, and this feature does not support nested structures or unpacking nested arrays.
This means that the compliance dashboard displays the overall compliance of a resource and not the compliance status for each specific rule which reports on a resource.

For example, if you check the configuration item (CI) for the resource type `AWS::Config::ResourceCompliance`, the dashboard will display the compliance results for all the rules that report on that resource.
If there are 10 rules that report on the resource, 9 of them are COMPLIANT, and only 1 is NON_COMPLIANT, the overall compliance of that resource will be NON_COMPLIANT.

**Compliance Summary By Resources**

Displays a pie chart comparing the number of compliant resources to
noncompliant resources from the selected aggregator. Hover over the chart
to see the exact number and percentage of compliant and noncompliant
resources.

The data displayed depends on the settings of the configuration recorder
for each account in the selected aggregator, and the Regions where the
selected aggregator is configured to collect data.

**Top 10 resource types by noncompliant resources**

Displays a horizontal bar graph comparing up to 10 resource types from the
selected aggregator in descending order by the number of noncompliant
resources. Hover over the graph to see the exact number of noncompliant
resources for each resource type.

The data displayed is dependent on the settings of the configuration
recorder for each account in the selected aggregator and the Regions where
the selected aggregator is configured to collect data.

**Top 10 accounts by noncompliant resources**

_Top 10 accounts by noncompliant resources_ displays a horizontal bar graph comparing
up to 10 accounts from the selected aggregator in descending order by the number of noncompliant resources.
Hover over the graph to see the exact number of noncompliant resources for each account.

The data displayed depends on the settings of the configuration recorder
for each account in the selected aggregator, and the Regions where the
selected aggregator is configured to collect data.

**Top 10 regions by noncompliant resources**

Displays a horizontal bar graph comparing up to 10 Regions where the
selected aggregator collects data in descending order by the number of
noncompliant resources. Hover over the graph to see the exact number of
noncompliant resources for each Region.

The data displayed depends on the settings of the configuration recorder
for each account in the selected aggregator.

**Top 10 account level conformance packs by noncompliant rules**

Displays a horizontal bar graph comparing up to 10 account level
conformance packs from the selected aggregator in descending order by the
number of noncompliant rules. Hover over the graph to see the percentage of
compliant and noncompliant rules for each account level conformance
pack.

The data displayed depends on the settings of the configuration recorder
for each account in the selected aggregator, and the Regions where the
selected aggregator is configured to collect data.

**Top 10 organization level conformance packs by noncompliant rules**

Displays a horizontal bar graph comparing up to 10 organizational level
conformance packs from the selected aggregator in descending order by the
number of noncompliant rules. Hover over the graph to see the percentage of
compliant and noncompliant rules in each organizational level conformance
pack.

The data displayed is dependent on the settings of the configuration
recorder for each account in the selected aggregator and the Regions where
the selected aggregator is configured to collect data.

**Top 10 accounts by noncompliant rules across conformance packs**

_Top 10 accounts by noncompliant rules across conformance packs_ displays a horizontal bar graph comparing up to 10 accounts from the selected aggregator in descending order by the number of noncompliant rules across all your conformance packs. Hover over the graph to see the exact number of noncompliant rules in each account.

The data displayed is dependent on the settings of the configuration
recorder for each account in the selected aggregator and the Regions where
the selected aggregator is configured to collect data.

## Inventory Dashboard

View automated inventory dashboards by using widgets that summarize insights about
resource configuration data within your aggregator.

**Top 10 resource types by resource count**

Displays a horizontal bar graph comparing up to 10 resource types from the
selected aggregator in descending order by resource count. Hover over the
graph to see the exact number of resources for each resource type.

The data displayed depends on the settings of the configuration recorder
for each account in the selected aggregator, and the Regions where the
selected aggregator is configured to collect data.

**Resource count by region**

Displays a horizontal bar graph comparing up to 10 Regions where the
selected aggregator collects data in descending order by resource count.
Hover over the graph to see the exact number of resources for each
Region.

The data displayed depends on the settings of the configuration recorder
for each account in the selected aggregator.

**Top 10 accounts by resource count**

Displays a horizontal bar graph comparing up to 10 accounts from the
selected aggregator in descending order by resource count. Hover over the
graph to see the exact number resources for each resource type.

The data displayed is dependent on the settings of the configuration
recorder for each account in the selected aggregator and the Regions where
the selected aggregator is configured to collect data.

**Resource count by Amazon EC2 service resource types**

Displays a horizontal bar graph comparing Amazon EC2 resource types from the
selected aggregator in descending order by resource count. Hover over the
graph to see the exact number of resources for each Amazon EC2 resource
type.

The data displayed depends on the settings of the configuration recorder
for each account in the selected aggregator, and the Regions where the
selected aggregator is configured to collect data. To use this chart, you
must configure the recorder to record Amazon EC2 resource types. For more
information, see [Selecting
Which Resources AWS Config Records](select-resources.md "select-resources.md").

**Top 10 EC2 instance types used**

Displays a horizontal bar graph comparing up to 10 Amazon EC2 instance
types from the selected aggregator in descending order by usage. Hover over
the graph to see usage for each EC2 instance type.

The data displayed depends on the settings of the configuration recorder
for each account in the selected aggregator and the Regions where the
selected aggregator is configured to collect data. To use this chart, you
must configure the recorder to record the EC2 instance resource type. For
more information, see [Recoding AWS Resources](select-resources.md "select-resources.md").

**EBS Volume counts by volume type and size**

Displays a vertical bar graph comparing EBS volumes from the selected
aggregator by resource count. Hover over the graph to see the count and size
breakdown for each type of EBS volume.

The data displayed depends on the settings of the configuration recorder
for each account in the selected aggregator and the Regions where the
selected aggregator is configured to collect data. To use this chart, you
must configure the recorder to record the EC2 volume resource type. For more
information, see [Selecting
Which Resources AWS Config Records](select-resources.md "select-resources.md").

**Number of EC2 instances that are running vs. stopped by type**

Displays a horizontal bar graph comparing EC2 instance types from the
selected aggregator that are running to EC2 instances that are stopped by
instance type. Hover over the graph to see the exact number of stopped and
running EC2 instances for each type.

The data displayed depends on the settings of the configuration recorder
for each account in the selected aggregator and the Regions where the
selected aggregator is configured to collect data. To use this chart, you
must configure the recorder to record the EC2 instance resource type. For
more information, see [Recoding AWS Resources](select-resources.md "select-resources.md").
