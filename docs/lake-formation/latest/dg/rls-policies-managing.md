

# Managing RLS policies
<a name="rls-policies-managing"></a>

This section covers how to create, update, delete, list, and manage row-level security (RLS) policies and their attachments.

**Permissions required**  


The following list shows the permissions required for each RLS policy operation.

Create  
Data lake administrators have implicit access. Non-admin principals need `CREATE_RLS_POLICY` permission on the catalog.

Update  
Data lake administrators have implicit access. Non-admin principals need `ALTER` permission on the RLS policy resource.

Delete  
Data lake administrators have implicit access. Non-admin principals need `DROP` permission on the RLS policy resource.

Attach, detach  
Data lake administrators have implicit access. Non-admin principals need `ASSOCIATE` permission on the RLS policy resource, plus `SELECT` with the grant option (or `ALL`) on the target table. For tag-based attachments, `MANAGE_TAG_POLICY` on the referenced LF-Tag keys and values is required instead of table permissions.

List policies, list attachments  
Any principal with `DESCRIBE` permission on the RLS policy resource. Data lake administrators can list all policies.

Data lake administrators have implicit permission to perform all RLS policy operations without explicit grants.

**Creating an RLS policy**  


------
#### [ AWS Management Console ]

**To create an RLS policy (console)**

1. Open the Lake Formation console.

1. In the navigation pane, choose **RLS policies**.

1. Choose **Create policy**.

1. For **Policy name**, enter a unique name. Names are case-insensitive.

1. For **Filter expression**, enter the PartiQL-subset expression (for example, `status = 'active'`).

1. Under **Attachment columns**, add each column referenced in the filter expression. Specify the column **Name** and **Type**.

1. Choose **Create**.

------
#### [ AWS CLI ]

```
aws lakeformation create-rls-policy \
  --name "active-orders-policy" \
  --filter-expression "status = 'active'" \
  --attachment-columns '[{"Name": "status", "Type": "string"}]'
```

------

**Field descriptions**  
The following table describes each field you specify when creating an RLS policy.


| Field | Required | Description | 
| --- | --- | --- | 
| Name | Yes | A unique, case-insensitive name for the policy. Maximum 255 characters. | 
| FilterExpression | Yes | The row filter expression. Maximum 2048 characters. Must use supported operators and reference only the declared attachment columns. | 
| AttachmentColumns | Yes | List of columns referenced in the filter. Each entry has a Name (string) and Type (string). | 

**Example Multi-column filter**  

```
aws lakeformation create-rls-policy \
  --name "engineering-us-policy" \
  --filter-expression "department = 'Engineering' AND country = 'US'" \
  --attachment-columns '[{"Name": "department", "Type": "string"}, {"Name": "country", "Type": "string"}]'
```

**Retrieving an RLS policy**  


```
aws lakeformation get-rls-policy \
  --name "active-orders-policy"
```

**Updating an RLS policy**  


You can update the filter expression of an existing policy. Attachment columns cannot be changed after creation. To change attachment columns, delete the policy and create a new one.

------
#### [ AWS Management Console ]

**To update an RLS policy (console)**

1. Open the Lake Formation console.

1. In the navigation pane, choose **RLS policies**.

1. Select the policy to update.

1. Choose **Edit**.

1. Modify the **Filter expression**.

1. Choose **Save**.

------
#### [ AWS CLI ]

```
aws lakeformation update-rls-policy \
  --name "active-orders-policy" \
  --filter-expression "status = 'active' OR status = 'pending'"
```

------

**Important**  
Changes to the filter expression apply to all existing attachments. It can take a few seconds for principals with this policy attached to see the updated row set.

**Deleting an RLS policy**  


Deleting a policy immediately removes all attachments and stops all filtering provided by the policy.

------
#### [ AWS Management Console ]

**To delete an RLS policy (console)**

1. Open the Lake Formation console.

1. In the navigation pane, choose **RLS policies**.

1. Select the policy to delete.

1. Choose **Delete**.

1. Confirm the deletion.

------
#### [ AWS CLI ]

```
aws lakeformation delete-rls-policy \
  --name "active-orders-policy"
```

------

**Warning**  
Deleting a policy is irreversible. Any RLS attachments made against the deleted policy become inconsequential. Therefore, if no other policies are attached and no default policy exists on the table, RLS no longer filters those principals' queries, and they see all rows their Lake Formation `SELECT` permission allows.

**Listing RLS policies and attachments**  


**Example List RLS policies**  

```
aws lakeformation list-rls-policies \
  --max-results 50
```

**Example List RLS policy attachments**  

```
aws lakeformation list-rls-policy-attachments \
  --name "active-orders-policy" \
  --max-results 50
```

**Attaching a policy to a table**  


For detailed instructions on attaching policies (including direct attachment, tag-based attachment, ABAC conditions, and default policies), see [Attaching and detaching RLS policies](rls-policies-granting.md).

**Example Quick reference: Direct attachment**  

```
aws lakeformation attach-rls-policy \
  --name "active-orders-policy" \
  --resource '{"Table": {"DatabaseName": "analytics_db", "Name": "orders"}}' \
  --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/DataAnalyst"}'
```

**Example Quick reference: Tag-based attachment**  

```
aws lakeformation attach-rls-policy \
  --name "pii-filter-policy" \
  --resource '{"LFTagPolicy": {"ResourceType": "TABLE", "Expression": [{"TagKey": "data-sensitivity", "TagValues": ["high"]}]}}' \
  --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/RestrictedUser"}'
```

**Note**  
Tag-based attachment depends on the tags assigned to a table. If those tags change or are removed, the attachment can stop applying and principals may see all rows. For the risk and how to mitigate it, see [Best practices for RLS policies](rls-policies-best-practices.md).