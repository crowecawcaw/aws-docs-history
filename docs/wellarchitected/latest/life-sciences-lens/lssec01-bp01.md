

# LSSEC01-BP01 Implement the principle of separation of duties
<a name="lssec01-bp01"></a>

 For users with increased privileges, it is important to distribute system administration activities, so no one administrator can hide their activities or control an entire system. Separation of duties can mitigate risk on critical tasks by requiring separate requesters and approvers for a task. A common example is the use of an approver during the [running of an automation on AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-require-approvals.html). This principle can be used to implement numerous tasks including controlling access to your cloud resources. Use roles with limited permissions based on functional needs when increased privileges are not required. 

 **Desired outcome:** Administrative tasks related to GxP data stores require approvals. 

 **Common anti-patterns:** 
+  Failure to implement a least privilege administration model. 
+  Lack of approvals in administration workflows. 

 **Benefits of establishing this best practice:** By implementing a least-privilege model and separating duties, appropriate control over access to GxP related resources can be demonstrated. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Determine which administrative tasks may have the potential to impact GxP data integrity. For each of these tasks, separate task approval from task execution. 

 Configure roles with least privilege to be used for routine functions that do not require administrative permissions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Introduce approval steps into automated administrative workflows. 

1.  Set required IAM permissions as needed. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_permissions_least_privileges.html) 

 **Related documents:** 
+  [Run an automation that requires approvals](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-require-approvals.html) 