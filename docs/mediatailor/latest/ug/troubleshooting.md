

# Troubleshooting MediaTailor
<a name="troubleshooting"></a>

If you encounter playback errors or similar difficulties when working with AWS Elemental MediaTailor, consult the topics in this section.

**Topics**
+ [Troubleshooting MediaTailor event flow issues](troubleshooting-event-flow.md)
+ [Troubleshooting playback from MediaTailor](playback-errors.md)
+ [Beacon deduplication](#troubleshooting-beacon-deduplication)
+ [Parameter troubleshooting](#parameter-troubleshooting-reference)
+ [MediaTailor ad skipping troubleshooting guide](troubleshooting-ad-skipping-overview.md)

## Beacon deduplication
<a name="troubleshooting-beacon-deduplication"></a>

This section provides troubleshooting guidance for MediaTailor's beacon deduplication feature in server-side tracking.

Symptom: Lower beacon counts than previously observed  
**Cause**: Beacon deduplication is preventing duplicate events that were previously being counted multiple times.  
**Resolution**: This is expected behavior and indicates more accurate measurement. The new counts represent actual ad viewing events rather than technical segment requests. Update your reporting baselines to reflect the deduplicated counts.

Symptom: Beacon counts vary between different player implementations  
**Cause**: Different players may have varying segment request patterns, but deduplication ensures consistent beacon counts regardless of these differences.  
**Resolution**: This is expected behavior. Deduplication provides consistent measurement across different player types and network conditions.

Symptom: Discrepancy between expected and actual beacon counts  
**Cause**: Previous expectations may have been based on inflated counts due to duplicate beacon firing.  
**Resolution**: Review historical data to identify patterns of duplicate beacons. Use the new deduplicated counts as the accurate baseline for measurement and reporting.

## Parameter troubleshooting
<a name="parameter-troubleshooting-reference"></a>

For troubleshooting issues related to dynamic ad variables, manifest query parameters, character restrictions, length limitations, and configuration aliases, see [MediaTailor parameter troubleshooting guide](parameter-troubleshooting.md) in [MediaTailor dynamic ad variables for ADS requests](variables.md).