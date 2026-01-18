# Testing

We recommend scheduling regular fault scenario recovery testing at least annually, and as part of the operating system or HANA Upgrades that may impact operations. For more details on best practices for regular testing, see SAP Lens – [Best Practice 4.3 – Regularly test business continuity plans and fault recovery](../../../wellarchitected/latest/sap-lens/best-practice-4-3.md "../../../wellarchitected/latest/sap-lens/best-practice-4-3.md").

The tests described here simulate failures. These can help you understand the behavior and operational requirements of your cluster.

In addition to checking the state of cluster resources, ensure that the service you are trying to protect is in the required state. Is client connectivity still possible?
Define the recovery time to ensure that it aligns with your business objectives. Record recovery actions in runbooks.

###### Topics

- [Test 1: Stop HANA on the primary node using HDB kill-9](#_test_1_stop_hana_on_the_primary_node_using_hdb_kill_9 "#_test_1_stop_hana_on_the_primary_node_using_hdb_kill_9")
- [Test 2: Simulate a hardware failure](#_test_2_simulate_a_hardware_failure "#_test_2_simulate_a_hardware_failure")
- [Test 3: Simulate a kernel panic](#_test_3_simulate_a_kernel_panic "#_test_3_simulate_a_kernel_panic")
- [Test 4: Simulate a network failure](#_test_4_simulate_a_network_failure "#_test_4_simulate_a_network_failure")
- [Test 5: Accidental shutdown](#_test_5_accidental_shutdown "#_test_5_accidental_shutdown")
- [Other Tests](#_other_tests "#_other_tests")

## Test 1: Stop HANA on the primary node using `HDB kill-9`

**Why** – Tests cluster response to an immediate HANA process termination. This validates the cluster’s ability to detect and respond to critical database process failures and ensures proper failover mechanisms are working.

**Simulate failure** – On `hanahost01` as `hdbadm`:

```
 hdbadm> HDB kill-9
```

**Expected behavior** – The cluster detects the HANA process failure and triggers immediate failover to the secondary node. The secondary node is promoted to primary, taking over the workload without attempting local recovery.

**Recovery action** –

1. Monitor cluster status using `crm_mon -r`
2. Verify HANA system replication status using `hdbnsutil -sr_state`
3. If AUTOMATED_REGISTER is "false", manually reregister the former primary:
   - See more details on how to register the secondary in [HSR Setup](sap-hana-pacemaker-rhel-hana-setup-hsr.md "sap-hana-pacemaker-rhel-hana-setup-hsr.md") :

   ```
    hdbnsutil -sr_register --name=<site_name> --remoteHost=<primary_host> --remoteInstance=<instance_number> --mode=sync --operationMode=logreplay
   ```

## Test 2: Simulate a hardware failure

**Why** – Tests cluster response to complete node failure, validating proper fencing behavior and resource failover when a node becomes completely unresponsive.

**Notes** – The double force option (`--force --force`) is used to simulate a hardware failure as closely as possible in a test environment. This command bypasses the system manager and forces an immediate shutdown without any cleanup, similar to a power loss or hardware failure. However, it’s important to note that this is still a simulation - some OS-level cleanup may still occur that wouldn’t happen in a real hardware failure or power loss scenario.

**Simulate failure** – On `hanahost01` as `root`:

```
 # poweroff --force --force
```

**Expected behavior** – Corosync detects the loss of node communication and Pacemaker on the surviving node initiates fencing through the fencing agent, followed by promotion of the secondary HANA instance to primary. Application connections should automatically reconnect to the new primary.

**Recovery action** –

1. Start the powered-off Amazon EC2 instance
2. Verify cluster status using `crm_mon -r`
3. Clean up STONITH history using `pcs stonith history cleanup`
4. Check HANA replication status using `hdbnsutil -sr_state`
5. If AUTOMATED_REGISTER is "false", manually register as secondary
6. Verify application connectivity to the new primary

## Test 3: Simulate a kernel panic

**Why** – Tests cluster response to catastrophic kernel failure, ensuring proper recovery mechanisms work when a node experiences a complete system crash.

**Notes** – To simulate a system crash, you must first ensure that `/proc/sys/kernel/sysrq` is set to 1.

**Simulate failure** – On `hanahost01` as `root`:

```
 # echo 'c' > /proc/sysrq-trigger
```

**Expected behavior** – The cluster detects node failure through lost heartbeat. The surviving node initiates fencing through the fencing agent, followed by promotion of the secondary HANA instance to primary.

**Recovery action** –

1. Restart the node after kernel panic
2. Verify cluster status using `crm_mon -r`
3. Clean up STONITH history using `pcs stonith history cleanup`
4. Check HANA replication status using `hdbnsutil -sr_state`
5. If AUTOMATED_REGISTER is "false", manually register as secondary
6. Verify all cluster resources are clean

## Test 4: Simulate a network failure

**Why** – Tests cluster behavior during network partition scenarios, ensuring split-brain prevention mechanisms work and proper fencing occurs when nodes can’t communicate.

**Notes** –

- Iptables must be installed
- Use a subnet in this command because of the secondary ring
- Check for any existing iptables rules as iptables -F will flush all rules
- Review pcmk_delay and priority parameters if you see neither node survives the fence race

**Simulate failure** – On either node as root:

```
 # iptables -A INPUT -s <CIDR_of_other_subnet> -j DROP; iptables -A OUTPUT -d <CIDR_of_other_subnet> -j DROP
```

**Expected behavior** – The cluster detects the network failure and fences one of the nodes to avoid a split-brain situation. The surviving node assumes control of cluster resources.

**Recovery action** –

1. If the failure is simulated on the surviving node, execute `iptables -F` to clear the network failure
2. Start the EC2 node and pacemaker service
3. Verify cluster status and resource placement

## Test 5: Accidental shutdown

**Why** – Tests proper handling of shutdown scenarios, ensuring the cluster manages resources appropriately during both planned and unplanned shutdowns.

**Notes** –

- Avoid shutdowns without cluster awareness
- We recommend the use of systemd to ensure predictable behavior
- Ensure the resource dependencies are in place

**Simulate failure** – Login to AWS Management Console, and stop the instance or issue a shutdown command.

**Expected behavior** – The node which has been shut down fails. The cluster will move the resources which were running on the failed node to the surviving node. If systemd and resource dependencies are not configured correctly, the cluster may detect an unclean stop of cluster services and fence the shutting-down instance.

**Recovery action** –

1. Start the EC2 node and pacemaker service
2. Verify cluster status and resource placement
3. Ensure resources are properly distributed according to constraints

## Other Tests

Consider these additional tests based on your environment and project requirements:

- **Secondary Node Testing**
  - Execute previous tests on the secondary, to ensure that secondary disruptions do not impact service availability on the primary
  - Execute previous tests with the nodes in reversed roles to validate full operational capability in either configuration

- **Scale-out Testing** (for scale-out deployments)
  - Test failures on coordinator and worker nodes
  - Test concurrent failure of multiple worker nodes to verify failover order
  - Test failures with blocked access to storage access including /hana/shared

- **Component-Level Testing**
  - Test index server failures and measure recovery times
  - Validate Fast Start Option behavior and hook script execution

- **Cluster Configuration Testing**
  - Direct fencing operations using `pcs stonith fence <node_name>`
  - Resource movement and constraint verification

Remember to document all test results, recovery times, and any unexpected behaviors for future reference and runbook updates.
