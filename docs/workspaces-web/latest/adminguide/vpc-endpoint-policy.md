

# Creating an endpoint policy for your interface VPC endpoint
<a name="vpc-endpoint-policy"></a>

An endpoint policy is an IAM resource that you can attach to an interface VPC endpoint. The default endpoint policy gives you full access to Amazon WorkSpaces Secure Browser APIs through the interface VPC endpoint. To control the access granted to Amazon WorkSpaces Secure Browser from your VPC, attach a custom endpoint policy to the interface VPC endpoint.

An endpoint policy specifies the following information:
+ The principals that can perform actions (AWS accounts, IAM users, and IAM roles).
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for Amazon WorkSpaces Secure Browser actions**  
The following is an example of a custom endpoint policy. When you attach this policy to your interface VPC endpoint, it grants access to the listed Amazon WorkSpaces Secure Browser actions for all principals on all resources.

```
{
     "Statement": [
         {
             "Action": "workspaces-web:*",
             "Effect": "Allow",
             "Resource": "*",
             "Principal": "*"
         }
     ]
}
```