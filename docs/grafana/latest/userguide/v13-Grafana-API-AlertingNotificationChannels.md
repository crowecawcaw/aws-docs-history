

# Alerting contact points API
<a name="v13-Grafana-API-AlertingNotificationChannels"></a>

In Grafana version 13, notifications are managed through Grafana's unified alerting. The legacy notification channels API (the `/api/alert-notifications` endpoints) was removed together with legacy alerting in Grafana version 11 and is no longer available. Instead, use the alerting provisioning API to work with *contact points*, which are the unified alerting replacement for notification channels.

**Note**  
To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid service account token. You include this in the `Authorization` field in the API request.

**Note**  
The alerting provisioning contact point endpoints that list, create, update, or delete contact points (`GET`, `POST`, `PUT`, and `DELETE` on `/api/v1/provisioning/contact-points`) are deprecated. Responses from these endpoints include a `Warning` header and an `X-API-Deprecation-Date` header with a date of `2026-04-07`. This topic documents the endpoints that are *not* deprecated—`GET /api/alert-notifiers` and `GET /api/v1/provisioning/contact-points/export`—in full, and lists the deprecated endpoints for reference only.

## List contact point types
<a name="v13-Grafana-API-AlertNotificationChannels-notifiers"></a>

Returns the list of contact point types (notifiers) available in your Amazon Managed Grafana workspace. Use this endpoint to discover which contact point types you can configure and the options that each type supports.

```
GET /api/alert-notifiers
```

**Query parameters**
+ `version` – (Optional) Set to `2` to return the full integration type schema for each contact point type. When omitted, the endpoint returns the default list of contact point types.

**Example request**

```
GET /api/alert-notifiers HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 1234abcd567exampleToken890
```

**Response**

The response is a JSON array in which each element describes an available contact point type. Each element includes the type identifier (`type`), the display `name`, a `description`, and the configuration `options` that the type supports.

## Export contact points
<a name="v13-Grafana-API-AlertNotificationChannels-export"></a>

Returns the contact points defined in your Amazon Managed Grafana workspace in a format that you can use to provision alerting as code. This endpoint is not deprecated.

```
GET /api/v1/provisioning/contact-points/export
```

**Query parameters**
+ `name` – (Optional) Filter the exported contact points by contact point name.
+ `decrypt` – (Optional) Whether to decrypt and include secure settings in the export. Defaults to `false`.
+ `format` – (Optional) The output format for the export, such as `json`, `yaml`, or `hcl` (Terraform).

**Example request**

```
GET /api/v1/provisioning/contact-points/export?format=yaml HTTP/1.1
Accept: application/json
Authorization: Bearer 1234abcd567exampleToken890
```

**Response**

Returns the contact points in the requested format, suitable for use with file provisioning or Terraform. By default, secure settings are redacted unless you set `decrypt` to `true`.

## Deprecated contact point endpoints
<a name="v13-Grafana-API-AlertNotificationChannels-deprecated"></a>

The following alerting provisioning endpoints manage contact points but are deprecated. Responses include a `Warning` header and an `X-API-Deprecation-Date` header with a date of `2026-04-07`. They are listed here for reference only and might be removed in a future release.
+ `GET /api/v1/provisioning/contact-points` – Returns all contact points. Accepts an optional `name` query parameter to filter by contact point name.
+ `POST /api/v1/provisioning/contact-points` – Creates a contact point.
+ `PUT /api/v1/provisioning/contact-points/{UID}` – Updates the contact point with the specified `UID`.
+ `DELETE /api/v1/provisioning/contact-points/{UID}` – Deletes the contact point with the specified `UID`.

The contact point object used by these endpoints includes the following fields.
+ `uid` – (Optional) A user-defined unique identifier for the contact point.
+ `name` – (Required) The contact point name. Contact points that share a name are grouped together.
+ `type` – (Required) The contact point type, such as `email`, `slack`, or `webhook`.
+ `settings` – (Required) A type-specific object that holds the configuration for the contact point.
+ `disableResolveMessage` – (Optional) Whether to suppress the notification that is sent when an alert resolves.
+ `provenance` – (Read-only) Indicates how the contact point was provisioned.