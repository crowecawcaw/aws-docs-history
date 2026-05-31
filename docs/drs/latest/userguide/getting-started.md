# Getting started with AWS Elastic Disaster Recovery

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Disaster recovery overview](#recovery-workflow-gs "#recovery-workflow-gs")
- [Elastic Disaster Recovery initialization and permissions](getting-started-initializing.md "getting-started-initializing.md")
- [Accessing the AWS Elastic Disaster Recovery Console](accessing-console.md "accessing-console.md")
- [AWS Elastic Disaster Recovery supported AWS Regions](supported-regions.md "supported-regions.md")
- [Using the AWS Elastic Disaster Recovery Console](drs-console.md "drs-console.md")
- [Best practices for Elastic Disaster Recovery](best_practices_drs.md "best_practices_drs.md")
- [Disaster recovery at scale](drs-at-scale.md "drs-at-scale.md")
- [Elastic Disaster Recovery quick start guide](quick-start-guide-gs.md "quick-start-guide-gs.md")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Disaster recovery overview

The general process is:

1. Initialize AWS Elastic Disaster Recovery in the target AWS Region. You can initialize through the
   [console or API](getting-started-initializing.md "getting-started-initializing.md").
   See the [list of supported AWS Regions](supported-regions.md "supported-regions.md").
2. [Install the AWS Replication Agent](agent-installation.md "agent-installation.md") on the source server.
3. Wait until initial sync is finished. After installing the agent, the initial
   synchronization process performs block-level replication from the source server
   to the replication server in the staging area.
4. Launch drill instances. Perform acceptance drills on the servers. After the
   drill is tested successfully, finalize the drill and delete the instance.
5. Configure [post-launch
   actions](post-launch-action-settings-overview.md "post-launch-action-settings-overview.md") if needed.
6. Confirm that there is no replication lag.
7. Initiate a failover by redirecting traffic.
8. Confirm that the Recovery instance was launched successfully.
9. To recover your data, initiate a [failback](failback-performing.md "failback-performing.md").
10. Complete the failback.
11. Return to normal operations.

For service quotas and limits, see
[AWS Elastic Disaster Recovery endpoints and quotas](../../../general/latest/gr/drs.md "../../../general/latest/gr/drs.md").

### Resources

The following free technical trainings are available for DRS:

- [AWS Elastic Disaster Recovery - A Technical Introduction](https://explore.skillbuilder.aws/learn/course/external/view/elearning/11123/aws-elastic-disaster-recovery-a-technical-introduction "https://explore.skillbuilder.aws/learn/course/external/view/elearning/11123/aws-elastic-disaster-recovery-a-technical-introduction")
