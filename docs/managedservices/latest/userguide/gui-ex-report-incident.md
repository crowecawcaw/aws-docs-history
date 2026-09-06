

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Reporting incidents
<a name="gui-ex-report-incident"></a>

Use the AMS console to report an incident. It's important to create a new incident for each new issue or question. When opening cases related to old inquiries, it's helpful to include the related case number so we can refer to previous correspondence.
**Note**  
If case correspondence strays from the original issue, an AMS operator might ask you to report a new incident.

To report an incident using the AMS console:

1. From the left navigation, choose **Incidents**

   The **Incidents** list opens:  
![Incidents page showing filter dropdown set to All open, with columns for Created, Subject, ID, and Status.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/guiIncidentlistOpenPnC.png)

   If your incident list is empty, the **Clear filter** option resets the filter to **Any status**.

   If you know you want to use phone or chat, click **Create incident in Support Center** to open the incident **Create** page in the Support Center Console, auto-populated with the AMS service type.
**Important**  
Phone calls initiated with Support are recorded, to better improve response. If the call drops, you must call back through the Support Center case, AWS has no mechanism for calling you back. 
Phone and chat support is designed to help with support cases, incidents. and service requests, not RFC or security issues.
For RFC issues, use the correspondence option on the relevant RFC details page, to reach an AMS engineer.
For security issues, create a high-priority (P1 or P2) support case. The live chat feature is not for security events.  
![Incidents page showing a list of resolved incidents with their creation dates, subjects, and IDs.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/guiIncidentList2.png)

1. If you want to find an existing incident, select an incident status filter in the drop-down list.    
<a name="sr-filter-options"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/managedservices/latest/userguide/gui-ex-report-incident.html)

1. Choose **Create**.

   The **Create an incident** page opens:  
![Incident details form with priority levels, Access Issues dropdown, subject field, and details section.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/guiIncidentCreate5.png)

1. Select a **Priority**:
   + **Low**: Non-critical functions of your business service or application related to AWS/AMS resources are impacted.
   + **Medium**: A business service or application related to AWS/AMS resources is moderately impacted and functioning in a degraded state.
   + **High**: Your business is significantly impacted. Critical functions of your application related to AWS/AMS resources are unavailable. Reserved for the most critical outages affecting production systems.

1. Select a **Category**.
**Note**  
If you are going to test incident functionality, then add the no-action flag (AMSTestNoOpsActionRequired) to your incident title.

1. Enter information for:
   + **Subject**: A descriptive title for the incident report.
   + **CC emails**: A list of email addresses for people you want informed about the incident report and resolution.
   + **Details**: A comprehensive description of the incident, the systems impacted, and the expected outcome of the resolution. Answer the pre-set questions, or delete them and enter any relevant information.

   To add an attachment, choose **Add Attachment**, browse to the attachment you want, and click **Open**. To delete the attachment, click the Delete icon: ![](http://docs.aws.amazon.com/managedservices/latest/userguide/images/icon-delete-attachment.png).

1. Choose **Submit**.

   A details page opens with information on the incident—such as **Type**, **Subject**, **Created**, **ID**, and **Status**—and a **Correspondence** area that includes the description of the request you created.

   Click **Reply** to open a correspondence area and provide additional details or updates in status.

   Click **Close Case** when the incident has been resolved.

   Click **Load More** if there is more correspondence than will fit on one page.

   Don't forget to rate the communication\!  
![](http://docs.aws.amazon.com/managedservices/latest/userguide/images/guiSRcorrespond.png)

   Your incident displays on the **Incidents** list page.

**YouTube Video**: [ How do I raise an incident from the AWS Managed Services console?](https://www.youtube.com/watch?v=A51d8Qm_MvA&list=PLhr1KZpdzukc_VXASRqOUSM5AJgtHat6-&index=6&t=46s)