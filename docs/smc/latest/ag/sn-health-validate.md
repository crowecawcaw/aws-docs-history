# Validating AWS Health integration

###### View AWS Health dashboard

###### Note

To view the the AWS Health dashboard, you must use the role **x_126749_aws_sc.health_dashboard_viewer**.

1.  Log in to your ServiceNow instance in the fulfiller (standard) view.
2.  In the search box, enter `AWS Service Management
Connector`.
3.  Choose **AWS Health** and then
    **Dashboards**.
4.  At the top-right, select your account from the **Select an
    AWS account** dropdown list. The following four tabs are
    available:

        * **Open and recent issues** (opens by
         default) displays health events that were updated within the past seven
         days. Choose an event to display its details and a list of affected
         resources.
        * **Scheduled changes** displays future
         health events with start times after the current date and time.
        * **Other notifications** displays health
         events that were updated within the past seven days.
        * **Event log** displays all health events
         for the selected AWS account.

    **View AWS Health incidents**

5.  Log in to your ServiceNow instance in the fulfiller (standard) view.
6.  In the navigator, enter `AWS Service Management Connector`.
7.  Under **AWS Health**, choose **AWS Health Incidents**.
    **View AWS Health change requests**

8.  Log in to your ServiceNow instance in the fulfiller (standard) view.
9.  In the navigator, enter `AWS Service Management Connector`.
10. Under **AWS Health**, choose **AWS Health Requests**.
    **Manually create an AWS Health incident**

11. Log in to your ServiceNow instance in the fulfiller (standard) view.
12. In the navigator, enter `AWS Service Management Connector`.
13. Choose **AWS Health** and then
    **Dashboards**.
14. Choose an event that doesn't already have an incident linked to it.
15. Choose **Create a New Incident**. You are
    redirected to the new-incident form, which has prefilled data fields for the
    selected health event.
    **Manually create an AWS Health change**

16. Log in to your ServiceNow instance in the fulfiller (standard) view.
17. In the navigator, enter `AWS Service Management Connector`.
18. Choose **AWS Health** and then
    **Dashboards**.
19. Choose an event that doesn't already have a change linked to it.
20. Choose **Create a New Change**. You are
    redirected to the new-incident form, which has prefilled data fields for the
    selected health event.
    **Validate the automatic creation of AWS Health incidents and changes**

21. Log in to your ServiceNow instance in the fulfiller (standard) view.
22. In the navigator, enter `AWS Service Management Connector`.
23. Navigate to **AWS Health** system properties, and enable automatic creation for health event types.
24. Generate new health events, and then sync AWS Health.
