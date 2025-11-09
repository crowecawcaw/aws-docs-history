AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Available endpoints for user when building URLs

This topic lists the URLs with root paths for endpoints. Each web application below is
defining a **root path**, shared by all endpoints. **Each endpoint then adds its own dedicated path**. The resulting URL to use
is the result of the concatenation of the paths. For instance, considering the first endpoint for
the Gapwalk application, we have:

- `/gapwalk-application` for the root web-application path.
- `/scripts` for the dedicated endpoint path.
  The resulting URL to use will be `http://`server`:`port`/gapwalk-application/scripts`

**server**

points at the server name (the one hosting the given web-application).

**port**

the port exposed by the server.
