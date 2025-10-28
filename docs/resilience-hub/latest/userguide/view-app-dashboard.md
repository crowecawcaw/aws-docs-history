# AWS Resilience Hub dashboard

The dashboard provides a comprehensive view of the resilience status of your application
portfolio. The dashboard aggregates and organizes resilience events (for example,
unavailable database or failed resilience validation), alerts, and insights from services
such as CloudWatch and AWS Fault Injection Service (AWS FIS).

The dashboard also generates a resilience score for each application that’s assessed. This
score indicates how well your application performs when assessed against recommended
resilience policies, alarms, recovery standard operating procedures (SOPs), and tests. You
can use this score to measure resilience improvements over time.

To view AWS Resilience Hub dashboard, choose **Dashboard** from navigation menu.
The **Dashboard** page displays the following sections:

## Application status

The application statuses indicate whether the applications have been assessed for
compliance with their attached resiliency policy or not. In addition, after an
assessment is completed, the status also indicates if the input sources of your
applications have been modified or not. Choose a number under each of the following
statuses to view all the applications that share the same status in the
**Applications** page:

- **Applications in policy** – Indicates all the
  applications that comply with their attached resiliency policy.
- **Applications breaching policy** – Indicates all the
  applications that does not comply with their attached resiliency policy.
- **Applications not assessed** – Indicates all the
  applications whose compliance has not been assessed or tracked yet.
- **Applications drifted** – Indicates all the
  applications that have drifted from their resiliency policy or if their
  resources have drifted.

## Application resiliency score over

time

With the application resiliency score over time, you can view a graph of your
application's resiliency over the past 30 days. While the dropdown menu can list 10 of
your applications, AWS Resilience Hub only shows you a graph of up to four applications at a
time. For more information about resiliency score, see [Understanding resiliency scores](resil-score.md "resil-score.md").

###### Note

AWS Resilience Hub does not run scheduled assessments at the same time. As a result, you
may need to return to the resiliency score over time graph at a later time to view
the daily assessment of your applications.

AWS Resilience Hub also uses Amazon CloudWatch to generate these graphs. Choose **View metrics in CloudWatch** to create and view more granular information about
your application's resiliency in your CloudWatch dashboard. For more information about CloudWatch,
see [Using dashboards](../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md") in the _Amazon CloudWatch User Guide_.

## Implemented alarms

This section lists all the alarms that you have set up in Amazon CloudWatch to monitor all the
applications. For more information , see [Viewing alarms](view-alarm.md "view-alarm.md").

## Implemented experiments

This section lists all fault injection experiments that you have implemented in all
the applications. For more information, see [Viewing AWS FIS experiments](view-fis-experiment.md "view-fis-experiment.md").
