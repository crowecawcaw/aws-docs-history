# VPC Flow Logs in Security Lake

The VPC Flow Logs feature of Amazon VPC captures information about the IP traffic going to
and from network interfaces within your environment.

When you add VPC Flow Logs as a source in Security Lake, Security Lake immediately starts collecting
your VPC Flow Logs. It consumes VPC Flow Logs directly from Amazon VPC through an independent
and duplicate stream of Flow Logs.

Security Lake doesn't manage your VPC Flow Logs or affect your Amazon VPC configurations. To manage
your Flow Logs, you must use the Amazon VPC service console. For more information, see [Work
with Flow Logs](../../../vpc/latest/userguide/working-with-flow-logs.md "../../../vpc/latest/userguide/working-with-flow-logs.md") in the _Amazon VPC Developer Guide_.

The following list provides GitHub repository links to the mapping reference for how
Security Lake normalizes VPC Flow Logs to OCSF.

###### **GitHub OCSF repository for VPC Flow Logs**

- Source version 1 [(v1.0.0-rc.2)](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.0.0-rc.2/VPC%20Flowlogs "https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.0.0-rc.2/VPC%20Flowlogs")
- Source version 2 [(v1.1.0)](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/VPC%20Flowlogs "https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/VPC%20Flowlogs")
