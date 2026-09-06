

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS Advanced interfaces
<a name="ams-interfaces"></a>
+ *AMS Advanced console*: You use the AMS Advanced console to create RFCs, report and respond to incidents, make service requests, and find information on existing VPCs and stacks. When in doubt of what to do, or when you need help with AMS or your managed resources, create a service request by using this interface.
+ *AWS Management Console*: Many AWS consoles can be useful for viewing AMS information, for example:
  + *Amazon EC2 console*: Use to view instance information including bastion IP addresses, Amazon EC2 Auto Scaling groups, and load balancers.
  + *Multi-Account Landing Zone AWS Config Rules compliance*: You can view compliance status across your accounts and identify non-compliant resources.
  + *AWS CloudFormation console*: Use to view stack information including stack IDs (you can find Amazon RDS stacks and Amazon RDS instance IDs here, and event information).
  + *Amazon RDS console*: Use to view event information such as a post made to a WordPress app on a site in your account. Note you must have the Amazon RDS instance ID.

  Depending on the mode of your login role, you have different level of access to the AWS Management Console. For more information on modes, see [AMS modes](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes.html). 
+ *AMS Advanced change management API* – Read/Write: Use the change management API (CM API) to request additions and specific changes to your managed infrastructure including resource monitoring, log, backup, and patch configurations. Also, use this API to request access to resources, delete resources, create AMIs, and create IAM instance profiles. You can access the CM API through the AMS CLI and SDKs.
+ *AMS SKMS API* – Read-Only: Use this API to list managed resources and get information needed for reporting or preparing requests for change.
+ *Support API*: Use the standard Support API to programmatically create and respond to incidents and service requests. To learn more, see [Getting Started with Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html).
+ *AWS APIs* – Read Only: Your main IT administrator can use the AWS APIs to see all resources under management, view CloudTrail logs, billing information, and many other read functions.