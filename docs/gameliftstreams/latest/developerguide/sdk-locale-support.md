# Locale preference

In Amazon GameLift Streams, you can set the locale preference per stream. This is useful if your application retrieves location-specific information
from the end user's operating system, such as time or currency.

Amazon GameLift Streams supports the following languages:

| Value         | Description            |
| ------------- | ---------------------- |
| `en_US`       | U.S. English (default) |
| `ja_jp.UTF-8` | Japanese               |

**To change the locale setting**

When you call [StartStreamSession](../apireference/API_StartStreamSession.md "../apireference/API_StartStreamSession.md") using the
Amazon GameLift Streams API, add `LANG=`<language>``to your`AdditionalEnvironmentVariables`. Since
locale preference is unique per user, you set this at the stream-session level. If you don't set this, the stream uses U.S. English by
default.

###### Example

```
aws gameliftstreams start-stream-session \
   --identifier `arn:aws:gameliftstreams:us-west-2:123456789012:streamgroup/1AB2C3De4` \
   --protocol `WebRTC` \
   --signal-request "`[webrtc-ice-offer json string]`" \
   --user-id `xnshijwh` \
   --additional-environment-variables '{"LANG": "`ja_JP.UTF-8`"}'
```
