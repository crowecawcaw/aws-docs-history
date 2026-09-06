

# AWS User Notifications for AWS Data Exchange events
<a name="user-notifications"></a>

You can use [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html) to set up delivery channels that notify you about AWS Data Exchange events. You receive a notification when an event matches a specified rule. You can receive notifications for events through multiple channels, including email, Amazon Q Developer in chat applications chat notifications, or AWS Console Mobile Application push notifications. You can also see notifications using the Console Notifications Center in the AWS User Notifications console. AWS User Notifications supports aggregation, which can reduce the number of notifications you receive during specific events. For more information, see the [AWS User Notifications User Guide](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html).

To use AWS User Notifications, you must have the correct AWS Identity and Access Management (IAM) permissions. For more information about configuring your IAM permissions, see [Configuring AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html#getting-started-step1) in the *AWS User Notifications User Guide*. 

The following table provides more information about the notifications that you can configure for AWS Data Exchange events using AWS User Notifications.


| Actions | Notification received by subscriber | 
| --- | --- | 
| Adds a file-based data set to a product and publishes it | Data Sets Published To Product | 
| Adds an Amazon Redshift data set to a product and publishes it | Redshift Data Shares Data Sets Published To Product | 
| Adds a file-based data set revision to a product and publishes it | Revision Published To Data Set | 
| Revokes revision to a product | Revision Revoked | 
| Adds an Amazon Redshift data set revision to a product and publishes it | Revision Published To Redshift Data Shares Data Set | 
| Takes an action on Amazon Redshift resources that might remove access from a subscriber | Action Performed On Redshift Data Share By Provider | 
| Takes an action on Amazon Redshift resources that removes access from a subscriber | Redshift Data Share Access Lost | 
| Adds an Amazon API Gateway data set to a product and publishes it | API Gateway API Data Sets Published To Product | 
| Adds an Amazon API Gateway data set revision to a product and publishes it | Revision Published To API Gateway API Data Set | 
| Adds an AWS Lake Formation data set to a product and publishes it (Preview) | Lake Formation Data Permission Data Sets Published To Product (Preview) | 
| Adds an AWS Lake Formation data set revision to a product and publishes it (Preview) | Revision Published To Lake Formation Data Permission Data Set (Preview) | 
| Auto-export job completed | Auto-export Job Completed | 
| Auto-export job failed | Auto-export Job Failed | 
| Sends notification for a data update | Data Updated in Data Set | 
| Sends notification for a schema change | Schema Change Planned for Data Set | 
| Sends notification for a data delay | Data Set Update Delayed | 
| Sends notification for a data deprecation | Deprecation Planned for Data Set | 