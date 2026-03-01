# Connecting a custom domain

You can connect an app that you’ve deployed with Amplify Hosting to a custom domain. When
you use Amplify to deploy your web app, Amplify hosts it for you on the default
`amplifyapp.com` domain with a URL such as
`https://branch-name.d1m7bkiki6tdw1.amplifyapp.com`. When you connect your app
to a custom domain, users see that your app is hosted on a custom URL, such as
`https://www.example.com`.

You can purchase a custom domain through an accredited domain registrar such as Amazon Route 53
or GoDaddy. Route 53 is Amazon’s Domain Name System (DNS) web service. For more information about
using Route 53, see [What is Amazon Route 53](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md"). For a list of third-party accredited domain registrars,
see the [Accredited Registrar
Directory](https://www.icann.org/en/accredited-registrars "https://www.icann.org/en/accredited-registrars") at the ICANN website.

When you set up your custom domain, you can use the default managed certificate that
Amplify provisions for you or you can use your own custom certificate. You can change the
certificate in use for the domain at any time. For detailed information about managing
certificates, see [Using SSL/TLS certificates](using-certificates.md "using-certificates.md").

Before you proceed with setting up a custom domain, verify that you have met the following
prerequisites.

- You own a registered domain name.
- You have a certificate issued by or imported into AWS Certificate Manager.
- You have deployed your app to Amplify Hosting.

For more information about completing this step, see [Getting started with deploying an app to Amplify Hosting](getting-started.md "getting-started.md").

- You have a basic knowledge of domains and DNS terminology.

For more information about domains and DNS, see [Understanding DNS terminology and concepts](understanding-dns-terminology-and-concepts.md "understanding-dns-terminology-and-concepts.md").

###### Warning

When initiating a DomainAssociation request for an Amplify app with a domain that is already or was previously associated with different Amplify App(s) in other AWS account(s) in the same region, this is considered a cross account domain association. Cross account domain association requests require manual verification. If you would like to proceed with a cross account domain association, please contact AWS support for assistance.

###### Topics

- [Understanding DNS terminology and concepts](understanding-dns-terminology-and-concepts.md "understanding-dns-terminology-and-concepts.md")
- [Using SSL/TLS certificates](using-certificates.md "using-certificates.md")
- [Adding a custom domain managed by Amazon Route 53](to-add-a-custom-domain-managed-by-amazon-route-53.md "to-add-a-custom-domain-managed-by-amazon-route-53.md")
- [Adding a custom domain managed by a third-party DNS provider](to-add-a-custom-domain-managed-by-a-third-party-dns-provider.md "to-add-a-custom-domain-managed-by-a-third-party-dns-provider.md")
- [Updating DNS records for a domain managed by GoDaddy](to-add-a-custom-domain-managed-by-godaddy.md "to-add-a-custom-domain-managed-by-godaddy.md")
- [Updating the SSL/TLS certificate for a domain](to-update-certificate.md "to-update-certificate.md")
- [Managing subdomains](to-manage-subdomains.md "to-manage-subdomains.md")
- [Setting up wildcard subdomains](wildcard-subdomain-support.md "wildcard-subdomain-support.md")
- [Setting up automatic subdomains for an Amazon Route 53 custom domain](to-set-up-automatic-subdomains-for-a-Route-53-custom-domain.md "to-set-up-automatic-subdomains-for-a-Route-53-custom-domain.md")
- [Troubleshooting custom domains](custom-domain-troubleshoot-guide.md "custom-domain-troubleshoot-guide.md")
