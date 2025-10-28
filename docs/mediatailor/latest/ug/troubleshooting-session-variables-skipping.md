# MediaTailor session variable ad

skipping troubleshooting

Session variables play a critical role in ad targeting and selection in AWS Elemental MediaTailor.
Incorrect session variable configuration is a common cause of ad skipping issues. This
comprehensive troubleshooting guide explains how to identify and resolve session
variable problems that can prevent successful ad insertion.

## Common session variable issues

Common session variable issues include the following:

- **Missing required variables**: Your ad
  decision server might require specific variables that aren't being
  provided.
- **Incorrect variable syntax**: Variables must
  use the correct syntax (for example, `[session.id]` instead of
  `${session.id}`).
- **URL encoding issues**: Special characters
  in variable values might need proper URL encoding.
- **Inconsistent player parameters**: Player
  parameters must be consistently passed across sessions.
- **Dynamic variable resolution failures**:
  Variables that can't be resolved are replaced with empty strings.
- **SCTE-35 UPID parsing issues**: Problems
  with segmentation UPID processing can cause session variable resolution
  failures.

## Verifying session variable

resolution

To verify that your session variables are being properly resolved:

1. Enable debug logging for your MediaTailor configuration
2. Check the `MediaTailor/AdDecisionServerInteractions` log group
   for the actual ADS request URLs
3. Verify that all variables in the template URL have been replaced with
   appropriate values
4. Look for any variables that were replaced with empty strings, which may
   indicate resolution failures

## SCTE-35 UPID parsing

troubleshooting

Problems with SCTE-35 segmentation UPID processing can cause session variable
issues:

- **Format requirements:** UPID must have
  `segmentation_upid_type` of 12 and include
  `format_identifier` for proper processing
- **Parsing rules:** Decoded UPID can contain
  colon delimiters for multiple values. The number of template variables and
  decoded UPID tokens must be equal
- **Invalid formats:** Avoid double colons with
  no values (e.g., `::` or `:46175218::4053`) as these
  cause parsing failures
