AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Configure security for Gapwalk

applications

The following topics describe how to secure Gapwalk applications.

It is your responsibility to provide the right configuration to ensure that the use of the
AWS Blu Age framework is secure.

All security-related features are disabled by default. To enable authentication (and
CSRF,XSS,CSP, and so on), set `gapwalk-application.security` to `enabled` and
`gapwalk-application.security.identity` to `oauth`.

###### Topics

- [Configure URI accessibility for Gapwalk
  applications](ba-runtime-filteringURIs.md "ba-runtime-filteringURIs.md")
- [Configure authentication for Gapwalk applications](ba-runtime-auth.md "ba-runtime-auth.md")
