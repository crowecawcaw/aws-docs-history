

# Setting up a role for AWS Budgets to run budget actions
<a name="budgets-action-role"></a>

To use budget actions, you must create a service role for AWS Budgets. A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

To allow AWS Budgets to perform actions on your behalf, you must grant the necessary permissions to the service role. The following table lists the permissions that you can grant the service role.


| Permissions policy for budget actions | Instructions | 
| --- | --- | 
| [Allows permission to control AWS resources](billing-permissions-ref.md#budget-managedIAM-SSM) | This is an AWS managed policy.<br />For instructions on how to attach a managed policy, see [To use a managed policy as a permissions policy for an identity (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#access_policies_manage-attach-detach-console) in the *IAM User Guide* | 
| [Allow AWS Budgets to apply IAM policies and SCPs](billing-example-policies.md#example-budgets-IAM-SCP) | You can use this example policy as an inline policy or a customer managed policy.<br />For instructions on how to embed an inline policy, see [To embed an inline policy for a user or role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#embed-inline-policy-console) in the *IAM User Guide*.<br />For instructions on how to create a customer managed policy, see [Creating IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*. | 
| [Allow AWS Budgets to apply IAM policies and SCPs and target EC2 and RDS instances](billing-example-policies.md#example-budgets-applySCP) | You can use this example policy as an inline policy or a customer managed policy.<br />For instructions on how to embed an inline policy, see [To embed an inline policy for a user or role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#embed-inline-policy-console) in the *IAM User Guide*.<br />For instructions on how to create a customer managed policy, see [Creating IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*. | 