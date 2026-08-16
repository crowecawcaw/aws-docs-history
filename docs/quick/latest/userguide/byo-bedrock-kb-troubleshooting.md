# Troubleshooting

## Troubleshoot access denied errors

When you query an Amazon Bedrock managed knowledge base in Amazon Quick, retrieval is authorized
only when every permission layer allows it. If you receive the error
_Insufficient permissions to access this knowledge base_, work
through the following layers in order and stop at the first layer that is not
satisfied.

###### Tip

First, check AWS CloudTrail for the `AccessDenied` event to
identify which principal and action were rejected. Then go directly to the
matching layer in the following list.

1. **Service role permissions.** Confirm that
   the Amazon Quick service role grants `bedrock:Retrieve` and
   `bedrock:GetDocumentContent` on the knowledge base.
2. **Cross-account resource policy.** For
   cross-account setups, confirm that the knowledge base resource policy grants
   those same actions to the Amazon Quick service role.
3. **Customer managed key.** If the knowledge
   base is encrypted with a customer managed key, confirm that the service role
   has `kms:Decrypt` and `kms:DescribeKey` on that
   key.
4. **Knowledge base ARN.** Confirm that the
   knowledge base ARN is correct in the Amazon Quick admin configuration. Amazon Quick
   scopes the service role policy to the ARN you enter, so an incorrect ARN
   denies retrieval.
5. **IAM policy assignments.** If IAM policy
   assignments are enabled in the account, Amazon Quick applies a per-user session
   policy at retrieval time and intersects it with the service role
   permissions. An action succeeds only if both the service role and the user's
   assigned IAM policy allow it. Check this layer when the knowledge base
   works for an administrator but fails for a specific user or group.

###### To grant retrieval permissions to affected users

    1. Open the [Quick console](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
    2. Choose **Manage account**, and then choose
     **IAM policy assignments**.
    3. Create a new assignment, or edit the IAM policy behind an
     existing assignment, to allow the knowledge base retrieval actions.
     For example:



    ```
    {
        "Sid": "AllowQuickFMKBRetrieve",
        "Effect": "Allow",
        "Action": ["bedrock:Retrieve", "bedrock:GetDocumentContent"],
        "Resource": "arn:aws:bedrock:`REGION`:`ACCOUNT_ID`:knowledge-base/`KB_ID`"
    }
    ```
    4. Add the affected users or groups to the assignment, and then save
     and enable it.

For more information about IAM policy assignments, see [IAM policy assignments](iam-policy-assignments.md "iam-policy-assignments.md").
