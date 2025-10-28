# MediaTailor ADS timeout ad skipping

troubleshooting

When ads are skipped with `ADS_TIMEOUT` or related reasons, you have
connectivity or performance issues with your ad decision server. AWS Elemental MediaTailor requires
reliable communication with your ADS to successfully insert ads. This troubleshooting
guide explains how to identify and resolve these connectivity issues.

## Common ADS connectivity issues

Common ADS connectivity issues include the following:

- Ad decision server not accessible from MediaTailor
- ADS not responding within the configured timeout period
- ADS unable to handle request volume during peak periods
- Network connectivity issues between MediaTailor and your ADS

## Resolution steps

To resolve ADS timeout issues:

1. Verify that your ad decision server is accessible from MediaTailor.
2. Check that your ADS responds within the configured timeout period.
3. Ensure your ADS can handle the request volume during peak periods.
4. Consider implementing a fallback ad strategy for when your primary ADS is
   unavailable.

## Monitoring ADS performance

Set up CloudWatch alarms for the `AdDecisionServer.Timeouts` metric to
proactively detect ADS connectivity issues.
