This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Configure Redundancy for AWS Elemental Conductor File

Nodes

Read this section if you have two Conductor nodes.

This section describes how to set up the two Conductor nodes to work in a redundant fashion, so that if one node fails, the other node automatically takes control of the cluster, with no loss of data.

This procedure will likely require 1 hour to complete.

###### Summary

- [Step A: Get Ready](config-cond-cf-cg-redundancy-ready.md "config-cond-cf-cg-redundancy-ready.md")
- [Step B: Create a dbrepl_config.yml File](config-cond-cf-cg-redundancy-yml.md "config-cond-cf-cg-redundancy-yml.md")
- [Step C: Run the Redundancy Install Script](config-cond-cf-cg-redundancy-run.md "config-cond-cf-cg-redundancy-run.md")
- [Step D: Test Failover](config-cond-cf-cg-redundancy-test.md "config-cond-cf-cg-redundancy-test.md")
