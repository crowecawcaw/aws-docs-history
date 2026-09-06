

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Platform system administrator components
<a name="sn-configure-connector"></a>

To enable the AWS Service Management Connector scoped application named **AWS Service Management**, the system admin must create a discovery source, and configure specific platform tables, forms, and views.

**Create a discovery source AWS Service Management Connector entry**

You must create a new discovery data source, AWS Service Management Connector. 

**To enable AWS to report discovered CIs into your CMDB**

1.  Choose **System Definition**. Then select **Choice Lists**.

1.  Choose **New**. 

1.  Create a new entry with these details: 
   + **Table:** **Configuration Item [cmdb\_ci]**
   + **Element:** **discovery\_source**
   + **Label:** **AWS Service Management Connector**
   + **Value:** **AWS Service Management Connector**

**Note**  
Make sure you are in Global mode in ServiceNow System Settings to modify System Definitions.