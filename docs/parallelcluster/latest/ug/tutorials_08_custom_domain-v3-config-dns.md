

# Configure DNS
<a name="tutorials_08_custom_domain-v3-config-dns"></a>

Complete the following steps to configure your domain name service (DNS) so that AWS ParallelCluster UI (PCUI) and Amazon Cognito respond on the desired custom domains.

This example assumes that you want to deploy PCUI with custom domain `xyz.example.com` and the Amazon Cognito interface with custom domain `auth-xyz.example.com`.

1. Deploy the PCUI stack with the following parameters:
   + **CustomDomainEndpoint:** Create an A record in your DNS for {{xyz.example.com}} that points to the alias specified in the output.
   + **CognitoCustomDomainEndpoint:** Create an A record in your DNS for {{auth-xyz.example.com}} that points to the alias specified in the output.

1. Wait about 10 minutes so that the DNS changes can be distributed.

1. When the DNS changes are distributed, PCUI responds on {{xyz.example.com/pcui}} and the Amazon Cognito authentication page responds on {{auth-xyz.example.com}}.