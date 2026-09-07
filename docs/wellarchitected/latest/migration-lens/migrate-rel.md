

# Migrate
<a name="migrate-rel"></a>

 The migrate phase is where the actual migration of the workload takes place. In this phase, we perform migration as planned, monitor the migration process, and keep a plan in place to rollback in case issues encountered during the migration. 


| MIG-REL-08: Have you tested high availability (HA), fault tolerance (FT), and disaster recovery (DR)? | 
| --- | 
|   | 

Test to validate that your workload meets functional and non-functional requirements before and after migration cutover. It is important to validate and update existing reliability components, which may be different in the new cloud environment.

## MIG-REL-BP-8.1 Before the cut-over, test HA and FT for the migrated workloads, and perform a DR dry-run after the migration
<a name="mig-rel-bp-8.1-before-the-cut-over-test-ha-and-ft-for-the-migrated-workloads-and-perform-a-dr-dry-run-after-the-migration"></a>

 This BP applies to the following best practice areas: Failure management 

### Implementation guidance
<a name="implementation-guidance-rel-8.1"></a>

 **Suggestion 8.1.1:** Follow the best practices (BPs) in the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html?) to complete the failure management testing for the migrated workloads. 

 This includes using playbooks to investigate failures, performing post-incident analysis, testing functional requirements for the migrated applications, testing scaling and performance, and testing resilience using chaos engineering.

 For more detail, see [How do you test reliability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-12.html). 