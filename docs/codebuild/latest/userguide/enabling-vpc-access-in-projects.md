# Allow Amazon VPC access in your CodeBuild

projects

Include these settings in your VPC configuration:

- For **VPC ID**, choose the VPC ID that CodeBuild uses.
- For **Subnets**, choose a private subnet with NAT translation
  that includes or has routes to the resources used by CodeBuild.
- For **Security Groups**, choose the security groups that
  CodeBuild uses to allow access to resources in the VPCs.
  To use the console to create a build project, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console"). When you
  create or change your CodeBuild project, in **VPC**, choose your VPC ID,
  subnets, and security groups.

To use the AWS CLI to create a build project, see [Create a build project (AWS CLI)](create-project.md#create-project-cli "create-project.md#create-project-cli"). If you are using the AWS CLI with CodeBuild, the
service role used by CodeBuild to interact with services on behalf of the IAM user must have
a policy attached. For information, see [Allow CodeBuild access to AWS services required to create a VPC network
interface](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-create-vpc-network-interface "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-create-vpc-network-interface").

The `vpcConfig` object should include your
`vpcId`, `securityGroupIds`, and
`subnets`.

- `vpcId`: Required. The VPC ID that CodeBuild uses. Run
  this command to get a list of all Amazon VPC IDs in your Region:

```
aws ec2 describe-vpcs
```

- `subnets`: Required. The subnet IDs that include
  resources used by CodeBuild. Run this command obtain these IDs:

```
aws ec2 describe-subnets --filters "Name=vpc-id,Values=<vpc-id>" --region us-east-1
```

###### Note

Replace `us-east-1` with your Region.

- `securityGroupIds`: Required. The security group IDs
  used by CodeBuild to allow access to resources in the VPCs. Run this command to
  obtain these IDs:

```
aws ec2 describe-security-groups --filters "Name=vpc-id,Values=<vpc-id>" --region us-east-1
```

###### Note

Replace `us-east-1` with your Region.
