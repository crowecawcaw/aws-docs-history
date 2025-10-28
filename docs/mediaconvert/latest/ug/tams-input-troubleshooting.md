# Troubleshooting TAMS inputs

If you encounter issues when processing TAMS content, the following information can help you identify and resolve common problems:

**Authentication errors**

If your job fails with authentication errors, verify the following:

- Your EventBridge connection ARN is correct and accessible from your MediaConvert
  service role.
- The OAuth credentials in your EventBridge connection are valid and not
  expired.
- Your OAuth scopes include the required TAMS API permissions.
- Your TAMS server is accessible and responding to authentication requests.

**Source and flow errors**

If your job fails during source or flow processing, verify the following:

- The source ID is a valid UUID that exists on your TAMS server.
- The source is a multi-format source with valid flow references.
- The flows contain segments for your specified time range.
- The total number of segments doesn't exceed 10,000 per flow.

**Time range errors**

If your job fails with time range errors, verify the following:

- Your time range format follows the correct pattern:
  `[start:nanoseconds_end:nanoseconds]`.
  - For example: `[0:500000000_10:0]` – From 0.5 seconds (inclusive)
    to 10.0 seconds (inclusive)

- The end time is later than the start time.
- The time range corresponds to available content on your TAMS server.

**Network connectivity issues**

If your job fails with network errors, verify the following:

- Your TAMS server is accessible from the internet and not blocked by
  firewalls.
- Your server can handle concurrent requests from MediaConvert.
- Network latency between MediaConvert and your TAMS server is reasonable.
- Your server has sufficient bandwidth for segment downloads.
- Your TAMS server URL uses HTTPS protocol and contains only the base server path
  without source IDs or query parameters.

For detailed error information, check the job error messages in the MediaConvert console or API response. MediaConvert provides specific error codes for TAMS-related issues to help you identify the root cause:

**Error 3459: Invalid source format**

The master source format is not `urn:x-nmos:format:multi`. Verify that your source ID points to a valid multi-format source on your TAMS server.

**Error 3460: No flows found**

No video, audio, or multi flows were found for the specified source. Check that your source contains valid flows with proper format identifiers.

**Error 3461: No segments found**

No segments were found in the specified timerange. Verify that your time range corresponds to available content and that segments exist for the specified flows.

**Error 3462: Too many segments**

The flow contains more than 10,000 segments for the specified timerange. Use a shorter time range or split your content into multiple jobs.

**Error 3464: Missing segment properties**

A segment is missing required properties such as `get_urls`, `timerange`, or `url`. Verify that your TAMS server returns complete segment metadata and that your base server URL is correctly formatted with HTTPS protocol.

###### Note

If you continue to experience issues, verify that your TAMS server implements the BBC TAMS API specification correctly and that all required endpoints are available and functioning.
