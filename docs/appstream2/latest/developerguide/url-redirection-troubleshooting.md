

# Troubleshooting
<a name="url-redirection-troubleshooting"></a>

**URLs not redirecting when expected**
+ Verify that the URL pattern includes the protocol (`https://`).
+ Check for typos in the pattern.
+ Verify that wildcards are used correctly.
+ Confirm that the feature is enabled on the stack.

**URLs redirecting when they are not expected to**
+ Add the URL pattern to the exception list.
+ Verify that exception list patterns are more specific than allowlist patterns.

**Local browser not launching**
+ Verify that the local device has a default browser configured.
+ Verify that the WorkSpaces Applications client is up to date.
+ Verify network connectivity on the local device.
+ On the web client, verify that popups are allowed on the streaming URL.