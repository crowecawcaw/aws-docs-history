# Testing

We recommend scheduling regular fault scenario recovery testing at least annually, and as part of the operating system or SAP kernel updates that may impact operations. For more details on best practices for regular testing, see SAP Lens – [Best Practice 4.3 – Regularly test business continuity plans and fault recovery](../../../wellarchitected/latest/sap-lens/best-practice-4-3.md "../../../wellarchitected/latest/sap-lens/best-practice-4-3.md").

The tests described here simulate failures. These can help you understand the behavior and operational requirements of your cluster.

In addition to checking the state of cluster resources, ensure that the service you are trying to protect is in the required state. Can you still connect to SAP? Are locks still available in SM12?

Define the recovery time to ensure that it aligns with your business objectives. Record recovery actions in runbooks.

###### Topics

- [Test 1: Stop SAP ASE database using sapcontrol](#test1 "#test1")
- [Test 2: Unmount FSx for ONTAP file system on primary host](#test2 "#test2")
- [Test 3: Kill the database processes on the primary host](#test3 "#test3")
- [Test 4: Simulate hardware failure of an individual node](#test4 "#test4")
- [Test 5: Simulate a network failure](#test5 "#test5")
- [Test 6: Simulate an NFS failure](#test6 "#test6")
- [Test 7: Accidental shutdown](#test7 "#test7")

## Test 1: Stop SAP ASE database using `sapcontrol`

**Simulate failure** – On rhxdbhost01 as root:

```
/usr/sap/hostctrl/exe/saphostctrl -function StopDatabase -dbname ARD -dbtybe syb -force
```

**Expected behavior** – SAP ASE database is stopped, and the `SAPDatabase` resource agent enters a failed state. The cluster will failover the database to the secondary instance.

**Recovery action** – No action required.

## Test 2: Unmount FSx for ONTAP file system on primary host

**Simulate failure** – On rhxdbhost01 as root:

```
umount -l /sybase/ARD/sapdata_1
```

**Expected behavior** – The `rsc_fs` resource enters a failed state. The cluster stops the SAP ASE database, and will failover to the secondary instance.

**Recovery action** – No action required.

## Test 3: Kill the database processes on the primary host

**Simulate failure** – On rhxdbhost01 as root:

```
ps -ef |grep -i sybaard
kill -9 <PID>
```

**Expected behavior** – SAP ASE database fails, and the `SAPDatabase ` resource enters a failed state. The cluster will failover the database to the secondary instance.

**Recovery action** – No action required.

## Test 4: Simulate hardware failure of an individual node

**Notes** – To simulate a system crash, you must first ensure that `/proc/sys/kernel/sysrq` is set to 1.

**Simulate failure** – On the primary host as root:

```
echo 'c' > /proc/sysrq-trigger
```

**Expected behavior** – The node which has been killed fails. The cluster moves the resource (SAP ASE database) that was running on the failed node to the surviving node.

**Recovery action** – Start the EC2 node.

## Test 5: Simulate a network failure

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

**Recovery action** – If the node where the command was run survives, execute iptables -F to clear the network failure. Start the EC2 node.

## Test 6: Simulate an NFS failure

**Notes** – See the following list.

- Iptables must be installed.
- Check for any existing iptables rules as iptables -F will flush all rules.
- Although rare, this is an important scenario to test. Depending on the activity it may take some time (10 min +) to notice that I/O to EFS is not occurring and fail either the Filesystem or SAP resources.

**Simulate failure** – On the primary host as root:

```
iptables -A OUTPUT -p tcp --dport 2049 -m state --state NEW,ESTABLISHED,RELATED -j DROP; iptables -A INPUT -p tcp --sport 2049 -m state --state ESTABLISHED -j DROP
```

**Expected behavior** – The cluster detects that NFS is not available, and the `SAPDatabase` resource agent fails, and moves to the FAILED state.

**Recovery action** – If the node where the command was run survives, execute iptables -F to clear the network failure. Start the EC2 node.

## Test 7: Accidental shutdown

**Notes** – See the following list.

- Avoid shutdowns without cluster awareness.
- We recommend the use of systemd to ensure predictable behaviour.
- Ensure the resource dependencies are in place.

**Simulate failure** – Login to AWS Management Console, and stop the instance or issue a shutdown command.

**Expected behavior** – The node which has been shut down fails. The cluster moves the resource (SAP ASE database) that was running on the failed node to the surviving node. If systemd and resource dependencies are not configured, you may notice that while the EC2 instance is shutting down gracefully, the cluster will detect an unclean stop of cluster services on the node and will fence the EC2 instance being shut down.

**Recovery action** – Start the EC2 node and pacemaker service.
