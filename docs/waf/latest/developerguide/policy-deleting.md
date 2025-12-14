**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Deleting an AWS Firewall Manager policy

You can delete a Firewall Manager policy by performing the following steps.

###### To delete a policy (console)

1. In the navigation pane, choose **Security policies**.
2. Choose the option next to the policy that you want to delete.
3. Choose **Delete**.

###### Note

When you delete a Firewall Manager common security group policy, to remove the policy's
replica security groups, choose the option to clean up the resources created by the
policy. Otherwise, after the primary is deleted, the replicas remain and require
manual management in each Amazon VPC instance.

###### Important

When you delete a Firewall Manager Shield Advanced policy, the policy is deleted, but your accounts remain
subscribed to Shield Advanced.
