

# Share stream sessions with stream URLs
<a name="stream-urls"></a>

Stream URLs let you quickly share your stream sessions with anyone. Recipients access your stream sessions in a supported web browser, with no AWS account or client integration required, and you control expiration, usage, and revocation. After creating a stream URL anyone who accesses it starts their own stream session without needing any credentials. Stream URLs are ideal for quickly and easily setting up demos, playtests, stakeholder reviews, and guest access.

**Important**  
Anyone who has the full URL can start a stream session until the stream URL expires, reaches its usage limit, or is revoked. Treat the stream URL like a credential: share it only through trusted channels, prefer the shortest workable expiration and usage limit, and revoke it immediately if it leaks.

## How stream URLs work
<a name="stream-urls-how"></a>

A stream URL ties together a stream group (the capacity that runs the stream) and one application in that stream group (the content to run). When you create a stream URL, Amazon GameLift Streams returns a stream URL of the following form:

```
https://gameliftstreams.aws.com/su-1AB2C3De4/stream?token=EXAMPLETOKEN
```

The workflow has four steps:
+ **Create.** You call [CreateStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamUrl.html) for a stream group and application, setting how long the stream URL stays valid (`UrlExpiresAfterMinutes`) and how many times it can be used (`UsageLimit`). The stream session configuration – launch arguments, environment variables, session length, display resolution, and so on – is frozen into the stream URL at creation time.
+ **Share.** You distribute the stream URL through your own channels, such as email, chat, or an event page.
+ **Activate.** Each time a user opens the stream URL and starts streaming, Amazon GameLift Streams consumes one use of the stream URL and starts a brand-new stream session using the frozen configuration. Every activation is an independent session; there is no shared state between the people who use the same stream URL.
+ **End.** Sessions started from a stream URL are short-lived and do not support reconnection. When a session ends, its use has already been counted; re-opening the stream URL starts a new session and consumes another use.

Because the stream URL is unauthenticated, the end user never sees or needs your AWS credentials. The service routes each end user to a nearby location based on the streaming location preference you set at creation time. Amazon GameLift Streams reorders your preferred streaming locations by proximity but never adds locations you did not include.

## The end-user experience
<a name="stream-urls-end-user"></a>

Users you share a stream URL with do not need an AWS account or any software install. They open the URL in a supported web browser and stream from a webpage that Amazon GameLift Streams hosts for you. Streaming uses WebRTC and has the same browser and device requirements as the Amazon GameLift Streams Web SDK client. For the supported browsers and minimum versions, see [Amazon GameLift Streams compatible devices and browsers](compatible-devices-browsers.md). If the stream group has no capacity available when an end user opens the URL, the page shows a message that the stream is temporarily at capacity, and the end user can retry. If the end user tries to close or reload the tab, the page prompts them to confirm, because leaving the page ends the session.

**Note**  
Sessions started from a stream URL are tuned for short, single-viewer playback. If the end user loses their connection or reloads the page, the session ends, and re-opening the stream URL starts a new session that consumes another use. See [Differences from sessions you start with StartStreamSession](#stream-urls-differences).

## Prerequisites
<a name="stream-urls-prerequisites"></a>

Before you create a stream URL, you need the following:
+ A stream group that is active and has capacity to run sessions.
+ An application that is linked to that stream group.
+ IAM permission for the stream URL actions. Creating a stream URL also requires `gameliftstreams:StartStreamSession` permission for the application it points to, because activating the stream URL starts a stream session that runs that application. See the [Create and manage stream URLs](security_iam_id-based-policy-examples.md#create-and-manage-streamurls-iam) policy example.
+ If you pass an IAM role in `RoleArn`, you also need `iam:PassRole` permission for that role.

## Creating a stream URL
<a name="stream-urls-creating"></a>

**Note**  
You can create a stream URL in the Amazon GameLift Streams console, with the AWS CLI, or with the API. The following examples use the AWS CLI.

The following AWS CLI example creates a stream URL for an application in a stream group. The stream URL is valid for two hours and can be used up to five times, and it prefers the `us-west-2` and `us-east-1` locations.

```
aws gameliftstreams create-stream-url \
    --identifier sg-1AB2C3De4 \
    --application-identifier a-9ZY8X7Wv6 \
    --protocol WebRTC \
    --url-expires-after-minutes 120 \
    --usage-limit 5 \
    --locations us-west-2 us-east-1 \
    --description "Preview build - reviewer invites"
```

A successful call returns the stream URL resource, including its `StreamUrlId` (prefixed `su-`), its ARN, the full shareable `StreamUrl`, the computed expiration time, and the initial remaining uses.

```
{
    "StreamUrlId": "su-1AB2C3De4",
    "Arn": "arn:aws:gameliftstreams:us-west-2:111122223333:streamurl/sg-1AB2C3De4/su-1AB2C3De4",
    "StreamUrl": "https://gameliftstreams.aws.com/su-1AB2C3De4/stream?token=EXAMPLETOKEN",
    "Status": "ACTIVE",
    "UsageLimit": 5,
    "RemainingUses": 5,
    "ExpiresAt": "2026-07-31T20:00:00+00:00"
}
```

The following parameters are required:


| Parameter | Description | 
| --- | --- | 
| Identifier (stream group) | The stream group whose capacity runs the sessions. Provide the stream group ID or ARN. | 
| ApplicationIdentifier | The application in that stream group to stream. Provide the application ID or ARN. | 
| Protocol | The stream protocol. WebRTC is the only supported value. | 
| UrlExpiresAfterMinutes | How long the stream URL stays valid, in minutes, from creation. Minimum 1; maximum 1,440 (24 hours). After this window the stream URL becomes EXPIRED. | 
| Locations | Your preferred locations, as AWS Region codes such as us-west-2, in priority order. Amazon GameLift Streams reorders these by end-user proximity but never adds locations you did not list. | 

The following parameters are optional. Any session settings you provide are frozen into the stream URL at creation time and applied to every session started from the stream URL.


| Parameter | Description | 
| --- | --- | 
| UsageLimit | How many times the stream URL can start a session. Default 1; maximum 50. | 
| Description | A label for the stream URL, 1–80 characters. | 
| SessionLengthSeconds | Maximum length of each session started from the stream URL. | 
| AdditionalLaunchArgs | Command-line arguments passed to the application at launch. | 
| AdditionalEnvironmentVariables | Environment variables set for the application at launch. | 
| DisplayConfiguration (Resolution) | The stream display resolution, given as a Resolution with required Width and Height in pixels. Each dimension must be from 320 to 4096. When omitted, the service uses a default resolution. | 
| RoleArn | An IAM role whose credentials the application can use during each session. The role is frozen into every session the stream URL starts. Passing a role requires iam:PassRole permission for it. | 
| ClientToken | A unique, case-sensitive identifier that makes the create request idempotent, so a retry with the same token does not create a duplicate stream URL. | 

## Monitoring your stream URLs
<a name="stream-urls-monitoring"></a>

Use [GetStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamUrl.html) to retrieve a single stream URL. Specify the stream group with `--identifier` and the stream URL with `--stream-url-identifier` (a stream URL ID or ARN). In addition to the stream URL's configuration, current `Status`, and `RemainingUses`, the response includes a `StreamSessions` list of the sessions started from it, so you can see who is actively streaming.

```
aws gameliftstreams get-stream-url \
    --identifier sg-1AB2C3De4 \
    --stream-url-identifier su-1AB2C3De4
```

Use [ListStreamUrls](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamUrls.html) to enumerate the stream URLs in your account. You can filter by `Status` and by stream group, and page through results with `MaxResults` (1–100, default 25) and `NextToken`.

```
aws gameliftstreams list-stream-urls \
    --status ACTIVE \
    --stream-group-identifier sg-1AB2C3De4
```

You can also audit stream URL management activity in CloudTrail. CloudTrail records calls to `CreateStreamUrl`, `GetStreamUrl`, `ListStreamUrls`, and `RevokeStreamUrl` as data events. An end user opening a stream URL and starting a session is not one of your API calls and is not recorded as customer CloudTrail activity. For more information, see [Logging Amazon GameLift Streams API calls using AWS CloudTrail](logging-using-cloudtrail.md).

## Revoking a stream URL
<a name="stream-urls-revoking"></a>

Revoke a stream URL when you want to stop it from starting any more sessions, for example when a preview period ends or it might have been unintentionally shared.

[RevokeStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RevokeStreamUrl.html) takes a `RevocationMode`:


| RevocationMode | Effect | 
| --- | --- | 
| REVOKE\_URL (default) | The stream URL can no longer start new sessions. Sessions already in progress continue until they end on their own. | 
| REVOKE\_AND\_TERMINATE\_SESSIONS | The stream URL can no longer start new sessions, and all sessions currently running from it are terminated. When a running session is terminated this way, the end user is disconnected and sees a message that the stream is no longer available. | 

```
aws gameliftstreams revoke-stream-url \
    --identifier sg-1AB2C3De4 \
    --stream-url-identifier su-1AB2C3De4 \
    --revocation-mode REVOKE_AND_TERMINATE_SESSIONS
```

A revoked stream URL transitions to the `REVOKED` status and cannot be reactivated. Create a new stream URL if you need to resume sharing.

Amazon GameLift Streams also automatically revokes a stream URL when a resource it depends on is deleted. Deleting the stream group revokes all stream URLs on that stream group, and deleting the application revokes all stream URLs that reference that application. In both cases the stream URL moves to `REVOKED` with a status reason that identifies the deleted resource.

**Note**  
Removing a resource that a stream URL depends on is not the same as deleting it, and does not automatically revoke the stream URL. The stream URL stays `ACTIVE`, but every attempt to start a session from it fails. This happens if you unlink the stream URL's application from the stream group, or if you remove all of the stream group locations that the stream URL was created with. Only deleting the stream group or the application triggers automatic revocation.

## Stream URL lifecycle and status
<a name="stream-urls-lifecycle"></a>

A stream URL is `ACTIVE` when created and stays that way until it expires, runs out of uses, or is revoked. It never returns to `ACTIVE` after leaving that state.


| Status | Meaning | 
| --- | --- | 
| ACTIVE | The stream URL can start new sessions. | 
| EXPIRED | The UrlExpiresAfterMinutes window has elapsed. | 
| REVOKED | The stream URL was revoked, either explicitly with RevokeStreamUrl or automatically when its stream group or application was deleted. | 
| LIMIT\_REACHED | The stream URL has used all of its UsageLimit. | 

When a stream URL is `REVOKED`, `GetStreamUrl` and `ListStreamUrls` also return a status reason that explains why.


| Status reason | Cause | 
| --- | --- | 
| userRevoked | Revoked with RevokeStreamUrl using REVOKE\_URL. | 
| revokedAndTerminatingSessions | Revoked with REVOKE\_AND\_TERMINATE\_SESSIONS; running sessions are being terminated. | 
| revokedAndSessionsTerminated | Revoked with REVOKE\_AND\_TERMINATE\_SESSIONS; running sessions have been terminated. | 
| streamGroupDeleted | The stream group was deleted. | 
| applicationDeleted | The referenced application was deleted. | 

## Differences from sessions you start with StartStreamSession
<a name="stream-urls-differences"></a>

Sessions started from a stream URL run on the same infrastructure as sessions you start yourself, but they are tuned for short, hands-off, single-viewer playback. Keep these differences in mind:
+ **No reconnection.** If the end user loses their connection or reloads the page, the session ends.
+ **Re-visiting consumes another use.** Because there is no reconnection, opening the stream URL again starts a completely new session and consumes another use from its `UsageLimit`.
+ **No data channels.** Streams started from a stream URL do not expose application data channels. Build your own client with the Amazon GameLift Streams Web SDK if you need them.

## Troubleshooting
<a name="stream-urls-troubleshooting"></a>

Amazon GameLift Streams deliberately hides the specific reason for a failed stream URL activation from end users. An end user who opens a stream URL that cannot start a stream always sees a generic "not found" page or an "at capacity" message, regardless of the underlying cause. To diagnose the real cause, inspect the stream URL from the creator side with `GetStreamUrl` and `ListStreamUrls`, check the `Status` and status reason, and review stream URL API activity in CloudTrail.
+ **The stream URL shows a "not found" or generic error page.** Check the `Status` with `GetStreamUrl`. `EXPIRED`, `REVOKED`, or `LIMIT_REACHED` each explains a non-startable stream URL. If the status is `ACTIVE` but activations still fail, a resource the stream URL depends on was most likely removed (not deleted): the application was unlinked from the stream group, or all of the stream group locations the stream URL was created with were removed. Re-link the application or restore a location, or create a new stream URL against valid resources.
+ **The end user sees an "at capacity" message.** The stream group has no available capacity to place a new session in the end user's nearest location. Each activation starts a new session and consumes capacity like `StartStreamSession`. Increase minimum (always-on) or maximum capacity, or use target idle (pre-warmed) capacity to keep capacity ready ahead of demand, especially for time-boxed events.
+ **The session ends when the end user refreshes or navigates away.** This is expected. URL-activated sessions do not reconnect, and each visit starts a new session that consumes a use. Advise end users not to refresh, and set a `UsageLimit` high enough to tolerate occasional reloads.
+ **The end user is disconnected mid-session and sees "This experience is no longer available."** End users see this generic message whenever a session ends on the server side. The most common cause for a stream URL is revoking it with `REVOKE_AND_TERMINATE_SESSIONS`, which ends running sessions immediately, but the same message appears if the session reaches its configured length limit or is otherwise terminated by the service. This is expected. Create a new stream URL to resume sharing.
+ **The stream does not load or fails to start for the end user.** The end user's browser might not meet the streaming requirements. Streaming requires a browser that supports WebRTC and H.264 (AVC); see [Amazon GameLift Streams compatible devices and browsers](compatible-devices-browsers.md) for supported browsers and minimum versions. A common cause is opening the stream URL in an in-app browser view, such as a link tapped inside a chat, email, or social app on a mobile device, which can disable WebRTC. Advise recipients to open the stream URL in a standalone browser such as Chrome, Edge, or Safari.
+ **`CreateStreamUrl` returns `ServiceQuotaExceededException`.** The request would exceed an active-count limit (20 active stream URLs per account or 5 per stream group). Revoke stream URLs you no longer need to free headroom, and use `ListStreamUrls` filtered by `Status` set to `ACTIVE` to see your current count.
+ **`CreateStreamUrl` returns `ValidationException`.** An input value is out of range. Set `UsageLimit` to 1 through 50, and `UrlExpiresAfterMinutes` to 1 through 1,440.