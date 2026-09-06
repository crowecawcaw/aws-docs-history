

# Granting Lambda function access to other accounts
<a name="permissions-function-cross-account"></a>

To share a function with another AWS account, add a cross-account permissions statement to the function's [resource-based policy](access-control-resource-based.md). We recommend using `put-resource-policy` to create a full JSON policy. With `put-resource-policy`, you can specify multiple principals, add conditions, and create deny statements. You can also use `add-permission` for simple use cases.

**Important**  
Using `put-resource-policy` replaces any existing resource-based policy on the resource. If the resource already has permissions defined with `add-permission`, `put-resource-policy` overwrites them. Use `get-resource-policy` to retrieve the existing policy before making changes.

## Using a full JSON policy (recommended)
<a name="permissions-function-cross-account-json"></a>

The following example policy grants two AWS accounts permission to invoke a function, with one restricted to a specific IAM role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "allow-account-invoke",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::111122223333:root",
                    "arn:aws:iam::444455556666:role/cross-account-role"
                ]
            },
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-function"
        }
    ]
}
```

Save the policy to a file named `policy.json` and apply it. The `resource-arn` can specify a function, version, or alias:

```
aws lambda put-resource-policy \
  --resource-arn arn:aws:lambda:{{us-east-2}}:{{123456789012}}:function:{{my-function}} \
  --policy file://policy.json
```

You can also restrict cross-account access to specific versions using an alias. The following policy grants invoke access only through the `prod` alias:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "allow-account-prod-alias",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:root"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-function:prod"
        }
    ]
}
```

Save this policy to a file named `alias-policy.json` and apply it to the alias:

```
aws lambda put-resource-policy \
  --resource-arn arn:aws:lambda:{{us-east-2}}:{{123456789012}}:function:{{my-function}}:{{prod}} \
  --policy file://alias-policy.json
```

The resource-based policy grants permission for the other account to access the function, but doesn't allow users in that account to exceed their permissions. Users in the other account must have the corresponding [user permissions](access-control-identity-based.md) to use the Lambda API.

You can grant cross-account access for most API actions that operate on an existing function. For example, you could grant access to `lambda:ListAliases` to let an account get a list of aliases, or `lambda:GetFunction` to let them download your function code.

To grant other accounts permission for multiple functions, or for actions that don't operate on a function, we recommend that you use [IAM roles](access-control-identity-based.md).

## Using add-permission
<a name="permissions-function-cross-account-add-permission"></a>

For simple use cases, you can use `add-permission` to add individual statements. The following example grants account `111122223333` permission to invoke `my-function` with the `prod` alias:

```
aws lambda add-permission \
  --function-name my-function:{{prod}} \
  --statement-id xaccount \
  --action lambda:InvokeFunction \
  --principal {{111122223333}} \
  --output text
```

You should see the following output:

```
{"Sid":"xaccount","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::111122223333:root"},"Action":"lambda:InvokeFunction","Resource":"arn:aws:lambda:us-east-1:123456789012:function:my-function"}
```

**Note**  
If you call `add-permission` after `put-resource-policy`, the new statement appends to the existing JSON policy.

To limit access to a user or role in another account, specify the full ARN of the identity as the principal. For example, `arn:aws:iam::123456789012:user/developer`.