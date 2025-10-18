# Getting started with CloudWatch automatic dashboards

The CloudWatch home page automatically displays metrics about every AWS service you use.
 You can additionally create custom dashboards to display metrics about your custom
 applications, and display custom collections of metrics that you choose.

Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").

The CloudWatch overview home page appears.


![An example of a CloudWatch overview home page, showing alarms and their current state, and examples of other metrics graph widgets that might appear on the overview home page.](images/CW-default-dashboard-update.png)
The overview displays the following items, refreshed automatically.


* **Alarms by AWS service** displays a list of AWS services you use in your account, along with
 the state of alarms in those services. Next to that, two or four alarms in
 your account are displayed. The number depends on how many AWS services you use. The alarms shown are
 those in the ALARM state or those that most recently changed state.


These upper areas help you quickly assess the health of your AWS services, by
 seeing the alarm states in every service and the alarms that most recently changed
 state. This helps you monitor and quickly diagnose issues.
* Below these areas is the *default dashboard*, if one exists. The default 
 dashboard is a custom dashboard that you have created and named
 **CloudWatch-Default**. This is a convenient way for
 you to add metrics about your own custom services or applications to the overview
 page, or to bring forward additional key metrics from AWS services that you most
 want to monitor.
###### Note

The automatic dashboards on the CloudWatch home page display only information from the current 
 account, even if the account is a monitoring account set up for CloudWatch cross-account observability.
 For information about creating custom cross-account dashboards, see 
 [Creating a CloudWatch cross-account cross-Region dashboard with the
 AWS Management Console](create_xaxr_dashboard.md "create_xaxr_dashboard.md").

From this overview, you can see a cross-service dashboard of metrics from multiple AWS service, or focus your view to a 
 specific resource group or a specific AWS
 service. This enables you to narrow your view to a subset of resources in which you are
 interested. 

###### Topics

* [Viewing the cross-service CloudWatch dashboard](CloudWatch_Automatic_Dashboards_Cross_Service.md "CloudWatch_Automatic_Dashboards_Cross_Service.md")
* [Removing a service from appearing in
 the CloudWatch cross-service dashboard](Remove_service_from_Cross_Service_Dashboard.md "Remove_service_from_Cross_Service_Dashboard.md")
* [Viewing a CloudWatch dashboard for a
 single AWS service](CloudWatch_Automatic_Dashboards_Focus_Service.md "CloudWatch_Automatic_Dashboards_Focus_Service.md")
* [Viewing a CloudWatch dashboard for a
 resource group](CloudWatch_Automatic_Dashboards_Resource_Group.md "CloudWatch_Automatic_Dashboards_Resource_Group.md")
