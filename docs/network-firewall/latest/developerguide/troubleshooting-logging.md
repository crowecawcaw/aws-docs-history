# Troubleshooting logging in AWS Network Firewall

Use the information here to help you diagnose common issues that you might encounter when working with logging in Network Firewall.

## My firewall isn't logging all traffic that matches pass action rules

Network Firewall only logs traffic for the rule action drop, alert, reject, or pass with an `alert` modifier keyword.
Rules with a pass action that do not use the `alert` modifier keyword silently allow the traffic in a way that any proceeding rules will not alert on that traffic.
If you want to log all traffic for troubleshooting purposes, add the `alert` modifier keyword to your pass rules.
When your pass rules include the `alert` modifier keyword, they will create an alert log for any traffic that matches applicable rules.
For example, to log allowed traffic to https://checkip.amazonaws.com, add the `alert` modifier keyword to a pass rule:

```
pass tls $HOME_NET any -> $EXTERNAL_NET any (ssl_state:client_hello; tls.sni; content:“checkip.amazonaws.com"; startswith; nocase; endswith; msg:"matching TLS allowlisted FQDNs"; flow:to_server; alert; sid:222222; rev:1;)
```

For more information about rule actions, see [Defining rule actions](rule-action.md "rule-action.md").

## I don't see Alert logs that match drop action rules in my rule group

A stateful rule sends alerts for specific rule actions (drop, alert, reject, and pass) that also include an `alert` modifier keyword.

Network Firewall can send alert logs to Amazon S3, CloudWatch, and Firehose.
Make sure you have enabled logging by [updating the firewall's logging configuration](firewall-update-logging-configuration.md "firewall-update-logging-configuration.md").
If you are using [strict evaluation order](suricata-rule-evaluation-order.md#suricata-strict-rule-evaluation-order "suricata-rule-evaluation-order.md#suricata-strict-rule-evaluation-order")
with a default action set to **Drop established**,
make sure you have also enabled an alert action so that the firewall will generate alert messages for this traffic.
You can select **Alert all** to log an alert message on all packets, or select **Alert established**
to log an alert message only on packets that are in established connections.
Flows dropped by the **Drop established** or **Drop all** stateful default actions won't generate alert logs
if you don't configure a stateful default alert action.

## I don’t see any TLS logs even though I have

TLS logging enabled

TLS logging reports only TLS errors and outbound traffic that fails certificate revocation checks.

Double check your firewall policy configuration. Your firewall policy must be configured
for [TLS inspection](tls-inspection-configurations.md "tls-inspection-configurations.md"). Additionally, for revocation check logging, your firewall must be configured with [outbound SSL/TLS inspection](tls-inspection-certificate-requirements.md#tls-inspection-certificate-requirements-outbound-inspection "tls-inspection-certificate-requirements.md#tls-inspection-certificate-requirements-outbound-inspection") enabled and [certificate
revocation status checking](tls-inspection-certificate-requirements.md#tls-inspection-check-certificate-revocation-status "tls-inspection-certificate-requirements.md#tls-inspection-check-certificate-revocation-status") enabled.

If your firewall policy is correctly configured, then it's possible that your traffic isn't generating anything for the logs.

- For TLS errors, currently the logs report SNI mismatches and naming errors. If your traffic doesn't have these errors, the logs might not report anything in this category.
- For revocation checks:

      + TLS inspection performs checks only on outbound traffic, and only for
       servers that you don't own or control.
      + TLS inspection only creates a log record when the check returns a status
       of `REVOKED` or `UNKNOWN`.

  If you don't have traffic of this type, or if the certificates for this type of
  traffic are all passing the revocation checks, Network Firewall won't log anything into your TLS logs for revocation checks.
