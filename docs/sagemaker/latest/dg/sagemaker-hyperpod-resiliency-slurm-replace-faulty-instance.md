# Manually

replace or reboot a node

This section talks about when you should manually reboot or replace a node, with
instructions on how to do both.

The HyperPod auto-resume functionality monitors if the state of your Slurm
nodes turns to `fail` or `down`. You can check the state of Slurm
nodes by running `sinfo`.

If you have a node stuck with an issue but not being fixed by the HyperPod
auto-resume functionality, we recommend you to run one of the following commands to
change the state of the node to `fail`.

## Manully reboot a node

**Reboot** should be your first approach for
temporary or recoverable issues that don't indicate underlying hardware problems.
Use rebooting when you encounter system hangs, performance degradation, memory
leaks, GPU driver issues, or hung processes - essentially any situation where the
hardware is functioning but the software stack needs a fresh start. Rebooting is
also necessary after kernel updates or patches that require a restart to take
effect.

In the following command , replace <ip-ipv4> with the Slurm node name (host
name) of the faulty instance you want to reboot.

```
scontrol update node=`<ip-ipv4>` state=`fail` reason="Action:Reboot"
```

## Manually replace a node

**Replace** the node when you're dealing with actual
hardware failures or when the system has reached an unrecoverable state that
rebooting cannot fix. This includes scenarios where hardware components (GPUs,
memory, networking) are physically failing, when repeated reboots don't resolve
persistent issues, or when the node consistently fails health checks even after
restarts. Replacement involves the more complex process of provisioning a new
instance and can take significantly longer than a simple reboot, so it should only
be used when the underlying hardware or system state is fundamentally
compromised.

In the following command, replace
`<ip-ipv4>` with the Slurm node name
(host name) of the faulty instance you want to replace.

```
scontrol update node=`<ip-ipv4>` state=`fail` reason="Action:Replace"
```

After running this command, the node will go into the `fail` state,
waits for the currently running jobs to finish, is replaced with a healthy instance,
and is recovered with the same host name. This process takes time depending on the
available instances in your Availability Zone and the time it takes to run your
lifecycle scripts. During the update and replacement processes, avoid changing the
state of the node manually again or restarting the Slurm controller; doing so can
lead to a replacement failure. If the node does not get recovered nor turn to the
`idle` state after a long time, contact [AWS Support](https://console.aws.amazon.com/support/ "https://console.aws.amazon.com/support/").

## Manually force change a node

If the faulty node is continuously stuck in the `fail` state, the last
resort you might try is to manually force change the node state to
`down`. This requires administrator privileges (sudo permissions).

###### Warning

Proceed carefully before you run the following command as it forces kill all
jobs, and you might lose all unsaved work.

```
scontrol update node=`<ip-ipv4>` state=`down` reason="Action:Replace"
```
