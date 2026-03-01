# GitLab connector for Amazon AppFlow

GitLab is an open source code repository and software development platform. If
you're a GitLab user, your account contains data about your projects and repositories.
You can use Amazon AppFlow to transfer data from
GitLab to certain AWS services or other supported applications.

## Amazon AppFlow support for GitLab

Amazon AppFlow supports GitLab as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from GitLab.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to GitLab.

**Supported API version**

Amazon AppFlow retrieves your data by sending requests to the GitLab v4 REST API.

## Before you begin

To use Amazon AppFlow to transfer data from GitLab to supported destinations, you must meet these
requirements:

- You have a GitLab account and one or more projects that contain the data that
  you want to transfer. For more information about the GitLab data objects that
  Amazon AppFlow supports, see [Supported objects](#gitlab-objects "#gitlab-objects").
- In the settings of your account, you've created either of the following resources for
  Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to access your data securely when
  it makes authenticated calls to your account.
  - An application, which provides OAuth 2.0 authentication. For the steps to create an
    application, see [User owned applications](https://docs.gitlab.com/ee/integration/oauth_provider.html#user-owned-applications "https://docs.gitlab.com/ee/integration/oauth_provider.html#user-owned-applications") in the GitLab Docs.
  - A personal access token. For the steps to create one, see [Create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token "https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token") in the GitLab Docs.

  Your personal access token must permit the `api` scope.

- If you created an application, you've configured it with the following settings:
  - You've specified a redirect URL for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from GitLab. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._
  - You've permitted the scopes that provide access to the data objects that you want to
    transfer. For information about GitLab OAuth 2.0 scopes, see [Authorized applications](https://docs.gitlab.com/ee/integration/oauth_provider.html#authorized-applications "https://docs.gitlab.com/ee/integration/oauth_provider.html#authorized-applications") in the GitLab Docs.

If you created an application, note the application ID and secret. If you created a personal
access token, note the token value. You provide these values to Amazon AppFlow when you connect to your
GitLab account.

## Connecting Amazon AppFlow to your GitLab account

To connect Amazon AppFlow to your GitLab account, provide the credentials from your
application, or provide a personal access token. If you haven't yet configured your
GitLab account for Amazon AppFlow integration, see [Before you begin](#gitlab-prereqs "#gitlab-prereqs").

###### To connect to GitLab

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **GitLab**.
4. Choose **Create connection**.
5. In the **Connect to GitLab** window, for **Select
   authentication type**, choose how to authenticate Amazon AppFlow with your GitLab
   account when it requests to access your data:
   - Choose **OAuth2** to authenticate Amazon AppFlow with the credentials from an
     application. Then, enter the following values:
     - **Client ID** – The application ID.
     - **Client secret** – The secret.

   - Choose **PersonalAccessToken** to authenticate Amazon AppFlow with a personal
     access token. Then, enter the token value for **Personal access
     token**.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Depending on the authentication type that you chose, do one of the following:

    * If you chose **OAuth2**, choose **Continue**. Then, in
     the window that appears, sign in to your GitLab account, and grant access to
     Amazon AppFlow.
    * If you chose **PersonalAccessToken**, choose
     **Connect**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses GitLab as the data source, you can select this connection.

## Transferring data from GitLab with a flow

To transfer data from GitLab, create an Amazon AppFlow flow, and choose GitLab as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for GitLab, see [Supported objects](#gitlab-objects "#gitlab-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#gitlab-destinations "#gitlab-destinations").

## Supported destinations

When you create a flow that uses GitLab as the data source, you can set the destination to any of the following connectors:

- [Amazon Lookout for Metrics](lookout.md "lookout.md")
- [Amazon Redshift](redshift.md "redshift.md")
- [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md "connectors-amazon-rds-postgres-sql.md")
- [Amazon S3](s3.md "s3.md")
- [HubSpot](connectors-hubspot.md "connectors-hubspot.md")
- [Marketo](marketo.md "marketo.md")
- [Salesforce](salesforce.md "salesforce.md")
- [SAP OData](sapodata.md "sapodata.md")
- [Snowflake](snowflake.md "snowflake.md")
- [Upsolver](upsolver.md "upsolver.md")
- [Zendesk](zendesk.md "zendesk.md")
- [Zoho CRM](connectors-zoho-crm.md "connectors-zoho-crm.md")

## Supported objects

When you create a flow that uses GitLab as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                                       | **Field**           | **Data type**            | **Supported filters** |
| ------------------------------------------------ | ------------------- | ------------------------ | --------------------- |
| Branch                                           | can_push            | Boolean                  |                       |
| commit                                           | Struct              |                          |
| default                                          | Boolean             |                          |
| developers_can_merge                             | Boolean             |                          |
| developers_can_push                              | Boolean             |                          |
| merged                                           | Boolean             |                          |
| name                                             | String              |                          |
| protected                                        | Boolean             |                          |
| search                                           | String              | EQUAL_TO                 |
| web_url                                          | String              |                          |
| Commit                                           | all                 | Boolean                  | EQUAL_TO              |
| author_email                                     | String              |                          |
| author_name                                      | String              |                          |
| authored_date                                    | DateTime            |                          |
| committed_date                                   | DateTime            |                          |
| committer_email                                  | String              |                          |
| committer_name                                   | String              |                          |
| created_at                                       | DateTime            |                          |
| first_parent                                     | Boolean             | EQUAL_TO                 |
| id                                               | String              |                          |
| message                                          | String              |                          |
| order                                            | String              | EQUAL_TO                 |
| parent_ids                                       | List                |                          |
| path                                             | String              | EQUAL_TO                 |
| ref_name                                         | String              | EQUAL_TO                 |
| short_id                                         | String              |                          |
| since                                            | DateTime            | GREATER_THAN_OR_EQUAL_TO |
| since_until                                      | DateTime            | BETWEEN                  |
| title                                            | String              |                          |
| trailers                                         | Boolean             | EQUAL_TO                 |
| until                                            | DateTime            | LESS_THAN_OR_EQUAL_TO    |
| web_url                                          | String              |                          |
| with_stats                                       | Boolean             | EQUAL_TO                 |
| Group                                            | auto_devops_enabled | String                   |                       |
| avatar_url                                       | String              |                          |
| created_at                                       | DateTime            |                          |
| default_branch_protection                        | Integer             |                          |
| description                                      | String              |                          |
| emails_disabled                                  | String              |                          |
| file_template_project_id                         | Integer             |                          |
| full_name                                        | String              |                          |
| full_path                                        | String              |                          |
| id                                               | Integer             |                          |
| ip_restriction_ranges                            | String              |                          |
| ldap_access                                      | String              |                          |
| ldap_cn                                          | String              |                          |
| lfs_enabled                                      | Boolean             |                          |
| mentions_disabled                                | String              |                          |
| min_access_level                                 | Integer             | EQUAL_TO                 |
| name                                             | String              |                          |
| order_by                                         | String              | EQUAL_TO                 |
| owned                                            | Boolean             | EQUAL_TO                 |
| parent_id                                        | String              |                          |
| path                                             | String              |                          |
| project_creation_level                           | String              |                          |
| request_access_enabled                           | Boolean             |                          |
| require_two_factor_authentication                | Boolean             |                          |
| search                                           | String              | EQUAL_TO                 |
| share_with_group_lock                            | Boolean             |                          |
| skip_groups                                      | Integer             | EQUAL_TO                 |
| sort                                             | String              | EQUAL_TO                 |
| statistics                                       | Boolean             | EQUAL_TO                 |
| subgroup_creation_level                          | String              |                          |
| top_level_only                                   | Boolean             | EQUAL_TO                 |
| two_factor_grace_period                          | Integer             |                          |
| visibility                                       | String              |                          |
| web_url                                          | String              |                          |
| with_custom_attributes                           | Boolean             | EQUAL_TO                 |
| Group Member                                     | access_level        | Integer                  |                       |
| avatar_url                                       | String              |                          |
| created_at                                       | DateTime            |                          |
| created_by                                       | Struct              |                          |
| email                                            | String              |                          |
| expires_at                                       | DateTime            |                          |
| group_saml_identity                              | Struct              |                          |
| id                                               | Integer             |                          |
| is_using_seat                                    | String              |                          |
| membership_state                                 | String              |                          |
| name                                             | String              |                          |
| query                                            | String              | EQUAL_TO                 |
| show_seat_info                                   | Boolean             | EQUAL_TO                 |
| skip_users                                       | Integer             | EQUAL_TO                 |
| state                                            | String              |                          |
| user_ids                                         | Integer             | EQUAL_TO                 |
| username                                         | String              |                          |
| web_url                                          | String              |                          |
| Group label                                      | closed_issues_count | Integer                  |                       |
| color                                            | String              |                          |
| description                                      | String              |                          |
| description_html                                 | String              |                          |
| id                                               | Integer             |                          |
| include_ancestor_groups                          | Boolean             | EQUAL_TO                 |
| include_descendant_groups                        | Boolean             | EQUAL_TO                 |
| name                                             | String              |                          |
| only_group_labels                                | Boolean             | EQUAL_TO                 |
| open_issues_count                                | Integer             |                          |
| open_merge_requests_count                        | Integer             |                          |
| search                                           | String              | EQUAL_TO                 |
| subscribed                                       | Boolean             |                          |
| text_color                                       | String              |                          |
| with_counts                                      | Boolean             | EQUAL_TO                 |
| Group milestone                                  | created_at          | DateTime                 |                       |
| description                                      | String              |                          |
| due_date                                         | Date                |                          |
| expired                                          | Boolean             |                          |
| group_id                                         | Integer             |                          |
| id                                               | Integer             |                          |
| iid                                              | Integer             |                          |
| iids                                             | Integer             | EQUAL_TO                 |
| include_parent_milestones                        | Boolean             | EQUAL_TO                 |
| search                                           | String              | EQUAL_TO                 |
| start_date                                       | Date                |                          |
| state                                            | String              | EQUAL_TO                 |
| title                                            | String              | EQUAL_TO                 |
| updated_at                                       | DateTime            |                          |
| web_url                                          | String              |                          |
| Issue                                            | \_links             | Struct                   |                       |
| assignee                                         | Struct              |                          |
| assignee_id                                      | Integer             | EQUAL_TO                 |
| assignee_username                                | String              | EQUAL_TO                 |
| assignees                                        | List                |                          |
| author                                           | Struct              |                          |
| author_id                                        | String              | EQUAL_TO                 |
| author_username                                  | String              | EQUAL_TO                 |
| blocking_issues_count                            | Integer             |                          |
| closed_at                                        | DateTime            |                          |
| closed_by                                        | String              |                          |
| confidential                                     | Boolean             | EQUAL_TO                 |
| created_after                                    | DateTime            | GREATER_THAN_OR_EQUAL_TO |
| created_at                                       | DateTime            |                          |
| created_before                                   | DateTime            | LESS_THAN_OR_EQUAL_TO    |
| created_before_after                             | DateTime            | BETWEEN                  |
| description                                      | String              |                          |
| discussion_locked                                | Boolean             |                          |
| downvotes                                        | Integer             |                          |
| due_date                                         | String              | EQUAL_TO                 |
| has_tasks                                        | Boolean             |                          |
| id                                               | Integer             |                          |
| iid                                              | Integer             |                          |
| iids                                             | Integer             | EQUAL_TO                 |
| issue_type                                       | String              | EQUAL_TO                 |
| labels                                           | List                |                          |
| merge_requests_count                             | Integer             |                          |
| milestone                                        | Struct              |                          |
| milestone_id                                     | String              | EQUAL_TO                 |
| moved_to_id                                      | String              |                          |
| my_reaction_emoji                                | String              | EQUAL_TO                 |
| non_archived                                     | Boolean             | EQUAL_TO                 |
| order_by                                         | String              | EQUAL_TO                 |
| project_id                                       | Integer             |                          |
| references                                       | Struct              |                          |
| scope                                            | String              | EQUAL_TO                 |
| search                                           | String              | EQUAL_TO                 |
| service_desk_reply_to                            | String              |                          |
| severity                                         | String              |                          |
| sort                                             | String              | EQUAL_TO                 |
| state                                            | String              | EQUAL_TO                 |
| task_completion_status                           | Struct              |                          |
| task_status                                      | String              |                          |
| time_stats                                       | Struct              |                          |
| title                                            | String              |                          |
| type                                             | String              |                          |
| updated_after                                    | DateTime            | GREATER_THAN_OR_EQUAL_TO |
| updated_at                                       | DateTime            |                          |
| updated_before                                   | DateTime            | LESS_THAN_OR_EQUAL_TO    |
| updated_before_after                             | DateTime            | BETWEEN                  |
| upvotes                                          | Integer             |                          |
| user_notes_count                                 | Integer             |                          |
| web_url                                          | String              |                          |
| with_labels_details                              | Boolean             | EQUAL_TO                 |
| Job                                              | allow_failure       | Boolean                  |                       |
| artifacts                                        | List                |                          |
| artifacts_expire_at                              | DateTime            |                          |
| artifacts_file                                   | Struct              |                          |
| commit                                           | Struct              |                          |
| coverage                                         | String              |                          |
| created_at                                       | DateTime            |                          |
| duration                                         | Integer             |                          |
| failure_reason                                   | String              |                          |
| finished_at                                      | DateTime            |                          |
| id                                               | Integer             |                          |
| name                                             | String              |                          |
| pipeline                                         | Struct              |                          |
| project                                          | Struct              |                          |
| queued_duration                                  | Integer             |                          |
| ref                                              | String              |                          |
| runner                                           | String              |                          |
| scope                                            | String              | EQUAL_TO                 |
| stage                                            | String              |                          |
| started_at                                       | DateTime            |                          |
| status                                           | String              |                          |
| tag                                              | Boolean             |                          |
| tag_list                                         | List                |                          |
| user                                             | Struct              |                          |
| web_url                                          | String              |                          |
| Pipeline                                         | created_at          | DateTime                 |                       |
| id                                               | Integer             |                          |
| iid                                              | Integer             |                          |
| order_by                                         | String              | EQUAL_TO                 |
| project_id                                       | Integer             |                          |
| ref                                              | String              | EQUAL_TO                 |
| scope                                            | String              | EQUAL_TO                 |
| sha                                              | String              | EQUAL_TO                 |
| sort                                             | String              | EQUAL_TO                 |
| source                                           | String              | EQUAL_TO                 |
| status                                           | String              | EQUAL_TO                 |
| updated_after                                    | DateTime            | GREATER_THAN_OR_EQUAL_TO |
| updated_at                                       | DateTime            |                          |
| updated_before                                   | DateTime            | LESS_THAN_OR_EQUAL_TO    |
| updated_before_after                             | DateTime            | BETWEEN                  |
| username                                         | String              | EQUAL_TO                 |
| web_url                                          | String              |                          |
| yaml_errors                                      | Boolean             | EQUAL_TO                 |
| Project                                          | \_links             | Struct                   |                       |
| allow_merge_on_skipped_pipeline                  | String              |                          |
| analytics_access_level                           | String              |                          |
| archived                                         | Boolean             | EQUAL_TO                 |
| auto_cancel_pending_pipelines                    | String              |                          |
| auto_devops_deploy_strategy                      | String              |                          |
| auto_devops_enabled                              | Boolean             |                          |
| autoclose_referenced_issues                      | Boolean             |                          |
| avatar_url                                       | String              |                          |
| build_timeout                                    | Integer             |                          |
| builds_access_level                              | String              |                          |
| can_create_merge_request_in                      | Boolean             |                          |
| ci_allow_fork_pipelines_to_run_in_parent_project | Boolean             |                          |
| ci_config_path                                   | String              |                          |
| ci_default_git_depth                             | Integer             |                          |
| ci_forward_deployment_enabled                    | Boolean             |                          |
| ci_job_token_scope_enabled                       | Boolean             |                          |
| ci_separated_caches                              | Boolean             |                          |
| compliance_frameworks                            | List                |                          |
| container_expiration_policy                      | Struct              |                          |
| container_registry_access_level                  | String              |                          |
| container_registry_enabled                       | Boolean             |                          |
| container_registry_image_prefix                  | String              |                          |
| created_at                                       | DateTime            |                          |
| creator_id                                       | Integer             |                          |
| default_branch                                   | String              |                          |
| description                                      | String              |                          |
| emails_disabled                                  | String              |                          |
| empty_Repo                                       | Boolean             |                          |
| enforce_auth_checks_on_uploads                   | Boolean             |                          |
| external_authorization_classification_label      | String              |                          |
| forking_access_level                             | String              |                          |
| forks_count                                      | Integer             |                          |
| http_url_to_repo                                 | String              |                          |
| id                                               | Integer             |                          |
| id_after                                         | Integer             | EQUAL_TO                 |
| id_before                                        | Integer             | EQUAL_TO                 |
| import_status                                    | String              |                          |
| imported                                         | Boolean             | EQUAL_TO                 |
| issues_access_level                              | String              |                          |
| issues_enabled                                   | Boolean             |                          |
| jobs_enabled                                     | Boolean             |                          |
| keep_latest_artifact                             | Boolean             |                          |
| last_activity_after                              | DateTime            | GREATER_THAN_OR_EQUAL_TO |
| last_activity_at                                 | DateTime            |                          |
| last_activity_before                             | DateTime            | LESS_THAN_OR_EQUAL_TO    |
| last_activity_before_after                       | DateTime            | BETWEEN                  |
| lfs_enabled                                      | Boolean             |                          |
| membership                                       | Boolean             | EQUAL_TO                 |
| merge_commit_template                            | String              |                          |
| merge_method                                     | String              |                          |
| merge_requests_access_level                      | String              |                          |
| merge_requests_enabled                           | Boolean             |                          |
| min_access_level                                 | Integer             | EQUAL_TO                 |
| name                                             | String              |                          |
| name_with_namespace                              | String              |                          |
| namespace                                        | Struct              |                          |
| only_allow_merge_if_all_discussions_are_resolved | Boolean             |                          |
| only_allow_merge_if_pipeline_succeeds            | Boolean             |                          |
| open_issues_count                                | Integer             |                          |
| operations_access_level                          | String              |                          |
| order_by                                         | String              | EQUAL_TO                 |
| owned                                            | Boolean             | EQUAL_TO                 |
| packages_enabled                                 | Boolean             |                          |
| pages_access_level                               | String              |                          |
| path                                             | String              |                          |
| path_with_namespace                              | String              |                          |
| permissions                                      | Struct              |                          |
| printing_merge_request_link_enabled              | Boolean             |                          |
| public_jobs                                      | Boolean             |                          |
| readme_url                                       | String              |                          |
| remove_source_branch_after_merge                 | Boolean             |                          |
| repository_access_level                          | String              |                          |
| repository_storage                               | String              | EQUAL_TO                 |
| request_access_enabled                           | Boolean             |                          |
| requirements_access_level                        | String              |                          |
| requirements_enabled                             | Boolean             |                          |
| resolve_outdated_diff_discussions                | Boolean             |                          |
| restrict_user_defined_variables                  | Boolean             |                          |
| runner_token_expiration_interval                 | String              |                          |
| search                                           | String              | EQUAL_TO                 |
| search_namespaces                                | Boolean             | EQUAL_TO                 |
| security_and_compliance_access_level             | String              |                          |
| security_and_compliance_enabled                  | Boolean             |                          |
| service_desk_enabled                             | Boolean             |                          |
| shared_runners_enabled                           | Boolean             |                          |
| shared_with_groups                               | List                |                          |
| simple                                           | Boolean             | EQUAL_TO                 |
| snippets_access_level                            | String              |                          |
| snippets_enabled                                 | Boolean             |                          |
| sort                                             | String              | EQUAL_TO                 |
| squash_commit_template                           | String              |                          |
| squash_option                                    | String              |                          |
| ssh_url_to_repo                                  | String              |                          |
| star_count                                       | Integer             |                          |
| starred                                          | Boolean             | EQUAL_TO                 |
| statistics                                       | Boolean             | EQUAL_TO                 |
| suggestion_commit_message                        | String              |                          |
| tag_list                                         | List                |                          |
| topic                                            | String              | EQUAL_TO                 |
| topic_id                                         | Integer             | EQUAL_TO                 |
| topics                                           | List                |                          |
| visibility                                       | String              | EQUAL_TO                 |
| web_url                                          | String              |                          |
| wiki_access_level                                | String              |                          |
| wiki_enabled                                     | Boolean             |                          |
| with_custom_attributes                           | Boolean             | EQUAL_TO                 |
| with_issues_enabled                              | Boolean             | EQUAL_TO                 |
| with_merge_requests_enabled                      | Boolean             | EQUAL_TO                 |
| with_programming_language                        | Boolean             | EQUAL_TO                 |
| Project Label                                    | closed_issues_count | Integer                  |                       |
| color                                            | String              |                          |
| description                                      | String              |                          |
| description_html                                 | String              |                          |
| id                                               | Integer             |                          |
| include_ancestor_groups                          | Boolean             | EQUAL_TO                 |
| is_project_label                                 | Boolean             |                          |
| name                                             | String              |                          |
| open_issues_count                                | Integer             |                          |
| open_merge_requests_count                        | Integer             |                          |
| priority                                         | Integer             |                          |
| search                                           | String              | EQUAL_TO                 |
| subscribed                                       | Boolean             |                          |
| text_color                                       | String              |                          |
| with_counts                                      | Boolean             | EQUAL_TO                 |
| Project Member                                   | access_level        | Integer                  |                       |
| avatar_url                                       | String              |                          |
| created_at                                       | DateTime            |                          |
| created_by                                       | Struct              |                          |
| email                                            | String              |                          |
| expires_at                                       | DateTime            |                          |
| group_saml_identity                              | Struct              |                          |
| id                                               | Integer             |                          |
| is_using_seat                                    | String              |                          |
| membership_state                                 | String              |                          |
| name                                             | String              |                          |
| query                                            | String              | EQUAL_TO                 |
| show_seat_info                                   | Boolean             | EQUAL_TO                 |
| skip_users                                       | Integer             | EQUAL_TO                 |
| state                                            | String              |                          |
| user_ids                                         | Integer             | EQUAL_TO                 |
| username                                         | String              |                          |
| web_url                                          | String              |                          |
| Project Merge Request                            | allow_collaboration | Boolean                  |                       |
| allow_maintainer_to_push                         | Boolean             |                          |
| approvals_before_merge                           | String              |                          |
| assignee                                         | Struct              |                          |
| assignee_id                                      | Integer             | EQUAL_TO                 |
| assignees                                        | List                |                          |
| author                                           | Struct              |                          |
| author_id                                        | Integer             | EQUAL_TO                 |
| author_username                                  | Integer             | EQUAL_TO                 |
| blocking_discussions_resolved                    | Boolean             |                          |
| closed_at                                        | DateTime            |                          |
| closed_by                                        | String              |                          |
| created_after                                    | DateTime            | GREATER_THAN_OR_EQUAL_TO |
| created_at                                       | DateTime            |                          |
| created_before                                   | DateTime            | LESS_THAN_OR_EQUAL_TO    |
| created_before_after                             | DateTime            | BETWEEN                  |
| deployed_after                                   | DateTime            | GREATER_THAN_OR_EQUAL_TO |
| deployed_before                                  | DateTime            | LESS_THAN_OR_EQUAL_TO    |
| deployed_before_after                            | DateTime            | BETWEEN                  |
| description                                      | String              |                          |
| discussion_locked                                | String              |                          |
| downvotes                                        | Integer             |                          |
| draft                                            | Boolean             |                          |
| environment                                      | String              | EQUAL_TO                 |
| force_remove_source_branch                       | Boolean             |                          |
| has_conflicts                                    | Boolean             |                          |
| id                                               | Integer             |                          |
| iid                                              | Integer             |                          |
| labels                                           | List                |                          |
| merge_commit_sha                                 | String              |                          |
| merge_status                                     | String              |                          |
| merge_user                                       | Struct              |                          |
| merge_when_pipeline_succeeds                     | Boolean             |                          |
| merged_at                                        | DateTime            |                          |
| merged_by                                        | Struct              |                          |
| milestone                                        | Struct              |                          |
| my_reaction_emoji                                | String              | EQUAL_TO                 |
| order_by                                         | String              | EQUAL_TO                 |
| project_id                                       | Integer             |                          |
| references                                       | Struct              |                          |
| reviewer_id                                      | Integer             | EQUAL_TO                 |
| reviewer_username                                | String              | EQUAL_TO                 |
| reviewers                                        | List                |                          |
| scope                                            | String              | EQUAL_TO                 |
| search                                           | String              | EQUAL_TO                 |
| sha                                              | String              |                          |
| should_remove_source_branch                      | Boolean             |                          |
| sort                                             | String              | EQUAL_TO                 |
| source_branch                                    | String              | EQUAL_TO                 |
| source_project_id                                | Integer             |                          |
| squash                                           | Boolean             |                          |
| squash_commit_sha                                | String              |                          |
| state                                            | String              | EQUAL_TO                 |
| target_branch                                    | String              | EQUAL_TO                 |
| target_project_id                                | Integer             |                          |
| task_completion_status                           | Struct              |                          |
| time_stats                                       | Struct              |                          |
| title                                            | String              |                          |
| updated_after                                    | DateTime            | GREATER_THAN_OR_EQUAL_TO |
| updated_at                                       | DateTime            |                          |
| updated_before                                   | DateTime            | LESS_THAN_OR_EQUAL_TO    |
| updated_before_after                             | DateTime            | BETWEEN                  |
| upvotes                                          | Integer             |                          |
| user_notes_count                                 | Integer             |                          |
| view                                             | String              | EQUAL_TO                 |
| web_url                                          | String              |                          |
| wip                                              | String              | EQUAL_TO                 |
| with_labels_details                              | Boolean             | EQUAL_TO                 |
| with_merge_status_recheck                        | Boolean             | EQUAL_TO                 |
| work_in_progress                                 | Boolean             |                          |
| Project milestone                                | created_at          | DateTime                 |                       |
| description                                      | String              |                          |
| due_date                                         | Date                |                          |
| expired                                          | Boolean             |                          |
| id                                               | Integer             |                          |
| iid                                              | Integer             |                          |
| iids                                             | Integer             | EQUAL_TO                 |
| include_parent_milestones                        | Boolean             | EQUAL_TO                 |
| project_id                                       | Integer             |                          |
| search                                           | String              | EQUAL_TO                 |
| start_date                                       | Date                |                          |
| state                                            | String              | EQUAL_TO                 |
| title                                            | String              | EQUAL_TO                 |
| updated_at                                       | DateTime            |                          |
| web_url                                          | String              |                          |
| Release                                          | \_links             | Struct                   |                       |
| assets                                           | Struct              |                          |
| author                                           | Struct              |                          |
| commit                                           | Struct              |                          |
| commit_path                                      | String              |                          |
| created_at                                       | DateTime            |                          |
| description                                      | String              |                          |
| evidences                                        | List                |                          |
| include_html_description                         | Boolean             | EQUAL_TO                 |
| milestones                                       | List                |                          |
| name                                             | String              |                          |
| order_by                                         | String              | EQUAL_TO                 |
| released_at                                      | DateTime            |                          |
| sort                                             | String              | EQUAL_TO                 |
| tag_name                                         | String              |                          |
| tag_path                                         | String              |                          |
| upcoming_release                                 | Boolean             |                          |
| Tag                                              | commit              | Struct                   |                       |
| message                                          | String              |                          |
| name                                             | String              |                          |
| order_by                                         | String              | EQUAL_TO                 |
| protected                                        | Boolean             |                          |
| release                                          | Struct              |                          |
| search                                           | String              | EQUAL_TO                 |
| sort                                             | String              | EQUAL_TO                 |
| target                                           | String              |                          |
