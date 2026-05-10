# Configure the exception list (optional)

The exception list lets you exclude specific URL patterns from redirection,
even if they match the allowlist.

**How URL evaluation works**

URLs are evaluated in the following order:

1. **Check exception list first.**
   If a URL matches an exception pattern, it opens in the remote session
   (no redirection).
2. **Check allowlist second.**
   If a URL matches an allowlist pattern and is not in the exception list,
   it redirects to the local browser.
3. **Default behavior.**
   If a URL matches neither list, it opens in the remote session.
   **Example scenarios**

_Scenario 1: Allow YouTube except for specific channels_

- Allowlist: `https://www.youtube.com/*`
- Exception list: `https://www.youtube.com/channel/UCrestrictedChannel`
- Result: `https://www.youtube.com/watch?v=abc123` redirects to the
  local browser. `https://www.youtube.com/channel/UCrestrictedChannel`
  opens in the remote session.
  _Scenario 2: Exclude specific subdomains_

- Allowlist: `https://*.example.com/*`
- Exception list: `https://admin.example.com/*`,
  `https://secure.example.com/*`
- Result: `https://www.example.com/page` redirects to the
  local browser. `https://admin.example.com/dashboard` opens
  in the remote session.
