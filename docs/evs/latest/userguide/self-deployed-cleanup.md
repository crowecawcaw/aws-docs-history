

# Clean up a Self-deployed environment

When you no longer need your Amazon Elastic VMware Service environment, delete its connectors, hosts, and the environment itself, to stop the charges for the hosts. You can use the Amazon EVS console or the AWS CLI. Then delete the network resources that you created outside of Amazon EVS.

**Warning**  
Deleting the hosts and the environment deletes the VMware Cloud Foundation (VCF) installation that runs in the environment. You can’t undo this action. Back up or migrate any workloads that you want to keep before you start.

## Delete the connectors
<a name="self-deployed-cleanup-connectors"></a>

Delete all connectors of the environment. For instructions, see [Delete a connector](evs-env-delete-connector.md).

## Delete the hosts and the environment
<a name="self-deployed-cleanup-env"></a>

Delete all hosts before you delete the environment, because you can’t delete an environment that still has hosts. To delete the hosts and the environment in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment that contains the hosts to delete.

1. Select the **Hosts** tab.

1. Select a host and choose **Delete**. Repeat this step for each host in the environment.

1. At the top of the **Environments** page, choose **Delete** and then **Delete environment**.

1. Find the ID of the environment.

   ```bash
   aws evs list-environments
   ```

1. Delete each host in the environment. Replace `<environment-id>` with the ID of your environment, and replace the example host name `esx01` with the name of the host.

   ```bash
   aws evs delete-environment-host \
       --environment-id <environment-id> \
       --host-name esx01
   ```

1. Repeat the previous step for the remaining hosts in your environment.

1. Delete the environment.

   ```bash
   aws evs delete-environment --environment-id <environment-id>
   ```

Environment deletion also deletes the Amazon EVS VLAN subnets and the AWS Secrets Manager secrets that Amazon EVS created. It doesn’t delete the VPC, the route server, or other AWS resources that you created outside of Amazon EVS. These resources can continue to incur costs.

To remove a single host from a running cluster instead, see [Delete a host (VCF 9.x)](host-delete.md).

## Delete the remaining resources
<a name="self-deployed-cleanup-other"></a>

To delete the remaining resources, do the following.

1. If you have Amazon EC2 Capacity Reservations that you no longer need, cancel them. For more information, see [Cancel a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-release.html) in the *Amazon EC2 User Guide*.

1. If you used diskless hosts, delete your external storage, such as the file system and its volumes, to stop accruing storage charges. Deleting the environment doesn’t delete external storage.

1. Delete the network resources, such as the route server, the network ACL, the route tables, the subnets, and the VPC. For instructions, see [Clean up network resources](cleanup.md).

You have cleaned up the environment.