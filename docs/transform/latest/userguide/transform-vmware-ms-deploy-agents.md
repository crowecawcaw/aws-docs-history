

# Step 3: Deploy replication agents
<a name="transform-vmware-ms-deploy-agents"></a>

To begin replicating data from your source servers to AWS, you install the AWS Replication Agent on each source server. AWS Transform offers three installation methods:
+ **Organization tools** – Use your organization's existing deployment tools (such as SCCM, Ansible, or Chef) to install agents across your servers. AWS Transform provides the installation commands with additional parameters for silent installation, including `--no-prompt`, `--aws-access-key-id`, `--aws-secret-access-key`, and `--aws-session-token`.
+ **MGN connector** – Use an MGN connector to automate agent installation. The connector connects to source machines over SSH (Linux) or WinRM (Windows) and installs the replication agent automatically. After it is configured, a connector can be reused across multiple waves and different target AWS accounts. For more information about the MGN connector, see [Set up the MGN Connector](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-setup-instructions.html) in the *MGN User Guide*.
**Note**  
Before using the MGN connector with AWS Transform, you must tag the connector's managed instance in AWS Systems Manager Fleet Manager with the following tags:  
Key: `CreatedFor` Value: `AWSTransform`
Key: `ATWorkspace` Value: {{workspace-id}}
To tag the managed instance, open the AWS Systems Manager console, navigate to **Fleet Manager** under **Node Tools**, choose the managed instance of your MGN connector, and apply the tags above. Find your workspace ID in the AWS Transform web app URL: `https://.../workspace/{{workspace-id}}/job/{{job-id}}`.
+ **Manual installation** – Install the agent directly on each source server. This method requires direct access to each server but gives you full control over the installation process.

After installation, AWS Transform verifies that all agents are successfully connected by checking that servers show a replication state of `INITIATING` or `INITIAL_SYNC`.

**Note**  
AWS Transform does not support MGN agentless replication. For information about agentless replication, see [Agentless replication overview](https://docs.aws.amazon.com/mgn/latest/ug/installing-vcenter-overview-mgn.html) in the *MGN User Guide*.

**Note**  
You must install the replication agent on all servers in a wave. Disconnect and archive servers on which you don't install the replication agent. You can use the `disconnect-from-service` command to disconnect servers, and the `mark-as-archived` command to archive disconnected servers. The archiving command only works for source servers whose lifecycle state is `DISCONNECTED`.

For quotas related to replication, see [MGN service quota limits](https://docs.aws.amazon.com/mgn/latest/ug/MGN-service-limits.html) in the *MGN User Guide*.