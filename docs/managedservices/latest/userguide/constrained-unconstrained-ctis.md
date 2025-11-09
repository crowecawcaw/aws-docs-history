# CT approval requirements

AMS CTs always have two approval conditions, **AwsApprovalId** and
**CustomerApprovalId** that indicate whether the RFC requires
AMS or you, or anyone, to approve the execution.

The approval condition is somewhat related to the execution mode; for details, see
[Automated and manual CTs](ug-automated-or-manual.md "ug-automated-or-manual.md").

To find out the approval condition for a CT, you can look in the
[AMS Change Type Reference](../ctref/index.md "../ctref/index.md"), or run
[GetChangeTypeVersion](../ApiReference-cm/API_GetChangeTypeVersion.md "../ApiReference-cm/API_GetChangeTypeVersion.md"). Both will also give you the CT `AutomationStatusId` or
**Execution mode**.

You can approve RFCs by using the AMS console or with the following command:

```
aws amscm approve-rfc --rfc-id `RFC_ID`
```

| CT approval condition                        | If the CT approval condition is                                                                                  | It requires approval from                                                                                                                                                                                                             | And |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| `AwsApprovalId: Required`                    | The AMS change type system,                                                                                      | No action is required. This condition is typical for automated CTs.                                                                                                                                                                   |
| `AwsApprovalId: NotRequiredIfSubmitter`      | The AMS change type system and no one else, if the submitted RFC is for<br>the account it was submitted against, | No action is required. This condition is typical for manual CTs because they will always be<br>reviewed by AMS operators.                                                                                                             |
| `CustomerApprovalId: NotRequired`            | The AMS change type system,                                                                                      | If the RFC passes syntax and parameter checks, it is auto approved.                                                                                                                                                                   |
| `CustomerApprovalId: Required`               | The AMS change type system and you,                                                                              | A notification is sent to you, and you must explicitly<br>approve the RFC, either by responding to the notice, or running<br>the [ApproveRfc](../ApiReference-cm/API_ApproveRfc.md "../ApiReference-cm/API_ApproveRfc.md") operation. |
| `CustomerApprovalId: NotRequiredIfSubmitter` | The AMS change type system and no one else, if you submitted the RFC.                                            | If the RFC passes syntax and parameter checks, it is auto approved.                                                                                                                                                                   |
| Urgent Security Incident or Patch            | AMS                                                                                                              | Is auto approved and implemented.                                                                                                                                                                                                     |
