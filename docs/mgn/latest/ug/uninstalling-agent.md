

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Uninstalling the Agent
<a name="uninstalling-agent"></a>

Uninstalling the AWS Replication Agent from a source server stops the replication of that server. Uninstalling the AWS Replication Agent removes the source server from the AWS Transform MGN console. 

**Note**  
The source server must be able to communicate with the MGN service in order for the Agent to be uninstalled successfully.
If the Agent is uninstalled directly from a source server without disconnecting the server from MGN or finalizing the cutover within the MGN console, the replication metering period continues and once 2160 hours have elapsed, billing for replication begins. 

## Uninstalling the Agent through the AWS Transform MGN console
<a name="uninstalling-agent-cirrus"></a>

To uninstall the AWS Replication Agent through the AWS Transform MGN console:

Navigate to the **Source servers** page. 

Check the box to the left of each server that you want to disconnect from MGN (by uninstalling the AWS Replication Agent). Open the **Actions** menu, and choose the **Disconnect from service** option to disconnect the selected server from MGN and AWS. 

On the **Disconnect X server/s from service** dialog, choose **Disconnect**. 

The AWS Replication Agent is uninstalled from all of the selected source servers. You can then archive these servers. [Learn more about archiving.](add-server-server-page.md#server-actions-main)

## Uninstalling the Agent manually through the source server
<a name="uninstalling-agent-mgn-manual"></a>

To uninstall the AWS Replication Agent manually through the source server:

**Windows**

Copy this folder to a new location:`C:\Program Files (x86)\AWS Replication Agent\dist`

From the new location, run in CMD as an administrator:

`install_agent_windows.exe --remove`

**Linux**

Run as root or with sudo these commands:

`/var/lib/aws-replication-agent/uninstall-agent.sh`