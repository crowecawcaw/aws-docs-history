

# Using parameterized managed permissions in AWS RAM
<a name="parameterized-managed-permissions"></a>

A parameterized managed permission is a managed permission with placeholders in its policy conditions that you fill in with your own values. These placeholders are template parameters. They don't create a new kind of managed permission. They add variability to the policy template of an existing one.

Instead of creating a separate customer managed permission for each unique condition value, you create one customer managed permission with parameters. When you associate it with a resource share, you provide a value for each parameter. AWS RAM substitutes your values into the policy template and attaches the resulting resource-based policy to the shared resources.

For example, a central platform team creates one customer managed permission for AWS Systems Manager Parameter Store parameters (resource type `ssm:Parameter`). It grants read access only to principals with an approved `team` tag. The platform team shares that customer managed permission with the accounts in its organization. Each account then uses it in its own resource shares, which can contain one or more Parameter Store parameters. In each resource share, the account supplies the `team` tag values of the principals that can read the shared Parameter Store parameters.

**Topics**
+ [Template parameter types](#template-parameter-types)
+ [Policy template syntax rules](#template-syntax-rules)
+ [Create a parameterized managed permission](#create-parameterized-permission)
+ [Versioning a parameterized managed permission](#parameterized-permission-versioning)
+ [Preview a rendered policy template](#preview-rendered-policy)
+ [Associate a parameterized managed permission with a resource share](#associate-parameterized-permission)
+ [View template parameters and values](#view-template-parameters)
+ [Sharing parameterized managed permissions across accounts](#sharing-parameterized-permissions)
+ [Control template parameter values with IAM policies](#template-iam-condition-keys)
+ [`STRING_LIST` parameter examples](#template-stringlist-examples)

## Template parameter types
<a name="template-parameter-types"></a>

AWS RAM supports two parameter types. The type determines how AWS RAM substitutes the value into the rendered policy. In the AWS RAM API and the AWS CLI, the types are `STRING` and `STRING_LIST`. The AWS RAM console shows them as **String** and **StringList**.

**`STRING`**  
Accepts exactly one string value.  
+ You can use a `STRING` parameter in a condition key or in a condition value.
+ You can embed a `STRING` parameter in other text. For example, `"arn:aws:iam::@{accountId}:role/Auditor"`.
+ The rendered value is always a string. Because IAM condition operators convert strings to the type that they compare, a `STRING` parameter can supply numeric, Boolean, date, IP address, or ARN values.

**`STRING_LIST`**  
Accepts from 1 to 100 string values.  
+ You can use a `STRING_LIST` parameter only in a condition value, not in a condition key.
+ If the condition value is a single string that contains only the parameter, for example `"@{teams}"`, AWS RAM renders an array of the values that you supply. If you supply a single value, AWS RAM renders a single string.
+ If the condition value has text before or after the parameter, for example `"arn:aws:iam::@{accountIds}:role/ParameterReader"`, AWS RAM combines each value with that text.
+ To combine each value with more than one string, list the strings in an array of condition values. AWS RAM renders each array entry for each value and removes duplicate results. The result is always an array.
+ AWS RAM and IAM don't split a string on commas. A comma-separated string is compared as one value.
For examples, see [`STRING_LIST` parameter examples](#template-stringlist-examples).

## Policy template syntax rules
<a name="template-syntax-rules"></a>

When you add parameters to the policy template of a managed permission, the following rules apply. If a request breaks one of these rules, AWS RAM rejects it with an `InvalidParameterException` or `InvalidPolicyException` error.
+ A parameter placeholder uses the syntax `@{parameterName}`.
+ Parameter names can contain letters (a-z, A-Z), numbers (0-9), colons (:), hyphens (-), and underscores (\_). Names must be unique within a managed permission version, and the comparison ignores case.
+ You must declare each parameter when you create the permission or the permission version. Each declaration requires a name, a type, and a description. The description can be up to 255 characters.
+ Every declared parameter must appear in the policy template.
+ Placeholders match declared names exactly, including case. Text in the `@{...}` format that doesn't exactly match a declared name stays in the policy as literal text. For example, if you declare `teams` but write `@{Teams}`, AWS RAM treats `@{Teams}` as text and rejects the request because `teams` isn't used.
+ Parameters can appear only in the `Condition` element, as a condition key or as a condition value. AWS RAM rejects parameters in the `Effect`, `Action`, or any other element.
+ A condition key can contain at most one parameter, and it must be a `STRING` parameter. A condition value can contain more than one parameter, for example `"@{project}-@{stage}"`. When a condition value combines `STRING_LIST` parameters, AWS RAM renders every combination of their values, up to 100 strings for each condition value.
+ You can declare up to 100 parameters for each managed permission version.
+ Parameters have no default values. When you associate the permission with a resource share, you must supply a non-empty value for every declared parameter, and you can't supply a name that isn't declared or supply the same name twice.

## Create a parameterized managed permission
<a name="create-parameterized-permission"></a>

You create a parameterized managed permission the same way that you create any other customer managed permission. The difference is that you declare parameters and use `@{parameterName}` placeholders in the conditions of the policy template.

------
#### [ Console ]

**To create a parameterized managed permission**

1. Open the **[Managed permissions library](https://console.aws.amazon.com/ram/home#Permissions:)** and choose **Create customer managed permission**.

1. Under **Customer managed permission details**, enter a name and choose the resource type.

1. Under **Policy template**, enter the policy. Use `@{parameterName}` placeholders in the conditions where you want each resource share to supply its own value.

1. Under **Template parameters**, choose **Add parameters from policy** to add a row for each placeholder in the policy, or choose **Add parameter** to add one row at a time. For each parameter, enter the **Parameter name**, choose the **Type** (**String** or **StringList**), and enter a **Description**. The description is shown to anyone who supplies a value for the parameter.

1. (Optional) Add tags.

1. Choose **Create customer managed permission**.

------
#### [ AWS CLI ]

**To create a parameterized managed permission**
+ Run the [create-permission](https://docs.aws.amazon.com/cli/latest/reference/ram/create-permission.html) command with the `--policy-template` and `--permission-template-parameters` parameters.

  The following example creates a customer managed permission for the `ssm:Parameter` resource type. In this policy, principals can read parameters only if the principal has a `team` tag whose value is in the `teams` list.

  ```
  $ aws ram create-permission \
      --name ParameterReadByTeam \
      --resource-type ssm:Parameter \
      --permission-template-parameters '[{"name":"teams","type":"STRING_LIST","description":"Values of the team principal tag that can read the shared parameters"}]' \
      --policy-template '{"Effect":"Allow","Action":["ssm:GetParameter","ssm:GetParameters"],"Condition":{"StringEquals":{"aws:PrincipalTag/team":"@{teams}"}}}'
  {
      "permission": {
          "arn": "arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam",
          "version": "1",
          "defaultVersion": true,
          "name": "ParameterReadByTeam",
          "resourceType": "ssm:Parameter",
          "status": "ATTACHABLE",
          "creationTime": 1763300000.000,
          "lastUpdatedTime": 1763300000.000,
          "permissionTemplateParameters": [
              {
                  "name": "teams",
                  "type": "STRING_LIST",
                  "description": "Values of the team principal tag that can read the shared parameters"
              }
          ]
      }
  }
  ```

------

## Versioning a parameterized managed permission
<a name="parameterized-permission-versioning"></a>

Parameterized managed permissions are versioned the same way as any other customer managed permission. Each version declares its parameters independently, so a new version can declare a different set of parameters than the version before it.

To create a new version, run the [create-permission-version](https://docs.aws.amazon.com/cli/latest/reference/ram/create-permission-version.html) command with the `--policy-template` and `--permission-template-parameters` parameters. The following example adds a second condition with a `STRING` parameter named `environment`.

```
$ aws ram create-permission-version \
    --permission-arn arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam \
    --permission-template-parameters '[{"name":"teams","type":"STRING_LIST","description":"Values of the team principal tag that can read the shared parameters"},{"name":"environment","type":"STRING","description":"Value of the environment principal tag that can read the shared parameters"}]' \
    --policy-template '{"Effect":"Allow","Action":["ssm:GetParameter","ssm:GetParameters"],"Condition":{"StringEquals":{"aws:PrincipalTag/team":"@{teams}","aws:PrincipalTag/environment":"@{environment}"}}}'
```

A new version becomes the default version as soon as you create it. Existing resource shares keep the version that they use. When the owner of a resource share updates it to the new version, the owner must supply values for the parameters that the new version declares. For more information, see [Updating AWS managed permissions to a newer version](working-with-sharing-update-permissions.md).

For more information about how customer managed permission versions and default versions work, see [Creating and using customer managed permissions in AWS RAM](create-customer-managed-permissions.md).

## Preview a rendered policy template
<a name="preview-rendered-policy"></a>

Before you associate a parameterized managed permission with a resource share, you can preview the policy that AWS RAM renders from specific parameter values.

In the AWS RAM console, when you create or update a resource share, enter the values under **Template parameter values** and choose **Preview rendered policy**.

In the AWS CLI, run the [get-permission](https://docs.aws.amazon.com/cli/latest/reference/ram/get-permission.html) command with the `--permission-template-parameters` parameter. The `permission` field of the response contains the policy with your values in place of the placeholders.

```
$ aws ram get-permission \
    --permission-arn arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam \
    --permission-template-parameters '[{"name":"teams","values":["payments","analytics"]},{"name":"environment","values":["prod"]}]'
{
    "permission": {
        "arn": "arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam",
        "version": "2",
        "defaultVersion": true,
        "name": "ParameterReadByTeam",
        "resourceType": "ssm:Parameter",
        "permission": "{\"Effect\":\"Allow\",\"Action\":[\"ssm:GetParameter\",\"ssm:GetParameters\"],\"Condition\":{\"StringEquals\":{\"aws:PrincipalTag/team\":[\"payments\",\"analytics\"],\"aws:PrincipalTag/environment\":\"prod\"}}}",
        "creationTime": 1763400000.000,
        "lastUpdatedTime": 1763400000.000,
        "isResourceTypeDefault": false,
        "permissionType": "CUSTOMER_MANAGED",
        "featureSet": "STANDARD",
        "status": "ATTACHABLE",
        "permissionTemplateParameters": [
            {
                "name": "teams",
                "type": "STRING_LIST",
                "description": "Values of the team principal tag that can read the shared parameters"
            },
            {
                "name": "environment",
                "type": "STRING",
                "description": "Value of the environment principal tag that can read the shared parameters"
            }
        ]
    }
}
```

Without the `--permission-template-parameters` parameter, the `get-permission` command returns the policy template with the `@{parameterName}` placeholders. The `permissionTemplateParameters` field lists the name, type, and description of each declared parameter.

## Associate a parameterized managed permission with a resource share
<a name="associate-parameterized-permission"></a>

When you associate a parameterized managed permission with a resource share, you must provide values for all of the parameters that the version declares. AWS RAM renders the policy template with your values and attaches the resulting resource-based policy to the shared resources of that type.

------
#### [ Console ]

**To associate a parameterized managed permission with a resource share**

1. When you create or update a resource share, on the **Associate managed permissions** page, choose the parameterized managed permission for the resource type.

1. Under **Template parameter values**, enter a value for each parameter. For a **StringList** parameter, press Enter after each value, or paste values separated by newlines.

1. (Optional) Choose **Preview rendered policy** to check the policy that AWS RAM will attach.

1. Complete the rest of the wizard. The review page lists the values under **Template parameter values**.

------
#### [ AWS CLI ]

**To associate a parameterized managed permission with a resource share**

1. Run [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) or [associate-resource-share-permission](https://docs.aws.amazon.com/cli/latest/reference/ram/associate-resource-share-permission.html) with the `--permission-template-parameters` parameter.

   For `create-resource-share`, the parameter is a list. Each entry contains a `permissionArn` and the `permissionTemplateParameters` values for that permission. The following example creates a resource share that shares a Parameter Store parameter with another AWS account. Principals with the `team` tag `payments` or `analytics` and the `environment` tag `prod` can read it.

   ```
   $ aws ram create-resource-share \
       --name PaymentsConfig \
       --resource-arns arn:aws:ssm:us-east-1:123456789012:parameter/payments/endpoint \
       --principals 111122223333 \
       --permission-arns arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam \
       --permission-template-parameters '[{"permissionArn":"arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam","permissionTemplateParameters":[{"name":"teams","values":["payments","analytics"]},{"name":"environment","values":["prod"]}]}]'
   {
       "resourceShare": {
           "resourceShareArn": "arn:aws:ram:us-east-1:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
           "name": "PaymentsConfig",
           "owningAccountId": "123456789012",
           "allowExternalPrincipals": true,
           "status": "ACTIVE",
           "creationTime": 1763300000.000,
           "lastUpdatedTime": 1763300000.000,
           "featureSet": "STANDARD"
       }
   }
   ```

   `create-resource-share` always uses the default version of each managed permission. You can associate only the default version of a managed permission with a resource share.

1. To change the parameter values on an existing resource share, or to move it to the default version of the permission, run [associate-resource-share-permission](https://docs.aws.amazon.com/cli/latest/reference/ram/associate-resource-share-permission.html) with the `--replace` parameter. For this command, `--permission-template-parameters` takes the parameter values directly.

   ```
   $ aws ram associate-resource-share-permission \
       --resource-share-arn arn:aws:ram:us-east-1:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
       --permission-arn arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam \
       --permission-template-parameters '[{"name":"teams","values":["payments"]},{"name":"environment","values":["prod"]}]' \
       --replace
   {
       "returnValue": true
   }
   ```

------

To move many resource shares from one version or permission to another, run [replace-permission-associations](https://docs.aws.amazon.com/cli/latest/reference/ram/replace-permission-associations.html). If the target version declares parameters, include `--permission-template-parameters`. AWS RAM applies the same values to every resource share that the command updates.

## View template parameters and values
<a name="view-template-parameters"></a>

You can view the parameters that a managed permission declares and the values that your resource shares supply.

**View the parameters that a managed permission declares**  
Run the [get-permission](https://docs.aws.amazon.com/cli/latest/reference/ram/get-permission.html) command. The `permissionTemplateParameters` field lists the name, type, and description of each parameter. In the console, the permission details page shows the same information.

**View the values that a resource share supplies**  
Run the [list-resource-share-permissions](https://docs.aws.amazon.com/cli/latest/reference/ram/list-resource-share-permissions.html) command. For each associated parameterized managed permission, the `permissionTemplateParameters` field includes the values that the resource share supplies.  

```
$ aws ram list-resource-share-permissions \
    --resource-share-arn arn:aws:ram:us-east-1:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
{
    "permissions": [
        {
            "arn": "arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam",
            "version": "2",
            "defaultVersion": true,
            "name": "ParameterReadByTeam",
            "resourceType": "ssm:Parameter",
            "status": "ATTACHABLE",
            "creationTime": 1763400000.000,
            "lastUpdatedTime": 1763400000.000,
            "isResourceTypeDefault": false,
            "permissionType": "CUSTOMER_MANAGED",
            "featureSet": "STANDARD",
            "permissionTemplateParameters": [
                {
                    "name": "teams",
                    "values": ["payments"]
                },
                {
                    "name": "environment",
                    "values": ["prod"]
                }
            ]
        }
    ]
}
```
The [list-permission-associations](https://docs.aws.amazon.com/cli/latest/reference/ram/list-permission-associations.html) command also returns the values for the resource shares that you own. When you list the resource shares in other AWS accounts that use a customer managed permission that you shared, the response doesn't include their values.

## Sharing parameterized managed permissions across accounts
<a name="sharing-parameterized-permissions"></a>

You can share a parameterized managed permission with other AWS accounts like any other customer managed permission. The receiving accounts can see the name, type, and description of each parameter, so write descriptions that tell them what value to supply. Each receiving account supplies its own values when it associates the shared managed permission with its own resource shares.

For instructions on sharing customer managed permissions, see [Sharing and using customer managed permissions across accounts in AWS RAM](sharing-customer-managed-permissions.md).

## Control template parameter values with IAM policies
<a name="template-iam-condition-keys"></a>

You can use the `ram:PermissionTemplateParameter/{{parameter-name}}` condition key in an IAM policy to control which values a principal can supply for a parameter. The key is multivalued and contains the values in the request for the named parameter. It is available on the permission resource for the `ram:CreateResourceShare`, `ram:AssociateResourceSharePermission`, and `ram:ReplacePermissionAssociations` actions.

In the following example policy, the first statement grants the actions on the `ParameterReadByTeam` customer managed permission. The second statement denies them if any value supplied for `teams` is something other than `payments` or `analytics`. Because the key is multivalued, the policy uses the `ForAnyValue` set operator. AWS RAM requires a value for every declared parameter, so a request that uses this customer managed permission always includes the key.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceSharePermission",
                "ram:ReplacePermissionAssociations"
            ],
            "Resource": "arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam"
        },
        {
            "Effect": "Deny",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceSharePermission",
                "ram:ReplacePermissionAssociations"
            ],
            "Resource": "arn:aws:ram:us-east-1:123456789012:permission/ParameterReadByTeam",
            "Condition": {
                "ForAnyValue:StringNotEquals": {
                    "ram:PermissionTemplateParameter/teams": [
                        "payments",
                        "analytics"
                    ]
                }
            }
        }
    ]
}
```

These statements control only the permission resource. The principal also needs permission for the other resources in the request, such as the resource share and the resources that it shares. For more examples, see [Example IAM policies for AWS RAM](security-iam-policies-examples.md).

## `STRING_LIST` parameter examples
<a name="template-stringlist-examples"></a>

The following examples show how AWS RAM renders `STRING_LIST` parameters.

**Example A `STRING_LIST` parameter alone in a condition value**  
Template:  

```
"Condition": {
    "StringEquals": {
        "aws:PrincipalTag/team": "@{teams}"
    }
}
```
Values: `["payments", "analytics"]`  
Rendered policy:  

```
"Condition": {
    "StringEquals": {
        "aws:PrincipalTag/team": ["payments", "analytics"]
    }
}
```
With the single value `["payments"]`, the rendered value is the string `"payments"`.

**Example A `STRING_LIST` parameter with surrounding text**  
AWS RAM combines each value with the text before and after the parameter.  
Template:  

```
"Condition": {
    "ArnLike": {
        "aws:PrincipalArn": "arn:aws:iam::@{accountIds}:role/ParameterReader"
    }
}
```
Values: `["111122223333", "444455556666"]`  
Rendered policy:  

```
"Condition": {
    "ArnLike": {
        "aws:PrincipalArn": [
            "arn:aws:iam::111122223333:role/ParameterReader",
            "arn:aws:iam::444455556666:role/ParameterReader"
        ]
    }
}
```

**Example A `STRING_LIST` parameter in an array of condition values**  
AWS RAM renders each entry in the array for each value, and removes duplicate results.  
Template:  

```
"Condition": {
    "ArnLike": {
        "aws:PrincipalArn": [
            "arn:aws:iam::@{accountIds}:role/Auditor",
            "arn:aws:iam::@{accountIds}:role/Reader"
        ]
    }
}
```
Values: `["111122223333", "444455556666"]`  
Rendered policy:  

```
"Condition": {
    "ArnLike": {
        "aws:PrincipalArn": [
            "arn:aws:iam::111122223333:role/Auditor",
            "arn:aws:iam::444455556666:role/Auditor",
            "arn:aws:iam::111122223333:role/Reader",
            "arn:aws:iam::444455556666:role/Reader"
        ]
    }
}
```