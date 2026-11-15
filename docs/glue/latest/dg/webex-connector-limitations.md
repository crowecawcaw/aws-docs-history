

# Limitations and notes for the Webex connector
<a name="webex-connector-limitations"></a>

The following are limitations and notes for the Webex connector:
+ Webex is supported as a source only. Writing to Webex is not supported.
+ To read `messages` from group spaces, use a user access token. Webex requires bots to filter messages in group spaces by `mentionedPeople`, which this connector doesn't send.
+ Job bookmarks are not supported.