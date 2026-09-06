

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating Support integration in Jira Service Management Cloud
<a name="cloud-sup-validate"></a>

 This section describes how to create, view, and manage integration features of Support. 

****To view Cases from Support****

1. Log in to your Jira Agent view. 

1. In the Jira Service Management Jira Agent view, choose the **Jira Project** associated to Support. 

1. Use the Jira filters to only view Issues with the **Support Case** Issue Type. 

****To create a general Support case as a Jira Incident****

1. Log in to your Jira Agent view. 

1. Choose **Requests** at the top right corner. 

1. In the Jira Service Management Jira Agent view, choose the **Jira Project** associated to Support. 

1. Choose **Create** from the list header and then select the **Support Case** Issue Type. 

1. Complete the following mandatory fields in the form:
   + **Summary**— A brief summary of the question or issue
   + **Description**— A detailed summary of the question or issue
   + **Priority**— The severity of the Support case
   + **Support Service and Category**— The AWS service and category of the Support case
   + **AWS Account**— The account to create the Support case
   + (optional)**AWS CC Email Addresses**— Additional email addresses for the Support case

1. Choose **Create**. 

1. Choose the Incident you created from the list. Service Management Connector displays the **AWS Case ID** and the **AWS Case Status**. 

****To create AMS Accelerate report incidents in Jira (for AMS Accelerate customers)****

1. Log in to the Jira Agent view. 

1. In the Jira Service Management Jira Agent view, choose the **Jira Project** associated to Support. 

1. Choose **Create** from the list header and then select the **Support Case** Issue Type. 

1. Complete the following mandatory fields in the form:
   + **Summary**— A brief summary of the question or issue
   + **Description**— A detailed summary of the question or issue
   + **Priority**— The severity of the Support case
   + **Support Service and Category**— AMS Operations - Report Incident and the chosen category
   + **AWS Account**— The account to create the Support case
   + (optional)**AWS CC Email Addresses**— Additional email addresses for the Support case

1. Choose **Create**. 

1. Choose the Incident you created from the list. Service Management Connector displays the **AWS Case ID** and the **AWS Case Status**. 

****To create AMS Accelerate service requests in Jira (for AMS Accelerate customers)****

1. Log in to the Jira Agent view. 

1. In the Jira Service Management Jira Agent view, choose the **Jira Project** associated to Support. 

1. Choose **Create** from the list header and then select the **Support Case** Issue Type. 

1. Complete the following mandatory fields in the form:
   + **Summary**— A brief summary of the question or issue
   + **Description**— A detailed summary of the question or issue
   + **Priority**— The severity of the Support case
   + **Support Service and Category**— AMS Operations - Service Request and the chosen category
   + **AWS Account**— The account to create the Support case
   + (optional)**AWS CC Email Addresses**— Additional email addresses for the Support case

1. Choose **Create**. 

1. Choose the Incident you created from the list. Service Management Connector displays the **AWS Case ID** and the **AWS Case Status**. 

****To add a correspondence and attach it to an existing Support case in Jira incident****

1. Log in to the Jira Agent view. 

1. In the Jira Service Management Jira Agent view, choose the **Jira Project** associated to Support. 

1. Choose **Create** from the list header and then select the **Support Case** Issue Type. 

1. Open the required **Support case**. 

1. At the bottom of the form, choose **Reply to customer** to add a correspondence. You can attach a maximum of three attachments, with a size limit of 5MB per attachment per correspondence. 

1. Choose **Save**. 

****To resolve an Support case in Jira****

1. Log in to the Jira Agent view. 

1. In the Jira Service Management Jira Agent view, choose the **Jira Project** associated to Support. 

1. Use Jira filters to display only issues with the **Support Case** Issue Type. 

1. Open the required Support case. 

1. Choose **Issue status** and then choose **Mark as Resolved**. 

**Note**  
AWS Service Management Connector also enables Jira internal customers without an Agent license to create Support cases. The validation steps above are applicable and valid for interactions with the **Support Case** issue type through the Jira customer portal. 