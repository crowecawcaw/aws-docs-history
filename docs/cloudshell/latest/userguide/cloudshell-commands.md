# Running a command in CloudShell from AWS Service
 consoles

You can run a command in the CloudShell terminal through
 [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html "https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html")
 and [Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html "https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html")
 consoles
 in the AWS Management Console.

To run a command in CloudShell from other AWS Service consoles, the IAM policy
 assigned to your role must include `cloudshell:approveCommand` permissions.

CloudShell opens on the **Console Toolbar** and **Run
 command** pop-up appears in CloudShell. On the **Run command**
 pop-up, the command appears in the command box.

To run a command in the CloudShell terminal, choose one of the following steps:


1. Enter a name in the **New environment name** box if you have not
 created a VPC environment in the CloudShell.


You can view the VPC environment details that is based on the VPC details of your
 resource.




	1. Choose **Create and run**.
	
	
	This step will create a new CloudShell VPC environment and run the command in the
	 CloudShell terminal.
2. You can view the CloudShell environment name if you have already created a
 CloudShell VPC environment.


###### Note

If you already have a CloudShell VPC environment, you can't create a new VPC
 environment. 




	1. Choose **Run**.
	
	
	This step will run the command in the CloudShell terminal in the selected
	 CloudShell VPC environment.
	
	
	###### Note
	
	If you don't have permission to view the created VPC environments, contact your
	 administrator to add the `cloudshell:describeEnvironments` permission. For
	 more information, see [Managing AWS
	 CloudShell access and usage with IAM policies](sec-auth-with-identities.md "sec-auth-with-identities.md").
You can continue to run commands in the CloudShell terminal.
