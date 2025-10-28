# Performing administrative actions on Amazon OpenSearch Service

domains

Amazon OpenSearch Service offers several administrative options that provide granular control if you need
to troubleshoot issues with your domain. These options include the ability to restart the
OpenSearch process on a data node and the ability to restart a data node.

OpenSearch Service monitors node health parameters and, when there are anomalies, takes corrective
actions to keep domains stable. With the administrative options to restart the OpenSearch
process on a node, and restart a node itself, you have control over some of these mitigation
actions.

You can use the AWS Management Console, AWS CLI, or the AWS SDK to perform these actions. The following
sections cover how to perform these actions with the console.

## Limitations

Administrative options have the following limitations:

- Administrative options are supported on Elasticsearch versions 7.x and
  higher.
- Administrative options don't support domains with Multi-AZ with Standby
  enabled.
- The OpenSearch and Elasticsearch process restart and the data node reboot are
  supported on domains with three or more data nodes.
- The Dashboards and Kibana process support is supported on domains with two or
  more data nodes.
- To restart the OpenSearch process on a node or reboot a node, the domain must
  not be in red state and all indexes must have replicas configured.
