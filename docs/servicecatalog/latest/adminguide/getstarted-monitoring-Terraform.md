# Step 10: Monitoring Terraform provisioning operations

If you want to monitor provisioning operations, you can review Amazon CloudWatch logs
and AWS Step Functions for any provisioning workflow.

There are two state machines for the provisioning workflow:

- `ManageProvisionedProductStateMachine` — AWS Service Catalog invokes this state machine when provisioning
  a new Terraform product and when updating an existing Terraform provisioned product.
- `TerminateProvisionedProductStateMachine` — AWS Service Catalog invokes this state machine
  when terminating an existing Terraform provisioned product.

###### To execute the monitoring state machine

1. Open the AWS management console and log in as an administrator in the admin hub account where the Terraform
   provisioning engine is installed.
2. Open **AWS Step Functions**.
3. In the left navigation panel, choose **State machines**.
4. Choose **ManageProvisionedProductStateMachine**.
5. In the **Executions** list, enter the provisioned product ID to locate your execution.

###### Note

AWS Service Catalog creates the provisioned product ID when you provision the product. The provisioned product
ID is formatted as follows: `pp-1111pwtn[ID number]`. 6. Choose the **execution ID**.
On the resulting **Execution details** page, you can view all of
the steps in the provisioning workflow. You can also review any failed steps to identify
the cause of the failure.
