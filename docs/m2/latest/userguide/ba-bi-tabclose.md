AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Troubleshooting: AWS Blu Insights does not open from the

console

This page describes how you can resolve Blu Insights page not opening from the AWS Mainframe Modernization
console.

- Engine: AWS Blu Age
- Component: Blu Insights
  When you try to access Blu Insights from the AWS Mainframe Modernization console, it doesn't open and the new tab is
  closed immediately.

## Common cause

The role you are using to access Blu Insights does not have sufficient permissions.

## Resolution

Attach an IAM policy to the role to allow it to access Blu Insights. Make sure the policy includes at least the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "m2:GetSignedBluinsightsUrl"
 ],
 "Resource": "*"
 }
 ]
}`

```

Make sure to replace `region` and `account` with the correct AWS Region and AWS account.
