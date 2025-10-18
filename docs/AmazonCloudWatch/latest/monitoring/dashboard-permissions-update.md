# CloudWatch dashboard permissions update

On May 1, 2018, AWS changed the permissions required to access CloudWatch dashboards.
 Dashboard access in the CloudWatch console now requires permissions that were introduced in
 2017 to support dashboard API operations:


* **cloudwatch:GetDashboard**
* **cloudwatch:ListDashboards**
* **cloudwatch:PutDashboard**
* **cloudwatch:DeleteDashboards**
To access CloudWatch dashboards, you need one of the following:


* The **AdministratorAccess** policy.
* The **CloudWatchFullAccess** policy.
* A custom policy that includes one or more of these specific
 permissions:




	+ `cloudwatch:GetDashboard` and
	 `cloudwatch:ListDashboards` to be able to view
	 dashboards
	+ `cloudwatch:PutDashboard` to be able to create or modify
	 dashboards
	+ `cloudwatch:DeleteDashboards` to be able to delete
	 dashboards
For more information about using policies to change permissions for an IAM user, see
 [Changing Permissions for
 an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html").

For more information about CloudWatch permissions, see [Amazon CloudWatch permissions reference](permissions-reference-cw.md "permissions-reference-cw.md").

For more information about dashboard API operations, see [PutDashboard](../APIReference/API_PutDashboard.md "../APIReference/API_PutDashboard.md") in the
 Amazon CloudWatch API Reference.
