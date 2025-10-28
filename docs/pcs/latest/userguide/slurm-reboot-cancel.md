# Cancel a pending reboot in AWS PCS

Cancel a pending reboot to avoid unnecessary downtime when the issue has been resolved or
when reboot is no longer needed.

## Prerequisites

- Slurm Admin privileges
- Node must have a pending reboot (showing "reboot issued" status)
- Access to login node for command execution

## Procedure

1. Connect to the login node.
2. Verify the node has a pending reboot using `scontrol show node`.

```
scontrol show node `nodename`
```

Look for "reboot issued" in the node status. 3. Execute the cancel command.

```
scontrol cancel_reboot `nodename`
```

4. Verify reboot cancellation and node status return to normal.

```
scontrol show node `nodename`
```
