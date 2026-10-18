

# Identity and access management
<a name="smsec01"></a>

Authentication and authorization systems control who can access content and how. This covers viewer-facing identity (subscription tiers, geo-restrictions) and infrastructure-level access (origin restrictions, CDN authentication).


| SMSEC01: How do you authorize access to content and content ingest? | 
| --- | 
| [SMSEC01-BP01 Use an identity provider to authenticate viewers and access policies to implement least privilege access to protected content](smsec01-bp01.md) | 
| [SMSEC01-BP02 Restrict content origin access to allow only authorized content distribution networks](smsec01-bp02.md) | 

## Capability intent
<a name="smsec01-intent"></a>
+ Only authenticated and authorized users access protected content based on subscription, licensing, and geography.
+ Content origins are accessible only through authorized distribution paths.
+ Access tokens are short-lived and scoped to the session.
+ Identity is federated from a central provider rather than managed per-application.

## Common issues to watch for
<a name="smsec01-issues"></a>
+ Relying on obscured URLs instead of identity verification.
+ Excessively long signed URL expiration that outlives the session.
+ No Origin Access Control between CDN and origin, leaving origins directly accessible.
+ Single shared API keys across all sessions rather than per-session tokens.