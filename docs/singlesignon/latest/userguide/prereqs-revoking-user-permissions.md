# Use a Deny policy to revoke
 active user permissions

You might need to revoke an IAM Identity Center user’s access to AWS accounts while the
 user is actively using a permission set. You can remove their ability to use
 their active IAM role sessions by implementing a Deny policy for an
 unspecified user in advance, then when needed, you can update the Deny policy to
 specify the user whose access you want to block. This topic explains how to
 create a Deny policy and considerations for how to deploy the policy. 


## Prepare to revoke an active
 IAM role session created by a permission set


You can prevent the user from taking actions with an IAM role they are
 actively using by applying a deny all policy for a specific user through the
 use of a Service Control Policy You can also prevent a user from using any
 permission set until you change their password, which removes a bad actor
 actively misusing stolen credentials. If you need to deny access broadly and
 prevent a user from re-entering a permission set or accessing other
 permission sets, you might also remove all user access, stop the active
 AWS access portal session, and disable the user sign-in. See [View and end active sessions for your workforce users](end-active-sessions.md "end-active-sessions.md") to learn how to use the Deny
 policy in conjunction with additional actions for broader access
 revocation.


### Deny policy


You can use a Deny policy with a condition that matches to the user’s
 `UserID` from the IAM Identity Center identity store to prevent further
 actions by an IAM role that the user is actively using. Using this
 policy avoids impact to other users who might be using the same
 permission set when you deploy the Deny policy. This policy uses the
 placeholder user ID, ``Add user ID
 here``, for `"identitystore:userId"`
 that you’ll update with the user ID for which you want to revoke
 access.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "identitystore:userId": "`Add user ID here`" 
 }
 }
 }
 ]
}`

```





Although you could use another condition key such as
 `“aws:userId”`, `“identitystore:userId”` is
 certain because it is a globally unique value that is associated with one
 person. Using `“aws:userId”` in the condition can be affected
 by how user attributes are synchronized from your source of identities
 and can change if the user’s username or email address changes.


From the IAM Identity Center console, you can find a user’s
 `identitystore:userId` by navigating to
 **Users**, searching for the user by name,
 expanding the **General information** section and
 copying the User ID. It's also convenient to stop a user’s AWS access portal
 session and disable their sign-in access in the same section while
 searching for the User ID. You can automate the process to create a Deny
 policy by obtaining the user’s User ID through querying the identity
 store APIs.


### Deploying the deny policy


 You can use a placeholder user ID that isn't valid, such as
 ``Add user ID here``, to
 deploy the Deny policy in advance using a Service Control Policy (SCP)
 that you attach to the AWS accounts users might have access to. This
 is the recommended approach for its ease and speed of impact. When you
 revoke a user’s access with the Deny policy, you'll edit the policy to
 replace the placeholder user ID with the user ID of the person whose
 access you want to revoke. This prevents the user from taking any
 actions with any permission set in every account that you attach the
 SCP. It blocks the user’s actions even if they use their active
 AWS access portal session to navigate to different accounts and assume
 different roles. With the user’s access fully blocked by the SCP, you
 can then disable their ability to sign in, revoke their assignments, and
 stop their AWS access portal session if needed. 


As an alternative to using SCPs, you can also include the Deny policy
 in the inline policy of permission sets and in customer managed policies
 that are used by the permission sets the user can access. 


If you must revoke access for more than one person, you can use a list
 of values in the condition block, such as:



```

            "Condition": {
                    "StringEquals": {
                        "identitystore:userId": [" `user1 userId`", "`user2 userId`"...]
                        }
        }
```

###### Important

Regardless of the method(s) you use, you must take any other
 corrective actions and keep the user’s user ID in the policy for at
 least 12 hours. After that time, any roles the user has assumed
 expire and you can then remove their user ID from the Deny
 policy.
