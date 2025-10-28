# Step 1: Specify a Host Domain to Embedded Amazon AppStream 2.0 Streaming Sessions

To embed an AppStream 2.0 streaming session in a webpage, first update your stack to specify
the domain to host the embedded streaming session. This a security measure to ensure
that only authorized website domains can embed AppStream 2.0 streaming sessions. AppStream 2.0 adds
the domain or domains that you specify to the `Content-Security-Policy` (CSP) header. For
more information, see [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP "https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP") in the Mozilla [MDN Web Docs](https://developer.mozilla.org/en-US/ "https://developer.mozilla.org/en-US/") documentation.

To update your stack to specify
the domain to host the embedded streaming session,
use any of the following methods:

- The AppStream 2.0 console
- The `EmbedHostDomains` API action
- The `embed-host-domains` AWS command line interface (AWS CLI) command
  To specify a host domain by using the AppStream 2.0 console, perform the following steps.

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Stacks**, and select the stack that you want.
3. Choose **Edit**.
4. Expand **Embed AppStream 2.0 (Optional)**.
5. In **Host Domains**, specify a valid domain. For example: `training.example.com`.

###### Note

Embedded streaming sessions are only supported over HTTPS [TCP port 443]. 6. Choose **Update**.
