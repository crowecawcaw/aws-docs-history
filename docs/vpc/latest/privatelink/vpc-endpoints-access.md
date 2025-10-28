# Control access to VPC endpoints using endpoint policies

An endpoint policy is a resource-based policy that you attach to a VPC endpoint to control
which AWS principals can use the endpoint to access an AWS service.

An endpoint policy does not override or replace identity-based policies or resource-based
policies. For example, if you're using an interface endpoint to connect to Amazon S3, you can
also use Amazon S3 bucket policies to control access to buckets from specific endpoints or
specific VPCs.

###### Contents

- [Considerations](#vpc-endpoint-policy-considerations "#vpc-endpoint-policy-considerations")
- [Default endpoint policy](#default-endpoint-policy "#default-endpoint-policy")
- [Policies for interface endpoints](#vpc-endpoint-policies-interface "#vpc-endpoint-policies-interface")
- [Principals for gateway endpoints](#vpc-endpoint-policies-gateway "#vpc-endpoint-policies-gateway")
- [Update a VPC endpoint policy](#update-vpc-endpoint-policy "#update-vpc-endpoint-policy")

## Considerations

- An endpoint policy is a JSON policy document that uses the IAM policy
  language. It must contain a [Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") element. The size of an endpoint policy cannot exceed
  20,480 characters, including white space.
- When you create an interface or gateway endpoint for an AWS service, you can
  attach a single endpoint policy to the endpoint. You can [update the endpoint policy](#update-vpc-endpoint-policy "#update-vpc-endpoint-policy") at
  any time. If you don't attach an endpoint policy, we attach the [default endpoint policy](#default-endpoint-policy "#default-endpoint-policy").
- Not all AWS services support endpoint policies. If an AWS service doesn't
  support endpoint policies, we allow full access to any endpoint for the service.
  For more information, see [View endpoint policy support](aws-services-privatelink-support.md#vpce-endpoint-policy-support "aws-services-privatelink-support.md#vpce-endpoint-policy-support").
- When you create a VPC endpoint for an endpoint service other than an
  AWS service, we allow full access to the endpoint.
- You can't use wildcard characters (\* or ?) or [numeric condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Numeric "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Numeric") with global context keys that reference
  system-generated identifiers (for example, `aws:PrincipalAccount` or `aws:SourceVpc`).
- When you use a [string condition operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String"), you must use at least six consecutive
  characters before or after each wildcard character.
- When you specify an ARN in a resource or condition element, the account portion
  of the ARN can include an account ID or a wildcard character, but not both.
- After you update an endpoint policy, it can take a few minutes for the changes
  to take effect.

## Default endpoint policy

The default endpoint policy grants full access to the endpoint.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

## Policies for interface endpoints

For example endpoint policies for AWS services, see [AWS services that integrate with
AWS PrivateLink](aws-services-privatelink-support.md "aws-services-privatelink-support.md").
The first column in the table contains links to AWS PrivateLink documentation for each
AWS service. If an AWS service supports endpoint policies, its documentation
includes example endpoint policies.

## Principals for gateway endpoints

With gateway endpoints, the `Principal` element must be set to `*`.
To specify a principal, use the `aws:PrincipalArn` condition key.

```
"Condition": {
    "StringEquals": {
        "aws:PrincipalArn": "`arn:aws:iam::123456789012:user/endpointuser`"
    }
}
```

If you specify the principal in the following format, access is granted to the
AWS account root user only, not all users and roles for the account.

```
"AWS": "`account_id`"
```

For example endpoint policies for gateway endpoints, see the following:

- [Endpoints for Amazon S3](vpc-endpoints-s3.md#edit-vpc-endpoint-policy-s3 "vpc-endpoints-s3.md#edit-vpc-endpoint-policy-s3")
- [Endpoints for DynamoDB](vpc-endpoints-ddb.md#iam-policies-ddb "vpc-endpoints-ddb.md#iam-policies-ddb")

## Update a VPC endpoint policy

Use the following procedure to update an endpoint policy for an AWS service.
After you update an endpoint policy, it can take a few minutes for the changes
to take effect.

###### To update an endpoint policy using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Select the VPC endpoint.
4. Choose **Actions**, **Manage
   policy**.
5. Choose **Full Access** to allow full access to the service,
   or choose **Custom** and attach a custom policy.
6. Choose **Save**.

###### To update an endpoint policy using the command line

- [modify-vpc-endpoint](../../../cli/latest/reference/ec2/modify-vpc-endpoint.md "../../../cli/latest/reference/ec2/modify-vpc-endpoint.md") (AWS CLI)
- [Edit-EC2VpcEndpoint](../../../powershell/latest/reference/items/Edit-EC2VpcEndpoint.md "../../../powershell/latest/reference/items/Edit-EC2VpcEndpoint.md") (Tools for Windows PowerShell)
