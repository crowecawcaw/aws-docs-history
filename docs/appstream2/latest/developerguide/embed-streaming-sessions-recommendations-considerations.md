# Recommendations and Usage Considerations for Embedding Amazon AppStream 2.0 Streaming Sessions

Consider the following recommendations and usage notes for embedded AppStream 2.0 streaming sessions.

- To maintain maximum control over the embedded AppStream 2.0 streaming
  experience for your users, we recommend that you configure short-lived streaming
  URLs that last approximately 5 seconds. Any user can inspect the contents of a
  webpage and view its source. This includes the document object model (DOM) and
  the src (source) URL of the iframe. If the URL is still valid when a user copies
  it, that user can paste the URL in a separate browser tab and stream the session
  with the standard AppStream 2.0 portal user interface, without the embed
  options.
- Concurrent sessions are not supported when custom domains are used for embedded AppStream 2.0
  streaming sessions. Concurrent sessions occur when users start two embedded
  AppStream 2.0 streaming sessions either on the same webpage or across two different
  browser tabs. You can't have a single user with concurrent sessions, but you can
  have multiple users. For example, a user logs into your app, your app generates
  a streaming URL to give to the customer (which counts as a unique user for
  billing), a customer loads the streaming URL, and the customer is assigned to an
  appstream instance within your specified pool.
