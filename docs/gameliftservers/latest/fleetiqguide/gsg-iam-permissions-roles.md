# Create IAM roles for cross-service

interaction

In order for Amazon GameLift Servers FleetIQ to work with your Amazon EC2 instances and Auto Scaling groups, you must allow
the services to interact with each other. This is done by creating IAM roles in your AWS
account and assigning a set of limited permissions. Each role also sspecifies which services
can assume the role.

Set up the following roles:

- [Create a role for Amazon GameLift Servers FleetIQ](gsg-iam-permissions-roles-gamelift.md "gsg-iam-permissions-roles-gamelift.md") to update your Amazon EC2
  resources.
- [Create a role for Amazon EC2](gsg-iam-permissions-roles-ec2.md "gsg-iam-permissions-roles-ec2.md") resources to communicate with
  Amazon GameLift Servers FleetIQ.
