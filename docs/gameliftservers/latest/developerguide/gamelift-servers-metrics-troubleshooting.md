# Troubleshooting guide

## Common issues and resolution steps

### Missing or incomplete metrics

#### Symptoms

- No metrics appearing in dashboards.
- Partial metric collection.
- Delayed metric updates.

#### Resolution steps

##### A. Verify collector status

Check systemd service:

```
sudo systemctl status gamelift-telemetry-collector
```

Review collector logs:

```
sudo journalctl -u gamelift-telemetry-collector
```

- Confirm collector configuration.

##### B. IAM permission verification

- Check instance role permissions.
- Verify required policies:
  - `aps:RemoteWrite`
  - `cloudwatch:PutMetricData`

- Validate role trust relationships.

##### C. Network connectivity

- Verify endpoint access.
- Check security group rules.
- Review network ACLs.

### Authentication errors

#### Symptoms

- SigV4 authentication failures.
- Access denied messages.
- Credential refresh issues.

#### Resolution steps

##### A. SigV4 authentication

- Verify temporary credentials.
- Check credential rotation.
- Validate instance profile.

##### B. AMP access

- Review workspace configuration.
- Verify remote write URL.
- Check IAM role bindings.

### Dashboard issues

#### Symptoms

- Empty dashboards.
- Missing data points.
- Authentication failures.

#### Resolution steps

##### A. Data source configuration

- Verify Prometheus connection.
- Check Amazon CloudWatch integration.
- Test data source permissions.

##### B. Grafana access

- Confirm SSO configuration.
- Verify 2FA setup if required.
- Check user permissions.

### Windows-specific issues

#### Symptoms

- Service startup failures.
- Metric collection gaps.
- Permission errors.

#### Resolution steps

- Verify Windows service status.
- Check Windows Event Logs.
- Review collector configuration.
- Validate Windows-specific paths.
