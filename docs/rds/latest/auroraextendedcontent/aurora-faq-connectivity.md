

# Connectivity
<a name="aurora-faq-connectivity"></a>

**Topics**
+ [When should I use the Data API vs. database drivers?](#aurora-faq-when-should-i-use-the-data-api-vs-database-drivers)
+ [How is the Data API secured?](#aurora-faq-how-is-the-data-api-secured)
+ [How is the Data API priced?](#aurora-faq-how-is-the-data-api-priced)

## When should I use the Data API vs. database drivers?
<a name="aurora-faq-when-should-i-use-the-data-api-vs-database-drivers"></a>

You should use the [Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) for new modern applications, particularly those built with [AWS Lambda](https://aws.amazon.com/lambda/) that need to access Aurora in a request/response model. The Data API is an HTTP-based API that eliminates the need to deploy database drivers, manage connection pools, or configure VPC networking.

Database drivers should be used when an existing application is highly coupled with database drivers, when there are long-running queries, or when the developer wants to take advantage of database features such as temporary tables or use session variables.

What benefits does Data API provide?

The [Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) simplifies and accelerates modern application development by eliminating database driver deployment, client-side connection pool management, and complex VPC networking between application and database. It automatically pools and shares database connections for better scalability and supports Aurora Global Database writer instances. See the [Data API documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) for Region and version availability.

## How is the Data API secured?
<a name="aurora-faq-how-is-the-data-api-secured"></a>

Users can invoke Data API operations only if they are authorized to do so. Administrators can give a user permission to use the Data API by attaching an [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) policy that defines their privileges. When you call the Data API, you can pass credentials for the Aurora DB cluster by using a secret in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).

## How is the Data API priced?
<a name="aurora-faq-how-is-the-data-api-priced"></a>

The Data API includes a free tier of 1 million requests per month (aggregated across all Regions) for the first year. After that, pricing is based on API request volume — see the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing/). Data API uses [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) for credentials (separate charges apply) and logs activity via [AWS CloudTrail](https://aws.amazon.com/pm/cloudtrail/) data events.