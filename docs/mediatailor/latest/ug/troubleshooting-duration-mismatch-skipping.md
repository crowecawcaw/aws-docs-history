

# MediaTailor duration mismatch ad skipping troubleshooting
<a name="troubleshooting-duration-mismatch-skipping"></a>

When ads are skipped with `AVAIL_DURATION_EXCEEDED`, `LEFTOVER_AVAIL_EXCEEDED_THRESHOLD`, or format-related reasons, you have duration or format compatibility issues. AWS Elemental MediaTailor requires proper duration formatting and matching between ad content and available ad break time. This troubleshooting guide explains how to identify and resolve these duration-related issues.

## Common duration issues
<a name="duration-mismatch-causes"></a>

Common duration issues include the following:
+ Ads longer than available ad break duration
+ Incorrect ad break markers in content signaling wrong duration
+ Personalization threshold not met for ad insertion
+ Incorrect duration format in EXT-X-CUE-OUT tags

## Duration format requirements
<a name="duration-format-requirements"></a>

The EXT-X-CUE-OUT tag duration parameter must be formatted as an integer value, not as an ISO 8601 duration format.


**Duration format requirements**  

| Format | Example | Status | 
| --- | --- | --- | 
| Integer (Correct) | 32 | Supported - represents 32 seconds | 
| Decimal (Correct) | 30.000 | Supported - represents 30 seconds | 
| ISO 8601 (Incorrect) | PT32S | Not supported - causes insertion failures | 

## Resolution steps
<a name="duration-mismatch-resolution"></a>

To resolve duration mismatch issues:

1. Ensure your ADS returns ads that fit within the available ad break duration.

1. Check that your ad break markers in the content correctly signal the intended duration.

1. Verify that EXT-X-CUE-OUT duration parameters use integer format.

1. Consider adjusting the personalization threshold if appropriate for your use case.