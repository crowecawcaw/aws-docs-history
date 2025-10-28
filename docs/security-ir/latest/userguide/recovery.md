# Recovery

Recovery is the process of restoring systems to a known safe state, validating that
backups are safe or unaffected by the incident prior to restoration, testing to
verify that the systems are working properly post-restoration, and addressing
vulnerabilities associated with the security event.

The order of recovery depends on your organization’s requirements. As part of
the process of recovery, you should perform a business impact analysis to determine, at minimum:

- Business or dependency priorities
- The restoration plan
- Authentication and authorization

The NIST SP 800-61 Computer Security Incident Handling Guide provides several steps to recover systems, including:

- Restoring systems from clean backups.
  - Verify that backups are evaluated before restoring to systems to make sure that the
    infection is not present and to prevent a resurgence of the security event.

  Backups should be evaluated on a regular basis as part of disaster recovery testing to
  verify that the backup mechanism is working properly and the data integrity meets recovery point objectives.
  - If possible, use backups from before the first event timestamp identified as part of root cause analysis.

- Rebuilding systems from scratch, including redeploying from trusted source using automation, sometime in a new AWS account.
- Replacing compromised files with clean versions.

You should exercise great caution when doing this. You must be absolutely certain
the file you are recovering is known safe and unaffected by the incident

- Installing patches.
- Changing passwords.
  - This includes passwords for IAM principals that might have been abused.
  - If possible, we recommend using roles for IAM principals and federation as part of a least privilege strategy.

- Tightening network perimeter security (firewall rulesets, boundary router access control lists).

Once the resources have been recovered, it is important to capture lessons learned to update incident response policies, procedures, and guides.

In summary, it is imperative to implement a recovery process that facilitates a return
to known safe operations. Recovery can take a long time and requires a close linkage
with containment strategies to balance business impact against risk of reinfection.
Recovery procedures should include steps for restoring resources and services, IAM
principals, and performing a security review of the account to assess residual risk.
