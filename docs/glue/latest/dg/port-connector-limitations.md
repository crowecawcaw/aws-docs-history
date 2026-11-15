

# Limitations and notes for the Port connector
<a name="port-connector-limitations"></a>

The following are limitations and notes for the Port connector:
+ Port is supported as a source only. Writing to Port is not supported.
+ Job bookmarks are not supported.
+ The access token expires after approximately three hours. Refresh the stored Secrets Manager secret when it expires.