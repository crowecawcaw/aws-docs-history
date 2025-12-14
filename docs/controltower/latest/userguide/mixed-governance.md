# Avoid mixed governance when configuring

Regions

It is important to update all accounts in an OU after you extend AWS Control Tower governance
to a new AWS Region, and after you remove AWS Control Tower governance from a Region.

_Mixed governance_ is an undesirable situation that can
occur if the controls governing an OU are not a complete match to the controls governing
each account within an OU. Mixed governance occurs in an OU if accounts are not updated
after AWS Control Tower extends governance to a new AWS Region, or removes governance.

In this situation, certain accounts within an OU may have different controls applied
in different Regions, when compared to other accounts in the OU, or when compared to the
landing zone's overall governance posture.

In an OU with mixed governance, if you provision a new account, that new account
receives the same (updated) Region and OU governance posture as the landing zone.
However, existing accounts that are not yet updated do not receive the updated Region
governance posture.

In general, mixed governance may create contradictory or inaccurate status indicators
in the AWS Control Tower console. For example, during mixed governance, opt-in Regions are shown
with **Not governed** status, in registered OUs, for accounts that are
not yet updated.

###### Note

AWS Control Tower does not permit controls to be enabled during a state of mixed
governance.

###### Behavior of controls during mixed governance

- During mixed governance, AWS Control Tower cannot consistently deploy controls that are
  based on AWS Config rules (that is, detective controls) in Regions that the OU already
  shows as **Governed**, because some accounts in the OU have not
  been updated. You may receive a `FAILED_TO_ENABLE` error
  message.
- During mixed governance, if you extend the landing zone's governance to an
  opt-in Region while any account in the OU has not yet been updated, the
  `EnableControl` API operation on the OU fails for detective and
  proactive controls. You will receive a `FAILED_TO_ENABLE` error
  message, because non-updated member accounts within the OU have not yet been
  opted into those Regions.
- During mixed governance, controls that are part of the **Security Hub CSPM
  Service-managed Standard: AWS Control Tower** cannot report compliance
  accurately in Regions where there is a mismatch between the landing zone
  configuration and the accounts that are not updated.
- Mixed governance does not change the behavior of SCP-based controls
  (preventive controls), which apply uniformly to every account in an OU, in every
  governed Region.

###### Note

Mixed governance is not the same as drift, and it is not reported as drift.

###### To repair mixed governance

- Customers are now able to repair mixed governance by resetting regional controls.
  Any non-global controls are regional (detective and proactive controls). You will be alerted
  that your OU is in a mixed governance through an alert banner.
