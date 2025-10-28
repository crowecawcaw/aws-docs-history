# Setting up redirects and rewrites for an Amplify

application

Redirects enable a web server to reroute navigation from one URL to another. Common reasons
for using redirects include to customize the appearance of a URL, to avoid broken links, to
move the hosting location of an app or site without changing its address, and to change a
requested URL to the form needed by a web app.

## Understanding the redirects that Amplify

supports

Amplify supports the following redirect types in the console.

**Permanent redirect (301)**

301 redirects are intended for lasting changes to the destination of a web address.
Search engine ranking history of the original address applies to the new destination
address. Redirection occurs on the client-side, so a browser navigation bar shows the
destination address after redirection.

Common reasons to use 301 redirects include:

- To avoid a broken link when the address of a page changes.
- To avoid a broken link when a user makes a predictable typo in an address.

**Temporary redirect (302)**

302 redirects are intended for temporary changes to the destination of a web address.
Search engine ranking history of the original address doesn’t apply to the new destination
address. Redirection occurs on the client-side, so a browser navigation bar shows the
destination address after redirection.

Common reasons to use 302 redirects include:

- To provide a detour destination while repairs are made to an original
  address.
- To provide test pages for A/B comparison of a user interface.

###### Note

If your app is returning an unexpected 302 response, the error is likely caused
by changes you've made to your app’s redirect and custom header configuration. To
resolve this issue, verify that your custom headers are valid, and then re-enable
the default 404 rewrite rule for your app.

**Rewrite (200)**

200 redirects (rewrites) are intended to show content from the destination address as if
it were served from the original address. Search engine ranking history continues to apply
to the original address. Redirection occurs on the server-side, so a browser navigation bar
shows the original address after redirection. Common reasons to use 200 redirects
include:

- To redirect an entire site to a new hosting location without changing the address
  of the site.
- To redirect all traffic to a single page web app (SPA) to its index.html page for
  handling by a client-side router function.

**Not Found (404)**

404 redirects occur when a request points to an address that doesn’t exist. The
destination page of a 404 is displayed instead of the requested one. Common reasons a 404
redirect occurs include:

- To avoid a broken link message when a user enters a bad URL.
- To point requests to nonexistent pages of a web app to its index.html page for
  handling by a client-side router function.

## Understanding the order of redirects

Redirects are applied from the top of the list down. Make sure that your ordering has
the effect you intend. For example, the following order of redirects causes all requests
for a given path under _/docs/_ to redirect to
the same path under _/documents/_, except
_/docs/specific-filename.html_ which redirects
to _/documents/different-filename.html_:

```
/docs/specific-filename.html /documents/different-filename.html 301
/docs/<*> /documents/<*>
```

The following order of redirects ignores the redirection of _specific-filename.html_ to _different-filename.html_:

```
/docs/<*> /documents/<*>
/docs/specific-filename.html /documents/different-filename.html 301
```

## Understanding how Amplify forwards query

parameters

You can use query parameters for more control over your URL matches. Amplify forwards
all query parameters to the destination path for 301 and 302 redirects, with the following
exceptions:

- If the original address includes a query string set to a specific value, Amplify
  doesn't forward query parameters. In this case, the redirect only applies to requests
  to the destination URL with the specified query value.
- If the destination address for the matching rule has query parameters, query
  parameters aren't forwarded. For example, if the destination address for the redirect
  is `https://example-target.com?q=someParam`, query parameters aren't
  passed through.
