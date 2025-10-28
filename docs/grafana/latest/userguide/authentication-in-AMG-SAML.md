# Use SAML with your Amazon Managed Grafana

workspace

###### Note

Amazon Managed Grafana does not currently support IdP initiated login for workspaces. You
should set up your SAML applications with a blank Relay State.

You can use SAML authentication to use your existing identity provider and
offer single sign-on for logging into the Grafana console of your Amazon Managed Grafana workspaces.
Rather than authenticating through IAM, SAML authentication for Amazon Managed Grafana
lets you use third-party identity providers to log in, manage access control, search
your data, and build visualizations. Amazon Managed Grafana supports identity providers that use the
SAML 2.0 standard and have built and tested integration applications with Azure AD,
CyberArk, Okta, OneLogin, and Ping Identity.

For details about how to set up SAML authentication during workspace creation, see
[Creating a workspace](AMG-create-workspace.md#creating-workspace "AMG-create-workspace.md#creating-workspace").

In the SAML authentication flow, an Amazon Managed Grafana workspace acts as the service provider
(SP), and interacts with the IdP to obtain user information. For more information about
SAML, see [Security Assertion Markup Language](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language "https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language").

You can map groups in your IdP to teams in the Amazon Managed Grafana workspace, and set
fine-grained access permissions on those teams. You can also map organization roles that
are defined in the IdP to roles in the Amazon Managed Grafana workspace. For example, if you have a
**Developer** role defined in the IdP, you can map that role to the
**Grafana Admin** role in the Amazon Managed Grafana workspace.

###### Note

When you create an Amazon Managed Grafana workspace that uses an IdP and SAML for authorization,
you must be signed on to an IAM principal that has the
**AWSGrafanaAccountAdministrator** policy attached.

To sign in to the Amazon Managed Grafana workspace, a user visits the workspace's Grafana console
home page and chooses **Log in using SAML**. The workspace reads the
SAML configuration and redirects the user to the IdP for authentication. The user enters
their sign-in credentials in the IdP portal, and if they are a valid user, the IdP
issues a SAML assertion and redirects the user back to the Amazon Managed Grafana workspace.
Amazon Managed Grafana verifies that the SAML assertion is valid, and the user is signed in and can
use the workspace.

Amazon Managed Grafana supports the following SAML 2.0 bindings:

- From the service provider (SP) to the identity provider (IdP):
  - HTTP-POST binding
  - HTTP-Redirect binding

- From the identity provider (IdP) to the service provider (SP):

      + HTTP-POST binding

  Amazon Managed Grafana supports signed and encrypted assertions, but does not support signed or
  encrypted requests.

Amazon Managed Grafana supports SP-initiated requests, and does not support IdP-initiated
requests.

## Assertion mapping

During the SAML authentication flow, Amazon Managed Grafana receives the assertion consumer
service (ACS) callback. The callback contains all relevant information for the user
being authenticated, embedded in the SAML response. Amazon Managed Grafana parses the response to
create (or update) the user within its internal database.

When Amazon Managed Grafana maps the user information, it looks at the individual attributes
within the assertion. You can think of these attributes as key-value pairs, although
they contain more information than that.

Amazon Managed Grafana provides configuration options so that you can modify which keys to look
at for these values.

You can use the Amazon Managed Grafana console to map the following SAML assertion attributes
to values in Amazon Managed Grafana:

- For **Assertion attribute role**, specify the name of the
  attribute within the SAML assertion to use as the user roles.
- For **Assertion attribute name**, specify the name of the
  attribute within the SAML assertion to use for the user full "friendly"
  names for SAML users.
- For **Assertion attribute login**, specify the name of
  the attribute within the SAML assertion to use for the user sign-in names
  for SAML users.
- For **Assertion attribute email**, specify the name of
  the attribute within the SAML assertion to use for the user email names for
  SAML users.
- For **Assertion attribute organization**, specify the
  name of the attribute within the SAML assertion to use for the "friendly"
  name for user organizations.
- For **Assertion attribute groups**, specify the name of
  the attribute within the SAML assertion to use for the "friendly" name for
  user groups.
- For **Allowed organizations**, you can limit user access
  to only the users who are members of certain organizations in the
  IdP.
- For **Editor role values**, specify the user roles from
  your IdP who should all be granted the `Editor` role in the
  Amazon Managed Grafana workspace.

## Connecting to your identity

provider

The following external identity providers have been tested with Amazon Managed Grafana and
provide applications directly in their app directories or galleries to help you
configure Amazon Managed Grafana with SAML.

###### Topics

- [Configure Amazon Managed Grafana to use Azure
  AD](AMG-SAML-providers-Azure.md "AMG-SAML-providers-Azure.md")
- [Configure Amazon Managed Grafana to use
  CyberArk](AMG-SAML-providers-CyberArk.md "AMG-SAML-providers-CyberArk.md")
- [Configure Amazon Managed Grafana to use Okta](AMG-SAML-providers-okta.md "AMG-SAML-providers-okta.md")
- [Configure Amazon Managed Grafana to use
  OneLogin](AMG-SAML-providers-onelogin.md "AMG-SAML-providers-onelogin.md")
- [Configure Amazon Managed Grafana to use Ping
  Identity](AMG-SAML-providers-pingone.md "AMG-SAML-providers-pingone.md")
