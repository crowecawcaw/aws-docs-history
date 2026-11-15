

# Getting compute node group details in AWS PCS
<a name="working-with_cng_get-details"></a>

You can use the AWS Management Console or the AWS CLI to get details about a compute node group, such as its ID, Amazon Resource Name (ARN), and status. You often need these values for AWS PCS API actions and configurations. The details also include the [instance settings](working-with_cng_instance-settings.md) on the compute node group: the AMI ID, security groups, and SSH key pair.

------
#### [ AWS Management Console ]

**To get compute node group details (console)**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters).

1. Choose the cluster that has the compute node group.

1. Choose **Compute node groups**, and then choose the compute node group.

The details page doesn't show whether the compute node group uses **Standard configuration** or **Launch template configuration**. With **Launch template configuration**, the **AMI ID**, **Security groups**, and **SSH key pair** fields show only values that you set on the compute node group. They don't show values from the launch template. An empty field means that AWS PCS uses the value in the launch template. To see the values in the launch template, view the launch template version in the Amazon EC2 console, or use the Amazon EC2 `DescribeLaunchTemplateVersions` operation.

------
#### [ AWS CLI ]

**To get compute node group details (AWS CLI)**

1. To find your cluster name or ID, run the following command. It uses the [ListClusters](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListClusters.html) API action. Replace {{region}} with the ID of the AWS Region where your cluster is, such as `us-east-1`.

   ```
   aws pcs list-clusters --region {{region}}
   ```

   **Example output:**

   ```
   {
       "clusters": [
           {
               "name": "get-started-cfn",
               "id": "pcs_abc1234567",
               "arn": "arn:aws:pcs:us-east-1:111122223333:cluster/pcs_abc1234567",
               "createdAt": "2025-04-01T20:11:22+00:00",
               "modifiedAt": "2025-04-01T20:11:22+00:00",
               "status": "ACTIVE"
           }
       ]
   }
   ```

1. To list the compute node groups in a cluster, run the following command. It uses the [ListComputeNodeGroups](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListComputeNodeGroups.html) API action. Replace {{cluster-name-or-id}} with the name or ID of your cluster.

   ```
   aws pcs list-compute-node-groups --region {{region}} --cluster-identifier {{cluster-name-or-id}}
   ```

   **Example call:**

   ```
   aws pcs list-compute-node-groups --region us-east-1 --cluster-identifier get-started-cfn
   ```

   **Example output:**

   ```
   {
       "computeNodeGroups": [
           {
               "name": "compute-1",
               "id": "pcs_abc123abc1",
               "arn": "arn:aws:pcs:us-east-1:111122223333:cluster/pcs_abc1234567/computenodegroup/pcs_abc123abc1",
               "clusterId": "pcs_abc1234567",
               "createdAt": "2025-04-01T20:19:25+00:00",
               "modifiedAt": "2025-04-01T20:19:25+00:00",
               "status": "ACTIVE"
           },
           {
               "name": "login",
               "id": "pcs_abc456abc7",
               "arn": "arn:aws:pcs:us-east-1:111122223333:cluster/pcs_abc1234567/computenodegroup/pcs_abc456abc7",
               "clusterId": "pcs_abc1234567",
               "createdAt": "2025-04-01T20:19:31+00:00",
               "modifiedAt": "2025-04-01T20:19:31+00:00",
               "status": "ACTIVE"
           }
       ]
   }
   ```

1. To get all the details for a compute node group, run the following command. It uses the [GetComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_GetComputeNodeGroup.html) API action. Replace {{compute-node-group-name-or-id}} with the name or ID of the compute node group.

   ```
   aws pcs get-compute-node-group --region {{region}} --cluster-identifier {{cluster-name-or-id}} --compute-node-group-identifier {{compute-node-group-name-or-id}}
   ```

   **Example call:**

   ```
   aws pcs get-compute-node-group --region us-east-1 --cluster-identifier get-started-cfn --compute-node-group-identifier compute-1
   ```

   **Example output:**

   ```
   {
       "computeNodeGroup": {
           "name": "compute-1",
           "id": "pcs_abc123abc1",
           "arn": "arn:aws:pcs:us-east-1:111122223333:cluster/pcs_abc1234567/computenodegroup/pcs_abc123abc1",
           "clusterId": "pcs_abc1234567",
           "createdAt": "2025-04-01T20:19:25+00:00",
           "modifiedAt": "2025-04-01T20:19:25+00:00",
           "status": "ACTIVE",
           "amiId": "ami-0123456789abcdef0",
           "securityGroupIds": [
               "sg-0123456789abcdef0"
           ],
           "sshKeyName": "my-key-pair",
           "subnetIds": [
               "subnet-abc012345789abc12"
           ],
           "purchaseOption": "ONDEMAND",
           "launchTemplateMode": "MANAGED",
           "iamInstanceProfileArn": "arn:aws:iam::111122223333:instance-profile/AWSPCS-get-started-cfn-us-east-1",
           "scalingConfiguration": {
               "minInstanceCount": 0,
               "maxInstanceCount": 4
           },
           "instanceConfigs": [
               {
                   "instanceType": "c6i.xlarge"
               }
           ]
       }
   }
   ```

   In this example, the compute node group uses standard configuration (`launchTemplateMode` is `MANAGED`). If a compute node group uses launch template configuration, `launchTemplateMode` is `CUSTOM` and the output also includes `customLaunchTemplate`. The output includes `amiId`, `securityGroupIds`, and `sshKeyName` only if you set them on the compute node group. It doesn't include values from the launch template. For more information, see [Viewing instance settings](working-with_cng_instance-settings.md#working-with_cng_instance-settings_view).

------