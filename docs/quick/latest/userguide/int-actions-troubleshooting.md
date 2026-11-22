

# Troubleshooting

When connectors encounter issues, systematic troubleshooting helps you quickly identify and resolve problems. This guidance covers common issues and their solutions to minimize downtime and restore functionality.

## Common issues and solutions
<a name="qbs-actions-troubleshooting-qbs-actions-common-issues"></a>

### Authentication problems
<a name="qbs-actions-troubleshooting-qbs-actions-authentication-problems"></a>

#### Token expiration
<a name="qbs-actions-troubleshooting-qbs-actions-token-expiration"></a>

```
Symptom: "Authentication token expired" error
Resolution:
```

1. Choose "Reconnect" in console.

1. Complete authentication flow.

1. Retry the tool.

#### Permission errors
<a name="qbs-actions-troubleshooting-qbs-actions-permission-errors"></a>

```
Symptom: "Insufficient permissions" message
Resolution:
```

1. Verify service permissions.

1. Check connector configuration.

1. Review tool requirements.

#### Connection failures
<a name="qbs-actions-troubleshooting-qbs-actions-connection-failures"></a>

```
Symptom: "Unable to connect to service" error
Resolution:
```

1. Verify service availability.

1. Check network connectivity.

1. Validate credentials.

1. Review service quotas.

### Tool-specific issues
<a name="qbs-actions-troubleshooting-qbs-actions-action-specific-issues"></a>

#### Form submission failures
<a name="qbs-actions-troubleshooting-qbs-actions-form-submission-failures"></a>

##### Validation errors
<a name="qbs-actions-troubleshooting-qbs-actions-validation-errors"></a>
+ Check required fields.
+ Verify data formats.
+ Review field limitations.
+ Check for special characters.

##### Timeout issues
<a name="qbs-actions-troubleshooting-qbs-actions-timeout-issues"></a>
+ Reduce form complexity.
+ Check network latency.
+ Review service response times.
+ Consider breaking the request into multiple tools.

#### Sync and performance issues
<a name="qbs-actions-troubleshooting-qbs-actions-sync-performance-issues"></a>

##### Slow response times
<a name="qbs-actions-troubleshooting-qbs-actions-slow-response-times"></a>

```
Resolution:
```

1. Check API rate limits.

1. Review concurrent executions.

1. Monitor service health.

1. Optimize tool configuration.

##### Failed executions
<a name="qbs-actions-troubleshooting-qbs-actions-failed-executions"></a>

```
Resolution:
```

1. Review CloudWatch logs.

1. Check error messages.

1. Verify service status.

1. Test connection health.

## Common error messages
<a name="qbs-actions-troubleshooting-qbs-actions-error-messages"></a>


**Error codes and resolutions**  

| Error code | Description | Resolution | 
| --- | --- | --- | 
| AUTH\_001 | Authentication failed | Verify credentials and retry | 
| CONN\_002 | Connection timeout | Check network and service status | 
| PERM\_003 | Insufficient permissions | Review required permissions | 
| TOKEN\_004 | Token expired | Reinitiate authentication | 