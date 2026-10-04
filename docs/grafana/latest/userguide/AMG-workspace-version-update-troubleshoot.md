

# Troubleshooting issues with updated workspaces
<a name="AMG-workspace-version-update-troubleshoot"></a>

Your updated workspace should continue to work after updating. This section can help you track down possible issues after you update.
+ **Differences between versions.**

  Some functionality has changed between versions.
  + For a list of major changes between versions, including changes that may cause issues in functionality, see [Differences between Grafana versions](version-differences.md). 
  + For documentation of version 9 specific functionality, see [Working in Grafana version 9](using-grafana-v9.md). For version 10, see [Working in Grafana version 10](using-grafana-v10.md). For version 12, see [Working in Grafana version 12](using-grafana-v12.md). For version 13, see [Working in Grafana version 13](using-grafana-v13.md).
+ **PostgreSQL TLS issue**

  If your **TLS/SSL Mode** was set to `require` in version 8, and you were only using a root certificate, you could experience TLS or certificate issues with the PostgreSQL data source after updating. Modify your TLS settings for your PostgreSQL data source (available in your Grafana workspace side menu, by choosing the **Configuration** icon, then **Data Sources**).
  + Change the **TLS/SSL Mode** to `verify-ca`.
  + Set **TLS/SSL Method** to `Certificate content`.
  + Set the **Root Certificate** to the root certificate for your PostgreSQL database server. This is the only field in which you should enter a certificate.
+ **Alertmanager status returns an authorization error for Viewer or Editor users (version 13)**

  In Grafana version 13, the Alertmanager status endpoint (`GET /api/alertmanager/grafana/api/v2/status`) requires the new `alert.notifications.system-status:read` permission. After updating, users with the **Viewer** or **Editor** role, and service accounts that call this endpoint, can receive an authorization error (a 4xx response) when they view alerting status, or when a dashboard or integration reads Alertmanager status on their behalf.

  To resolve this, assign a role that includes the `alert.notifications.system-status:read` permission, or add the permission to a custom role, for the affected users, teams, or service accounts. For more information, see [Breaking changes](version-differences.md#version-diff-v13-breaking-changes).