# Learn about the silk:is-user-entitled meta tag

The `<meta name="silk:is-user-entitled" content="true|false">` tag is a
new meta tag introduced by the Silk web browser application. This tag is designed to inform
Silk whether the current user is entitled to the content on the web page. It is particularly
useful in scenarios where the webpage implements a paywall or other content restriction
mechanism. Silk uses the value of this tag to decide whether to display a web page
summarization option to the user.

When Silk encounters a web page with `<meta name="silk:is-user-entitled"
 content="false">`, it will assume that the current user is not entitled to the
contents on the page. In this case, Silk will not provide a web page summarization option to
the user on that page. If the tag is Silk present or has `content="true"`, Silk
will assume that the user is entitled to the full content on the page, and the summarization
option will be displayed.

## Usage guidelines

The `<meta name="silk:is-user-entitled" content="true|false">` tag
should be included in the `<head>` section of the HTML document. The
content attribute can take one of two values:

- `true`: Indicates that the current user is entitled to access the
  content on the web page.
- `false`: Indicates that the current user is not entitled to access
  the content on the web page, typically due to a subscription
  requirement.

Follow these guidelines when implementing this tag:

1. **Consistency with Paywall/Content Restriction
   Implementation:** The value of the `content` attribute
   should be consistent with the paywall/content restriction implementation on the
   website. If a paywall is displayed to a non-subscribed user, the content
   attribute should be set to `false`.
2. **Omit the Tag for Entitled Users:** If the user
   is entitled to view the entire content of the page, the
   `silk:is-user-entitled` tag can be omitted, as Silk will assume
   entitlement by default.

By following these guidelines, website publishers can ensure that Silk accurately
understands the user's entitlement status and provides the appropriate functionality,
such as the web page summarization option, based on the specified content
restrictions.

## Examples

When a page is behind a paywall because the current user does not have a subscription,
include the tag with `content="false"`:

```
<!DOCTYPE html>
<html>
  <head>
    <title>Paywalled Content Page</title>
    <meta name="silk:is-user-entitled" content="false">
    <!— Other meta tags and stylesheets -->
  </head>
  <body>
    <!— Paywalled content -->
  </body>
</html>
```

When a page is not behind a paywall because the user has a subscription, you can
include the tag with `content="true"` or omit the tag altogether:

```
<!DOCTYPE html>
<html>
  <head>
    <title>Free Content Page</title>
      <meta name="silk:is-user-entitled" content="true">
      <!— Other meta tags and stylesheets -->
  </head>
  <body>
    <!— Page content -->
  </body>
</html>
```
