# Changing the identity provider type for Amazon WorkSpaces Secure Browser

You can change the authentication type of your portal at any time. To do this, follow these steps.

- To change from **IAM Identity Center** to **Standard**, follow the
  steps at [Configuring the standard authentication type for Amazon WorkSpaces Secure Browser](configure-standard.md "configure-standard.md").
- To change from **Standard** to **IAM Identity Center**, follow the
  steps at [Configuring the IAM Identity Center authentication type for Amazon WorkSpaces Secure Browser](configure-iam.md "configure-iam.md").
  Changes to the identity provider type may take up to 15 minutes to deploy, and will not
  automatically terminate in-progress sessions.

You can view identity provider type changes to your portal through AWS CloudTrail by inspecting
`UpdatePortal` events. The type is visible in the request and response payloads of
the event.
