# AWS DRS launch settings

The launch settings are a set of instructions that comprise an EC2 launch template and
other settings, which determine how a recovery instance is launched for each source server
on AWS.

Launch settings, including the EC2 launch template, are automatically created every time
you add a server to AWS Elastic Disaster Recovery.

The launch settings can be modified at any time, including before the source servers have
even completed initial sync.

[Learn more about individual launch
settings.](launching-target-servers.md "launching-target-servers.md")

###### Important

**If the source server’s instance type includes instance store, please consider the following:**

- It is **not** recommended to change the instance type of an instance to a type that has no ephemeral volumes, or has
  a different number of ephemeral volumes, as such changes could lead to data inconsistencies and
  may even cause recovery, drill, or failback to fail.
