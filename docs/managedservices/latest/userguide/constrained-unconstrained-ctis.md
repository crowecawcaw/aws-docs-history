

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# CT approval requirements
<a name="constrained-unconstrained-ctis"></a>

AMS CTs always have two approval conditions, **AwsApprovalId** and **CustomerApprovalId** that indicate whether the RFC requires AMS or you, or anyone, to approve the execution.

The approval condition is somewhat related to the execution mode; for details, see [Automated and manual CTs](ug-automated-or-manual.md).

To find out the approval condition for a CT, you can look in the [AMS Change Type Reference](https://docs.aws.amazon.com/managedservices/latest/ctref/index.html), or run [GetChangeTypeVersion](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_GetChangeTypeVersion.html). Both will also give you the CT `AutomationStatusId` or **Execution mode**.

You can approve RFCs by using the AMS console or with the following command:

```
aws amscm approve-rfc --rfc-id {{RFC_ID}}
```


**CT approval condition**  

| If the CT approval condition is | It requires approval from | And | 
| --- | --- | --- | 
| `AwsApprovalId: Required` | The AMS change type system, | No action is required. This condition is typical for automated CTs. | 
| `AwsApprovalId: NotRequiredIfSubmitter` | The AMS change type system and no one else, if the submitted RFC is for the account it was submitted against, | No action is required. This condition is typical for manual CTs because they will always be reviewed by AMS operators. | 
| `CustomerApprovalId: NotRequired` | The AMS change type system, | If the RFC passes syntax and parameter checks, it is auto approved. | 
| `CustomerApprovalId: Required` | The AMS change type system and you, | A notification is sent to you, and you must explicitly approve the RFC, either by responding to the notice, or running the [ApproveRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ApproveRfc.html) operation. | 
| `CustomerApprovalId: NotRequiredIfSubmitter` | The AMS change type system and no one else, if you submitted the RFC. | If the RFC passes syntax and parameter checks, it is auto approved. | 
| Urgent Security Incident or Patch | AMS | Is auto approved and implemented. | 