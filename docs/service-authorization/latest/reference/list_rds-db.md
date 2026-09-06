

# Actions, resources, and condition keys for Amazon RDS IAM Authentication
<a name="list_rds-db"></a>

Amazon RDS IAM Authentication (service prefix: `rds-db`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/rds-db/rds-db.json) for this service.

**Topics**
+ [Actions defined by Amazon RDS IAM Authentication](#list_rds-db-actions-as-permissions)
+ [Resource types defined by Amazon RDS IAM Authentication](#list_rds-db-resources-for-iam-policies)
+ [Condition keys for Amazon RDS IAM Authentication](#list_rds-db-policy-keys)

## Actions defined by Amazon RDS IAM Authentication
<a name="list_rds-db-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [connect](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.IAMPolicy.html)  **
  - **Description:** Allows IAM role or user to connect to RDS database
  - **Resource types (\*required):** [db-user\*](#list_rds-db-resource-db-user)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write



## Resource types defined by Amazon RDS IAM Authentication
<a name="list_rds-db-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [db-user](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.html)  | arn:${Partition}:rds-db:${Region}:${Account}:dbuser:${DbiResourceId}/${DbUserName} |   | 

## Condition keys for Amazon RDS IAM Authentication
<a name="list_rds-db-policy-keys"></a>

Amazon RDS IAM Authentication has no service-specific condition keys that can be used in the `Condition` element of policy statements.