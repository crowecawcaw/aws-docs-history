

# Step 6: Cutover
<a name="transform-vmware-ms-cutover"></a>

Cutover is the final migration step where your production workloads are moved to AWS. For more information, see [Launch cutover instances](https://docs.aws.amazon.com/mgn/latest/ug/launch-cutover-instances.html) in the *MGN User Guide*. Similar to testing, AWS Transform supports full wave cutover or selective cutover for specific servers.

During cutover, AWS Transform launches Amazon EC2 instances from the latest replicated data and provides the instance IDs for each server. After verifying the cutover instances, you finalize the cutover, which stops the ongoing source machine replication.

The cutover process includes the following steps:

1. **Launch cutover instances** – AWS Transform launches Amazon EC2 instances for the selected servers. You can choose full wave cutover or selective cutover.

1. **Verify cutover instances** – Connect to the launched instances and verify they are functioning correctly.

1. **Finalize cutover** – Confirm the cutover to stop source machine replication. You can finalize all servers in the wave or select specific servers. Finalization stops replication agents from sending data, removes replication agents from source servers, and locks the server lifecycle state. This action cannot be easily undone. For more information, see [Finalize cutover](https://docs.aws.amazon.com/mgn/latest/ug/finalizing-cutover-2.html) in the *MGN User Guide*.

1. **Archive source servers (optional)** – After finalization, you can mark source servers as archived to free up source server quota in your account.

**Important**  
Finalizing cutover stops the ongoing source machine replication. Make sure you have verified your cutover instances before finalizing.

**Note**  
Downtime occurs between source shutdown and cutover instance availability. Plan your cutover window accordingly.