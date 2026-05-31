# CheckVoiceId

Checks the enrollment status, voice authentication or fraud detection results of the
voice analysis returned by Voice ID.

## Parameter object

```
{
 "CheckVoiceIdOption": "enrollmentStatus"
}
```

```
{
 "CheckVoiceIdOption": "voiceAuthentication"
}
```

```
{
 "CheckVoiceIdOption": "fraudDetection"
}
```

## Execution results and conditions

The checkVoiceId action returns results of the voice analysis and the status
returned by Voice ID. The following is returned when CheckVoiceIdOption input is set
as:

- **enrollmentStatus**:

      + **Enrolled**: The caller is enrolled in voice
       authentication.
      + **Not enrolled**: The caller has not yet been
       enrolled in voice authentication. When this status is returned, for
       example, you may want to directly route the call to an agent for
       enrollment.
      + **Opted out**: The caller has opted out of voice
       authentication.

  You are not charged for checking enrollment status.

- **voiceAuthentication**:

      + **Authenticated**: The caller's identity has been
       verified. That is, the authentication score is greater than or equal
       to the threshold (default threshold of 90 or your custom
       threshold).
      + **Not authenticated**: The authentication score
       is lower than threshold that you configured.
      + **Inconclusive**: Unable to analyze a caller's
       speech for authentication. This is usually because Voice ID did not
       get the required 10 seconds to provide a result for authentication.
      + **Not enrolled**: The caller has not yet been
       enrolled in voice authentication. When this status is returned, for
       example, you may want to directly route the call to an agent for
       enrollment.
      + **Opted out**: The caller has opted out of voice
       authentication.

  You are not charged if the result is **Inconclusive**,
  **Not enrolled** or **Opted
  out**.

- **fraudDetection**:
  - **High risk**: The risk score meets or exceeds
    the set threshold.
  - **Low risk**: The risk score did not meet the set
    threshold.
  - **Inconclusive**: Unable to analyze a caller's
    voice for detection of fraudsters in a watchlist.

## Errors

- NoMatchingError if no condition matches.

## Restrictions

Only supported for voice channel. If used with the chat or task channels, the
action takes the **Error** branch.

## Corresponding block in the UI

[Check Voice ID](../adminguide/check-voice-id.md "../adminguide/check-voice-id.md")
