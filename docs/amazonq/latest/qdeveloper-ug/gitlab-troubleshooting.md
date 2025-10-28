# Troubleshooting issues for GitLab Duo with Amazon Q

Consult the following section to troubleshoot common onboarding problems when using GitLab Duo
with Amazon Q.

## GitLab instance blocks inbound requests

**Problem**: My GitLab instance blocks inbound requests, and Amazon Q can't call back
into my GitLab instance.

**Solution**: Identify what's blocking the inbound request, and make modifications to
accept inbound requests from Amazon Q, which could be in the form of one of the following:

- A proxy
- A firewall layer
- Denylist or allowlist at any infrastructure layer

You need to reonboard to your GitLab instance to resync. For more information, see
[Set up GitLab Duo with Amazon Q](https://docs.gitlab.com/user/duo_amazon_q/setup/ "https://docs.gitlab.com/user/duo_amazon_q/setup/") in the
_GitLab documentation_.

## Connection between Gitlab and Amazon Q out of sync

**Problem**: I modified GitLab Duo with Amazon Q application and now the connection between
GitLab and Amazon Q is out of sync.

**Solution**: When GitLab and Amazon Q are out of sync, it can lead to invalid credentials,
inability to refresh credentials, and unauthorized response from GitLab when Amazon Q calls into GitLab.

## Instance domain name not resolvable

**Problem**: I modified the GitLab instance URL after onboarding, and now the connection
between GitLab and Amazon Q are out of sync. Amazon Q ins't able to call the GitLab instance successfully anymore.

**Solution**: You need to ensure the domain name is resolvable. Reonboard to your GitLab
instance. For more information, see
[Set up GitLab Duo with Amazon Q](https://docs.gitlab.com/user/duo_amazon_q/setup/ "https://docs.gitlab.com/user/duo_amazon_q/setup/") in the
_GitLab documentation_.

## Incorrect IAM role and identity provider (IdP)

**Problem**: My IAM role doesn't provide the correct permissions to the APIs required by GitLab Duo
with Amazon Q.

**Solution**: Ensure the identity provider (IdP) and IAM roles are set up correctly. For more
information, see [Set up GitLab Duo with Amazon Q](https://docs.gitlab.com/user/duo_amazon_q/setup/ "https://docs.gitlab.com/user/duo_amazon_q/setup/") in the
_GitLab documentation_.

## Amazon Q Developer profile doesn't exist

**Problem**: I'm trying to onboard to GitLab Duo with Amazon Q, but coming across the following issue:
`Application could not be craeted by the AI Gateway: Error 400 - {"detail":"An error occured (ValidationException) 
 when calling the CreateOAuthAppConnection operation: ProfileDoesNotExist"}`

**Solution**: You need to first create an Amazon Q Developer profile through the Amazon Q Developer console. For
more information, see [Set up GitLab Duo with Amazon Q](https://docs.gitlab.com/user/duo_amazon_q/setup/ "https://docs.gitlab.com/user/duo_amazon_q/setup/") in
the _GitLab documentation_.
