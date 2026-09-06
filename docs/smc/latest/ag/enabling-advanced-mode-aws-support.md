

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Advanced Mode for Support integration (optional)
<a name="enabling-advanced-mode-aws-support"></a>

AWS Service Management Connector allows you to enable an intermediate table for the creation of Support Cases. This allows you to add custom logic using ServiceNow business rules and workflows to align with your internal Incident or Case Management process. 

For more information about enabling advanced mode, refer to the *Advanced mode* row in the above table. 

After you create an Support Case, the API only allows specific changes by an end user. The allowable changes for design considerations while using Support integration are:
+ Adding a correspondence to the case
+ Resolving the case
+ Reopening a case, which occurs if you add correspondence to a previously resolved support case