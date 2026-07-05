After careful consideration, we have made the decision to close new customer access to **AWS Mainframe Modernization self-managed experience**,
effective June 30, 2026. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for
AWS Mainframe Modernization self-managed experience, but we do not plan to introduce new features. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Troubleshooting: AWS Transform for mainframe refactor does not open from the console

This page describes how you can resolve AWS Transform for mainframe refactor page not opening from the AWS Mainframe Modernization
console.

- Engine: AWS Transform for mainframe
- Component: AWS Transform for mainframe refactor
  When you try to access AWS Transform for mainframe refactor from the AWS Mainframe Modernization console, it doesn't open and the new tab is
  closed immediately.

## Common cause

The role you are using to access AWS Transform for mainframe refactor does not have sufficient permissions.

## Resolution

Attach an IAM policy to the role to allow it to access AWS Transform for mainframe refactor. Make sure the policy includes at least the following permissions.

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
