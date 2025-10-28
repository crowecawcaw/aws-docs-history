# Fix CDN session management and tracking issues

for MediaTailor

AWS Elemental MediaTailor content delivery network (CDN) session management is critical for proper ad
personalization and tracking. If you encounter session-related errors or inconsistent
behavior across requests:

1.  Check for session ID consistency:
    - Verify that your player maintains the same session ID across all
      requests for a single playback session
    - Check CDN logs to confirm session IDs are being forwarded
      correctly
    - Ensure session IDs are properly URL-encoded in query parameters
    - Use CloudWatch Logs to verify session ID consistency across requests (see
      validation steps below)

2.  Validate session initialization:
    - Confirm that the first manifest request successfully creates a
      session
    - Check for proper session parameter forwarding (for example,
      `aws.sessionId`)
    - Verify session initialization using debug logs (see debug log setup
      below)

3.  Enable debug logging for detailed session troubleshooting:
    - **For server-side reporting:** Add
      `?aws.logMode=DEBUG` to your playback request:

    ```
    GET <mediatailorURL>/v1/master/<hashed-account-id>/<origin-id>/<asset-id>?aws.logMode=DEBUG
    ```

    - **For client-side reporting:** Include
      `"logMode": "DEBUG"` in your session initialization
      request body
    - **Important:** The `DEBUG`
      value is case-sensitive
    - Maximum of 10 active debug sessions allowed simultaneously

4.  Use CloudWatch Logs queries to validate session behavior:

        * **Verify debug session is
         active:**



        ```
        fields @timestamp, @message

    | filter sessionId = "your-session-id-here"
    | filter eventType = "SESSION_INITIALIZED" # client-side reporting or mediaTailorPath like "/v1/master" # server-side reporting HLS or mediaTailorPath like "/v1/dash" # server-side reporting DASH `<br>• **View all events for a session:**` fields @timestamp, @message, eventType, mediaTailorPath
    | filter sessionId = "your-session-id-here"
    | sort @timestamp asc `<br>• **Check manifest generation for a session:**` fields @timestamp, responseBody, @message
    | filter mediaTailorPath like "/v1/master/" and eventType = "GENERATED_MANIFEST" and sessionId = "your-session-id-here" ```5. Test session parameter forwarding through CDN: <br>• Test manifest requests with session parameters directly against MediaTailor (bypassing CDN) <br>• Compare session behavior with and without CDN to identify forwarding issues <br>• Verify CDN query parameter forwarding configuration includes session-related parameters <br>• Check that CDN doesn't cache responses that should be session-specific **Common session error messages:** <br>•`ConflictException`(HTTP 409) - Multiple simultaneous playlist requests for the same session. **Solution:** Ensure your player requests playlists one at a time according to HLS specification <br>•`NotFoundException`(HTTP 404) - Session is unavailable or configuration doesn't exist. **Solution:** Check your configuration validity and reinitialize the session <br>•`BadRequestException`(HTTP 400) - Invalid session ID or improperly formatted request. **Solution:** Verify request formatting and session ID validity **Additional troubleshooting resources:** <br>• For complete debug logging setup and field reference, see [Generating AWS Elemental MediaTailor debug logs](debug-log-mode.md "debug-log-mode.md") <br>• For CloudWatch Logs query examples and log analysis, see [Writing AWS Elemental MediaTailor logs directly to Amazon CloudWatch Logs](monitoring-cw-logs.md "monitoring-cw-logs.md") <br>• For CDN query parameter forwarding configuration, see [Set up CDN routing behaviors for MediaTailor](cdn-routing-behaviors.md "cdn-routing-behaviors.md") <br>• For comprehensive error code reference, see [Troubleshooting playback from MediaTailor](playback-errors.md "playback-errors.md") **Success criteria:** When resolved, sessions should initialize correctly, maintain consistent session IDs across requests, and debug logs should show proper`SESSION_INITIALIZED` events and manifest generation without errors.
