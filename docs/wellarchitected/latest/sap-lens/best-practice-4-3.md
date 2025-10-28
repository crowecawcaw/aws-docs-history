# Best Practice 4.3 – Regularly test

business continuity plans and fault recovery

SAP systems are generally business critical and depended upon for major customer
facing transactions. Enabling the quick resumption of IT operations and minimizing data
loss during a fault or disaster situation is critical for operational excellence. Business
continuity plans (BCP) and fault recovery procedures are required to ensure that your
operations team and systems know what to do, when to do it, and workload service can be
resumed promptly in case of a fault.

Critical to the successful resumption of services is that your BCP procedures and
fault recovery plans are regularly tested, improved upon and refined as your systems and
support team evolves. Testing your BCP and recovery plans outside of real crisis
situations ensures that when a real system fails or disaster does occur, you can be
confident in your ability to successfully resume service and that you will meet your
recovery time objective (RTO) and recovery point objective (RPO).

**Suggestion 4.3.1. - Create a BCP and fault recovery testing
calendar**

Create a calendar which schedules regular (at least annually) BCP and fault scenario
recovery testing for your SAP workload. Involve technology operational teams, support
personnel and business stakeholders in this test so that procedures are understood and
expectations are aligned. Aim to test your systems in as real a situation as
possible.

Consider testing the following scenarios and validating recovery metrics for each of
them:

- SAP application service failure

_(for example, SAP application service fails to start due to a configuration
change)_

- Single instance host failure

_(for example, SAP application server EC2 instance becomes
unreachable)_

- Single storage volume failure

_(for example, a single EBS volume becomes unreachable)_

- Network failure and switch over to redundant connection

_(for example, your on-premises Direct Connect connection is
unreachable)_

- Automated failover between primary and secondary clustered components

_(for example, SUSE HAE cluster forces primary HANA database to move to the
secondary database in an alternate Availability Zone)_

- Manual fail over between primary and secondary components

_(for example, manual invocation of Oracle DataGuard switch over to secondary
database in an alternate Availability Zone)_

- Load balancing between multiply redundant components

_(for example, primary web dispatcher fails in a high availability pair
across Availability Zones)_

- Recovery of your SAP application in an alternate AWS Region (if required)
- Recovery from backup in event of ransomware

_(for example, recovering your entire SAP ERP system from Amazon S3 WORM
backup)_

**Suggestion 4.3.2 - Regularly review and update BCP and fault
recovery procedures as part of workload changes**

As your workload evolves and changes over time, ensure that BCP and recovery
procedures are considered in these changes. When a code or infrastructure change might
affect your RTO or RPO, ensure that documentation and configuration is updated, and the
new BCP and recovery process is tested as part of the release process or regular test
calendar.

- AWS Documentation: [Business Continuity Plan (BCP) Definition](../../../whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.md "../../../whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.md")
- AWS Documentation: [Architecture Guidance for Availability and Reliability of SAP on AWS](../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md "../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md")
- SAP Lens [Reliability]: [Best Practice 11.4 -
  Conduct periodic tests of resilience](best-practice-11-4.md "best-practice-11-4.md")
