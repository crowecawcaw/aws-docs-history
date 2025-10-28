# Creating a VPC endpoint policy for

AWS Organizations

You can attach an endpoint policy to your VPC endpoint that controls access to
Organizations. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.
  For more information, see [Control access to VPC
  endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

## Example: VPC endpoint policy for

AWS Organizations actions

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "Organizations:DescribeAccount"
         ],
         "Resource":"*"
      }
   ]
}
```
