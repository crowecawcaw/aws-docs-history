

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Creating a service request
<a name="serv-req-mgmt-examples"></a>

To create a service request using the AWS Managed Services (AMS) console:

1. From the left navigation, choose **Service requests**.

   The **Service requests** list opens.  
![Service requests page with filter dropdown, table headers, and Create service request button.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/guiSrCreateOpenPnC.png)

   If your service request list is empty, the **Clear filter** option resets the filter to **Any status**.  
![Service requests list showing multiple resolved requests with subjects, IDs, and status.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/guiSRlist2.png)

   If you know you want to use phone or chat, click **Create service request in Support Center** to open the service request **Create** page in the Support Center Console, auto-populated with the AMS service type.
**Note**  
Phone calls initiated with Support center are recorded, to better improve response. If the call drops, you must call back through the Support Center case, AWS has no mechanism for calling you back. 
**Important**  
Phone and chat support is designed to help with support cases, incidents and service requests. For RFC issues, use the correspondence option on the relevant RFC details page, to reach an AMS engineer.

1. If you want to find an existing service request, select a service request status filter in the drop-down list.    
<a name="sr-filter-options"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/serv-req-mgmt-examples.html)

1. Choose **Create**.

   The **Create a service request** page opens.  
![Create a service request form with fields for Category, Subject, CC Emails, Details, and attachment option.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/guiServiceRequestCreate.png)

1. Select a **Category**.
**Note**  
If you are going to test service request functionality, add the no-action flag, `AMSTestNoOpsActionRequired`. to your service request title.

1. Enter information for:
   + **Subject**: This creates a link to the service request details on the list page.
   + **CC emails**: These emails receive correspondence in addition to your default email contacts.
   + **Details**: Provide as much information here as possible.

   To add an attachment, choose **Add Attachment**, browse to the attachment you want, and click **Open**. To delete the attachment, click the Delete icon: ![](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/icon-delete-attachment.png).

1. Choose **Submit**.

   A details page opens with information on the service request--such as **Type**, **Subject**, **Created**, **ID**, and **Status**--and a **Correspondence** area that includes the description of the request you created.  
![Service Request Detail page showing Type, Subject, Created date, ID, and Resolved status.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/guiSRdetail.png)

   Additionally, your service request displays on the **Service Request** list page. Use this when you have an alert but have not yet heard from AMS.

   Click **Reply** to open a correspondence area and provide additional details or status updates.

   Click **Resolve Case** when the service request has been resolved.

   Click **Load More** to view additional correspondences that do not fit on the inital page.

   Don't forget to rate the communication\!  
![Correspondence interface showing email exchange with star rating options for feedback.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/guiSRcorrespond.png)

For billing-related queries, use the **Other** Category in the AMS console; the `ChangeTypeId ct-1e1xtak34nx76` in the AMS CM API, or the `IssueType=AMS` in the AWS Support API.