# Deregistering managed nodes

in a hybrid and multicloud environment

If you no longer want to manage an on-premises server, edge device, or virtual
machine (VM) by using AWS Systems Manager, then you can deregister it. Deregistering a
hybrid-activated node removes it from the list of managed nodes in Systems Manager. AWS Systems Manager
Agent (SSM Agent) running on the hybrid-activated node won't be able to refresh its
authorization token because it's no longer registered. SSM Agent hibernates and
reduce its ping frequency to Systems Manager in the cloud to once per hour. Systems Manager stores the
command history for a deregistered managed node for 30 days.

###### Note

You can reregister an on-premises server, edge device, or VM using the same
activation code and ID as long as you haven't reached the instance limit for the
designated activation code and ID. You can verify the instance limit in the
console by choosing **Node tools**, and then choose
**Hybrid activations**. If the value of
**Registered instances** is less than
**Registration limit**, you can reregister a machine using
the same activation code and ID. If it's greater, you must use a different
activation code and ID.

The following procedure describes how to deregister a hybrid-activated node by
using the Systems Manager console. For information about how to do this by using the
AWS Command Line Interface, see [deregister-managed-instance](../../../cli/latest/reference/ssm/deregister-managed-instance.md "../../../cli/latest/reference/ssm/deregister-managed-instance.md").

For related information, see the following topics:

- [Deregister and reregister a managed node (Linux)](hybrid-multicloud-ssm-agent-install-linux.md#systems-manager-install-managed-linux-deregister-reregister "hybrid-multicloud-ssm-agent-install-linux.md#systems-manager-install-managed-linux-deregister-reregister") (Linux)
- [Deregister and reregister a managed node (Windows Server)](hybrid-multicloud-ssm-agent-install-windows.md#systems-manager-install-managed-win-deregister-reregister "hybrid-multicloud-ssm-agent-install-windows.md#systems-manager-install-managed-win-deregister-reregister") (Windows Server)

###### To deregister a hybrid-activated node (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Select the checkbox next to the managed node that you want to
   deregister.
4. Choose **Node actions, Tools, Deregister this managed
   node**.
5. Review the information in the **Deregister this managed
   node** dialog box. If you approve, choose
   **Deregister**.
