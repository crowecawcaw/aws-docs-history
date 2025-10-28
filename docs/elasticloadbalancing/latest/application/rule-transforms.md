# Transforms for listener rules

A rule transform rewrites inbound requests before they are routed to targets.
Rewriting a request does not change the routing decision made when evaluating
the rule conditions. This is useful when clients send a different URL or host
header than what the targets expect.

Using rule transforms offloads the responsibility for modifying paths, query
strings, and host headers to the load balancer. This eliminates the need to
add custom modification logic to your application code or rely on a third-party
proxy to perform the modifications.

Application Load Balancers support the following transforms for listener rules.

###### Transforms

`host-header-rewrite`

Rewrites the host header in the request. The transform uses a regular
expression to match a pattern in the host header and then replaces it
with a replacement string.

`url-rewrite`

Rewrites the request URL. The transform uses a regular expression
to match a pattern in the request URL and then replaces it with a
replacement string.

###### Transform basics

- You can add one host header rewrite transform and one URL rewrite transform
  per rule.
- You can't add a transform to a default rule.
- If there is no pattern match, the original request is sent to the target.
- If there is a pattern match but the transform fails, we return an HTTP 500
  error.

## Host header rewrite transforms

You can modify the domain name specified in the host header.

###### Example host header transform

You can specify a transform when you create or modify a rule. For more
information, see the [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") and [modify-rule](../../../cli/latest/reference/elbv2/modify-rule.md "../../../cli/latest/reference/elbv2/modify-rule.md") commands. The following is an example host
header transform. It transforms the host header to an internal endpoint.

```
[
  {
      "Type": "host-header-rewrite",
      "HostHeaderRewriteConfig": {
          "Rewrites": [
              {
                  "Regex": "`^mywebsite-(.+).com$`",
                  "Replace": "`internal.dev.$1.myweb.com`"
              }
          ]
      }
  }
]
```

For example, this transform rewrites the host header
`https://mywebsite-example.com/project-a`
as
`https://internal.dev.example.myweb.com/project-a`.

## URL rewrite transforms

You can modify the path or the query string of the URL. By rewriting the URL at
the load balancer level, your frontend URLs can remain consistent for users and
search engines even if your backend services change. You can also simplify complex
URL query strings to make them easier for customers to type.

Note that you can't modify the protocol or port of the URL, only the path and the
query string.

###### Example URL rewrite transform

You can specify a transform when you create or modify a rule. For more
information, see the [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") and [modify-rule](../../../cli/latest/reference/elbv2/modify-rule.md "../../../cli/latest/reference/elbv2/modify-rule.md") commands. The following is an example URL rewrite
transform. It transforms the directory structure to a query string.

```
[
  {
      "Type": "url-rewrite",
      "UrlRewriteConfig": {
          "Rewrites": [
              {
                  "Regex": "`^/dp/([A-Za-z0-9]+)/?$`",
                  "Replace": "`/product.php?id=$1`"
              }
          ]
      }
  }
]
```

For example, this transform rewrites the request URL
`https://www.example.com/dp/B09G3HRMW`
as
`https://www.example.com/product.php?id=B09G3HRMW`.

**How URL rewrites differ from URL redirects**

| Characteristic | URL redirects                                             | URL rewrites                                                            |
| -------------- | --------------------------------------------------------- | ----------------------------------------------------------------------- |
| URL display    | Changes in the browser address bar                        | No change in the browser address bar                                    |
| Status codes   | Uses 301 (permanent) or 302 (temporary)                   | No status code change                                                   |
| Processing     | Browser-side                                              | Server-side                                                             |
| Common uses    | Domain change, website consolidation, fixing broken links | Clean URLs for SEO, hide complex structures, provide legacy URL mapping |
