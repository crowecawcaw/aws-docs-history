

# Tags Column
<a name="table-dictionary-cur2-tag-columns"></a>

Tags column contains data about user, account, cost category and resource tags that apply to the line item. If you select this column, you need not select Resource tags and Cost category columns in your CUR 2.0.



| Column name | Description | Data type | 
| --- | --- | --- | 
| tags | A map column containing key-value pairs of all tags and their values for a given line item. The values in this column are all of data type "string".<br />Tag keys only appear in this column if they've been enabled as cost allocation tags in the Billing console. After being enabled, a particular key only appears in the map column if it has a value that applies to the specific line item.<br />The keys of this column can be queried as individual columns using the dot operator. For more information, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-data-query.html). | map <string, string> | 

## Understanding Tag Prefixes and Overlapping Tag Keys
<a name="table-dictionary-cur2-tag-prefixes"></a>

 When using cost allocation tags alongside other AWS tagging mechanisms, you may encounter situations where the same tag key (such as "department" or "aws:createdBy") appears across different tagging contexts. AWS automatically prefixes these tags to prevent conflicts and ensure accurate cost allocation. 

**Tag Prefix Types**

AWS uses the following prefixes to distinguish between different tag sources:

1. resourceTags/ - Tags applied directly to AWS resources.

1. userAttribute/ - User attributes imported from IAM Identity Center.

1. accountTag/ - Tags applied at the AWS account level.

1. costCategory/ - Tags derived from AWS Cost Categories.

1. iamPrincipal/- Tags applied to [IAM principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_additional-resources).

**Example: Overlapping Tag Keys**

Consider a scenario where multiple tagging mechanisms use the same tag keys. Here's how AWS handles them:

```
{
  "resourceTags/department": "teamA", 
  "resourceTags/appName": "app1", 
  "userAttribute/Department": "teamB", 
  "accountTag/department": "teamC", 
  "accountTag/appName": "app3", 
  "costCategory/department": "teamD"
}
```

In this example:
+ The resource is tagged with department "teamA" at the resource level
+ The user who accessed the resource belongs to the "teamB" department in IAM Identity Center
+ The AWS account has an account-level tag indicating the "teamC" department
+ A cost category rule has assigned this cost to the "teamD" department

Each tag is preserved with its unique prefix, allowing you to analyze costs from multiple perspectives simultaneously. This enables you to:
+ Track which resources belong to which teams (`resourceTags/department`)
+ Understand which users from which departments are consuming resources (`userAttribute/Department`)
+ Allocate costs based on account ownership (`accountTag/department`)
+ Apply custom business logic through cost categories (`costCategory/department`)