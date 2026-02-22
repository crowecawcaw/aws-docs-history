# Troubleshooting

When action connectors encounter issues, systematic troubleshooting helps you quickly identify and resolve problems. This guidance covers common issues and their solutions to minimize downtime and restore functionality.

## Common issues and solutions

### Authentication problems

#### Token expiration

```
Symptom: "Authentication token expired" error
Resolution:
```

1. Choose "Reconnect" in console.
2. Complete authentication flow.
3. Retry action.

#### Permission errors

```
Symptom: "Insufficient permissions" message
Resolution:
```

1. Verify service permissions.
2. Check connector configuration.
3. Review action requirements.

#### Connection failures

```
Symptom: "Unable to connect to service" error
Resolution:
```

1. Verify service availability.
2. Check network connectivity.
3. Validate credentials.
4. Review service quotas.

### Action-specific issues

#### Form submission failures

##### Validation errors

- Check required fields.
- Verify data formats.
- Review field limitations.
- Check for special characters.

##### Timeout issues

- Reduce form complexity.
- Check network latency.
- Review service response times.
- Consider breaking into multiple actions.

#### Sync and performance issues

##### Slow response times

```
Resolution:
```

1. Check API rate limits.
2. Review concurrent executions.
3. Monitor service health.
4. Optimize action configuration.

##### Failed executions

```
Resolution:
```

1. Review CloudWatch logs.
2. Check error messages.
3. Verify service status.
4. Test connection health.

## Common error messages

| Error codes and resolutions | Error code               | Description                      | Resolution |
| --------------------------- | ------------------------ | -------------------------------- | ---------- |
| AUTH_001                    | Authentication failed    | Verify credentials and retry     |
| CONN_002                    | Connection timeout       | Check network and service status |
| PERM_003                    | Insufficient permissions | Review required permissions      |
| TOKEN_004                   | Token expired            | Reinitiate authentication        |
