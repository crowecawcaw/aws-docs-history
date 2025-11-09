# Monitoring audit logs in Amazon OpenSearch Service

If your Amazon OpenSearch Service domain uses fine-grained access control, you can enable audit logs for your
data. Audit logs are highly customizable and let you track user activity on your OpenSearch
clusters, including authentication success and failures, requests to OpenSearch, index
changes, and incoming search queries. The default configuration tracks a popular set of user
actions, but we recommend tailoring the settings to your exact needs.

Just like [OpenSearch application logs and
slow logs](createdomain-configure-slow-logs.md "createdomain-configure-slow-logs.md"), OpenSearch Service publishes audit logs to CloudWatch Logs. If enabled, [standard CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") applies.

###### Note

To enable audit logs, your user role must be mapped to the `security_manager`
role, which gives you access to the OpenSearch `plugins/_security` REST API. To
learn more, see [Modifying the master user](fgac.md#fgac-forget "fgac.md#fgac-forget").

###### Topics

- [Limitations](#audit-logs-limitations "#audit-logs-limitations")
- [Enabling audit logs](#audit-log-enabling "#audit-log-enabling")
- [Enable audit logging using the AWS CLI](#audit-log-enabling-cli "#audit-log-enabling-cli")
- [Enable audit logging using the configuration
  API](#audit-log-enabling-api "#audit-log-enabling-api")
- [Audit log layers and categories](#audit-log-layers "#audit-log-layers")
- [Audit log settings](#audit-log-settings "#audit-log-settings")
- [Audit log example](#audit-log-example "#audit-log-example")
- [Configuring audit logs using the REST API](#audit-log-rest-api "#audit-log-rest-api")

## Limitations

Audit logs have the following limitations:

- Audit logs don't include cross-cluster search requests that were rejected by the
  destination's domain access policy.
- The maximum size of each audit log message is 10,000 characters. The audit log message
  is truncated if it exceeds this limit.

## Enabling audit logs

Enabling audit logs is a two-step process. First, you configure your domain to publish
audit logs to CloudWatch Logs. Then, you enable audit logs in OpenSearch Dashboards and configure them to
meet your needs.

###### Important

If you encounter an error while following these steps, see [Can't enable audit logs](handling-errors.md#troubleshooting-audit-logs-error "handling-errors.md#troubleshooting-audit-logs-error") for troubleshooting information.

### Step 1: Enable audit logs and configure an access

policy

These steps describe how to enable audit logs using the console. You can also [enable them using the AWS CLI](#audit-log-enabling-cli "#audit-log-enabling-cli"), or the [OpenSearch Service API](#audit-log-enabling-api "#audit-log-enabling-api").

###### To enable audit logs for an OpenSearch Service domain (console)

1. Choose the domain to open its configuration, then go to the
   **Logs** tab.
2. Select **Audit logs** and then **Enable**.
3. Create a CloudWatch log group, or choose an existing one.
4. Choose an access policy that contains the appropriate permissions, or create a
   policy using the JSON that the console provides:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "es.amazonaws.com"
 },
 "Action": [
 "logs:PutLogEvents",
 "logs:CreateLogStream"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/opensearch/domains/domain-name/*"
 }
 ]
}`

```

We recommend that you add the `aws:SourceAccount` and
`aws:SourceArn` condition keys to the policy to protect yourself against
the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"). The
source account is the owner of the domain and the source ARN is the ARN of the domain.
Your domain must be on service software R20211203 or later in order to add these
condition keys.

For example, you could add the following condition block to the policy:

```
"Condition": {
    "StringEquals": {
        "aws:SourceAccount": "`account-id`"
    },
    "ArnLike": {
        "aws:SourceArn": "arn:aws:es:`region`:`account-id`:domain/`domain-name`"
    }
}
```

5. Choose **Enable**.

### Step 2: Turn on audit logs in

OpenSearch Dashboards

After you enable audit logs in the OpenSearch Service console, you _must_ also
enable them in OpenSearch Dashboards and configure them to match your needs.

1. Open OpenSearch Dashboards and choose **Security** from the left side
   menu.
2. Choose **Audit logs**.
3. Choose **Enable audit logging**.

The Dashboards UI offers full control of audit log settings under **General
settings** and **Compliance settings**. For a description of all
configuration options, see [Audit log
settings](#audit-log-settings "#audit-log-settings").

## Enable audit logging using the AWS CLI

The following AWS CLI command enables audit logs on an existing domain:

```
aws opensearch update-domain-config --domain-name `my-domain` --log-publishing-options "AUDIT_LOGS={CloudWatchLogsLogGroupArn=`arn:aws:logs:us-east-1:123456789012:log-group:my-log-group`,Enabled=true}"
```

You can also enable audit logs when you create a domain. For detailed information, see the
[AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

## Enable audit logging using the configuration

API

The following request to the configuration API enables audit logs on an existing
domain:

```
POST https://es.us-east-1.amazonaws.com/2021-01-01/opensearch/domain/`my-domain`/config
{
  "LogPublishingOptions": {
    "AUDIT_LOGS": {
      "CloudWatchLogsLogGroupArn":"arn:aws:logs:`us-east-1`:`123456789012`:log-group1:sample-domain",
      "Enabled":true
    }
  }
}
```

For more information, see the [Amazon OpenSearch
Service API reference](../APIReference/API_LogPublishingOption.md "../APIReference/API_LogPublishingOption.md").

## Audit log layers and categories

Cluster communication occurs over two separate _layers_:
the REST layer and the transport layer.

- The REST layer covers communication with HTTP clients such as curl, Logstash,
  OpenSearch Dashboards, the Java high-level REST client, the Python [Requests](https://2.python-requests.org/ "https://2.python-requests.org/") library—all HTTP requests
  that arrive at the cluster.
- The transport layer covers communication between nodes. For example, after a search
  request arrives at the cluster (over the REST layer), the coordinating node serving the
  request sends the query to other nodes, receives their responses, gathers the necessary
  documents, and collates them into the final response. Operations such as shard allocation
  and rebalancing also occur over the transport layer.

You can enable or disable audit logs for entire layers, as well as individual audit
categories for a layer. The following table contains a summary of audit categories and the
layers for which they are available.

| Category                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                        | Available for REST | Available for transport |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------- |
| FAILED_LOGIN                      | A request contained invalid credentials, and authentication failed.                                                                                                                                                                                                                                                                                                                                                                | Yes                | Yes                     |
| MISSING_PRIVILEGES                | A user did not have the privileges to make the request.                                                                                                                                                                                                                                                                                                                                                                            | Yes                | Yes                     |
| GRANTED_PRIVILEGES                | A user had the privileges to make the request.                                                                                                                                                                                                                                                                                                                                                                                     | Yes                | Yes                     |
| OPENSEARCH_SECURITY_INDEX_ATTEMPT | A request tried to modify the `.opendistro_security` index.                                                                                                                                                                                                                                                                                                                                                                        | No                 | Yes                     |
| AUTHENTICATED                     | A request contained valid credentials, and authentication succeeded.                                                                                                                                                                                                                                                                                                                                                               | Yes                | Yes                     |
| INDEX_EVENT                       | A request performed an administrative operation on an index, such as creating<br>one, setting an alias, or performing a force merge. The full list of<br>`indices:admin/` actions that this category includes are available in the<br>[OpenSearch documentation](https://docs.opensearch.org/latest/security-plugin/access-control/permissions/ "https://docs.opensearch.org/latest/security-plugin/access-control/permissions/"). | No                 | Yes                     |

In addition to these standard categories, fine-grained access control offers several
additional categories designed to meet data compliance requirements.

| Category                         | Description                                                               |
| -------------------------------- | ------------------------------------------------------------------------- |
| COMPLIANCE_DOC_READ              | A request performed a read event on a document in an index.               |
| COMPLIANCE_DOC_WRITE             | A request performed a write event on a document in an index.              |
| COMPLIANCE_INTERNAL_CONFIG_READ  | A request performed a read event on the `.opendistro_security`<br>index.  |
| COMPLIANCE_INTERNAL_CONFIG_WRITE | A request performed a write event on the `.opendistro_security`<br>index. |

You can have any combination of categories and message attributes. For example, if you
send a REST request to index a document, you might see the following lines in the audit
logs:

- AUTHENTICATED on REST layer (authentication)
- GRANTED_PRIVILEGE on transport layer (authorization)
- COMPLIANCE_DOC_WRITE (document written to an index)

## Audit log settings

Audit logs have numerous configuration options.

### General settings

General settings let you enable or disable individual categories or entire layers. We
highly recommend leaving GRANTED_PRIVILEGES and AUTHENTICATED as excluded categories.
Otherwise, these categories are logged for every valid request to the cluster.

| Name                          | Backend setting               | Description                                                                                                                                                   |
| ----------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REST layer                    | enable_rest                   | Enable or disable events that occur on the REST layer.                                                                                                        |
| REST disabled categories      | disabled_rest_categories      | Specify audit categories to ignore on the REST layer. Modifying these<br>categories can dramatically increase the size of the audit logs.                     |
| Transport layer               | enable_transport              | Enable or disable events that happen on the transport layer.                                                                                                  |
| Transport disabled categories | disabled_transport_categories | Specify audit categories which must be ignored on the transport layer.<br>Modifying these categories can dramatically increase the size of the audit<br>logs. |

Attribute settings let you customize the amount of detail in each log line.

| Name            | Backend setting       | Description                                                                                                                               |
| --------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Bulk requests   | resolve_bulk_requests | Enabling this setting generates a log for each document in a bulk request,<br>which can dramatically increase the size of the audit logs. |
| Request body    | log_request_body      | Include the request body of the requests.                                                                                                 |
| Resolve indices | resolve_indices       | Resolve aliases to indices.                                                                                                               |

Use ignore settings to exclude a set of users or API paths:

| Name             | Backend setting | Description                                        |
| ---------------- | --------------- | -------------------------------------------------- |
| Ignored users    | ignore_users    | Specify users that you want to exclude.            |
| Ignored requests | ignore_requests | Specify request patterns that you want to exclude. |

### Compliance settings

Compliance settings let you tune for index, document, or field-level access.

| Name               | Backend setting   | Description                           |
| ------------------ | ----------------- | ------------------------------------- |
| Compliance logging | enable_compliance | Enable or disable compliance logging. |

You can specify the following settings for read and write event logging.

| Name                    | Backend setting | Description                                                                 |
| ----------------------- | --------------- | --------------------------------------------------------------------------- |
| Internal config logging | internal_config | Enable or disable logging of events on the `.opendistro_security`<br>index. |

You can specify the following settings for read events.

| Name           | Backend setting     | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Read metadata  | read_metadata_only  | Include only metadata for read events. Do not include any document<br>fields.                                                                                                                                                                                                                                                                                                                            |
| Ignored users  | read_ignore_users   | Do not include certain users for read events.                                                                                                                                                                                                                                                                                                                                                            |
| Watched fields | read_watched_fields | Specify the indices and fields to watch for read events. Adding watched fields<br>generates one log per document access, which can dramatically increase the size of<br>the audit logs. Watched fields support index patterns and field patterns:<br>`<br>{<br>"index-name-pattern": [<br>"field-name-pattern"<br>],<br>"logs*": [<br>"message"<br>],<br>"twitter": [<br>"id",<br>"user*"<br>]<br>}<br>` |

You can specify the following settings for write events.

| Name           | Backend setting       | Description                                                                                                                                                                                    |
| -------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Write metadata | write_metadata_only   | Include only metadata for write events. Do not include any document<br>fields.                                                                                                                 |
| Log diffs      | write_log_diffs       | If write_metadata_only is false, include only the differences between write<br>events.                                                                                                         |
| Ignored users  | write_ignore_users    | Do not include certain users for write events.                                                                                                                                                 |
| Watch indices  | write_watched_indices | Specify the indices or index patters to watch for write events. Adding watched<br>fields generates one log per document access, which can dramatically increase the<br>size of the audit logs. |

## Audit log example

This section includes an example configuration, search request, and the resulting audit
log for all read and write events of an index.

### Step 1: Configure audit logs

After you enable the publishing of audit logs to a CloudWatch Logs group, navigate to the
OpenSearch Dashboards audit logging page and choose **Enable audit
logging**.

1. In **General Settings**, choose **Configure** and
   make sure that the **REST layer** is enabled.
2. In **Compliance Settings**, choose
   **Configure**.
3. Under **Write**, in **Watched Fields**, add
   `accounts` for all write events to this index.
4. Under **Read**, in **Watched Fields**, add
   `ssn` and `id-` fields of the `accounts`
   index:

```
{
  "accounts-": [
    "ssn",
    "id-"
  ]
}
```

### Step 2: Perform read and write events

1. Navigate to OpenSearch Dashboards, choose **Dev Tools**, and index a
   sample document:

```
PUT accounts/_doc/0
{
  "ssn": "123",
  "id-": "456"
}
```

2. To test a read event, send the following request:

```
GET accounts/_search
{
  "query": {
    "match_all": {}
  }
}
```

### Step 3: Observe the logs

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Log groups**.
3. Choose the log group that you specified while enabling audit logs. Within the log
   group, OpenSearch Service creates a log stream for each node in your domain.
4. In **Log streams**, choose **Search all**.
5. For the read and write events, see the corresponding logs. You can expect a delay of
   5 seconds before the log appears.

**Sample write audit log**

```
{
  "audit_compliance_operation": "CREATE",
  "audit_cluster_name": "824471164578:audit-test",
  "audit_node_name": "be217225a0b77c2bd76147d3ed3ff83c",
  "audit_category": "COMPLIANCE_DOC_WRITE",
  "audit_request_origin": "REST",
  "audit_compliance_doc_version": 1,
  "audit_node_id": "3xNJhm4XS_yTzEgDWcGRjA",
  "@timestamp": "2020-08-23T05:28:02.285+00:00",
  "audit_format_version": 4,
  "audit_request_remote_address": "3.236.145.227",
  "audit_trace_doc_id": "lxnJGXQBqZSlDB91r_uZ",
  "audit_request_effective_user": "admin",
  "audit_trace_shard_id": 8,
  "audit_trace_indices": [
    "accounts"
  ],
  "audit_trace_resolved_indices": [
    "accounts"
  ]
}
```

**Sample read audit log**

```
{
  "audit_cluster_name": "824471164578:audit-docs",
  "audit_node_name": "806f6050cb45437e2401b07534a1452f",
  "audit_category": "COMPLIANCE_DOC_READ",
  "audit_request_origin": "REST",
  "audit_node_id": "saSevm9ASte0-pjAtYi2UA",
  "@timestamp": "2020-08-31T17:57:05.015+00:00",
  "audit_format_version": 4,
  "audit_request_remote_address": "54.240.197.228",
  "audit_trace_doc_id": "config:7.7.0",
  "audit_request_effective_user": "admin",
  "audit_trace_shard_id": 0,
  "audit_trace_indices": [
    "accounts"
  ],
  "audit_trace_resolved_indices": [
    "accounts"
  ]
}
```

To include the request body, return to **Compliance settings** in
OpenSearch Dashboards and disable **Write metadata**. To exclude events by a
specific user, add the user to **Ignored Users**.

For a description of each audit log field, see [Audit log
field reference](https://docs.opensearch.org/latest/security-plugin/audit-logs/field-reference/ "https://docs.opensearch.org/latest/security-plugin/audit-logs/field-reference/"). For information on searching and analyzing your audit log data,
see [Analyzing Log Data with CloudWatch Logs
Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") in the _Amazon CloudWatch Logs User Guide_.

## Configuring audit logs using the REST API

We recommend using OpenSearch Dashboards to configure audit logs, but you can also use the
fine-grained access control REST API. This section contains a sample request. Full
documentation on the REST API is available in the [OpenSearch documentation](https://opensearch.org/docs/latest/security/access-control/api/#audit-logs "https://opensearch.org/docs/latest/security/access-control/api/#audit-logs").

```
PUT _opendistro/_security/api/audit/config
{
  "enabled": true,
  "audit": {
    "enable_rest": true,
    "disabled_rest_categories": [
      "GRANTED_PRIVILEGES",
      "AUTHENTICATED"
    ],
    "enable_transport": true,
    "disabled_transport_categories": [
      "GRANTED_PRIVILEGES",
      "AUTHENTICATED"
    ],
    "resolve_bulk_requests": true,
    "log_request_body": true,
    "resolve_indices": true,
    "exclude_sensitive_headers": true,
    "ignore_users": [
      "kibanaserver"
    ],
    "ignore_requests": [
      "SearchRequest",
      "indices:data/read/*",
      "/_cluster/health"
    ]
  },
  "compliance": {
    "enabled": true,
    "internal_config": true,
    "external_config": false,
    "read_metadata_only": true,
    "read_watched_fields": {
      "read-index-1": [
        "field-1",
        "field-2"
      ],
      "read-index-2": [
        "field-3"
      ]
    },
    "read_ignore_users": [
      "read-ignore-1"
    ],
    "write_metadata_only": true,
    "write_log_diffs": false,
    "write_watched_indices": [
      "write-index-1",
      "write-index-2",
      "log-*",
      "*"
    ],
    "write_ignore_users": [
      "write-ignore-1"
    ]
  }
}
```
