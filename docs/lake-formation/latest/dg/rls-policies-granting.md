

# Attaching and detaching RLS policies
<a name="rls-policies-granting"></a>

This section explains how to attach row-level security (RLS) policies to principals to grant row-level access, and how to detach them to revoke that access. It covers direct attachment, tag-based attachment, ABAC conditions, and default policy setup.

**Overview**  


To grant a principal access to specific rows, you attach an RLS policy to that principal on a Data Catalog resource (a table, or a set of tables via LF-Tags). The attachment establishes the relationship between the policy, the resource, and the principal. Once attached, the policy's filter expression is enforced immediately when the principal queries those tables.

To revoke access, you detach the policy. The principal can no longer see rows granted by that policy (unless other attached policies still provide access through additive semantics).

**Attaching a policy**  
You can attach an RLS policy using the Lake Formation console or the AWS CLI.

------
#### [ AWS Management Console ]

**To attach an RLS policy (console)**

1. Open the Lake Formation console.

1. In the navigation pane, choose **RLS policies**.

1. Select the policy you want to attach.

1. Choose **Attach**.

1. For **Database**, select the database containing the target table.

1. For **Table**, select the table.

1. For **Principal**, choose the principal type (IAM user, IAM role, or SAML identity) and provide the ARN or identifier.

1. (Optional) To set this as a default policy, select **Set as default policy**. When set as default, you do not specify a principal.

1. Choose **Attach**.

------
#### [ AWS CLI ]

Direct attachment:

```
aws lakeformation attach-rls-policy \
  --name "region-filter-policy" \
  --resource '{"Table": {"DatabaseName": "analytics_db", "Name": "orders"}}' \
  --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/DataAnalyst"}'
```

Default policy attachment:

```
aws lakeformation attach-rls-policy \
  --name "no-rows-access-policy" \
  --resource '{"Table": {"DatabaseName": "main_db", "Name": "customers"}}' \
  --set-default
```

------

**Attaching a policy using the API or CLI**  


**Direct attachment to a principal**  
Use the `AttachRLSPolicy` API to attach a policy to a specific table and principal.

------
#### [ API ]

```
{
  "Name": "region-filter-policy",
  "Resource": {
    "Table": {
      "DatabaseName": "analytics_db",
      "Name": "orders"
    }
  },
  "Principal": {
    "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/DataAnalyst"
  }
}
```

------
#### [ AWS CLI ]

```
aws lakeformation attach-rls-policy \
  --name "region-filter-policy" \
  --resource '{"Table": {"DatabaseName": "analytics_db", "Name": "orders"}}' \
  --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/DataAnalyst"}'
```

------

**Tag-based attachment**  
To attach a policy to all tables matching an LF-Tag expression, use an `LFTagPolicy` resource instead of a direct table reference.

------
#### [ API ]

```
{
  "Name": "pii-filter-policy",
  "Resource": {
    "LFTagPolicy": {
      "ResourceType": "TABLE",
      "Expression": [
        {
          "TagKey": "classification",
          "TagValues": ["confidential"]
        }
      ]
    }
  },
  "Principal": {
    "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/RestrictedAnalyst"
  }
}
```

------
#### [ AWS CLI ]

```
aws lakeformation attach-rls-policy \
  --name "pii-filter-policy" \
  --resource '{"LFTagPolicy": {"ResourceType": "TABLE", "Expression": [{"TagKey": "classification", "TagValues": ["confidential"]}]}}' \
  --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/RestrictedAnalyst"}'
```

------

With tag-based attachment, the policy applies to any table that matches the tag expression. If new tables are tagged with `classification=confidential`, the policy automatically applies to them.

**Note**  
Tag-based attachments are validated at query time, not at attach time. If the filter expression references columns that do not exist on a matched table, the query returns an empty result for that table rather than failing.

**ABAC conditions on attachment**  
You can add a `Condition` field to the `AttachRLSPolicy` request to make the attachment conditional on IAM session attributes. The condition is evaluated at query time. For ABAC, you typically attach to all IAM principals in the account by setting the principal identifier to `account-id:IAMPrincipals`; the condition then selects which principals the policy applies to at query time.

------
#### [ API ]

```
{
  "Name": "department-filter",
  "Resource": {
    "Table": {
      "DatabaseName": "hr_db",
      "Name": "employees"
    }
  },
  "Principal": {
    "DataLakePrincipalIdentifier": "111122223333:IAMPrincipals"
  },
  "Condition": {
    "Expression": "tag:department = 'HR'"
  }
}
```

------
#### [ AWS CLI ]

```
aws lakeformation attach-rls-policy \
  --name "department-filter" \
  --resource '{"Table": {"DatabaseName": "hr_db", "Name": "employees"}}' \
  --principal '{"DataLakePrincipalIdentifier": "111122223333:IAMPrincipals"}' \
  --condition '{"Expression": "tag:department = '\''HR'\''"}'
```

------

How ABAC conditions work:
+ The condition evaluates IAM session tags or principal tags at query time.
+ If the condition evaluates to true, the RLS policy attachment is active, and the filter is applied.
+ If the condition evaluates to false, the attachment is ignored for that session.
+ ABAC conditions only support IAM attributes. IAM Identity Center attributes are not supported.

**Setting up a default policy**  
A default RLS policy applies to all principals accessing the table. Think of the default as a deny-by-default baseline: create a policy whose filter expression is `FALSE` so that principals see no rows by default, and then grant explicit policies to the principals who need access. To create the default policy attachment, use `SetDefault: true` and omit the `Principal` field.

First, create the no-rows policy, then attach it as the default.

------
#### [ API ]

Create the no-rows policy:

```
{
  "Name": "no-rows-access-policy",
  "FilterExpression": "FALSE",
  "AttachmentColumns": []
}
```

Attach it as the default:

```
{
  "Name": "no-rows-access-policy",
  "Resource": {
    "Table": {
      "DatabaseName": "main_db",
      "Name": "customers"
    }
  },
  "SetDefault": true
}
```

------
#### [ AWS CLI ]

Create the no-rows policy:

```
aws lakeformation create-rls-policy \
  --name "no-rows-access-policy" \
  --filter-expression "FALSE" \
  --attachment-columns '[]'
```

Attach it as the default:

```
aws lakeformation attach-rls-policy \
  --name "no-rows-access-policy" \
  --resource '{"Table": {"DatabaseName": "main_db", "Name": "customers"}}' \
  --set-default
```

------

Default policy behavior:
+ All principals querying the table see only rows matching the default policy filter.
+ If a principal also has an explicit policy attachment, the results are additive (union). The principal sees rows matching either the default policy or their explicit policy.
+ Only one default policy can be set per table at a time.

**Detaching a policy (revoking access)**  


------
#### [ AWS Management Console ]

**To detach an RLS policy (console)**

1. Open the Lake Formation console.

1. In the navigation pane, choose **RLS policies**.

1. Select the policy.

1. On the **Attachments** tab, select the attachment you want to remove.

1. Choose **Detach**.

------
#### [ AWS CLI ]

```
aws lakeformation detach-rls-policy \
  --name "region-filter-policy" \
  --resource '{"Table": {"DatabaseName": "analytics_db", "Name": "orders"}}' \
  --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/DataAnalyst"}'
```

------

**Detaching a policy using the API or CLI**  
Use the `DetachRLSPolicy` API to remove an attachment.

------
#### [ API ]

```
{
  "Name": "region-filter-policy",
  "Resource": {
    "Table": {
      "DatabaseName": "analytics_db",
      "Name": "orders"
    }
  },
  "Principal": {
    "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/DataAnalyst"
  }
}
```

------
#### [ AWS CLI ]

```
aws lakeformation detach-rls-policy \
  --name "region-filter-policy" \
  --resource '{"Table": {"DatabaseName": "analytics_db", "Name": "orders"}}' \
  --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/DataAnalyst"}'
```

------

**Removing a default policy**  
To remove a default policy, use `RemoveDefault: true` instead of specifying a principal.

------
#### [ API ]

```
{
  "Name": "no-rows-access-policy",
  "Resource": {
    "Table": {
      "DatabaseName": "main_db",
      "Name": "customers"
    }
  },
  "RemoveDefault": true
}
```

------
#### [ AWS CLI ]

```
aws lakeformation detach-rls-policy \
  --name "no-rows-access-policy" \
  --resource '{"Table": {"DatabaseName": "main_db", "Name": "customers"}}' \
  --remove-default
```

------

**Preserving access for existing users**  


Because RLS policies are additive, attaching a policy to one principal never changes what other principals can see, and attaching an additional policy to a principal only expands the rows they can see. To narrow a principal's access, detach the policy granting the broader access.

If you detach all policies from a principal and no default policy exists on the table, RLS no longer filters that principal's queries. They see all rows their Lake Formation `SELECT` permission allows.