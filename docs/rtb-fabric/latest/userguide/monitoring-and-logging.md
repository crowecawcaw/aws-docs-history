

# Monitoring and logging
<a name="monitoring-and-logging"></a>

Use gateway-level operational logs and metrics to monitor inbound external links with custom domains. For general monitoring guidance, see Monitoring RTB Fabric.

## Recommended monitoring checks
<a name="recommended-monitoring-checks"></a>
+ **Resolved link ID per request.** Verify that incoming requests are routed to the expected link by inspecting the link ID in gateway operational logs.
+ **(HTTPS only) TLS certificate selection.** Confirm that the correct customer certificate is served for your custom domain by monitoring TLS handshake outcomes in gateway logs.
+ **Rule evaluation outcomes.** Check that routing rules are matching as expected. If requests return 404 responses, verify that rule conditions cover the incoming traffic patterns.
+ **Gateway-level metrics.** Use Amazon CloudWatch metrics to track request rates, latency, and error rates at the gateway level.

**Note**  
Custom domain–specific metrics (such as per-rule match counts or certificate resolution breakdowns) are not yet emitted separately. Use gateway-level logs and metrics for debugging. See the Supported and unsupported features table for details.