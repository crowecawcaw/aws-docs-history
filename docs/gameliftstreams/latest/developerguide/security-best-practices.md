

# Security best practices for Amazon GameLift Streams
<a name="security-best-practices"></a>

Amazon GameLift Streams provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don't represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions. 
+ At this time, the operating system and runtime environment for a stream group is updated only when you create a new stream group. To patch, update, and secure the operating system and other applications that are part of the runtime environment, we recommend that you recycle stream groups every two to four weeks, regardless of application updates.
+ **Treat stream URLs as secrets.** A stream URL grants temporary, unauthenticated access to start a stream session, so anyone who obtains the full stream URL can start a session until it expires, is revoked, or reaches its usage limit. To reduce exposure:
  + Handle each stream URL as a bearer credential. Distribute it only over trusted, encrypted channels, and never embed it in client-side code, logs, or public locations.
  + Use the shortest workable expiration. Set `UrlExpiresAfterMinutes` to the smallest value that fits your use case (the maximum is 1,440 minutes, or 24 hours).
  + Use the lowest workable usage limit. Set `UsageLimit` to the fewest activations you need (the default is 1). Each activation, including a page refresh, consumes one use.
  + Revoke stream URLs when you are done, or immediately if one might have been unintentionally shared. Use `REVOKE_AND_TERMINATE_SESSIONS` when you also want to end sessions that are already live; the default `REVOKE_URL` blocks new activations but leaves existing sessions running.
  + Monitor stream URL usage with `ListStreamUrls` and `GetStreamUrl`, and log the stream URL API operations with AWS CloudTrail. For more information, see [Logging Amazon GameLift Streams API calls using AWS CloudTrail](logging-using-cloudtrail.md).

  For more information, see [Share stream sessions with stream URLs](stream-urls.md).
+ [Best practices for security, identity, and compliance](https://aws.amazon.com/architecture/security-identity-compliance)