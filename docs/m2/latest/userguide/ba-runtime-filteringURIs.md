After careful consideration, we have made the decision to close new customer access to **AWS Mainframe Modernization self-managed experience**,
effective June 30, 2026. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for
AWS Mainframe Modernization self-managed experience, but we do not plan to introduce new features. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Configure URI accessibility for Gapwalk applications

This topic describes how to configure the filtering of URIs for Gapwalk applications. This
feature does not require an identity provider (IdP).

To block a list of URIs, add the following two lines to the
`application-main.yml` of your modernized application, replacing
`URI-1`, `URI-2`, and so on, with the URIs that
you want to block.

```
gapwalk-application.security.filterURIs: enabled
gapwalk-application.security.blockedURIs: `URI-1`, `URI-2`, `URI-3`
```
