# Using an OpenSearch Ingestion pipeline with

Atlassian Services

You can use the Atlassian Jira and Confluence source plugins to ingest data from Atlassian
services into your OpenSearch Ingestion pipeline. These integrations enable you to create a
unified searchable knowledge base by synchronizing complete Jira projects and Confluence
spaces, while maintaining real-time relevance through continuous monitoring and automatic
synchronization of updates.

Integrating with Jira
Transform your Jira experience with powerful contextual search capabilities by
integrating your Jira content into OpenSearch. The Data Prepper [Atlassian Jira](https://www.atlassian.com/software/jira "https://www.atlassian.com/software/jira") source
plugin enables you to create a unified searchable knowledge base by
synchronizing complete Jira projects, while maintaining real-time relevance
through continuous monitoring and automatic synchronization of updates. This
integration allows for data synchronization with flexible filtering options for
specific projects, issue types, and status, ensuring that only the information
you need is imported.

To ensure secure and reliable connectivity, the plugin supports multiple
authentication methods, including basic API key authentication and OAuth2
authentication, with the added security of managing credentials using a secret
stored in AWS Secrets Manager. It also features automatic token renewal for uninterrupted
access, ensuring continuous operation. Built on Atlassian's [API version 2](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#version%22%3Eapi-version-2 "https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#version%22%3Eapi-version-2"), this integration empowers teams to unlock valuable
insights from their Jira data through OpenSearch's advanced search
capabilities.

Integrating with Confluence
Enhance your team's knowledge management and collaboration capabilities by
integrating [Atlassian
Confluence](https://www.atlassian.com/software/confluence "https://www.atlassian.com/software/confluence") content into OpenSearch through Data Prepper's
Confluence source plugin. This integration enables you to create a centralized,
searchable repository of collective knowledge, improving information discovery
and team productivity. By synchronizing Confluence content and continuously
monitoring for updates, the plugin ensures that your OpenSearch index remains
up-to-date and comprehensive.

The integration offers flexible filtering options, allowing you to selectively
import content from specific spaces or page types, tailoring the synchronized
content to your organization's needs. The plugin supports both basic API key and
OAuth2 authentication methods, with the option of securely managing credentials
through AWS Secrets Manager. The plugin's automatic token renewal feature ensures
uninterrupted access and seamless operation. Built on Atlassian's Confluence
[API](https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth "https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#auth"), this integration enables teams to leverage OpenSearch's
advanced search capabilities across their Confluence content, enhancing
information accessibility and utilization within the organization.

###### Topics

- [Prerequisites](#atlassian-prerequisites "#atlassian-prerequisites")
- [Configure a pipeline role](#atlassian-pipeline-role "#atlassian-pipeline-role")
- [Jira connector pipeline configuration](#jira-connector-pipeline "#jira-connector-pipeline")
- [Confluence connector pipeline
  configuration](#confluence-connector-pipeline "#confluence-connector-pipeline")
- [Data consistency](#data-consistency "#data-consistency")
- [Limitations](#limitations "#limitations")
- [Metrics in CloudWatch for Atlassian connectors](#metrics "#metrics")
- [Connecting an
  Amazon OpenSearch Ingestion pipeline to Atlassian Jira or Confluence using OAuth 2.0](configure-client-atlassian-OAuth2-setup.md "configure-client-atlassian-OAuth2-setup.md")

## Prerequisites

Before you create your OpenSearch Ingestion pipeline, complete the following steps:

1. Prepare credentials for your Jira site by choosing one of the following
   options. OpenSearch Ingestion requires only `ReadOnly` authorization to
   the content.
   1. **Option 1: API key** – Log in to
      your Atlassian account and use the information in the following topic to
      generate your API key:
      - [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/ "https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/")

   2. **Option 2: OAuth2** – Log in to
      your Atlassian account and use the information in [Connecting an
      Amazon OpenSearch Ingestion pipeline to Atlassian Jira or Confluence using OAuth 2.0](configure-client-atlassian-OAuth2-setup.md "configure-client-atlassian-OAuth2-setup.md").

2. [Create a secret in
   AWS Secrets Manager](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") to store the credentials created in the previous step.
   Make the following choices as you follow the procedure:
   - For **Secret type**, choose **Other type of
     secret**.
   - For **Key/value pairs**, create the following pairs,
     depending on your selected authorization type:

API key

```
{
   "username": `user-name-usualy-email-id`,
   "password": `api-key`
}
```

OAuth 2.0

```
{
   "clientId": `client-id`
   "clientSecret": `client-secret`
   "accessKey": `access-key`
   "refreshKey": `refresh-key`
}
```

After you've created the secret, copy the Amazon Resource Name (ARN) of the
secret. You will include it in the pipeline role permissions policy.

## Configure a pipeline role

The role passed in the pipeline must have the following policy attached to read and
write to the secret created in the prerequisites section.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SecretReadWrite",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetResourcePolicy",
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret",
 "secretsmanager:PutSecretValue",
 "secretsmanager:ListSecretVersionIds"
 ],
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`secret-name`-`random-6-characters`"
 }
 ]
}`

```

The role should also have a policy attached to access and write to your chosen sink.
For example, if you choose OpenSearch as your sink, the policy looks similar to the
following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OpenSearchWritePolicy",
 "Effect": "Allow",
 "Action": "aoss:*",
 "Resource": "arn:aws:aoss:`us-east-1`:`111122223333`:collection/`collection-id`"
 }
 ]
}`

```

## Jira connector pipeline configuration

You can use a preconfigured Atlassian Jira blueprint to create this pipeline. For more
information, see [Working with blueprints](pipeline-blueprint.md "pipeline-blueprint.md").

Replace the `placeholder values` with your own
information.

```
version: "2"
extension:
  aws:
    secrets:
      jira-account-credentials:
        secret_id: "`secret-arn`"
        region: "`secret-region`"
        sts_role_arn: "`arn:aws:iam::123456789012:role/Example-Role`"
atlassian-jira-pipeline:
  source:
    jira:
      # We only support one host url for now
      hosts: ["`jira-host-url`"]
      acknowledgments: true
      authentication:
        # Provide one of the authentication method to use. Supported methods are 'basic' and 'oauth2'.
        # For basic authentication, password is the API key that you generate using your jira account
        basic:
          username: ${{aws_secrets:jira-account-credentials:username}}
          password: ${{aws_secrets:jira-account-credentials:password}}
        # For OAuth2 based authentication, we require the following 4 key values stored in the secret
        # Follow atlassian instructions at the below link to generate these keys.
        # https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/
        # If you are using OAuth2 authentication, we also require, write permission to your AWS secret to
        # be able to write the renewed tokens back into the secret.
        # oauth2:
          # client_id: ${{aws_secrets:jira-account-credentials:clientId}}
          # client_secret: ${{aws_secrets:jira-account-credentials:clientSecret}}
          # access_token: ${{aws_secrets:jira-account-credentials:accessToken}}
          # refresh_token: ${{aws_secrets:jira-account-credentials:refreshToken}}
      filter:
        project:
          key:
            include:
              # This is not project name.
              # It is an alphanumeric project key that you can find under project details in Jira.
              - "`project-key`"
              - "`project-key`"
            # exclude:
              # - "`project-key`"
              # - "`project-key`"
        issue_type:
          include:
            - "`issue-type`"
            # - "Story"
            # - "Bug"
            # - "Task"
         # exclude:
             # - "Epic"
        status:
          include:
            - "`ticket-status`"
            # - "To Do"
            # - "In Progress"
            # - "Done"
         # exclude:
           # - "Backlog"

  sink:
    - opensearch:
        # Provide an Amazon OpenSearch Service domain endpoint
        hosts: [ "`https://search-mydomain-1a2a3a4a5a6a7a8a9a0a9a8a7a.us-east-1.es.amazonaws.com`" ]
        index: "index_${getMetadata(\"project\")}"
        # Ensure adding unique document id which is the unique ticket id in this case
        document_id: '${/id}'
        aws:
          # Provide a Role ARN with access to the domain. This role should have a trust relationship with osis-pipelines.amazonaws.com
          sts_role_arn: "`arn:aws:iam::123456789012:role/Example-Role`"
          # Provide the region of the domain.
          region: "`us-east-1`"
          # Enable the 'serverless' flag if the sink is an Amazon OpenSearch Serverless collection
          serverless: false
          # serverless_options:
            # Specify a name here to create or update network policy for the serverless collection
            # network_policy_name: "network-policy-name"
        # Enable the 'distribution_version' setting if the Amazon OpenSearch Service domain is of version Elasticsearch 6.x
        # distribution_version: "es6"
        # Enable and switch the 'enable_request_compression' flag if the default compression setting is changed in the domain.
        # See Compressing HTTP requests in Amazon OpenSearch Service
        # enable_request_compression: true/false
        # Optional: Enable the S3 DLQ to capture any failed requests in an S3 bucket. Delete this entire block if you don't want a DLQ.
        dlq:
          s3:
            # Provide an S3 bucket
            bucket: "`your-dlq-bucket-name`"
            # Provide a key path prefix for the failed requests
            # key_path_prefix: "kinesis-pipeline/logs/dlq"
            # Provide the region of the bucket.
            region: "`us-east-1`"
            # Provide a Role ARN with access to the bucket. This role should have a trust relationship with osis-pipelines.amazonaws.com
            sts_role_arn: "`arn:aws:iam::123456789012:role/Example-Role`"
```

Key to attributes in the Jira source:

1. **hosts**: Your Jira cloud or on-premises URL.
   Generally, it looks like
   `https://`your-domain-name`.atlassian.net/`.
2. **acknowledgments**: To guarantee the delivery of
   data all the way to the sink.
3. **authentication**: Describes how you want the
   pipeline to access your Jira instance. Choose `Basic` or
   `OAuth2` and specify the corresponding key attributes referencing
   the keys in your AWS secret..
4. **filter**: This section helps you select which
   portion of your Jira data to extract and synchronize.
   1. **project**: List the project keys that
      you want to sync in the `include` section. Otherwise, list
      the projects that you want to exclude under the `exclude`
      section. Provide only one of the include or exclude options at any given
      time.
   2. **issue_type**: Specific issue types that
      you want to sync. Follow the similar `include` or
      `exclude` pattern that suits your needs. Note that
      attachments will appear as anchor links to the original attachment, but
      the attachment content won't be extracted.
   3. **status**: Specific status filter you
      want to apply for the data extraction query. If you specify
      `include`, only tickets with those statuses will be
      synced. If you specify `exclude`, then all tickets except
      those with the listed excluded statuses will be synced.

## Confluence connector pipeline

configuration

You can use a preconfigured Atlassian Confluence blueprint to create this pipeline.
For more information, see [Working with blueprints](pipeline-blueprint.md "pipeline-blueprint.md").

```
version: "2"
extension:
  aws:
    secrets:
      confluence-account-credentials:
        secret_id: "`secret-arn`"
        region: "`secret-region`"
        sts_role_arn: "`arn:aws:iam::123456789012:role/Example-Role`"
atlassian-confluence-pipeline:
  source:
    confluence:
      # We currently support only one host URL.
      hosts: ["`confluence-host-url`"]
      acknowledgments: true
      authentication:
        # Provide one of the authentication method to use. Supported methods are 'basic' and 'oauth2'.
        # For basic authentication, password is the API key that you generate using your Confluence account
        basic:
          username: ${{aws_secrets:confluence-account-credentials:confluenceId}}
          password: ${{aws_secrets:confluence-account-credentials:confluenceCredential}}
        # For OAuth2 based authentication, we require the following 4 key values stored in the secret
        # Follow atlassian instructions at the following link to generate these keys:
        # https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/
        # If you are using OAuth2 authentication, we also require write permission to your AWS secret to
        # be able to write the renewed tokens back into the secret.
        # oauth2:
          # client_id: ${{aws_secrets:confluence-account-credentials:clientId}}
          # client_secret: ${{aws_secrets:confluence-account-credentials:clientSecret}}
          # access_token: ${{aws_secrets:confluence-account-credentials:accessToken}}
          # refresh_token: ${{aws_secrets:confluence-account-credentials:refreshToken}}
      filter:
        space:
          key:
            include:
              # This is not space name.
              # It is a space key that you can find under space details in Confluence.
              - "`space key`"
              - "`space key`"
           # exclude:
             #  - "`space key`"
             #  - "`space key`"
        page_type:
          include:
            - "`content type`"
            # - "page"
            # - "blogpost"
            # - "comment"
         # exclude:
            # - "attachment"

  sink:
    - opensearch:
        # Provide an Amazon OpenSearch Service domain endpoint
        hosts: [ "`https://search-mydomain-1a2a3a4a5a6a7a8a9a0a9a8a7a.us-east-1.es.amazonaws.com`" ]
         index: "index_${getMetadata(\"space\")}"
        # Ensure adding unique document id which is the unique ticket ID in this case.
        document_id: '${/id}'
        aws:
          # Provide the Amazon Resource Name (ARN) for a role with access to the domain. This role should have a trust relationship with osis-pipelines.amazonaws.com.
          sts_role_arn: "`arn:aws:iam::123456789012:role/Example-Role`"
          # Provide the Region of the domain.
          region: "`us-east-1`"
          # Enable the 'serverless' flag if the sink is an Amazon OpenSearch Serverless collection
          serverless: false
          # serverless_options:
            # Specify a name here to create or update network policy for the serverless collection.
            # network_policy_name: "network-policy-name"
        # Enable the 'distribution_version' setting if the Amazon OpenSearch Service domain is of version Elasticsearch 6.x
        # distribution_version: "es6"
        # Enable and switch the 'enable_request_compression' flag if the default compression setting is changed in the domain.
        # For more information, see Compressing HTTP requests in Amazon OpenSearch Service.
        # enable_request_compression: true/false
        # Optional: Enable the S3 DLQ to capture any failed requests in an S3 bucket. Delete this entire block if you don't want a DLQ.
        dlq:
          s3:
            # Provide an S3 bucket
            bucket: "`your-dlq-bucket-name`"
            # Provide a key path prefix for the failed requests
            # key_path_prefix: "kinesis-pipeline/logs/dlq"
            # Provide the Rregion of the bucket.
            region: "`us-east-1`"
            # Provide the Amazon Resource Name (ARN) for a role with access to the bucket. This role should have a trust relationship with osis-pipelines.amazonaws.com
            sts_role_arn: "`arn:aws:iam::123456789012:role/Example-Role`"
```

Key attributes in the Confluence source:

1. **hosts**: Your Confluence cloud or on-premises
   URL. Generally, it looks like
   `https://`your-domain-name`.atlassian.net/`
2. **acknowledgments**: To guarantee the delivery of
   data all the way to the sink.
3. **authentication**: Describes how you want the
   pipeline to access your Confluence instance. Choose `Basic` or
   `OAuth2` and specify the corresponding key attributes referencing
   the keys in your AWS secret.
4. **filter**: This section helps you select which
   portion of your Confluence data to extract and synchronize.
   1. **space**: List the space keys that you
      want to sync in the `include` section. Otherwise, list the
      spaces that you want to exclude under the `exclude` section.
      Provide only one of the include or exclude options at any given
      time.
   2. **page_type**: Specific page types (like
      page, blogpost, or attachments) that you want to sync. Follow the
      similar `include` or `exclude` pattern that suits
      your needs. Note that attachments will appear as anchor links to the
      original attachment, but the attachment content won't be
      extracted.

## Data consistency

Based on the filters specified in the pipeline YAML, selected projects (or spaces)
will be extracted once and fully synced to the target sink. Then continuous change
monitoring will capture changes as they occur and update the data in the sink. One
exception is that the change monitoring syncs only `create` and
`update` actions, not `delete` actions.

## Limitations

- User delete actions won't be synced. Data once recorded in the sink will
  remain in the sink. Updates will overwrite the existing content with new changes
  if the ID mapping is specified in the sink settings.
- On-premises instances using older versions of Atlassian software that don't
  support the following APIs are not compatible with this source:
  - Jira Search API version 3
    - `rest/api/3/search`
    - `rest/api/3/issue`

  - Confluence
    - `wiki/rest/api/content/search`
    - `wiki/rest/api/content`
    - `wiki/rest/api/settings/systemInfo`

## Metrics in CloudWatch for Atlassian connectors

**Type: Jira connector metrics**

| Source                            | Metric  | Metric Type                                                                                     |
| --------------------------------- | ------- | ----------------------------------------------------------------------------------------------- | -------------------------------------- |
| acknowledgementSetSuccesses.count | Counter | If acknowledgments are enabled, this metric provides the number of tickets successfully synced. |
| acknowledgementSetFailures.count  | Counter | If acknowledgments are enabled, this metric provides the number of tickets that failed to sync. |
| crawlingTime.avg                  | Timer   | The time it took to crawl through all the new changes.                                          |
| ticketFetchLatency.avg            | Timer   | The ticket fetch API latency average.                                                           |
| ticketFetchLatency.max            | Timer   | The ticket fetch API latency maximum.                                                           |
| ticketsRequested.count            | Counter | Number of ticket fetch requests made.                                                           |
| ticketRequestedFailed.count       | Counter | Number of ticket fetch requests failed.                                                         |
| ticketRequestedSuccess.count      | Counter | Number of ticket fetch requests succeeded.                                                      |
| searchCallLatency.avg             | Timer   | Search API call latency average.                                                                |
| searchCallLatency.max             | Timer   | Search API call latency maximum.                                                                |
| searchResultsFound.count          | Counter | Number of items found in a given search call.                                                   |
| searchRequestFailed.count         | Counter | Search API call failures count.                                                                 |
| authFailures.count                | Counter | Authentication failure count.                                                                   | **Type: Confluence connector metrics** |
| Source                            | Metric  | Metric Type                                                                                     |
| ---                               | ---     | ---                                                                                             |
| acknowledgementSetSuccesses.count | Counter | If acknowledgments are enabled, this metric provides the number of pages successfully synced.   |
| acknowledgementSetFailures.count  | Counter | If acknowledgments are enabled, this metric provides the number of pages that failed to sync.   |
| crawlingTime.avg                  | Timer   | The time it took to crawl through all the new changes.                                          |
| pageFetchLatency.avg              | Timer   | Content fetching API latency (average).                                                         |
| pageFetchLatency.max              | Timer   | Content fetching API latency (maximum).                                                         |
| pagesRequested.count              | Counter | Number of invocations of content fetching API.                                                  |
| pageRequestFailed.count           | Counter | Number of failed requests of content fetching API.                                              |
| pageRequestedSuccess.count        | Counter | Number of successful requests of content fetching API.                                          |
| searchCallLatency.avg             | Timer   | Search API call latency average.                                                                |
| searchCallLatency.max             | Timer   | Search API call latency max.                                                                    |
| searchResultsFound.count          | Counter | Number of items found in a given search call.                                                   |
| searchRequestsFailed.count        | Counter | Search API call failures count.                                                                 |
| authFailures.count                | Counter | Authentication failure count.                                                                   |
