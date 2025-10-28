# Delete a resource-based

delegation policy with AWS Organizations

When you no longer need to delegate the management of policies in your organization,
you can delete the resource-based delegation policy from the organization's management
account.

###### Important

If you delete your resource-based delegation policy, you can't recover it.

###### Minimum permissions

To delete the resource-based delegation policy, you need permissions to run the
following action: `organizations:DeleteResourcePolicy`.

AWS Management Console

###### To delete a delegation policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Choose **Settings**.
3. In the **Delegated administrator for AWS Organizations**
   section, choose **Delete**.
4. In the **Delete policy** confirmation dialog box,
   type `delete`. Then, choose **Delete
   policy**.

AWS CLI & AWS SDKs

###### Delete a delegation policy

You can use the following command to delete a delegation policy:

- AWS CLI: [delete-resource-policy](../../../cli/latest/reference/organizations/delete-resource-policy.md "../../../cli/latest/reference/organizations/delete-resource-policy.md")

The following example deletes the policy.

```
`$` **aws organizations delete-resource-policy**
```

- AWS SDK: [DeleteResourcePolicy](../APIReference/API_DeleteResourcePolicy.md "../APIReference/API_DeleteResourcePolicy.md")
