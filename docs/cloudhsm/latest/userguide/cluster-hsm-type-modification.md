# Cluster HSM type migration

AWS CloudHSM offers the ability to change the HSM type of an existing cluster. Review the table on this page to determine whether the HSM type modification is allowed.

For more information on the types of HSMs supported and their features please refer to [HSM types in AWS CloudHSM](hsm-types.md "hsm-types.md").

###### Note

You cannot change the FIPS mode of a cluster during this operation.



| From | To | Comment |
| --- | --- | --- |
| **hsm1.medium** | **hsm2m.medium** | **Allowed** |
| **hsm2m.medium** | **hsm1.medium** | **Conditional**. You can roll back from hsm2m.medium to hsm1.medium within 24 hours of the start of a migration. | ###### Topics <br>• [Migrating from hsm1.medium to hsm2m.medium](hsm1-to-hsm2-migration.md "hsm1-to-hsm2-migration.md")
