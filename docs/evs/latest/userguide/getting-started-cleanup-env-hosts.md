

# Delete an EVS-deployed environment

This page applies to EVS-deployed environments (VCF 5.2.x). For Self-deployed environments that run VCF 9.x, see [Deploy in Self-deployed mode](getting-started-self-deployed.md).

Delete the Amazon Elastic VMware Service hosts and then the environment with the Amazon EVS console or the AWS CLI. After that, delete the network resources that you created for the environment. For a Self-deployed environment, see [Clean up a Self-deployed environment](self-deployed-cleanup.md).

**Warning**  
Deleting the hosts and the environment deletes the VMware Cloud Foundation (VCF) installation that runs in your Amazon EVS environment. You can’t undo this action.

You must delete all hosts in an environment before you can delete the environment. To remove one host and keep the environment, see [Delete a host (VCF 5.x)](evs-env-delete-host.md).

## Delete the hosts and the environment
<a name="cleanup-evs-deployed-procedure"></a>

You can delete the hosts and the environment by using the Amazon EVS console or the AWS CLI.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment that contains the hosts to delete.

1. Choose the **Hosts** tab.

1. Select a host and choose **Delete**. Repeat this step for each host in the environment.

1. Wait until the **Hosts** tab shows no hosts.

1. At the top of the **Environments** page, choose **Delete** and then **Delete environment**.

1. If you have Amazon EC2 Capacity Reservations that you no longer need, cancel them. For more information, see [Cancel a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-release.html) in the *Amazon EC2 User Guide*.

1. Open a terminal session.

1. Identify the environment that contains the hosts to delete.

   ```bash
   aws evs list-environments
   ```

   The following is a sample response.

   ```json
   {
       "environmentSummaries": [
           {
               "environmentId": "env-abcde12345",
               "environmentName": "testEnv",
               "vcfVersion": "VCF-5.2.2",
               "environmentState": "CREATED",
               "createdAt": "2025-04-13T14:42:41.430000+00:00",
               "modifiedAt": "2025-04-13T14:43:33.412000+00:00",
               "environmentArn": "arn:aws:evs:us-east-2:111122223333:environment/env-abcde12345"
           },
           {
               "environmentId": "env-edcbaEXAMPLE",
               "environmentName": "testEnv2",
               "vcfVersion": "VCF-5.2.2",
               "environmentState": "CREATED",
               "createdAt": "2025-04-13T13:39:49.546000+00:00",
               "modifiedAt": "2025-04-13T13:52:13.342000+00:00",
               "environmentArn": "arn:aws:evs:us-east-2:111122223333:environment/env-edcbaEXAMPLE"
           }
       ]
   }
   ```

   The ARNs in the sample use the `aws` partition. In other partitions, the ARN starts with that partition name.

1. Delete a host from the environment. The following is a sample `aws evs delete-environment-host` request.

   ```bash
   aws evs delete-environment-host \
   --environment-id env-abcde12345 \
   --host-name esx01
   ```

1. Repeat the previous step for each remaining host in the environment.

1. Wait until the following command returns no hosts.

   ```bash
   aws evs list-environment-hosts --environment-id env-abcde12345
   ```

1. Delete the environment.

   ```bash
   aws evs delete-environment --environment-id env-abcde12345
   ```

1. If you have Amazon EC2 Capacity Reservations that you no longer need, cancel them. For more information, see [Cancel a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-release.html) in the *Amazon EC2 User Guide*.

You have deleted the hosts and the environment.

## What environment deletion removes
<a name="cleanup-evs-deployed-what-remains"></a>

Environment deletion also deletes the Amazon EVS VLAN subnets and the AWS Secrets Manager secrets that Amazon EVS created.

**Important**  
Environment deletion doesn’t delete the AWS resources that you created, such as the VPC, the service access subnet, the route server, and the network ACL. These resources can continue to incur charges until you delete them.

## Next step
<a name="cleanup-evs-deployed-next"></a>

Delete the network resources that you created for the environment, including IPAM resources if you configured HCX internet connectivity. For more information, see [Clean up network resources](cleanup.md).