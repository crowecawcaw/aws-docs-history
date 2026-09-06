

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Health integration
<a name="sn-health-validate"></a>

**View AWS Health dashboard**
**Note**  
To view the the AWS Health dashboard, you must use the role **x\_126749\_aws\_sc.health\_dashboard\_viewer**.

1. Log in to your ServiceNow instance in the fulfiller (standard) view.

1. In the search box, enter **AWS Service Management Connector**.

1. Choose **AWS Health** and then **Dashboards**.

1. At the top-right, select your account from the **Select an AWS account** dropdown list. The following four tabs are available:
   + **Open and recent issues** (opens by default) displays health events that were updated within the past seven days. Choose an event to display its details and a list of affected resources.
   + **Scheduled changes** displays future health events with start times after the current date and time.
   + **Other notifications** displays health events that were updated within the past seven days.
   + **Event log** displays all health events for the selected AWS account.

**View AWS Health incidents**

1. Log in to your ServiceNow instance in the fulfiller (standard) view.

1. In the navigator, enter **AWS Service Management Connector**.

1. Under **AWS Health**, choose **AWS Health Incidents**.

**View AWS Health change requests**

1. Log in to your ServiceNow instance in the fulfiller (standard) view.

1. In the navigator, enter **AWS Service Management Connector**.

1. Under **AWS Health**, choose **AWS Health Requests**.

**Manually create an AWS Health incident**

1. Log in to your ServiceNow instance in the fulfiller (standard) view.

1. In the navigator, enter **AWS Service Management Connector**.

1. Choose **AWS Health** and then **Dashboards**.

1. Choose an event that doesn't already have an incident linked to it.

1. Choose **Create a New Incident**. You are redirected to the new-incident form, which has prefilled data fields for the selected health event.

**Manually create an AWS Health change**

1. Log in to your ServiceNow instance in the fulfiller (standard) view.

1. In the navigator, enter **AWS Service Management Connector**.

1. Choose **AWS Health** and then **Dashboards**.

1. Choose an event that doesn't already have a change linked to it.

1. Choose **Create a New Change**. You are redirected to the new-incident form, which has prefilled data fields for the selected health event.

**Validate the automatic creation of AWS Health incidents and changes**

1. Log in to your ServiceNow instance in the fulfiller (standard) view.

1. In the navigator, enter **AWS Service Management Connector**.

1. Navigate to **AWS Health** system properties, and enable automatic creation for health event types.

1. Generate new health events, and then sync AWS Health.