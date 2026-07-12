# Actions, resources, and condition keys for AWS Marketplace Commerce Analytics Service

AWS Marketplace Commerce Analytics Service (service prefix: `marketplacecommerceanalytics`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](https://s3.amazonaws.com/awsmp-loadforms/AWS-Marketplace-Commerce-Analytics-Service-Onboarding-and-Technical-Guide.pdf "https://s3.amazonaws.com/awsmp-loadforms/AWS-Marketplace-Commerce-Analytics-Service-Onboarding-and-Technical-Guide.pdf").
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/marketplacecommerceanalytics/marketplacecommerceanalytics.json "https://servicereference.us-east-1.amazonaws.com/v1/marketplacecommerceanalytics/marketplacecommerceanalytics.json") for this service.

###### Topics

- [Actions defined by AWS Marketplace Commerce Analytics Service](#list_marketplacecommerceanalytics-actions-as-permissions "#list_marketplacecommerceanalytics-actions-as-permissions")
- [Resource types defined by AWS Marketplace Commerce Analytics Service](#list_marketplacecommerceanalytics-resources-for-iam-policies "#list_marketplacecommerceanalytics-resources-for-iam-policies")
- [Condition keys for AWS Marketplace Commerce Analytics Service](#list_marketplacecommerceanalytics-policy-keys "#list_marketplacecommerceanalytics-policy-keys")

## Actions defined by AWS Marketplace Commerce Analytics Service

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                | Description                                                          | Resource types (\*required) | Condition keys | Access level |
| ---------------------- | -------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| GenerateDataSet        | Request a data set to be published to your Amazon S3 bucket.         |                             |                | Write        |
| StartSupportDataExport | Request a support data set to be published to your Amazon S3 bucket. |                             |                | Write        |

## Resource types defined by AWS Marketplace Commerce Analytics Service

AWS Marketplace Commerce Analytics Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Marketplace Commerce Analytics Service

AWS Marketplace Commerce Analytics Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
