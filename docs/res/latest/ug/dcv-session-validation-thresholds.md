# Configurable DCV session validation thresholds

When a VDI session is resuming or starting, RES repeatedly checks whether the
DCV session has reached a READY state. If the session does not become ready within a certain
number of retries, it is marked as ERROR.

These retry thresholds are configurable via the
``<env-name>`.cluster-settings` DynamoDB table,
allowing administrators to tune them based on their environment. This is particularly
useful for environments with longer bootstrap times due to custom AMI configurations,
additional software installations, or other VDI setup logic.

| Key                                | Description                                                 | Default value |
| ---------------------------------- | ----------------------------------------------------------- | ------------- |
| `vdc.validation_request_threshold` | Maximum retries before marking a non-ready session as ERROR | 50            |
| `vdc.session_deleted_threshold`    | Maximum retries before marking a DELETED session as ERROR   | 15            |
