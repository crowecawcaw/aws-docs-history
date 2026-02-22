# Initiating sign-on from

Quick

|                                            |
| ------------------------------------------ |
| \*_Applies<br>to:_<br>• Enterprise Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

###### Note

IAM identity federation doesn't support syncing identity provider groups
with Amazon Quick.

In this scenario, your user initiates the sign-on process from an Amazon Quick
application portal without being signed on to the identity provider. In this case, the
user has a federated account managed by a third-party IdP. The user might have a user
account on Quick. Quick sends an authentication request to the
IdP. After the user is authenticated, Quick opens.

Beginning with the user signing into Quick, authentication flows through
these steps:

1. The user opens Quick. At this point, the user isn't signed in to
   the IdP.
2. The user attempts to sign in to Amazon Quick.
3. Amazon Quick redirects the user's input to the federation service and requests
   authentication.
4. The federation service and the IdP authenticate the user:
   1. The federation service requests authentication from the organization's
      identity store.
   2. The identity store authenticates the user and returns the
      authentication response to the federation service.
   3. When authentication is successful, the federation service posts the
      SAML assertion to the user's browser.
   4. The user's browser posts the SAML assertion to the AWS
      Sign-In SAML endpoint (`https://signin.aws.amazon.com/saml`).
   5. AWS Sign-In receives the SAML request, processes the
      request, authenticates the user, and forwards the authentication token
      to the Amazon Quick service.

5. Amazon Quick accepts the authentication token from AWS and
   presents Amazon Quick to the user.
   From the user's perspective, the process happens transparently. The user starts at an
   Amazon Quick application portal. Amazon Quick negotiates authentication with your
   organization's federation service and AWS. Amazon Quick opens, without the user
   needing to supply any additional credentials.
