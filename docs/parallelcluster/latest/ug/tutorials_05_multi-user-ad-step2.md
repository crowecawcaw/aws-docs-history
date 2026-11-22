

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# (Optional) Manage AD users and groups

In this step, you manage users and groups from an Amazon EC2 Amazon Linux 2023 instance that's joined to the Active Directory (AD) domain.

If you followed the *automated* path, restart and log in to the AD joined instance that was created as part of the automation.

If you followed the *manual* path, restart and log in to the instance that you created and joined to the AD in preceding steps.

In these steps, you use the [adcli](https://www.mankier.com/package/adcli) and [openldap-clients](https://www.mankier.com/package/openldap-clients) tools that were installed in the instance as part of a preceding step.

**Log in to an Amazon EC2 instance that is joined to the AD domain**

1. From the Amazon EC2 console, select the untitled Amazon EC2 instance that was created in previous steps. The instance state might be **Stopped**.

1. If the instance state is **Stopped**, choose **Instance state** and then **Start instance**.

1. After the status checks pass, select the instance and choose **Connect** and SSH in to the instance.

**Manage users and groups when logged into an Amazon EC2 Amazon Linux 2023 instance that's joined to the AD**

When you run the `adcli` commands with the ` -U "Admin"` option, you're prompted to enter the AD `Admin` password. You include the AD `Admin` password as part of the `ldapsearch` commands.

1. 

**Create a user.**

   ```bash
   $ adcli create-user {{"clusteruser"}} --domain {{"corp.example.com"}} -U "Admin"
   ```

1. 

**Set a user password.**

   ```bash
   $ aws --region {{"region-id"}} ds reset-user-password --directory-id {{"d-abcdef01234567890"}} --user-name {{"clusteruser"}} --new-password {{"new-p@ssw0rd"}}
   ```

1. 

**Create a group.**

   ```bash
   $ adcli create-group {{"clusterteam"}} --domain {{"corp.example.com"}} -U "Admin"
   ```

1. 

**Add a user to a group.**

   ```bash
   $ adcli add-member {{"clusterteam"}} {{"clusteruser"}} --domain {{"corp.example.com"}} -U "Admin"
   ```

1. 

**Describe users and groups.**

   Describe all users.

   ```bash
   $ ldapsearch "(&(objectClass={{user}}))" -x -h {{"192.0.2.254"}} -b "DC={{corp}},DC={{example}},DC={{com}}" -D "CN=Admin,OU=Users,OU={{CORP}},DC={{corp}},DC={{example}},DC={{com}}" -w {{"p@ssw0rd"}}
   ```

   Describe a specific user.

   ```bash
   $ ldapsearch "(&(objectClass={{user}})(cn={{clusteruser}}))" -x -h {{"192.0.2.254"}} -b "DC={{corp}},DC={{example}},DC={{com}}" -D "CN=Admin,OU=Users,OU={{CORP}},DC={{corp}},DC={{example}},DC={{com}}" -w {{"p@ssw0rd"}}
   ```

   Describe all users with a name pattern.

   ```bash
   $ ldapsearch "(&(objectClass={{user}})(cn={{user*}}))" -x -h {{"192.0.2.254"}} -b "DC={{corp}},DC={{example}},DC={{com}}" -D "CN=Admin,OU=Users,OU={{CORP}},DC={{corp}},DC={{example}},DC={{com}}" -w {{"p@ssw0rd"}}
   ```

   Describe all users that are part of a specific group.

   ```bash
   $ ldapsearch "(&(objectClass={{user}})(memberOf=CN={{clusterteam}},OU=Users,OU={{CORP}},DC={{corp}},DC={{example}},DC={{com}}))" -x -h {{"192.0.2.254"}} -b "DC={{corp}},DC={{example}},DC={{com}}" -D "CN=Admin,OU=Users,OU={{CORP}},DC={{corp}},DC={{example}},DC={{com}}" -w {{"p@ssw0rd"}}
   ```

   Describe all groups

   ```bash
   $ ldapsearch "objectClass={{group}}" -x -h {{"192.0.2.254"}} -b "DC={{corp}},DC={{example}},DC={{com}}" -D "CN=Admin,OU=Users,OU={{CORP}},DC={{corp}},DC={{example}},DC={{com}}" -w {{"p@ssw0rd"}}
   ```

   Describe a specific group

   ```bash
   $ ldapsearch "(&(objectClass={{group}})(cn={{clusterteam}}))" -x -h {{"192.0.2.254"}} -b "DC={{corp}},DC={{example}},DC={{com}}" -D "CN=Admin,OU=Users,OU={{CORP}},DC={{corp}},DC={{example}},DC={{com}}" -w {{"p@ssw0rd"}}
   ```

1. 

**Remove a user from a group.**

   ```bash
   $ adcli remove-member {{"clusterteam"}} {{"clusteruser"}} --domain {{"corp.{{example}}.com"}} -U "Admin"
   ```

1. 

**Delete a user.**

   ```bash
   $ adcli delete-user {{"clusteruser"}} --domain {{"corp.{{example}}.com"}} -U "Admin"
   ```

1. 

**Delete a group.**

   ```bash
   $ adcli delete-group {{"clusterteam"}} --domain {{"corp.{{example}}.com"}} -U "Admin"
   ```