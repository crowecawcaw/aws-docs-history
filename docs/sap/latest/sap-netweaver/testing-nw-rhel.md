# Testing

We recommend scheduling regular fault scenario recovery testing at least annually, and as part of the operating system or SAP kernel updates that may impact operations. For more details on best practices for regular testing, see SAP Lens – [Best Practice 4.3 – Regularly test business continuity plans and fault recovery](../../../wellarchitected/latest/sap-lens/best-practice-4-3.md "../../../wellarchitected/latest/sap-lens/best-practice-4-3.md").

The tests described here simulate failures. These can help you understand the behavior and operational requirements of your cluster.

In addition to checking the state of cluster resources, ensure that the service you are trying to protect is in the required state. Can you still connect to SAP? Are locks still available in SM12?

Define the recovery time to ensure that it aligns with your business objectives. Record recovery actions in runbooks.

###### Topics

- [Test 1: Stop ASCS on the primary node using sapcontrol](#test1-nw-rhel "#test1-nw-rhel")
- [Test 2: Stop ERS on the secondary node using sapcontrol](#test2-nw-rhel "#test2-nw-rhel")
- [Test 3: Kill the message server process on the primary node](#test3-nw-rhel "#test3-nw-rhel")
- [Test 4: Kill the enqueue server process on the primary node](#test4-nw-rhel "#test4-nw-rhel")
- [Test 5: Kill the ER process](#test5-nw-rhel "#test5-nw-rhel")
- [Test 6: Simulate hardware failure of an individual node, and repeat for other node](#test6-nw-rhel "#test6-nw-rhel")
- [Test 7: Simulate a network failure](#test7-nw-rhel "#test7-nw-rhel")
- [Test 8: Simulate an NFS failure](#test8-nw-rhel "#test8-nw-rhel")
- [Test 9: Accidental shutdown](#test9-nw-rhel "#test9-nw-rhel")

## Test 1: Stop ASCS on the primary node using `sapcontrol`

**Notes** – Ensure that the connector has been installed and the parameters have been updated.

**Simulate failure** – On `rhxhost01` as `rhxadm`:

```
sapcontrol -nr <00> -function Stop
```

**Expected behavior** – ASCS should be stopped on `rhxhost01`, and the cluster should not perform any activity.

**Recovery action** – Start ASCS manually.

## Test 2: Stop ERS on the secondary node using `sapcontrol`

**Notes** – Ensure that the connector has been installed, and the parameters are updated.

**Simulate failure** – On `rhxhost02` as `rhxadm`:

```
sapcontrol -nr <10> -function Stop
```

**Expected behavior** – ERS should be stopped on `rhxhost02`, and the cluster should not perform any activity.

**Recovery action** – Start ERS manually.

## Test 3: Kill the message server process on the primary node

**Simulate failure** – On `rhxhost01` as `rhxadm`:

```
kill -9 $(pgrep -f "ms.sap<RHX>_ASCS<00>")
```

**Expected behavior** – The message server should immediately respawn based on the Restart parameter.

**Recovery action** – No action required.

## Test 4: Kill the enqueue server process on the primary node

**Notes** – Check that locks have persisted, and review the location constraints that only exist for ENSA1.

**Simulate failure** – On `rhxhost01` as `rhxadm`:

```
kill -9 $(pgrep -f "[en|enq].sap<RHX>_ASCS<00>")
```

**Expected behavior** – ENSA2: Cluster will restart the ENQ process and retrieve the locks remotely. ENSA1: Cluster will failover the ASCS resource to the node where the ERS is running.

**Recovery action** – No action required.

## Test 5: Kill the ER process

**Simulate failure** – On `rhxhost02` as `rhxadm`:

```
kill -9 $(pgrep -f "[er|enqr].sap<RHX>_ERS<10>")
```

**Expected behavior** – Cluster will restart the ERS on the same node.

**Recovery action** – No action required.

## Test 6: Simulate hardware failure of an individual node, and repeat for other node

**Notes** – To simulate a system crash, you must first ensure that `/proc/sys/kernel/sysrq` is set to 1.

**Simulate failure** – On both nodes as root:

```
echo 'b' > /proc/sysrq-trigger
```

**Expected behavior** – The node which has been killed fails. The cluster will move the resources (ASCS/ERS) which were running on the failed node to the surviving node.

**Recovery action** – Start the EC2 node and pacemaker service. The cluster will detect that the node is online and move the ERS resource so that the ASCS and ERS are not running on the same node (colocation constraint).

## Test 7: Simulate a network failure

**Notes** – See the following list.

- Iptables must be installed.
- Use a subnet in this command because of the secondary ring.
- Check for any existing iptables rules as iptables -F will flush all rules.
- Review pcmk_delay and priority parameters if you see neither node survives the fence race.

**Simulate failure** – On either node as root:

```
iptables -A INPUT -s <CIDR_of_other_subnet> -j DROP; iptables -A OUTPUT -d <CIDR_of_other_subnet> -j DROP
```

**Expected behavior** – The cluster detects the network failure, and fences one of the nodes to avoid a split-brain situation.

**Recovery action** – If the node where the command was run survives, execute iptables -F to clear the network failure. Start the EC2 node and pacemaker service. The cluster will detect that the node is online and move the ERS resource so that the ASCS and ERS are not running on the same node (colocation constraint).

## Test 8: Simulate an NFS failure

**Notes** – See the following list.

- Iptables must be installed.
- Check for any existing iptables rules as iptables -F will flush all rules.
- Although rare, this is an important scenario to test. Depending on the activity it may take some time (10 min +) to notice that I/O to EFS is not occurring and fail either the Filesystem or SAP resources.

**Simulate failure** – On either node as root:

```
iptables -A OUTPUT -p tcp --dport 2049 -m state --state NEW,ESTABLISHED,RELATED -j DROP; iptables -A INPUT -p tcp --sport 2049 -m state --state ESTABLISHED -j DROP
```

**Expected behavior** – The cluster detects that NFS is not available, and the SAP Instance resource agent will fail and move to the FAILED state. Because of the option "on-fail=restart" configuration, the cluster will try a local restart before eventually fencing the node and failing over.

**Recovery action** – If the node where the command was run survives, execute iptables -F to clear the network failure. Start the EC2 node and pacemaker service. The cluster will detect that the node is online and move the ERS resource so that the ASCS and ERS are not running on the same node (colocation constraint).

## Test 9: Accidental shutdown

**Notes** – See the following list.

- Avoid shutdowns without cluster awareness.
- We recommend the use of systemd to ensure predictable behaviour.
- Ensure the resource dependencies are in place.

**Simulate failure** – Login to AWS Management Console, and stop the instance or issue a shutdown command.

**Expected behavior** – The node which has been shut down fails. The cluster will move the resources (ASCS/ERS) which were running on the failed node to the surviving node. If systemd and resource dependencies are not configured, you may notice that while the EC2 instance is shutting down gracefully, the cluster will detect an unclean stop of cluster services on the node and will fence the EC2 instance being shut down. For more information, see [Red Hat documentation – Stopping the Cluster Services on a Node](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_high_availability_clusters/assembly_maintaining-a-cluster-configuring-and-managing-high-availability-clusters#proc_stopping-cluster-services-on-a-node-maintaining-a-cluster "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_high_availability_clusters/assembly_maintaining-a-cluster-configuring-and-managing-high-availability-clusters#proc_stopping-cluster-services-on-a-node-maintaining-a-cluster").

**Recovery action** – Start the EC2 node and pacemaker service. The cluster will detect that the node is online, and move the ERS resource so that the ASCS and ERS are not running on the same node (colocation constraint).
