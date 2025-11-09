# MediaTailor duration mismatch ad

skipping troubleshooting

When ads are skipped with `AVAIL_DURATION_EXCEEDED`,
`LEFTOVER_AVAIL_EXCEEDED_THRESHOLD`, or format-related reasons, you have
duration or format compatibility issues. AWS Elemental MediaTailor requires proper duration formatting
and matching between ad content and available ad break time. This troubleshooting guide
explains how to identify and resolve these duration-related issues.

## Common duration issues

Common duration issues include the following:

- Ads longer than available ad break duration
- Incorrect ad break markers in content signaling wrong duration
- Personalization threshold not met for ad insertion
- Incorrect duration format in EXT-X-CUE-OUT tags

## Duration format requirements

The EXT-X-CUE-OUT tag duration parameter must be formatted as an integer value,
not as an ISO 8601 duration format.

| Duration format requirements | Format   | Example                                      | Status |
| ---------------------------- | -------- | -------------------------------------------- | ------ |
| Integer (Correct)            | `32`     | Supported<br>• represents 32 seconds         |
| Decimal (Correct)            | `30.000` | Supported<br>• represents 30 seconds         |
| ISO 8601 (Incorrect)         | `PT32S`  | Not supported<br>• causes insertion failures |

## Resolution steps

To resolve duration mismatch issues:

1. Ensure your ADS returns ads that fit within the available ad break
   duration.
2. Check that your ad break markers in the content correctly signal the
   intended duration.
3. Verify that EXT-X-CUE-OUT duration parameters use integer format.
4. Consider adjusting the personalization threshold if appropriate for your
   use case.
