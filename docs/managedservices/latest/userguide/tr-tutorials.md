# Configure remediation tutorials

The following tutorials provide examples of creating common remediations in Trusted Remediator

## Remediate all resources manually

This example configures manual remediation for all Amazon EBS volumes with the Trusted Advisor check ID DAvU99Dc4C (Underutilized Amazon EBS Volumes).

###### Configure manual remediation for Amazon EBS volumes with check ID DAvU99Dc4C

1. Use the **Remediation Configuration|Update**, change type to request the configuration update.
2. Enter the following parameters:
   - **CheckIds:** DAvU99Dc4C
   - **ExecutionMode:** Manual

###### Note

Multiple checks can be configured in a single request. For checks that require the same configuration, include multiple check IDs in the
**CheckIds** parameter. For checks that require a different configuration, create a new **RemediationConfiguration**
object. 3. Submit the RFC.

## Remediate all resources automatically, except for selected resources

This example configures automatic remediation for all Amazon EBS volumes with the Trusted Advisor check ID DAvU99Dc4C (Underutilized Amazon EBS Volumes), with the exception of specified volumes that won't be remediated (designated **Inactive**.

###### Configure automatic remediation for Amazon EBS volumes with check ID DAvU99Dc4C, with the exception of selected inactive resources

1. Override automated remediation for selected Amazon EBS volumes:

Use [Tag | Update](../ctref/management-advanced-tag-update.md "../ctref/management-advanced-tag-update.md") or [Tag | Bulk Update](../ctref/management-advanced-tag-bulk-update.md "../ctref/management-advanced-tag-bulk-update.md") change type to apply the following tag for volumes to be excluded from automated remediation:

    * **Key:** TR-DAvU99Dc4C-Execution-Mode
    * **Value:** Inactive

2. Use the **Remediation Configuration|Update** change type to request the configuration update.
3. Enter the following parameters:
   - **CheckIds:** DAvU99Dc4C
   - **ExecutionMode:** Automated

4. Submit the RFC.

## Remediate tagged resources automatically

This example configures automatic remediation for all Amazon EBS volumes with the tag `Stage=NonProd` with the Trusted Advisor check ID DAvU99Dc4C (Underutilized Amazon EBS Volumes). All other resources without this tag aren't remediated.

###### Configure automatic remediation for Amazon EBS volumes with the tag `Stage=NonProd` for check ID DAvU99Dc4C

1. Use the [Remediation Configuration | Update](../ctref/management-trusted-remediation-configuration-update.md "../ctref/management-trusted-remediation-configuration-update.md"), change type to request the configuration update.
2. Enter the following parameters:
   - **CheckIds:** DAvU99Dc4C
   - **ExecutionMode:** Conditional
   - **AutomatedForTaggedOnly:** {"Stage":"NonProd"}

###### Note

The value specified for the **AutomatedForTaggedOnly** parameter overrides the previously configured value. To retain existing tags, include them in the new value. 3. Submit the RFC.

## Reset configuration to default

This example removes existing **automated-for-tagged-only** configuration for the check **Hs4Ma3G104**. To remove previously applied tag configuration, set the **AutomatedForTaggedOnly** parameter value to **{}**.

###### Reset configuration to default for check Hs4Ma3G104

1. Use the [Remediation Configuration | Update](../ctref/management-trusted-remediation-configuration-update.md "../ctref/management-trusted-remediation-configuration-update.md") change type to request the configuration update.
2. Enter the following parameters:
   - **CheckIds:** Hs4Ma3G104
   - **ExecutionMode:** Enter the currently used value
   - **AutomatedForTaggedOnly:** {}

3. Submit the RFC.
