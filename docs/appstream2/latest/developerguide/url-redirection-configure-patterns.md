

# Configure URL patterns (allowlist)
<a name="url-redirection-configure-patterns"></a>

The URL patterns field defines which links redirect to the local browser. Only URLs that match these patterns are redirected. All other URLs open in the remote session.

Enter one URL pattern per line in the text field. The following example shows three URL patterns.

```
https://www.youtube.com/*
https://www.linkedin.com
https://docs.aws.amazon.com
```

**Wildcard support**

URL patterns support two wildcard characters for flexible matching.


**Wildcard characters for URL pattern matching**  

| Wildcard | Matches | Example | Matches URLs | 
| --- | --- | --- | --- | 
| \* | Multiple characters (zero or more) | https://www.youtube.com/\* | https://www.youtube.com/watch?v=abc, https://www.youtube.com/playlist/xyz | 
| ? | Single character (exactly one) | https://www.example.com/page? | https://www.example.com/page1, https://www.example.com/pageA | 

**Common wildcard patterns**
+ Redirect all pages within a domain: `https://www.youtube.com/*`
+ Redirect all subdomains: `https://*.example.com/*`

**Pattern matching rules**
+ Case sensitivity: Patterns are case-insensitive for domains and paths.
+ Protocol matching: The protocol (`http://` or `https://`) must match exactly.