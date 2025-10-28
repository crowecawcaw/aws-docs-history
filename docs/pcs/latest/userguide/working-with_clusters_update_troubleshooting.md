# Troubleshooting AWS PCS cluster updates

This topic helps you identify and resolve common problems that can occur when updating cluster configurations.

## Update fails with accounting configuration error

### Common cause

The cluster enters `UPDATE_FAILED` state and the error message indicates an accounting configuration issue. This typically occurs when the accounting configuration is incompatible with the current Slurm version or contains invalid settings.

### Resolution

Review your accounting settings for compatibility with your cluster's Slurm version and submit a corrected update request with valid configuration parameters.

## Update fails with custom settings error

### Common cause

The cluster enters `UPDATE_FAILED` state and the error message indicates a Slurm custom settings issue. This occurs when you provide invalid Slurm parameter values or unsupported parameter combinations.

### Resolution

Validate your Slurm custom settings against the supported parameters and submit a corrected update request with valid parameter values and combinations.

## Cannot submit update request

### Common cause

The update button is disabled in the console or the API returns a 400-level error. This occurs when the cluster is not in an appropriate state, associated resources are not active, or there are validation failures in your configuration.

### Resolution

Wait for the cluster and all associated resources to reach `ACTIVE` state, then review your configuration for validation errors before resubmitting the update request.

## Validation errors

### Common cause

The command returns immediately with a 400-level HTTP error and descriptive message. This occurs due to invalid cluster state, resource state, or configuration parameters.

### Resolution

Address the specific validation error mentioned in the response and retry the update operation.
