

# Delete your IAM Identity Center instance
<a name="delete-config"></a>

When an IAM Identity Center instance is deleted, all the data in that instance is deleted and cannot be recovered. The following table describes what data is deleted based on the directory type that is configured in IAM Identity Center.


| What data gets deleted | Connected directory - AWS Managed Microsoft AD, AD Connector, or external identity provider | IAM Identity Center identity store | 
| --- | --- | --- | 
| All permission sets you have configured for AWS accounts |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes  |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes  | 
| All applications you have configured in IAM Identity Center |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes  |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes  | 
| All user assignments you have configured for AWS accounts and applications |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes  |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes  | 
| All users and groups in the directory or store | N/A |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes  | 

If you replicated your IAM Identity Center instance to additional Regions, you must remove those Regions before deleting the instance.

Use the following procedure to delete your IAM Identity Center instance.

**To delete your IAM Identity Center instance**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. In the left navigation pane, choose **Settings**.

1. On the **Settings** page, choose the **Management** tab.

1. In the **Delete IAM Identity Center configuration** section, choose **Delete**.

1. In the **Delete IAM Identity Center configuration** dialog, select each checkbox to acknowledge you understand that your data will be deleted. Type your IAM Identity Center instance in the text box, and then choose **Confirm**.