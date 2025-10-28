# Uninstalling the agent

Uninstalling the AWS Replication Agent from a source server stops the replication of
that server. Uninstalling the AWS Replication Agent removes the source server from the
Elastic Disaster Recovery Console.

## Uninstalling the Agent through the AWS Elastic Disaster Recovery console

To uninstall the AWS Replication Agent though the AWS Elastic Disaster Recovery console.

Navigate to the **Source servers** page.

Check the box to the left of each server that you want to disconnect from Elastic
Disaster Recovery (by uninstalling the AWS Replication Agent). Open the **Actions** menu, and choose the **Disconnect from AWS**
option to disconnect the selected server from AWS Elastic Disaster Recovery and AWS.

When the **Disconnect X server/s from service** dialog
appears, click **Disconnect**.

The AWS Replication Agent is uninstalled from all of the selected source
servers.

## Uninstalling the Agent manually through the source server

To uninstall the AWS Replication Agent manually through the source server:

**Windows**

Copy the following folder to a new location:`C:\Program Files (x86)\AWS Replication
 Agent\dist`

From the new
location, run in CMD as an
administrator:

`install_agent_windows.exe --remove`

**Linux**

As root, cd to `/var/lib/aws-replication-agent`.

Run the following commands from that folder:

`./stopAgent.sh`

`./uninstall_agent_linux.sh`
