

# Creating a VPC endpoint policy for AWS Organizations
<a name="create-vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to Organizations. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

## Example: VPC endpoint policy for AWS Organizations actions
<a name="Log-entries-close-account"></a>

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