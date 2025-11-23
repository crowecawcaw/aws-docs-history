# Step 1: Specify a Host Domain to Embedded Amazon WorkSpaces Applications Streaming Sessions

To embed an WorkSpaces Applications streaming session in a webpage, first update your stack to specify
the domain to host the embedded streaming session. This a security measure to ensure
that only authorized website domains can embed WorkSpaces Applications streaming sessions. WorkSpaces Applications adds
the domain or domains that you specify to the `Content-Security-Policy` (CSP) header. For
more information, see [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP "https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP") in the Mozilla [MDN Web Docs](https://developer.mozilla.org/en-US/ "https://developer.mozilla.org/en-US/") documentation.

To update your stack to specify
the domain to host the embedded streaming session,
use any of the following methods:

- The WorkSpaces Applications console
- The `EmbedHostDomains` API action
- The `embed-host-domains` AWS command line interface (AWS CLI) command
  To specify a host domain by using the WorkSpaces Applications console, perform the following steps.

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").
2. In the left navigation pane, choose **Stacks**, and select the stack that you want.
3. Choose **Edit**.
4. Expand **Embed WorkSpaces Applications (Optional)**.
5. In **Host Domains**, specify a valid domain. For example: `training.example.com`.

###### Note

Embedded streaming sessions are only supported over HTTPS [TCP port 443]. 6. Choose **Update**.
