# Managing tiers

Parameter Store includes _standard
parameters_ and _advanced
parameters_. You individually configure parameters to use either the
standard-parameter tier (the default tier) or the advanced-parameter tier.

You can change a standard parameter to an advanced parameter at any time. You
_can’t_ change an advanced parameter to a standard parameter for the following reasons:

- Reverting would cause the system to
  truncate the size of the parameter from 8 KB to 4 KB, resulting in data loss.
- Reverting would remove policies attached to the parameter.
- Reverting would change the parameter encryption.
  For information about encryption used by Parameter Store, see [How
  AWS Systems Manager Parameter Store uses AWS KMS](../../../kms/latest/developerguide/services-parameter-store.md "../../../kms/latest/developerguide/services-parameter-store.md") in the
  _AWS Key Management Service Developer Guide_.

###### Note

If you no longer need an advanced parameter, or if you no longer want to incur
charges for an advanced parameter, delete it and recreate it as a new standard
parameter.

## Standard and advanced parameters

The following table describes the differences between parameter tiers.

| Feature                                                | Standard             | Advanced                                                                                                                                                                                                                            |
| ------------------------------------------------------ | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum parameters<br>(per AWS account and AWS Region) | 10,000               | 100,000                                                                                                                                                                                                                             |
| Maximum value size                                     | 4 KB                 | 8 KB                                                                                                                                                                                                                                |
| Parameter policies                                     | Not supported        | Supported<br>For more information, see [Assigning parameter policies in Parameter Store](parameter-store-policies.md "parameter-store-policies.md").                                                                                |
| Share parameters across AWS accounts                   | Not supported        | Supported<br>For more information, see [Working with shared parameters in Parameter Store](parameter-store-shared-parameters.md "parameter-store-shared-parameters.md").                                                            |
| Cost                                                   | No additional charge | Charges apply<br>For more information, see [AWS Systems Manager<br>Pricing for Parameter Store](https://aws.amazon.com/systems-manager/pricing/#Parameter_Store "https://aws.amazon.com/systems-manager/pricing/#Parameter_Store"). |

###### Topics

- [Specifying a default parameter tier](ps-default-tier.md "ps-default-tier.md")
- [Changing a standard parameter to an advanced parameter](parameter-store-advanced-parameters-enabling.md "parameter-store-advanced-parameters-enabling.md")
