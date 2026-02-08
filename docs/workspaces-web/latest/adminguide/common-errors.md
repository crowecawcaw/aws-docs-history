# Common error messages

The following are common error messages and their resolutions when setting up custom domains:

## Invalid CSRF Token error

This error happens when Secure Browser does not receive your request properly through the
CloudFront setup.

To resolve this issue:

- Check the custom origin settings on your CloudFront distribution.
- Verify that the name of the custom header exactly matches
  `workspacessecurebrowser-custom-domain` and the value exactly matches your custom
  domain (without https:// or any query parameters).
- Clear the cache on your local browser.
- Invalidate the cache on CloudFront.

## 502 Bad Gateway error

This error typically indicates cache configuration issues.

To resolve this issue:

- Check cache settings on your CloudFront distribution.
- Verify that Cache policy is set to `CachingDisabled`.
- Verify that Origin request policy is set to `AllViewerExceptHostHeader`.
- Clear the cache on your local browser.
- Invalidate the cache on CloudFront.

## Access Denied error

This error could occur if your custom domain is configured incorrectly.

To resolve this issue:

- Check origin settings on your CloudFront distribution.
- Verify that origin is set to the correct portal URL.
- Verify that portal is configured with the correct custom domain.
- Clear the cache on your local browser.
- Invalidate the cache on CloudFront.
