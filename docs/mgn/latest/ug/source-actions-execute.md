

# Executing source actions

Source actions are executed from the MGN connector account where the AWS Transform MGN Connector is deployed. The connector communicates with source servers to run the scripts.

## Starting an execution job
<a name="source-actions-execute-overview"></a>

To execute a source action on your on-premises machines:

1. Navigate to **Settings** > **Source actions**

1. Choose **Execute**

1. Select the **Action** to execute from the list of available actions

1. Select one or more **Machines** to target, up to 100 machines per job

   In the delegated admin account, you can run a source action on machines from one account at a time. To select all of the machines in an account, filter the source server list by account, server name, or another attribute.

1. Review the execution settings (action name, machines, timeout)

1. Choose **Start execution**

A job is created and the AWS Transform MGN connector begins executing the source action on each selected machine.

**Note**  
If one of the selected machines is not connected to an AWS Transform MGN connector, AWS Transform MGN displays a warning and continues to execute the source action on all of the connected machines.

## Source action job quotas
<a name="source-actions-quotas"></a>

The following quotas apply to source action execution jobs:


| Quota | Value | 
| --- | --- | 
| Machines per job | 100 | 
| Jobs per account, including completed jobs | 100 | 
| Running jobs per account | 20 | 
| Running jobs per connector and member account | 1 | 
| Script timeout | 5,400 seconds (1.5 hours) | 

**Note**  
When you reach the quota of 100 jobs and start another job, AWS Transform MGN deletes the oldest job to make room for the new one. The new job doesn't fail. If you need the results of older jobs, review them before you start new jobs.

## Execution flow and status
<a name="source-actions-execution-flow"></a>

When you execute a source action, the following occurs:

1. An **execution job** is created for each AWS Transform MGN connector that manages the selected machines. If the selected machines are connected to different connectors, AWS Transform MGN creates a separate job for each connector, and each job runs the source action on the machines connected to that connector

1. The job status changes to **In Progress**

1. For each selected machine, an **invocation** is created

1. The connector connects to each on-premises machine via SSH (Linux) or WinRM (Windows)

1. The script from SSM Parameter Store is retrieved and executed

1. SSM Run Command captures the script output (standard output and standard error)

1. The invocation completes with a status (Success, Failed, or Timeout)

1. When all invocations complete, the job status updates

**Important**  
A script can run after its job has timed out or failed.  
SSM Agent on the AWS Transform MGN connector runs the script invocations. When a job targets many machines, or the script takes a long time to finish, SSM Agent queues the invocations and can start them long after the job was created. All jobs that use the same connector share this queue. Invocations that are already in the queue can still run after the job ends, including after the job times out or fails.  
To avoid scripts running later than you expect, plan the number of machines in each job, the script duration, the timeout, and the number of jobs that run on the same connector at the same time. Keep your scripts repeatable, so that a late or repeated run doesn't cause problems.

## Source actions after launching test or cutover instances
<a name="source-actions-after-launch"></a>

**Important**  
Source actions run on whichever machine answers at the address in **FQDN for Action Framework**. If the source server has no address set, MGN uses the source server's primary private IP address. If the address is a DNS name, the MGN connector resolves it each time the action runs. The connector does not check that the machine at the address is the original source server.  
A launched test or cutover instance is a copy of the source server. It has the same operating system users and passwords and, unless you regenerate them, the same SSH host keys and WinRM certificates. If the MGN connector can reach the launched instance at the address, for example over a Site-to-Site VPN or AWS Direct Connect, it can sign in to the instance. The source action then runs on the launched instance instead of on the source server.  
This can happen when:  
**FQDN for Action Framework** is set to a DNS name, and you point that DNS name to a launched test or cutover instance.
You launch a test or cutover instance with [Copy private IP](copy-private.md) enabled, and the connector's network routes that IP to AWS. This can happen, for example, after you migrate the subnet to AWS over a Site-to-Site VPN or AWS Direct Connect. Setting **FQDN for Action Framework** to an IP address doesn't prevent this.

**Recommendations**
+ **Use the source server's IP address if you plan to move a DNS name.** If you plan to point the source server's DNS name to a launched test or cutover instance, set **FQDN for Action Framework** to the source server's IP address instead of the DNS name.
+ **Be careful when you retain the IP and have a VPN or Direct Connect to AWS.** With Copy private IP, the source server and the launched instance share the same IP. If the MGN connector's network is connected to the VPC over a Site-to-Site VPN or AWS Direct Connect and routes that IP to AWS, setting **FQDN for Action Framework** to that IP doesn't guarantee that the action runs on the source server.

You can set **FQDN for Action Framework** when you edit the source server, or with the [`mgn:server:fqdn-for-action-framework`](import-parameters.md) field in the inventory file.