NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Uninstalling the Agent

Uninstalling the AWS Replication Agent from a source server stops the replication of that
server. Uninstalling the AWS Replication Agent removes the source server from the AWS Application Migration Service
console.

###### Note

- The source server must be able to communicate with the Application Migration Service service in order for the
  Agent to be uninstalled successfully.
- If the Agent is uninstalled directly from a source server without disconnecting the
  server from Application Migration Service or finalizing the cutover within the Application Migration Service console, the replication
  metering period continues and once 2160 hours have elapsed, billing for replication
  begins.

## Uninstalling the Agent through the AWS Application Migration Service

console

To uninstall the AWS Replication Agent though the AWS Application Migration Service console.

Navigate to the **Source servers** page.

Check the box to the left of each server that you want to disconnect from Application Migration Service (by
uninstalling the AWS Replication Agent). Open the **Actions**
menu, and choose the **Disconnect from service** option to
disconnect the selected server from Application Migration Service and AWS.

On the **Disconnect X server/s from service** dialog, click
**Disconnect**.

The AWS Replication Agent is uninstalled from all of the selected source servers.
You can then archive these servers. [Learn more
about archiving.](add-server-server-page.md#server-actions-main "add-server-server-page.md#server-actions-main")

## Uninstalling the Agent manually through the

source server

To uninstall the AWS Replication Agent manually through the source server:

**Windows**

Copy this folder to a new location:`C:\Program Files (x86)\AWS Replication
 Agent\dist`

From the new location, run in CMD as an administrator:

`install_agent_windows.exe --remove`

**Linux**

Run as root or with sudo these commands:

`/var/lib/aws-replication-agent/uninstall-agent.sh`
