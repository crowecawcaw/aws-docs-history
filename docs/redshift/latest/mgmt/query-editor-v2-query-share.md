Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Sharing a query

You can share your queries with your team. You can also view the history of saved
queries and manage query versions.

To share a query with your team, make sure that you have the principal tag
`sqlworkbench-team` set to the same value as the rest of your team
members in your account. For example, an administrator might set the value to
`accounting-team` for everyone in the accounting department.
For an example, see
[Permissions
required to use the query editor v2](redshift-iam-access-control-identity-based.md#redshift-policy-resources.required-permissions.query-editor-v2 "redshift-iam-access-control-identity-based.md#redshift-policy-resources.required-permissions.query-editor-v2") .

###### To share a query with a team

1. Choose **Queries** from the navigation pane.
2. Open the context (right-click) menu of the query that you want to share
   and choose **Share with my team**.
3. Choose the team or teams that you want to share the query with and then
   choose **Save sharing options**.
