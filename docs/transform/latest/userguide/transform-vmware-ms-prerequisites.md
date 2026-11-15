

# Prerequisites
<a name="transform-vmware-ms-prerequisites"></a>

If you completed all the steps of an end-to-end migration job in AWS Transform, your target accounts, inventory file, and network infrastructure are already prepared. You can proceed to Configure Migration Defaults.

If you are starting server migration independently, ensure you have the following in place:
+ **Supported operating systems** – Source servers must run a supported operating system. For the full list, see [Supported operating systems](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html) in the *MGN User Guide*.
+ **Target accounts for migration** – The AWS account IDs where you need your servers to be migrated. You can use AWS Transform landing zone or any other tools to set up your infrastructure.
+ **Network infrastructure in place** – VPCs, subnets, and security groups deployed and configured. You can use AWS Transform network migration or any other tools to set up your network infrastructure.
+ **Inventory file** – Prepared with server details, wave assignments, target account information, and Amazon EC2 instance type preferences. You can use AWS Transform migration planning to generate this file.