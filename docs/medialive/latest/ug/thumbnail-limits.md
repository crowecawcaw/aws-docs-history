# Limit on thumbnails in MediaLive

There is a limit to the number of MediaLivethumbnails that you can view or retrieve. The
limit is:

`A number of API transactions per second, per account, in one
 Region`

The transaction limit is shared by all thumbnails — those that you
display on the console, and those that you retrieve using an AWS
API. For the current limit, see the MediaLive page in the [Service Quotas](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/medialive/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/medialive/quotas") console.

On the console, a thumbnail is generated for a channel only when
the channel details page is displayed, and only in the active tab
(meaning only for one pipeline in the channel). For the relevant
pipelines, MediaLive makes a call to the API approximately every 2
seconds.
