# Create a VPC endpoint policy for Amazon WorkSpaces

You can create a policy for Amazon VPC endpoints for Amazon WorkSpaces to specify the
following:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.
  For more information, see [Controlling
  Access to Services with VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User
  Guide_.

###### Note

VPC endpoint policies aren't supported for Federal Information Processing
Standard (FIPS) Amazon WorkSpaces endpoints.

The following example VPC endpoint policy specifies that all users who have access
to the VPC interface endpoint are allowed to invoke the Amazon WorkSpaces hosted endpoint named
`ws-f9abcdefg`.

```
{
     "Statement": [
         {
             "Action": "workspaces:*",
             "Effect": "Allow",
             "Resource": "arn:aws:workspaces:us-west-2:1234567891011:workspace/ws-f9abcdefg",
             "Principal": "*"
         }
     ]
}
```

In this example, the following actions are denied:

- Invoking Amazon WorkSpaces hosted endpoints other than `ws-f9abcdefg`.
- Performing an action on any resource besides the one specified
  (WorkSpace ID: `ws-f9abcdefg`).

###### Note

In this example, users can still take other Amazon WorkSpaces API actions from outside the
VPC. To restrict API calls to those from within the VPC, see
[Identity and access management for WorkSpaces](workspaces-access-control.md "workspaces-access-control.md")
for information about using identity-based policies to control access to Amazon WorkSpaces API
endpoints.
