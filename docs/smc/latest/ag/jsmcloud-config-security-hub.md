

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Integrating AWS Security Hub CSPM in Jira Service Management Cloud
<a name="jsmcloud-config-security-hub"></a>

 AWS Security Hub CSPM enables users to view security Findings from AWS services such as Amazon Guard Duty and Amazon Inspector, as well as AWS Partner solutions. 

If you use both [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc) and [ Jira Service Management](https://www.atlassian.com/software/jira/service-management), the AWS Service Management Connector for Jira Service Management allows you to create an automated, bidirectional integration between Security Hub and Jira Service Management. This two-way integration synchronizes your Security Hub CSPM Findings and Jira Issues. 

Specifically, as a Jira administrator, you can use this integration to automatically create Jira Issues from AWS Security Hub CSPM Findings. When you update those tickets in Jira, the changes are automatically replicated back to the original Security Hub CSPM Findings. For example, when you resolve the issue in Jira, the workflow status of the Security Hub finding also changes to `RESOLVED`. This action ensures that Security Hub CSPM always has up-to-date information about your security posture.

**Note**  
If you are aggregating your Security Hub CSPM findings to a single management AWS account and have onboarded management to the connector, internal customers and Jira agents updates on the Finding issue will **not** be synched to the finding in Security Hub CSPM. 