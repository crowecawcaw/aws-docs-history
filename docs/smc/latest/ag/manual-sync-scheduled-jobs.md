

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Manually syncing scheduled jobs
<a name="manual-sync-scheduled-jobs"></a>

The Connector for ServiceNow includes nine sync jobs related to AWS services integrations. During the initial setup, manually execute the sync job for your AWS service integration instead of waiting for Scheduled Jobs to run.

**To sync AWS service integrations or accounts manually**

1.  Log in as system administrator. 

1.  Find **Scheduled Jobs** in the navigator panel. 

1.  Search the following AWS Service Management Connector scheduled jobs (including default sync intervals) in the table below:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/smc/latest/ag/manual-sync-scheduled-jobs.html)

1. Choose the desired sync job, and choose **Execute Now**.
**Note**  
If you do not see **Execute Now** in the upper left corner, choose **Conﬁgure Job Deﬁnition**. **Execute Now** is visible. ServiceNow Administrator can adjust the Scheduled Job repeat interval as required.

Data is visible in the AWS Service Management scoped app menus after the Connector’s scheduled synchronization job has run.