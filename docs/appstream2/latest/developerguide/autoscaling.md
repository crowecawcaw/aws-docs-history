# Fleet Auto Scaling for Amazon WorkSpaces Applications

Fleet Auto Scaling lets you change the size of your WorkSpaces Applications Always-On or On-Demand fleet
automatically to match the supply of available instances to user demand. The size of your
fleet determines the number of users who can stream concurrently. For a multi-session fleet,
more than one user can use a single instance. For a non multi-session fleet, one instance is
required for each user session. You can specify your fleet capacity in terms of instances
(for single-session fleets) and user sessions (for multi-session fleets). Based on your
fleet configurations and auto scaling policies, the required number of instances will be
made available. You can define scaling policies that adjust the size of your fleet
automatically based on a variety of utilization metrics, and optimize the number of
available instances to match user demand. You can also choose to turn off automatic scaling
and make the fleet run at a fixed size.

###### Note

Elastic fleet capacity is automatically managed by WorkSpaces Applications for you. You do not need to
create auto scaling rules to manage the number of fleet streaming instances that are
available for Elastic fleets.

###### Note

As you develop your plan for WorkSpaces Applications fleet scaling, make sure that your network
configuration meets your requirements.

Before you can use Fleet Auto Scaling, Application Auto Scaling needs permissions to access Amazon CloudWatch
alarms and WorkSpaces Applications fleets. For more information, see [Using AWS Managed Policies and Linked Roles to Manage Administrator Access to WorkSpaces Applications Resources](controlling-administrator-access-with-policies-roles.md "controlling-administrator-access-with-policies-roles.md") and [Using IAM Policies to Manage Administrator Access to Application Auto Scaling](autoscaling-iam-policy.md "autoscaling-iam-policy.md").

###### Note

When you use scaling, you work with the Application Auto Scaling API. For Fleet Auto Scaling to work
correctly for WorkSpaces Applications, Application Auto Scaling requires permission to describe and update your WorkSpaces Applications
fleets and describe your Amazon CloudWatch alarms, and permissions to modify your fleet capacity
on your behalf. For more information, see [Roles Required for WorkSpaces Applications, Application Auto Scaling,
and AWS Certificate Manager Private CA](roles-required-for-appstream.md "roles-required-for-appstream.md") and [Using IAM Policies to Manage Administrator Access to Application Auto Scaling](autoscaling-iam-policy.md "autoscaling-iam-policy.md").

The following topics provide information to help you understand and use WorkSpaces Applications Fleet Auto
Scaling.

###### Contents

- [Scaling Concepts for Amazon WorkSpaces Applications](autoscaling-concepts.md "autoscaling-concepts.md")
- [Managing Fleet Scaling Using the Amazon WorkSpaces Applications Console](autoscaling-console.md "autoscaling-console.md")
- [Managing Fleet Scaling Using the AWS CLI for Amazon WorkSpaces Applications](autoscaling-cli.md "autoscaling-cli.md")
- [Additional Resources for Auto Scaling Amazon WorkSpaces Applications](autoscaling-additional-resources.md "autoscaling-additional-resources.md")
