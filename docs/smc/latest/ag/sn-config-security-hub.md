

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# AWS Security Hub CSPM in ServiceNow
<a name="sn-config-security-hub"></a>

 AWS Security Hub CSPM enables users to view security Findings from AWS services such as Amazon Guard Duty and Amazon Inspector, as well as AWS Partner solutions. 

If you use both [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc) and ServiceNow ITSM, the AWS Service Management Connector for ServiceNow allows you to create an automated, bidirectional integration between Security Hub and ServiceNow ITSM. This two-way integration synchronizes your Security Hub CSPM findings and ServiceNow tickets. 

Specifically, as a ServiceNow administrator, you can use this integration to automatically create ServiceNow incident or problem tickets from AWS Security Hub CSPM findings. When you update those tickets in ServiceNow, the changes are automatically replicated back to the original Security Hub CSPM findings. For example, when you resolve the ticket in ServiceNow, the workflow status of the Security Hub finding also changes to `RESOLVED`. This action ensures that Security Hub CSPM always has up-to-date information about your security posture.

View the following video, *AWS Security Hub CSPM - Bidirectional integration with ServiceNow ITSM*, for an overview of the AWS Security Hub CSPM integration to the Connector for ServiceNow.

[![AWS Videos](http://img.youtube.com/vi/OYTi0sjEggE/0.jpg)](http://www.youtube.com/watch?v=OYTi0sjEggE)
