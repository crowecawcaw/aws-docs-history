# Analysis and maintenance

This section covers the following topics.

###### Topics

- [Viewing the cluster state](#clsuter-state "#clsuter-state")
- [Performing planned maintenance](#planned-maintenance "#planned-maintenance")
- [Post-failure analysis and reset](#analysis-reset "#analysis-reset")
- [Alerting and monitoring](#alerting-monitoring "#alerting-monitoring")

## Viewing the cluster state

You can view the state of the cluster based on your operating system.

**Operating system based**

There are multiple operating system commands that can be run as root or as a user with appropriate permissions. The commands enable you to get an overview of the status of the cluster and its services. See the following commands for more details.

```
pcs status
```

Sample output:

```
pcs status
Cluster name: rhelha
Cluster Summary:
* Stack: corosync
* Current DC: <rhxdbhost01> (version 2.1.2-4.el8_6.5-ada5c3b36e2) - partition with quorum
* Last updated: Wed Apr 12 19:38:46 2023
* Last change: Mon Apr 10 14:55:08 2023 by root via crm_resource on <rhxdbhost01>
* 2 nodes configured
* 10 resource instances configured
Node List:
* Online: [ awnulaeddb awnulaeddbha ]
Full List of Resources:
* rsc_aws_stonith_ARD (stonith:fence_aws): Started awnulaeddb
* Resource Group: grp_ARD_ASEDB:
* rsc_ip_ARD_ASEDB (ocf::heartbeat:aws-vpc-move-ip): Started <rhxdbhost01>
* rsc_fs_ARD_sybase (ocf::heartbeat:Filesystem): Started <rhxdbhost01>
* rsc_fs_ARD_data (ocf::heartbeat:Filesystem): Started <rhxdbhost01>
* rsc_fs_ARD_log (ocf::heartbeat:Filesystem): Started <rhxdbhost01>
* rsc_fs_ARD_sapdiag (ocf::heartbeat:Filesystem): Started <rhxdbhost01>
SAP NetWeaver on {aws} SAP NetWeaver Guides
Analysis and maintenance
140
* rsc_fs_ARD_saptmp (ocf::heartbeat:Filesystem): Started <rhxdbhost01>
* rsc_fs_ARD_backup (ocf::heartbeat:Filesystem): Started <rhxdbhost01>
* rsc_fs_ARD_usrsap (ocf::heartbeat:Filesystem): Started <rhxdbhost01>
* rsc_ase_ARD_ASEDB (ocf::heartbeat:SAPDatabase): Started <rhxdbhost01>
Daemon Status:
corosync: active/enabled
pacemaker: active/enabled
pcsd: active/enabled
```

The following table provides a list of useful commands.

| Command              | Description                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `crm_mon`            | Display cluster status on the console with updates as they occur                                                             |
| `crm_mon -1`         | Display cluster status on the console just once, and exit                                                                    |
| `crm_mon -Arnf`      | -A Display node attributes<br>-n Group resources by node<br>-r Display inactive resources<br>-f Display resource fail counts |
| `pcs help`           | View more options                                                                                                            |
| `crm_mon --help-all` | View more options                                                                                                            |

## Performing planned maintenance

The cluster connector is designed to integrate the cluster with SAP start framework (`sapstartsrv`), including the rolling kernel switch (RKS) awareness. Stopping and starting the SAP system using `sapcontrol` should not result in any cluster remediation activities as these actions are not interpreted as failures. Validate this scenario when testing your cluster.

There are different options to perform planned maintenance on nodes, resources, and the cluster.

###### Topics

- [Maintenance mode](#maintenance-mode "#maintenance-mode")
- [Placing a node in standby mode](#node-standby "#node-standby")
- [Moving a resource (not recommended)](#moving-resource "#moving-resource")

### Maintenance mode

Use maintenance mode if you want to make any changes to the configuration or take control of the resources and nodes in the cluster. In most cases, this is the safest option for administrative tasks.

###### Example

On
Use the following command to turn on maintenance mode.

```
pcs property set maintenance-mode="true"
```

Off

- Use the following command to turn off maintenance mode.

```
pcs property set maintenance-mode="false"
```

### Placing a node in standby mode

To perform maintenance on the cluster without system outage, the recommended method for moving active resources is to place the node you want to remove from the cluster in standby mode.

```
pcs node standby <rhxdbhost01>
```

The cluster will cleanly relocate resources, and you can perform activities, including reboots on the node in standby mode. When maintenance activities are complete, you can re-introduce the node with the following command.

```
pcs node unstandby <rhxdbhost01>
```

### Moving a resource (not recommended)

Moving individual resources is not recommended because of the migration or move constraints that are created to lock the resource in its new location. These can be cleared as described in the info messages, but this introduces an additional setup.

```
<rhxdbhost01>:~ # pcs resource move <grp_ARD_ASEDB>

Note: Move constraint created for <grp_ARD_ASEDB> to <rhxdbhost02>
Note: Use “pcs constraint location remove cli-prefer-grp_ARD_ASEDB” to remove this constraint.
```

## Post-failure analysis and reset

A review must be conducted after each failure to understand the source of failure as well the reaction of the cluster. In most scenarios, the cluster prevents an application outage. However, a manual action is often required to reset the cluster to a protective state for any subsequent failures.

###### Topics

- [Checking the logs](#checking-logs "#checking-logs")
- [Cleanup pcs status](#cleanup-pcs "#cleanup-pcs")
- [Restart failed nodes or pacemaker](#restart-nodes "#restart-nodes")
- [Further analysis](#further-analysis "#further-analysis")

### Checking the logs

Start your troubleshooting by checking the operating system log `/var/log/messages`. You can find additional information in the cluster and pacemaker logs.

- **Cluster logs** – updated in the `corosync.conf` file located at `/etc/corosync/corosync.conf`.
- **Pacemaker logs** – updated in the `pacemaker.log` file located at `/var/log/pacemaker`.
- **Resource agents** – `/var/log/messages`

Application based failures can be investigated in the SAP work directory.

### Cleanup `pcs status`

If failed actions are reported using the `crm status` command, and if they have already been investigated, then you can clear the reports with the following command.

```
pcs resource cleanup <resource> <hostname>
```

```
pcs stonith cleanup
```

###### Note

Use the help command to understand the impact of these commands.

### Restart failed nodes or `pacemaker`

It is recommended that failed (or fenced) nodes are not automatically restarted. It gives operators a chance to investigate the failure, and ensure that the cluster doesn’t make assumptions about the state of resources.

You need to restart the instance or the pacemaker service based on your approach.

### Further analysis

If further analysis from Red Hat is required, they may request an sos report, or logs of the cluster from `crm_report` or `pcs cluster report`.

**sos report** – The sos report command is a tool that collects configuration details, system information, and diagnostic information from a Red Hat Enterprise Linux system. For instance, the running kernel version, loaded modules, and system and service configuration files. The command also runs external programs to collect further information, and stores this output in the resulting archive. For more information, see Red Hat documentation [What is an sos report and is it different from an sosreport?](https://access.redhat.com/solutions/3592#sos_report "https://access.redhat.com/solutions/3592#sos_report")

**crm report** – collects the cluster logs/information from the node where the command is being run. For more information, see Red Hat documentation [How do I generate a crm_report from a RHEL 6 or 7 High Availability cluster node using pacemaker?](https://access.redhat.com/solutions/787853 "https://access.redhat.com/solutions/787853")

```
crm_report
```

**pcs cluster report** – command collects the cluster logs/information from all the nodes involved in the cluster.

```
pcs cluster report <destination_path>
```

###### Note

The `pcs cluster report` command relies on passwordless ssh being set up between the nodes.

## Alerting and monitoring

**Using the cluster alert agents**

Within the cluster configuration, you can call an external program (an alert agent) to handle alerts. This is a _push_ notification. It passes information about the event via environment variables.

The agents can then be configured to send emails, log to a file, update a monitoring system, etc. For example, the following script can be used to access Amazon SNS.

```
#!/bin/sh

#alert_sns.sh
#modified from /usr/share/pacemaker/alerts/alert_smtp.sh.sample

##############################################################################
#SETUP
* Create an SNS Topic and subscribe email or chatbot
* Note down the ARN for the SNS topic
* Give the IAM Role attached to both Instances permission to publish to the SNS Topic
* Ensure the aws cli is installed
* Copy this file to /usr/share/pacemaker/alerts/alert_sns.sh or other location on BOTH nodes
* Ensure the permissions allow for hacluster and root to execute the script
* Run the following as root (modify file location if necessary and replace SNS ARN):

#SLES:
crm configure alert aws_sns_alert /usr/share/pacemaker/alerts/alert_sns.sh meta timeout=30s timestamp-format="%Y-%m-%d_%H:%M:%S" to <{ arn:aws:sns:region:account-id:myPacemakerAlerts  }>

#RHEL:
pcs alert create id=aws_sns_alert path=/usr/share/pacemaker/alerts/alert_sns.sh meta timeout=30s timestamp-format="%Y-%m-%d_%H:%M:%S"
pcs alert recipient add aws_sns_alert value=<arn:aws:sns:region:account-id:myPacemakerAlerts>

#Additional information to send with the alerts.
node_name=`uname -n`
sns_body=`env | grep CRM_alert_`

#Required for SNS
TOKEN=$(/usr/bin/curl --noproxy '*' -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

#Get metadata
REGION=$(/usr/bin/curl --noproxy '*' -w "\n" -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/document | grep region | awk -F\" '{print $4}')

sns_subscription_arn=${CRM_alert_recipient}

#Format depending on alert type
case ${CRM_alert_kind} in
   node)
     sns_subject="${CRM_alert_timestamp} ${cluster_name}: Node '${CRM_alert_node}' is now '${CRM_alert_desc}'"
   ;;
   fencing)
     sns_subject="${CRM_alert_timestamp} ${cluster_name}: Fencing ${CRM_alert_desc}"
   ;;
   resource)
     if [ ${CRM_alert_interval} = "0" ]; then
         CRM_alert_interval=""
     else
         CRM_alert_interval=" (${CRM_alert_interval})"
     fi
     if [ ${CRM_alert_target_rc} = "0" ]; then
         CRM_alert_target_rc=""
     else
         CRM_alert_target_rc=" (target: ${CRM_alert_target_rc})"
     fi
     case ${CRM_alert_desc} in
         Cancelled)
           ;;
         *)
           sns_subject="${CRM_alert_timestamp}: Resource operation '${CRM_alert_task}${CRM_alert_interval}' for '${CRM_alert_rsc}' on '${CRM_alert_node}': ${CRM_alert_desc}${CRM_alert_target_rc}"
           ;;
     esac
     ;;
   attribute)
     sns_subject="${CRM_alert_timestamp}: The '${CRM_alert_attribute_name}' attribute of the '${CRM_alert_node}' node was updated in '${CRM_alert_attribute_value}'"
     ;;
   *)
     sns_subject="${CRM_alert_timestamp}: Unhandled $CRM_alert_kind alert"
     ;;
esac

#Use this information to send the email.
aws sns publish --topic-arn "${sns_subscription_arn}" --subject "${sns_subject}" --message "${sns_body}" --region ${REGION}
```
