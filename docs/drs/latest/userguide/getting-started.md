

# Getting started with AWS Elastic Disaster Recovery
<a name="getting-started"></a>

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Disaster recovery overview](#recovery-workflow-gs)
+ [Elastic Disaster Recovery initialization and permissions](getting-started-initializing.md)
+ [Accessing the AWS Elastic Disaster Recovery Console](accessing-console.md)
+ [AWS Elastic Disaster Recovery supported AWS Regions](supported-regions.md)
+ [Using the AWS Elastic Disaster Recovery Console](drs-console.md)
+ [Best practices for Elastic Disaster Recovery](best_practices_drs.md)
+ [Disaster recovery at scale](drs-at-scale.md)
+ [Elastic Disaster Recovery quick start guide](quick-start-guide-gs.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Disaster recovery overview
<a name="recovery-workflow-gs"></a>

The general process is:

1. Initialize AWS Elastic Disaster Recovery in the target AWS Region. You can initialize through the [console or API](getting-started-initializing.md). See the [list of supported AWS Regions](supported-regions.md).

1. [Install the AWS Replication Agent](agent-installation.md) on the source server.

1. Wait until initial sync is finished. After installing the agent, the initial synchronization process performs block-level replication from the source server to the replication server in the staging area.

1. Launch drill instances. Perform acceptance drills on the servers. After the drill is tested successfully, finalize the drill and delete the instance.

1. Configure [post-launch actions](post-launch-action-settings-overview.md) if needed.

1. Confirm that there is no replication lag.

1. Initiate a failover by redirecting traffic.

1. Confirm that the Recovery instance was launched successfully.

1. To recover your data, initiate a [failback](failback-performing.md).

1. Complete the failback.

1. Return to normal operations.

For service quotas and limits, see [AWS Elastic Disaster Recovery endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/drs.html).

### Resources
<a name="drs-technical-training"></a>

The following free technical trainings are available for DRS:
+  [AWS Elastic Disaster Recovery - A Technical Introduction ](https://explore.skillbuilder.aws/learn/course/external/view/elearning/11123/aws-elastic-disaster-recovery-a-technical-introduction) 