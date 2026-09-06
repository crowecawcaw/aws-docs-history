

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Configure remediation tutorials
<a name="tr-tutorials"></a>

The following tutorials provide examples of creating common remediations in Trusted Remediator

## Remediate all resources manually
<a name="tr-tutorials-man"></a>

This example configures manual remediation for all Amazon EBS volumes with the Trusted Advisor check ID DAvU99Dc4C (Underutilized Amazon EBS Volumes).

**Configure manual remediation for Amazon EBS volumes with check ID DAvU99Dc4C**

1. Use the **Remediation Configuration\|Update**, change type to request the configuration update.

1. Enter the following parameters:
   + **CheckIds:** DAvU99Dc4C
   + **ExecutionMode:** Manual
**Note**  
Multiple checks can be configured in a single request. For checks that require the same configuration, include multiple check IDs in the **CheckIds** parameter. For checks that require a different configuration, create a new **RemediationConfiguration** object.

1. Submit the RFC.

## Remediate all resources automatically, except for selected resources
<a name="tr-tutorials-auto"></a>

This example configures automatic remediation for all Amazon EBS volumes with the Trusted Advisor check ID DAvU99Dc4C (Underutilized Amazon EBS Volumes), with the exception of specified volumes that won't be remediated (designated **Inactive**.

**Configure automatic remediation for Amazon EBS volumes with check ID DAvU99Dc4C, with the exception of selected inactive resources**

1. Override automated remediation for selected Amazon EBS volumes:

   Use [Tag \| Update](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-tag-update.html) or [Tag \| Bulk Update](https://docs.aws.amazon.com/managedservices/latest/ctref/management-advanced-tag-bulk-update.html) change type to apply the following tag for volumes to be excluded from automated remediation:
   + **Key:** TR-DAvU99Dc4C-Execution-Mode
   + **Value:** Inactive

1. Use the **Remediation Configuration\|Update** change type to request the configuration update.

1. Enter the following parameters:
   + **CheckIds:** DAvU99Dc4C
   + **ExecutionMode:** Automated

1. Submit the RFC.

## Remediate tagged resources automatically
<a name="tr-tutorials-auto-tags"></a>

This example configures automatic remediation for all Amazon EBS volumes with the tag `Stage=NonProd` with the Trusted Advisor check ID DAvU99Dc4C (Underutilized Amazon EBS Volumes). All other resources without this tag aren't remediated.

**Configure automatic remediation for Amazon EBS volumes with the tag `Stage=NonProd` for check ID DAvU99Dc4C**

1. Use the [Remediation Configuration \| Update](https://docs.aws.amazon.com/managedservices/latest/ctref/management-trusted-remediation-configuration-update.html), change type to request the configuration update.

1. Enter the following parameters:
   + **CheckIds:** DAvU99Dc4C
   + **ExecutionMode:** Conditional
   + **AutomatedForTaggedOnly:** {"Stage":"NonProd"}
**Note**  
The value specified for the **AutomatedForTaggedOnly** parameter overrides the previously configured value. To retain existing tags, include them in the new value.

1. Submit the RFC.

## Reset configuration to default
<a name="tr-tutorials-reset-config"></a>

This example removes existing **automated-for-tagged-only** configuration for the check **Hs4Ma3G104**. To remove previously applied tag configuration, set the **AutomatedForTaggedOnly** parameter value to **{}**.

**Reset configuration to default for check Hs4Ma3G104**

1. Use the [Remediation Configuration \| Update](https://docs.aws.amazon.com/managedservices/latest/ctref/management-trusted-remediation-configuration-update.html) change type to request the configuration update.

1. Enter the following parameters:
   + **CheckIds:** Hs4Ma3G104
   + **ExecutionMode:** Enter the currently used value
   + **AutomatedForTaggedOnly:** {}

1. Submit the RFC.