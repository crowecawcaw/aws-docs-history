# Parameter Reference

The cluster setup relies on the following parameters. Gather this information prior to configuring Pacemaker to ensure a smooth setup process.

###### Topics

- [Global AWS parameters](#global-aws-parameters-nw-sles "#global-aws-parameters-nw-sles")
- [Amazon EC2 instance parameters](#ec2-parameters-nw-sles "#ec2-parameters-nw-sles")
- [SAP Instance Parameters](#sap-pacemaker-resource-parameters-nw-sles "#sap-pacemaker-resource-parameters-nw-sles")
- [Pacemaker Parameters](#sles-cluster-parameters "#sles-cluster-parameters")

## Global AWS parameters

| Name           | Parameter      | Example        |
| -------------- | -------------- | -------------- |
| AWS account ID | `<account_id>` | `123456789100` |
| AWS Region     | `<region_id>`  | `us-east-1`    |

- AWS account – For more details, see [Your AWS account ID and its alias](../../../IAM/latest/UserGuide/console-account-alias.md "../../../IAM/latest/UserGuide/console-account-alias.md").
- AWS Region – For more details, see [Describe your Regions](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#using-regions-availability-zones-describe "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#using-regions-availability-zones-describe").

## Amazon EC2 instance parameters

| Name                          | Parameter              | Host 1                                         | Host 2                     |
| ----------------------------- | ---------------------- | ---------------------------------------------- | -------------------------- |
| Amazon EC2 instance ID        | `<instance_id>`        | `i-xxxxinstidforhost1`                         | `i-xxxxinstidforhost2`     |
| Hostname                      | `<hostname>`           | `slxhost01`                                    | `slxhost02`                |
| Host IP                       | `<host_ip>`            | `10.1.10.1`                                    | `10.1.20.1`                |
| Host additional IP            | `<host_additional_ip>` | `10.1.10.2`                                    | `10.1.20.2`                |
| Configured subnet             | `<subnet_id>`          | `subnet-xxxxxxxxxxsubnet1`                     | `subnet-xxxxxxxxxxsubnet2` |
| Associated VPC Route Table(s) | `<routetable_id>`      | `rtb-xxxxxroutetable1 [,rtb-xxxxxroutetable2]` |                            |
| Sapmnt NFS ID or CNAME        | `<sapmnt_nfs_id>`      | `fs-xxxxxxxxxxxxxefs1`                         |                            |

- **Hostname** – Hostnames must comply with SAP requirements outlined in [SAP Note 611361 - Hostnames of SAP ABAP Platform servers](https://me.sap.com/notes/611361 "https://me.sap.com/notes/611361") (requires SAP portal access).

Run the following command on your instances to retrieve the hostname.

```
# hostname
```

- **Amazon EC2 instance ID** – run the following command (IMDSv2 compatible) on your instances to retrieve instance metadata.

```
# /usr/bin/curl --noproxy '*' -w "\n" -s -H "X-aws-ec2-metadata-token: $(curl --noproxy '*' -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")" http://169.254.169.254/latest/meta-data/instance-id
```

For more details, see [Retrieve instance metadata](../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md "../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md") and [Instance identity documents](../../../AWSEC2/latest/UserGuide/instance-identity-documents.md "../../../AWSEC2/latest/UserGuide/instance-identity-documents.md").

- **Amazon EC2 subnet ID** – run the following command to retrieve the subnet ID for each of your instances.

```
# INSTANCE_ID=i-xxxxinstidforhost1
# aws ec2 describe-instances --instance-ids $INSTANCE_ID --query 'Reservations[0].Instances[0].SubnetId' --output text
```

For more details, see [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") and [VPC subnets](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md").

- **Route table(s) for subnets** – run the following AWS CLI commands to retrieve the route table(s) associated with both cluster node subnets.

```
# SUBNET_ID_1=subnet-xxxxxxxxxxsubnet1
# SUBNET_ID_2=subnet-xxxxxxxxxxsubnet2
# aws ec2 describe-route-tables --filters "Name=association.subnet-id,Values=$SUBNET_ID_1,$SUBNET_ID_2" --query 'RouteTables[].RouteTableId' --output text
```

If both cluster nodes are in subnets associated with the same route table, only one route table ID will be returned. If they are associated with different route tables, both route table IDs will be returned.

For more details, see [describe-route-tables](../../../cli/latest/reference/ec2/describe-route-tables.md "../../../cli/latest/reference/ec2/describe-route-tables.md") and [Route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md").

## SAP Instance Parameters

| Name                 | Parameter                | Example       |
| -------------------- | ------------------------ | ------------- |
| SID                  | `<SID>` or `<sid>`       | `SLX`         |
| ASCS Alias           | `<ascs_virt_hostname>`   | `slxascs`     |
| ASCS System Number   | `<ascs_sys_nr>`          | `00`          |
| ASCS Overlay IP      | `<ascs_overlayip>`       | `172.16.1.50` |
| ASCS NFS Mount Point | `<ascs_nfs_mount_point>` | `/SLX_ASCS00` |
| ERS Alias            | `<ers_virt_hostname>`    | `slxers`      |
| ERS System Number    | `<ers_sys_nr>`           | `10`          |
| ERS Overlay IP       | `<ers_overlayip>`        | `172.16.1.51` |
| ERS NFS Mount Point  | `<ers_nfs_mount_point>`  | `/SLX_ERS10`  |
| ENSA Type            | `<ensa_type>`            | `ENSA2`       |

## Pacemaker Parameters

| Name                    | Parameter                 | Example                      |
| ----------------------- | ------------------------- | ---------------------------- |
| Cluster user            | `cluster_user`            | `hacluster`                  |
| Cluster password        | `cluster_password`        |                              |
| Cluster tag             | `cluster_tag`             | `pacemaker`                  |
| AWS CLI cluster profile | `aws_cli_cluster_profile` | `cluster`                    |
| Cluster connector       | `cluster_connector`       | `sap-suse-cluster-connector` |
