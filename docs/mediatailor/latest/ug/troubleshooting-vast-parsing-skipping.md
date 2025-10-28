# MediaTailor VAST parsing ad skipping

troubleshooting

When ads are skipped with `VAST_PARSING_ERROR` or
`MEDIA_FILE_UNAVAILABLE`, you have issues with your VAST responses or ad
media files. AWS Elemental MediaTailor requires properly formatted VAST responses and accessible media
files for successful ad insertion. This troubleshooting guide explains how to identify
and resolve these issues.

## Common VAST issues

Common VAST issues include the following:

- VAST response format not compliant with VAST specification
- Media file URLs in VAST response not publicly accessible
- Special characters not properly encoded in VAST XML
- VAST response missing required media files or formats

## Resolution steps

To resolve VAST parsing issues:

1. Validate your VAST response format against the VAST specification.
2. Ensure all media file URLs in the VAST response are publicly
   accessible.
3. Check for proper encoding of special characters in your VAST XML.
4. Verify that your VAST response includes media files in formats compatible
   with MediaTailor.

## VAST wrapper troubleshooting

For issues with `INVALID_VAST_WRAPPER_AD` or
`REJECTED_REPLICA_VAST`:

- Validate VAST wrapper responses against the VAST specification
- Ensure all wrapper elements are properly formatted and contain valid
  VASTAdTagURI
- Check ad server configuration for duplicate content detection
  policies
- Ensure VAST responses contain unique creative content within the same
  session
