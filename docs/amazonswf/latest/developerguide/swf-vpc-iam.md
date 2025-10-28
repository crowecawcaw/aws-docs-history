# Amazon Virtual Private Cloud Endpoint Policies for Amazon SWF

You can create an Amazon VPC endpoint policy for Amazon SWF in which you specify the
following:

- The **principal** that can perform
  actions.
- The actions that can be performed.
- The resources on which the actions can be performed.
  The following example adds a specific IAM role to a policy:

```
"Principal": {
   "AWS": "arn:aws:iam::123456789012:role/MyRole"
}
```

- For more information about creating endpoint policies, see [Controlling Access to Services with
  VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md").
- For information about how you can use IAM to control access to your AWS and Amazon SWF resources, see
  [Identity and Access Management in Amazon Simple Workflow Service](swf-dev-iam.md "swf-dev-iam.md").
