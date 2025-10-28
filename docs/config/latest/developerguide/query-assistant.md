# Natural language query processor for AWS Config advanced

queries

###### Note

The public preview of AWS Config Natural Language Query Processor will be discontinued by January 15, 2026.
Additionally, you can chat about your AWS resources using natural
language prompts with Amazon Q Developer. For more information, see [Chatting about your resources
with Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/chat-actions.md "../../../amazonq/latest/qdeveloper-ug/chat-actions.md").

The natural language query processor for advanced queries uses [Amazon Bedrock](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md"), a generative artificial intelligence (generative AI) technology
which allows you to enter prompts in plain English and convert them into a ready-to-use
query format. With the natural language query processor, you can query your
AWS account or across an AWS organization.

A prompt can be a question or a statement. For example, you can enter prompts such as
"Which load balancers are created after January 1, 2024?" and “List all my lambda
function that is running node js 16.”

## Considerations

The natural language query processor cannot do the following actions:

- Generate queries from languages other than English.
- Generate queries from prompts that do not relate to advanced
  queries.
- Generate queries from prompts with more than 1000 characters.
- Generate queries from follow-up corrections or from previous
  sessions.
- Explain code that has been generated.

## Query using the natural language query

processor

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Advanced queries** from the left navigation to
   query your resource configurations for a single account and Region or for
   multiple accounts and Regions.
3. On the **Advanced queries** page, choose **New
   query** to go to the
   Query
   editor.
   - (Optional) To run a query on an aggregator, create an aggregator.
     For more information, see [Creating Aggregators for AWS Config](aggregated-create.md "aggregated-create.md").
   - If you've already set up an aggregator, in the query scope, choose
     the aggregator to run an advanced query on that aggregator. When you
     select an aggregator, consider adding the AWS account ID and AWS
     Region in the query statement to view that information in the
     results.

4. In the Query editor, go to the **Natural language
   query processor** section. Enter a prompt in plain English, and
   then choose **Generate**. For examples, see [Example prompts](query-assistant.md#example-prompts "query-assistant.md#example-prompts").
5. After you generate a query, you can choose **Copy**
   (functionally equivalent to Ctrl+C) to copy the query to your clipboard, or
   choose **Populate to editor**. If populated to the editor,
   you can edit the generated query to fit your needs.
6. To save this query to a new query, choose **Save
   As**.
   - In the **Query Name** field, update the name of
     the query.
   - In the **Description** field, update the
     description of the query.
   - Enter up to 50 unique tags for this query.
   - Choose **Save**.

7. Choose **Run**. The query results display in the table
   below the query editor.
8. Choose **Export as** to export the query results in CSV
   or JSON format.

###### Note

The query results are paginated. When you export, up to 500 results
are exported.

You can also use the APIs to retrieve all the results. The results are
paginated and you can retrieve 100 results at a time.

## Example prompts

The following are prompts and the generate queries which you can use as
examples.

Example: What load balancers were created after January 1,
2024?
**Prompt**: What load balancers were created
after January 1, 2024?

**Generated query**:

```
SELECT
    resourceId,
    resourceType,
    resourceCreationTime
WHERE
    resourceType IN ('AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::LoadBalancer')
AND
    resourceCreationTime > '2024-01-01T00:00:00.0Z'
ORDER BY
    resourceCreationTime
DESC
```

Example: Which of my RDS database instances are publicly
accessible?
**Prompt**: Which of my RDS database instances
are publicly accessible?

**Generated query**:

```
SELECT
    resourceId,
    resourceType,
    configuration.publiclyAccessible
WHERE
    resourceType = 'AWS::RDS::DBInstance'
AND
    configuration.publiclyAccessible = true
```

Example: How many EC2 instances were created in last one
year?
**Prompt**: How many EC2 instances were
created in last one year?

**Generated query**:

```
SELECT
    COUNT(*)
WHERE
    resourceType = 'AWS::EC2::Instance'
AND
    resourceCreationTime
BETWEEN
    '2023-05-10T16:56:25.000Z'
AND
    '2024-05-10T16:56:25.000Z'
```

Example: How many EC2 instances do I have in each of my
AWS accounts?
**Prompt**: How many EC2 instances do I have
in each of my AWS accounts?

**Generated query**:

```
SELECT
    accountId,
    COUNT(*)
WHERE
    resourceType = 'AWS::EC2::Instance'
GROUP BY
    accountId'
```

Example: Which IAM roles have the managed policy
AdministratorAccess attached?
**Prompt**: Which IAM roles have the managed
policy AdministratorAccess attached?

**Generated query**:

```
SELECT
    resourceId,
    resourceName,
    resourceType
WHERE
    resourceType = 'AWS::IAM::Role'
AND
    configuration.attachedManagedPolicies.policyName = 'AdministratorAccess'
```

Example: EBS volumes without encryption
**Prompt**: EBS volumes without encryption

**Generated query**:

```
SELECT
    accountId
WHERE
    resourceType = 'AWS::EC2::Volume'
AND
    configuration.encrypted = false
```

Example: Get noncompliant resources
**Prompt**: Get noncompliant
resources

**Generated query**:

```
SELECT
    resourceId,
    resourceType
WHERE
    resourceType = 'AWS::Config::ResourceCompliance'
AND
    configuration.complianceType = 'NON_COMPLIANT'
```

Example: List all my lambda function that is running node js
16
**Prompt**: List all my lambda function that
is running node js 16

**Generated query**:

```
SELECT
    accountId,
    resourceName
WHERE
    resourceType = 'AWS::Lambda::Function'
AND
    configuration.runtime = 'nodejs16.x'
```

Example: What ACM certificates expire the next 30
days?
**Prompt**: What ACM certificates expire the
next 30 days?

**Generated query**:

```
SELECT
    resourceId,
    configuration.domainName,
    configuration.notAfter
WHERE
    resourceType = 'AWS::ACM::Certificate'
AND
    configuration.notAfter
BETWEEN
    '`2024-05-10 16:59:53`'
AND
    '`2024-06-10 16:59:53`’
```

###### Note

The times in the generated query depend on the time when you enter
the prompt.

## Providing feedback

You can provide overall feedback about the natural language query processor or
feedback about a specific generated query.

**Providing feedback on the natural language query
processor**

Choose the **Provide feedback** button that appears above
natural language query processor to the right. You can enter your satisfaction or
dissatisfaction and provide feedback on how AWS Config can make the natural language query
more helpful.

###### Note

Do not disclose any personal, commercially sensitive, or confidential
information.

**Providing feedback on a specific generated query**

You can provide your feedback on a generated query by choose the thumbs up or
thumbs down button that appears below the generated query.

## Region Support

The natural language query processor is supported in the following Regions.

| Region Name           | Region    | Endpoint                       | Protocol |
| --------------------- | --------- | ------------------------------ | -------- |
| US East (N. Virginia) | us-east-1 | config.us-east-1.amazonaws.com | HTTPS    |
| US West (Oregon)      | us-west-2 | config.us-west-2.amazonaws.com | HTTPS    |
