# Enabling and disabling HTTPS

Read this section only
if you are using Conductor Live version 3.25 or earlier. With these versions, you must explicitly enable
HTTPS if you want users or applications to have a secure connection to Conductor Live and worker
nodes.

(With Conductor Live version 3.26 and later, HTTPS is enabled by default. There is no need to enable
it.)

###### Note

The HTTPS configuration must be the same for AWS Elemental Conductor Live and all the worker nodes in the
cluster. Either enable HTTPS for all nodes, or disable it for all nodes.

We recommend that you enable HTTPS.

- If your nodes are appliances, then the software was already installed on delivery, with
  HTTPS disabled. You can enable it now on each node.

- If your nodes are on qualified hardware or on VMs, you specified whether to enable HTTPS
  when you installed the software. If you didn't enable HTTPS when you installed, you can
  enable it now on each node.
  Enabling HTTPS has the following impact:

- All the nodes use HTTPS for communications within the cluster.
- When you enter commands using the CLI, you must include the `--https` option.
  These commands include the following:
  - The `run` script that installs or upgrades the software.
  - The `configure` script that configures the software.

###### Warning

If you enter one of these commands and omit `--https`, you will _inadvertently disable HTTPS_ on the node.
**Where to perform the configuration**

Make sure you perform the configuration on the correct nodes.

| Node                          | Work on this node? |
| ----------------------------- | ------------------ |
| Primary Conductor Live node   | Yes                |
| Secondary Conductor Live node | Yes                |
| Each worker node              | Yes                |

###### Topics

- [Enabling HTTPS](#conductor-live-config-ssl "#conductor-live-config-ssl")
- [Disabling HTTPS](#conductor-live-config-ssl-chg "#conductor-live-config-ssl-chg")

## Enabling HTTPS

###### Note

This information applies only to Conductor Live 3.25 and earlier.

###### To enable HTTPS

1. For a worker node, if you have already added the node to the cluster, you must [remove it from the cluster](conductor-live-config-nodes-remove.md "conductor-live-config-nodes-remove.md").

For a Conductor Live node, if you have already added the node to the cluster, you must [disable HA (high availability)](conductor-live-config-ha-chg.md "conductor-live-config-ha-chg.md") and [remove the node from the cluster](conductor-live-config-nodes-remove.md "conductor-live-config-nodes-remove.md"). 2. At your workstation, [start a remote
terminal session](ready-conductor-live-config-access.md "ready-conductor-live-config-access.md") to the primary Conductor Live node. 3. Change to the directory where the configuration script is located and run the
configuration script:

```
[elemental@hostname ~]$ **cd /opt/elemental\_se**
[elemental@hostname elemental_se]$ **sudo ./configure --https --skip-all**
```

The `skip--all` option means that the script enables HTTPS but doesn't
change the configuration in any other way.

###### Note

If you run this command (with the `--https` option) when HTTPS is already
enabled, nothing changes in the configuration. HTTPS is still enabled.

## Disabling HTTPS

###### Note

This information applies only to Conductor Live 3.25 and earlier.

Change to the directory where the configuration script is located and run the
configuration script:

```
[elemental@hostname ~]$ **cd /opt/elemental\_se**
[elemental@hostname elemental_se]$ **sudo ./configure --skip-all**
```

The `skip--all` option means that the script disables HTTPS but doesn't change
the configuration in any other way.

###### Note

If you run the script without the `--https` option when HTTPS is already
disabled, nothing changes in the configuration. HTTPS is still disabled.
