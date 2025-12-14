# Alerting and monitoring

This section covers the following topics.

###### Topics

- [Using Amazon CloudWatch Application Insights](#application-insights-nw-sles "#application-insights-nw-sles")
- [Using the cluster alert agents](#cluster-alert-nw-sles "#cluster-alert-nw-sles")

## Using Amazon CloudWatch Application Insights

For monitoring and visibility of cluster state and actions, Application Insights includes metrics for monitoring enqueue replication state, cluster metrics, and SAP and high availability checks. Additional metrics, such as EFS and CPU monitoring can also help with root cause analysis.

For more information, see [Get started with Amazon CloudWatch Application Insights](../../../AmazonCloudWatch/latest/monitoring/appinsights-getting-started.md "../../../AmazonCloudWatch/latest/monitoring/appinsights-getting-started.md") and [SAP NetWeaver High Availability on Amazon EC2](../../../AmazonCloudWatch/latest/monitoring/component-configuration-examples-netweaver-ha.md "../../../AmazonCloudWatch/latest/monitoring/component-configuration-examples-netweaver-ha.md").

## Using the cluster alert agents

Within the cluster configuration, you can call an external program (an alert agent) to handle alerts. This is a _push_ notification. It passes information about the event via environment variables.

The agents can then be configured to send emails, log to a file, update a monitoring system, etc. For example, the following script can be used to access Amazon SNS.

```
#!/bin/sh

# alert_sns.sh
# modified from /usr/share/pacemaker/alerts/alert_smtp.sh.sample

##############################################################################
# SETUP
# * Create an SNS Topic and subscribe email or chatbot
# * Note down the ARN for the SNS topic
# * Give the IAM Role attached to both Instances permission to publish to the SNS Topic
# * Ensure the aws cli is installed
# * Copy this file to /usr/share/pacemaker/alerts/alert_sns.sh or other location on BOTH nodes
# * Ensure the permissions allow for hacluster and root to execute the script
# * Run the following as root (modify file location if necessary and replace SNS ARN):
#
# SLES:
# crm configure alert aws_sns_alert /usr/share/pacemaker/alerts/alert_sns.sh meta timeout=30s timestamp-format="%Y-%m-%d_%H:%M:%S" to <{ arn:aws:sns:region:account-id:myPacemakerAlerts  }>
#
# RHEL:
# pcs alert create id=aws_sns_alert path=/usr/share/pacemaker/alerts/alert_sns.sh meta timeout=30s timestamp-format="%Y-%m-%d_%H:%M:%S"
# pcs alert recipient add aws_sns_alert value=arn:aws:sns:region:account-id:myPacemakerAlerts
##############################################################################

# Additional information to send with the alerts
node_name=`uname -n`
sns_body=`env | grep CRM_alert_`

# Required for SNS
TOKEN=$(/usr/bin/curl --noproxy '*' -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

# Get metadata
REGION=$(/usr/bin/curl --noproxy '*' -w "\n" -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/document | grep region | awk -F\" '{print $4}')

sns_subscription_arn=${CRM_alert_recipient}

# Format depending on alert type
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

# Use this information to send the email.
aws sns publish --topic-arn "${sns_subscription_arn}" --subject "${sns_subject}" --message "${sns_body}" --region ${REGION}
```
