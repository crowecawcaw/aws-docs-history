

# Troubleshooting guide
<a name="gamelift-servers-metrics-troubleshooting"></a>

## Common issues and resolution steps
<a name="common-issues-resolution"></a>

### Missing or incomplete metrics
<a name="troubleshooting-missing-metrics"></a>

#### Symptoms
<a name="missing-metrics-symptoms"></a>
+ No metrics appearing in dashboards.
+ Partial metric collection.
+ Delayed metric updates.

#### Resolution steps
<a name="missing-metrics-resolution"></a>

##### A. Verify collector status
<a name="verify-collector-status"></a>

Check systemd service:

```
sudo systemctl status gamelift-telemetry-collector
```

Review collector logs:

```
sudo journalctl -u gamelift-telemetry-collector
```
+ Confirm collector configuration.

##### B. IAM permission verification
<a name="iam-permission-verification"></a>
+ Check instance role permissions.
+ Verify required policies:
  + `aps:RemoteWrite`
  + `cloudwatch:PutMetricData`
+ Validate role trust relationships.

##### C. Network connectivity
<a name="network-connectivity"></a>
+ Verify endpoint access.
+ Check security group rules.
+ Review network ACLs.

### Authentication errors
<a name="troubleshooting-authentication-errors"></a>

#### Symptoms
<a name="auth-errors-symptoms"></a>
+ SigV4 authentication failures.
+ Access denied messages.
+ Credential refresh issues.

#### Resolution steps
<a name="auth-errors-resolution"></a>

##### A. SigV4 authentication
<a name="sigv4-authentication"></a>
+ Verify temporary credentials.
+ Check credential rotation.
+ Validate instance profile.

##### B. AMP access
<a name="amp-access"></a>
+ Review workspace configuration.
+ Verify remote write URL.
+ Check IAM role bindings.

### Dashboard issues
<a name="troubleshooting-dashboard-issues"></a>

#### Symptoms
<a name="dashboard-issues-symptoms"></a>
+ Empty dashboards.
+ Missing data points.
+ Authentication failures.

#### Resolution steps
<a name="dashboard-issues-resolution"></a>

##### A. Data source configuration
<a name="data-source-configuration"></a>
+ Verify Prometheus connection.
+ Check Amazon CloudWatch integration.
+ Test data source permissions.

##### B. Grafana access
<a name="grafana-access"></a>
+ Confirm SSO configuration.
+ Verify 2FA setup if required.
+ Check user permissions.

### Windows-specific issues
<a name="troubleshooting-windows-issues"></a>

#### Symptoms
<a name="windows-issues-symptoms"></a>
+ Service startup failures.
+ Metric collection gaps.
+ Permission errors.

#### Resolution steps
<a name="windows-issues-resolution"></a>
+ Verify Windows service status.
+ Check Windows Event Logs.
+ Review collector configuration.
+ Validate Windows-specific paths.