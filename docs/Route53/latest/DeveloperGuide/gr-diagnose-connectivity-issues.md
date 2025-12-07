# Diagnose DNS connectivity issues with

Route 53 Global Resolver

Route 53 Global Resolver provides reliable DNS resolution, but connectivity issues can occasionally occur
due to configuration, authentication, or network problems. When client devices cannot resolve
domain names using Route 53 Global Resolver, use these systematic approaches to identify and resolve connectivity
problems.

## Client devices cannot resolve

domains

Follow these steps to diagnose resolution failures:

1. **Verify queries reach the global resolver**
   - Check DNS query logs for queries from the affected client device IP address
   - Confirm the client device is configured with the correct anycast IP addresses
   - Test network connectivity from the client device to the anycast IPs

2. **Check client device authentication**
   - Verify the client device is authenticated to the correct DNS view
   - Check Access Source rules for the client device's IP address or CIDR block
   - Confirm access tokens are valid and not expired (for token-based authentication)

3. **Review firewall rules**
   - Check if firewall rules are blocking the queries
   - Review rule priority and ensure allow rules have higher priority than block
     rules
   - Verify firewall fail-open behavior settings

4. **Confirm DNS view associations**
   - Verify private hosted zone associations for internal domains
   - Check that DNS records exist in the associated private hosted zones
   - Ensure domain names in queries exactly match zone names

## Intermittent resolution failures

For sporadic DNS resolution issues, investigate these potential causes:

Authentication issues

- Check for access token expiration and renewal patterns
- Review authentication logs for failed authentication attempts
- Verify client device clock synchronization for token validation

Network connectivity

- Monitor for network path changes or routing issues
- Check for firewall or NAT device configuration changes
- Verify consistent anycast routing to the nearest Region

Service health

- Check AWS Service Health Dashboard for Route 53 Global Resolver issues
- Review CloudWatch metrics for error rate spikes
- Monitor private hosted zone association status

## Unexpected public resolution

When queries resolve to public DNS instead of private hosted zones:

1. **Verify private hosted zone configuration**
   - Confirm the private hosted zone contains the expected DNS records
   - Check that record names exactly match the queried domain
   - Verify record types match the query type (A, AAAA, CNAME, etc.)

2. **Check DNS view associations**
   - Verify the private hosted zone is associated with the correct DNS view
   - Confirm the client device is authenticated to the DNS view
   - Check association status in the console

3. **Review firewall rules**
   - Check for firewall rules that might be blocking private zone queries
   - Verify rule evaluation order and priority
   - Review DNS query logs for firewall actions
