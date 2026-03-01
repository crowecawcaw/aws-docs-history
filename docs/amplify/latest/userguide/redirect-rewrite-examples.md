# Redirects and rewrites example reference

This section provides examples for a variety of common redirect scenarios.

###### Important

Domain-specific redirects do not support path components in the source field.

**Supported**:

- `"source": "https://example.com"` (paths automatically
  appended)
  **Not Supported**:

- `"source": "https://example.com/specific-path"`
- Rules with `domain+path` combinations are not currently
  supported.
  **Alternative Patterns**

For domain-specific path redirects, use:

1. Separate domain-only rules (paths are automatically appended)
2. Path-only rules with conditional logic
3. Multiple rule combinations
   You can use these examples to understand the JSON syntax for creating your own redirects
   and rewrites in the Amplify console JSON editor.

###### Note

Original address domain matching is case-insensitive.

###### Topics

- [Simple redirects and rewrites](#simple-redirects-and-rewrites "#simple-redirects-and-rewrites")
- [Redirects for single page web apps (SPA)](#redirects-for-single-page-web-apps-spa "#redirects-for-single-page-web-apps-spa")
- [Reverse proxy rewrite](#reverse-proxy-rewrite "#reverse-proxy-rewrite")
- [Trailing slashes and clean URLs](#trailing-slashes-and-clean-urls "#trailing-slashes-and-clean-urls")
- [Placeholders](#placeholders "#placeholders")
- [Query strings and path parameters](#query-strings-and-path-parameters "#query-strings-and-path-parameters")
- [Region-based redirects](#region-based-redirects "#region-based-redirects")
- [Using wildcard expressions in redirects and rewrites](#wildcard-redirects "#wildcard-redirects")

## Simple redirects and rewrites

You can use the following example to permanently redirect a specific page to a new
address.

| Original address | Destination Address | Redirect Type              | Country Code |
| ---------------- | ------------------- | -------------------------- | ------------ |
| `/original.html` | `/destination.html` | `permanent redirect (301)` |              |

JSON format

```
[
  {
    "source": "/original.html",
    "status": "301",
    "target": "/destination.html",
    "condition": null
  }
]
```

You can use the following example to redirect any path under a folder to the same path
under a different folder.

| Original address | Destination Address | Redirect Type              | Country Code |
| ---------------- | ------------------- | -------------------------- | ------------ |
| `/docs/<*>`      | `/documents/<*>`    | `permanent redirect (301)` |              |

JSON format

```
[
  {
    "source": "/docs/<*>",
    "status": "301",
    "target": "/documents/<*>",
    "condition": null
  }
]
```

You can use the following example to redirect all traffic to index.html as a rewrite. In
this scenario, the rewrite makes it appear to the user that they have arrived at the
original address.

| Original address | Destination Address | Redirect Type   | Country Code |
| ---------------- | ------------------- | --------------- | ------------ |
| `/<*>`           | `/index.html`       | `rewrite (200)` |              |

JSON format

```
[
  {
    "source": "/<*>",
    "status": "200",
    "target": "/index.html",
    "condition": null
  }
]
```

You can use the following example to use a rewrite to change the subdomain that appears
to the user.

| Original address       | Destination Address        | Redirect Type   | Country Code |
| ---------------------- | -------------------------- | --------------- | ------------ |
| `https://mydomain.com` | `https://www.mydomain.com` | `rewrite (200)` |              |

JSON format

```
[
  {
    "source": "https://mydomain.com",
    "status": "200", "target": "https://www.mydomain.com",
    "condition": null
  }
]
```

You can use the following example to redirect to a different domain with a path
prefix.

| Original address       | Destination Address                  | Redirect Type              | Country Code |
| ---------------------- | ------------------------------------ | -------------------------- | ------------ |
| `https://mydomain.com` | `https://www.mydomain.com/documents` | `temporary redirect (302)` |              |

JSON format

```
[
  {
    "source": "https://mydomain.com",
    "status": "302",
    "target": "https://www.mydomain.com/documents/",
    "condition": null
  }
]
```

You can use the following example to redirect paths under a folder that can’t be found
to a custom 404 page.

| Original address | Destination Address | Redirect Type     | Country Code |
| ---------------- | ------------------- | ----------------- | ------------ |
| `/<*>`           | `/404.html`         | `not found (404)` |              |

JSON format

```
[
  {
    "source": "/<*>",
    "status": "404",
    "target": "/404.html",
    "condition": null
  }
]
```

###### Important

Path components in domain-based source rules (such as
`"https://domain.com/path"`) are not supported and will cause the rule
to be ignored without error.

## Redirects for single page web apps (SPA)

Most SPA frameworks support HTML5 history.pushState() to change browser location without
initiating a server request. This works for users who begin their journey from the root (or
_/index.html_), but fails for users who
navigate directly to any other page.

The following example uses regular expressions to set up a 200 rewrite for all files to
index.html, except for the file extensions specified in the regular expression.

| Original address | Destination Address | Redirect Type | Country Code |
| ---------------- | ------------------- | ------------- | ------------ | --- | --- | --- | --- | --- | ---- | ----- | --- | --- | ---- | ------------------ | ------------- | ----- | --- |
| `</^[^.]+$       | \.(?!(css           | gif           | ico          | jpg | js  | png | txt | svg | woff | woff2 | ttf | map | json | webp)$)([^.]+$)/>` | `/index.html` | `200` |     |

JSON format

```
[
  {
    "source": "</^[^.]+$|\.(?!(css|gif|ico|jpg|js|png|txt|svg|woff|woff2|ttf|map|json|webp)$)([^.]+$)/>",
    "status": "200",
    "target": "/index.html",
    "condition": null
  }
]
```

## Reverse proxy rewrite

The following example uses a rewrite to proxy content from another location so that it
appears to the user that the domain hasn’t changed. HTTPS is the only protocol supported for reverse proxies.

| Original address | Destination Address                  | Redirect Type   | Country Code |
| ---------------- | ------------------------------------ | --------------- | ------------ |
| `/images/<*>`    | `https://images.otherdomain.com/<*>` | `rewrite (200)` |              |

JSON format

```
[
  {
    "source": "/images/<*>",
    "status": "200",
    "target": "https://images.otherdomain.com/<*>",
    "condition": null
  }
]
```

## Trailing slashes and clean URLs

To create clean URL structures like _about_
instead of _about.html_, static site generators
such as Hugo generate directories for pages with an index.html (_/about/index.html_). Amplify automatically creates
clean URLs by adding a trailing slash when required. The table below highlights different
scenarios:

| User inputs in browser                 | URL in the address bar | Document served     |
| -------------------------------------- | ---------------------- | ------------------- |
| `/about`                               | `/about`               | `/about.html`       |
| `/about (when about.html returns 404)` | `/about/`              | `/about/index.html` |
| `/about/`                              | `/about/`              | `/about/index.html` |

## Placeholders

You can use the following example to redirect paths in a folder structure to a matching
structure in another folder.

| Original address                       | Destination Address                         | Redirect Type              | Country Code |
| -------------------------------------- | ------------------------------------------- | -------------------------- | ------------ |
| `/docs/<year>/<month>/<date>/<itemid>` | `/documents/<year>/<month>/<date>/<itemid>` | `permanent redirect (301)` |              |

JSON format

```
[
  {
    "source":  "/docs/<year>/<month>/<date>/<itemid>",
    "status": "301",
    "target": "/documents/<year>/<month>/<date>/<itemid>",
               "condition": null
   }
]
```

## Query strings and path parameters

###### Warning

Don’t include secrets, credentials, or sensitive data in URLs as path or query
parameters. These values are viewable in plain text in your Amplify application’s
access logs.

You can use the following example to redirect a path to a folder with a name that
matches the value of a query string element in the original address:

| Original address             | Destination Address                  | Redirect Type              | Country Code |
| ---------------------------- | ------------------------------------ | -------------------------- | ------------ |
| `/docs?id=<my-blog-id-value` | `/documents/<my-blog-post-id-value>` | `permanent redirect (301)` |              |

JSON format

```
[
  {
    "source": "/docs?id=<my-blog-id-value>",
    "status": "301",
    "target": "/documents/<my-blog-id-value>",
    "condition": null
  }
]
```

###### Note

Amplify forwards all query string parameters to the destination path for 301 and
302 redirects. However, if the original address includes a query string set to a
specific value, as demonstrated in this example, Amplify doesn't forward query
parameters. In this case, the redirect applies only to requests to the destination
address with the specified query value `id`.

You can use the following example to redirect all paths that can’t be found at a given
level of a folder structure to index.html in a specified folder.

| Original address                                          | Destination Address     | Redirect Type     | Country Code |
| --------------------------------------------------------- | ----------------------- | ----------------- | ------------ |
| `/documents/<folder>/<child-folder>/<grand-child-folder>` | `/documents/index.html` | `not found (404)` |              |

JSON format

```
[
  {
    "source": "/documents/<x>/<y>/<z>",
    "status": "404",
    "target": "/documents/index.html",
    "condition": null
  }
]
```

## Region-based redirects

You can use the following example to redirect requests based on region.

| Original address | Destination Address | Redirect Type              | Country Code |
| ---------------- | ------------------- | -------------------------- | ------------ |
| `/documents`     | `/documents/us/`    | `temporary redirect (302)` | `<US>`       |

JSON format

```
[
  {
    "source": "/documents",
    "status": "302",
    "target": "/documents/us/",
    "condition": "<US>"
  }
]
```

## Using wildcard expressions in redirects and rewrites

You can use the wildcard expression, `<*>`, in the original address for
a redirect or rewrite. You must place the expression at the end of the original address,
and it must be unique. Amplify ignores original addresses that include more than one
wildcard expression, or use it in a different placement.

The following is an example of a valid redirect with a wildcard expression.

| Original address | Destination Address | Redirect Type              | Country Code |
| ---------------- | ------------------- | -------------------------- | ------------ |
| `/docs/<*>`      | `/documents/<*>`    | `permanent redirect (301)` |              |

The following two examples demonstrate _invalid_ redirects with
wildcard expressions.

| Original address        | Destination Address          | Redirect Type              | Country Code |
| ----------------------- | ---------------------------- | -------------------------- | ------------ |
| `/docs/<*>/content`     | `/documents/<*>/content`     | `permanent redirect (301)` |              |
| `/docs/<*>/content/<*>` | `/documents/<*>/content/<*>` | `permanent redirect (301)` |              |
