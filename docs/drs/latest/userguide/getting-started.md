# Getting started with AWS Elastic Disaster Recovery

###### Topics

- [Disaster recovery overview](#recovery-workflow-gs "#recovery-workflow-gs")
- [Elastic Disaster Recovery initialization and permissions](getting-started-initializing.md "getting-started-initializing.md")
- [Accessing the AWS Elastic Disaster Recovery Console](accessing-console.md "accessing-console.md")
- [AWS Elastic Disaster Recovery supported AWS Regions](supported-regions.md "supported-regions.md")
- [Using the AWS Elastic Disaster Recovery Console](drs-console.md "drs-console.md")
- [Best practices for Elastic Disaster Recovery](best_practices_drs.md "best_practices_drs.md")
- [Elastic Disaster Recovery quick start guide](quick-start-guide-gs.md "quick-start-guide-gs.md")

## Disaster recovery overview

The general process is:

1. Install the AWS Replication Agent on the source server.
2. Wait until initial sync is finished.
3. Launch drill instances. Perform acceptance drills on the servers
4. Initiate a failover by redirecting traffic.
5. Confirm that the Recovery instance was launched successfully.
6. To recover your data, initiate a failback.
7. Complete the failback
8. Return to normal operations.

### Resources

The following free technical trainings are available for DRS:

- [AWS Elastic Disaster Recovery - A Technical Introduction](https://explore.skillbuilder.aws/learn/course/external/view/elearning/11123/aws-elastic-disaster-recovery-a-technical-introduction "https://explore.skillbuilder.aws/learn/course/external/view/elearning/11123/aws-elastic-disaster-recovery-a-technical-introduction")
