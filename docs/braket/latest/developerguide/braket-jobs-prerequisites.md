# Prerequisites

Before you run your first hybrid job, you must ensure that you have sufficient permissions to
proceed with this task. To determine that you have the correct permissions, select
**Permissions** from the menu on left side of the
Braket Console. The **Permissions management for
Amazon Braket** page helps you verify whether one of your
existing roles has permissions that are sufficient to run your hybrid job or guides you through
the creation of a default role that can be used to run your hybrid job if you do not already have
such a role.

![Permissions and settings page for Amazon Braket service showing a service-linked role and option to verify existing roles for Hybrid Jobs execution role.](images/braket-jobs-first-permissions.png)
To verify that you have roles with sufficient permissions to run a hybrid job, select the
**Verify existing role** button. If you do, you get a
message that the roles were found. To see the names of the roles and their role ARNs,
select the **Show roles** button.

![Amazon Braket permissions and settings screen showing a service-linked role found and existing roles with sufficient permissions to execute hybrid jobs.](images/braket-jobs-first-permissions-verify-yes.png)
If you do not have a role with sufficient permissions to run a hybrid job, you get a
message that no such role was found. Select the **Create default
role** button to obtain a role with sufficient permissions.

![Amazon Braket permissions and settings page showing service-linked role found and no hybrid jobs execution roles found.](images/braket-jobs-first-permissions-verify-no.png)
If the role was created successfully, you get a message confirming this.

![Amazon Braket permissions and settings page showing a service-linked role found and a Hybrid jobs execution role created successfully.](images/braket-jobs-first-permissions-verify-created.png)
If you do not have permissions to make this inquiry, you will be denied access. In this
case, contact your internal AWS administrator.

![AccessDenied error message indicating user is not authorized to perform iam:ListAttachedRolePolicies on an AmazonBraketJobsExecutionRole with an explicit deny.](images/braket-jobs-first-permissions-access-denied.png)
