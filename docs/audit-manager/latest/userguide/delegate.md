

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Delegations in AWS Audit Manager
<a name="delegate"></a>



As you navigate through the assessment process in AWS Audit Manager, you might encounter situations where you need help from subject matter experts to review and validate the collected evidence. This is where the concept of delegations comes into play. 

## Key points
<a name="delegate-key-points"></a>

Delegations enable [audit owners](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#audit-owner) to assign specific control sets to [delegates](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#delegate-persona) – individuals with specialized expertise in relevant areas. By using the delegation feature, you can ensure that the evidence for each control is thoroughly evaluated by the appropriate personnel. This helps you to streamline the review process and enhance the overall accuracy and reliability of your assessments. Whether you need guidance on interpreting technical evidence, clarifying compliance requirements, or gaining deeper insights into specific domains, delegations enable you to collaborate effectively with subject matter experts.

At a high level, the delegation process is as follows:

1. The audit owner chooses a control set in their assessment and delegates it for review.

1. The delegate reviews those controls and their evidence, and submits the control set back to the audit owner when finished.

1.  The audit owner is notified that the review is complete, and checks the reviewed controls for any remarks from the delegate.

**Note**  
An AWS account can be an audit owner or a delegate in different AWS Regions. 

## Additional resources
<a name="delegate-next-steps"></a>

Use the following sections of this chapter to learn more about how to manage delegation tasks in AWS Audit Manager. 
+ [Understanding the different delegation tasks for audit owners](delegate-for-audit-owners.md)
  + [Delegating a control set for review in AWS Audit Manager](delegation-for-audit-owners-delegating-a-control-set.md)
  + [Finding and reviewing the delegations that you've sent in AWS Audit Manager](delegation-for-audit-owners-reviewing-delegations.md)
  + [Deleting your completed delegations in AWS Audit Manager](delegation-for-audit-owners-cancel-delegations.md)
+ [Understanding the different delegation tasks for delegates](delegation-for-delegates.md)
  + [Viewing your notifications for incoming delegation requests](delegation-for-delegates-viewing-notifications.md)
  + [Reviewing the delegated control set and its related evidence](delegation-for-delegates-reviewing-control-set-and-evidence.md)
  + [Adding comments about a control during a control set review](delegation-for-delegates-add-comment.md)
  + [Marking a control as reviewed in AWS Audit Manager](delegation-for-delegates-changing-control-status.md)
  + [Submitting a reviewed control set back to the audit owner](delegation-for-delegates-submitting-back-to-audit-owner.md)