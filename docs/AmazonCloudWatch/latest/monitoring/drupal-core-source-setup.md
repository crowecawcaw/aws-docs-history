# Source configuration for Drupal Core

## Integrating with Drupal Core

Drupal Core is the foundational open-source web application framework built on PHP that provides the base platform for building websites, applications, and digital experiences. CloudWatch Pipeline uses the custom View-based REST API to retrieve audit log data — including content changes, user authentication events, and administrative actions — from your Drupal Core site. The API enables access to time-filtered log data through REST endpoints, allowing retrieval of activity records scoped to a configurable time window.

## Authenticating with Drupal Core

To read the logs, the pipeline needs to authenticate with your Drupal Core site. The plugin supports Basic Authentication (HTTP Basic Auth using a username and password).

**Configure Basic Authentication for Drupal Core**

- Log in to your Drupal Core admin interface and navigate to Administration → Extend (`/admin/modules`).
- Enable the following modules: RESTful Web Services, Serialization, HTTP Basic Authentication, and Views. Choose Install.
- Install and enable the Admin Audit Trail module by using Composer (`composer require drupal/admin_audit_trail`) and run `drush en admin_audit_trail -y && drush cr` to activate it.
- Navigate to Structure → Views and create a new View named `Audit Logs API`. Set Show to `Log entries`, enable Provide a REST export, and set the REST export path to `/api/v1/audit-logs`.
- In the View editor, add two exposed Watchdog: Timestamp filters — one with operator `is greater than or equal to` and filter identifier `starttime`, and another with operator `is less than` and filter identifier `endtime`.
- In the REST EXPORT SETTINGS section of the View, choose Authentication and enable `basic_auth`.
- Navigate to People → Permissions and grant the roles that need API access the Access admin audit trail and Administer REST resource configuration permissions. Save the View.
- In AWS Secrets Manager, create a secret and store the Drupal Core username under the key `username` and the account password under the key `password`.

## Configuring the CloudWatch Pipeline

To configure the pipeline to read logs, choose Drupal Core as the data source. Fill in the required information:

- **Domain** — The base URL of your Drupal Core site (for example, `https://your-drupal-site.example.com`).
- **API Endpoint** — The path to the View REST export endpoint (for example, `/api/v1/audit-logs`). Must start with `/`.
- **Range** — Specify the lookback duration in ISO 8601 format (for example, `PT21H` for the last 21 hours, `P7D` for the last 7 days). The default is 0 hours, and the maximum is 90 days.

After you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and transforms events that map to Authentication (3002), Entity Management (3004), HTTP Activity (4002), and Application Lifecycle (6002). Events that are not listed are not mapped to OCSF and will be forwarded to the sink as raw logs.

**Authentication** contains the following event types:

- user — Login and authentication related events

**Entity Management** contains the following event types:

- user — User creation and deletion
- content
- comment

**HTTP Activity** contains the following event types:

- access denied
- page not found
- php
- new custom types

**Application Lifecycle** contains the following event types:

- system
- cron
