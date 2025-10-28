# Limitations and notes for Facebook Ads connector

The following are limitations or notes for the Facebook Ads connector:

- As Facebook Ads supports dynamic metadata, all fields can be queried. All the fields support filtration and records are fetched if the data is available, or else Facebook returns a Bad request (400) response with a proper error message.
- An app's call count is the number of calls a user can make during a rolling one-hour window 200 multiplied by the number of users. For rate limit details, see [Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/ "https://developers.facebook.com/docs/graph-api/overview/rate-limiting/"), and [Business Use Case Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#buc-rate-limits "https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#buc-rate-limits").
