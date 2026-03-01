# Troubleshooting custom domains

If you encounter issues when connecting a custom domain to your Amplify application,
consult the topics in this section for help.

If you don't see a solution to your issue here, contact Support. For more information,
see [Creating a
support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") in the _AWS Support User Guide_.

###### Topics

- [I need to verify that my CNAME resolves](#how-do-i-verify-that-my-cname-resolves "#how-do-i-verify-that-my-cname-resolves")
- [My domain hosted with a third-party is stuck in the Pending Verification state](#my-domain-hosted-with-a-third-party-is-stuck-in-the-pending-verification-state "#my-domain-hosted-with-a-third-party-is-stuck-in-the-pending-verification-state")
- [My domain hosted with Amazon Route 53 is stuck in the Pending Verification state](#my-domain-hosted-with-amazon-route-53-is-stuck-in-the-pending-verification-state "#my-domain-hosted-with-amazon-route-53-is-stuck-in-the-pending-verification-state")
- [My app with multi-level subdomains is stuck in the Pending Verification state](#multilevel-domain-is-stuck-in-the-pending-verification-state "#multilevel-domain-is-stuck-in-the-pending-verification-state")
- [My DNS provider doesn't support A records with fully qualified domain names](#FQDN-A-recored-unsupported "#FQDN-A-recored-unsupported")
- [I get a CNAMEAlreadyExistsException error](#i-get-a-cnamealreadyexistsexception-error "#i-get-a-cnamealreadyexistsexception-error")
- [I get an Additional Verification Required error](#i-get-an-additionalverificationrequired-error "#i-get-an-additionalverificationrequired-error")
- [I get a 404 error on the CloudFront URL](#i-get-a-404-cloudfront-url "#i-get-a-404-cloudfront-url")
- [I get SSL certificate or HTTPS errors when visiting my domain](#ssl-HTTPS-errors-on-domain "#ssl-HTTPS-errors-on-domain")
- [Path components not supported in domain redirects](#domain-redirects-path-components "#domain-redirects-path-components")
- [I get a 400 error for cross account domain association](#cross-account-domain-association-400-error "#cross-account-domain-association-400-error")

## I need to verify that my CNAME resolves

1. After you update your DNS records with your third-party domain provider,
   you can use a tool such as [dig](<https://en.wikipedia.org/wiki/Dig_(command)> "https://en.wikipedia.org/wiki/Dig_(command)") or a free
   website such as [https://www.whatsmydns.net/](https://www.whatsmydns.net/ "https://www.whatsmydns.net/") to verify that your CNAME record is
   resolving correctly. The following screenshot demonstrates how to use
   whatsmydns.net to check your CNAME record for the domain **www.example.com**.

![The whatsmydns.net application, where you enter the name of a website to check.](images/amplify-troubleshooting-whatsmydns-1Update.png) 2. Choose **Search**, and **whatsmydns.net** displays the results for your CNAME. The
following screenshot is an example of a list of results that verify that the
CNAME resolves correctly to a cloudfront.net URL.

![The whatsmydns.net application showing the results of a resolving CNAME.](images/amplify-troubleshooting-whatsmydns-2Update.png)

## My domain hosted with a third-party is stuck in the Pending Verification state

1. If your custom domain is stuck in the **Pending
   Verification** state, verify that your CNAME
   records are resolving. See the previous troubleshooting topic, [How do I verify that my
   CNAME resolves](#how-do-i-verify-that-my-cname-resolves "#how-do-i-verify-that-my-cname-resolves"), for instructions on performing
   this task.
2. If your CNAME records are not resolving, confirm that the
   CNAME entry exists in your DNS settings with your domain
   provider.

###### Important

It is important to update your CNAME records as soon
as you create your custom domain. After your app is created in the
Amplify console, your CNAME record is checked every few
minutes to determine if it resolves. If it doesn’t resolve after an
hour, the check is made every few hours, which can lead to a delay in
your domain being ready to use. If you added or updated your
CNAME records a few hours after you created your app,
this is the most likely cause for your app to get stuck in the
**Pending Verification** state. 3. If you have verified that the CNAME record exists, then
there may be an issue with your DNS provider. You can either contact the DNS
provider to diagnose why the DNS verification CNAME is not
resolving or you can migrate your DNS to Route 53. For more information, see
[Making Amazon
Route 53 the DNS service for an existing domain](../../../Route53/latest/DeveloperGuide/MigratingDNS.md "../../../Route53/latest/DeveloperGuide/MigratingDNS.md").

## My domain hosted with Amazon Route 53 is stuck in the Pending Verification state

If you transferred your domain to Amazon Route 53, it is possible that your domain has
different name servers than those issued by Amplify when your app was created.
Perform the following steps to diagnose the cause of the error.

1. Sign in to the [Amazon Route 53
   console](https://console.aws.amazon.com/route53/home "https://console.aws.amazon.com/route53/home")
2. In the navigation pane, choose **Hosted Zones** and then
   choose the name of the domain you are connecting.
3. Record the name server values from the **Hosted Zone
   Details** section. You need these values to complete the next
   step. The following screenshot of the Route 53 console displays the location of
   the name server values in the lower-right corner.

![The Hosted Zone Details section in the Route 53 console displaying the name server values.](images/1555952748759-111.png) 4. In the navigation pane, choose **Registered domains**.
Verify that the name servers displayed on the **Registered
domains** section match the name server values that you
recorded in the previous step from the **Hosted Zone
Details** section. If they do not match, edit the name server
values to match the values in your **Hosted Zone**. The
following screenshot of the Route 53 console displays the location of the name
server values on the right side.

![The Registered domains section of the Route 53 console displaying the name server values.](images/1555952748759-607.png) 5. If this doesn't resolve the issue, contact Support. For more information,
see [Creating a support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") in the
_AWS Support User Guide_.

## My app with multi-level subdomains is stuck in the Pending Verification state

If an app with multi-level subdomains is stuck in the **Pending
Verification** state when connecting to a third-party DNS provider,
there might be an issue with the format of your DNS records. Some DNS providers
automatically add the second-level domain (SLD) and top-level domain (TLD) domain
suffixes to your records. If you are also specifying the domain in the format that
includes the SLD and TLD, this can cause a domain verification issue.

When you connect a domain, first try specifying the domain name using the full
format provided by Amplify, for example
`_hash.docs.backend.example.com`. If the SSL configuration gets stuck
in the **Pending Verification** state, try removing the TLD and SLD
from the records. For example, if the full format is
`_hash.docs.backend.example.com`, specify
`_hash.docs.backend`. Wait 15 to 30 minutes to allow the records to
propagate. Then use a tool such as MX Toolbox to check whether the verification
process is working.

## My DNS provider doesn't support A records with fully qualified domain names

Some DNS providers don't support A records with a fully qualified domain name
(FQDN), such as `example.cloudfront.net`. For example, Cloudflare
A records can only write IPv4 addresses and don't
support FQDNs. To work around this limitation, we recommend using
CNAME records instead of A records in your
DNS configuration.

As an example, the following DNS configuration uses an A
record.

```
A     | @ | ***.cloudfront.net
CNAME | www | ***.cloudfront.net
```

Change it to the following DNS configuration to use
CNAME records only.

```
CNAME | @ | ***.cloudfront.net
CNAME | www | ***.cloudfront.net
```

This workaround enables you to properly point your apex domain (@ record) to
services like CloudFront, while avoiding the IPv4-only limitation of A
records in Cloudflare's system.

## I get a CNAMEAlreadyExistsException error

If you get a **CNAMEAlreadyExistsException** error,
this means that one of the host names that you tried to connect (a subdomain, or the
apex domain) is already deployed to another Amazon CloudFront distribution. The source of
your error depends on your current hosting and DNS providers.

A CNAME alias, such as `example.com` or
`sub.example.com` can only be associated with a single CloudFront
distribution at a time. The **CNAMEAlreadyExistsException** indicates that your domain is already
associated with another CloudFront distribution, either within the same AWS account, or
potentially in a different account. The domain must be disassociated from the
previous CloudFront distribution before the new distribution created by Amplify Hosting
will work. You might need to check more than one account if you or your organization
owns multiple AWS accounts.

Perform the following steps to diagnose the cause of the **CNAMEAlreadyExistsException** error.

1. Sign in to the [Amazon
   CloudFront console](https://console.aws.amazon.com/cloudfront/home?# "https://console.aws.amazon.com/cloudfront/home?#") and verify that you don't have this domain
   deployed to another distribution. A single CNAME record can
   be attached to one CloudFront distribution at a time.
2. If you previously deployed the domain to a CloudFront distribution you must
   remove it.
   1. Choose **Distributions** on the left navigation
      menu.
   2. Select the name of the distribution to edit.
   3. Choose the **General** tab. In the
      **Settings** section, choose
      **Edit**.
   4. Remove the domain name from **Alternate domain name
      (CNAME)**. Then choose, **Save
      changes**.

3. Confirm that no other CloudFront distribution exists that is using this domain
   in the current AWS account or other AWS accounts. If it won't disrupt
   any currently running services, try deleting and recreating the hosted
   zone.
4. Check to see whether this domain is connected to a different Amplify app
   that you own. If so, make sure you are not trying to reuse one of the
   hostnames. If you are using `www.example.com` for another app,
   you cannot use `www.example.com` with the app that you are
   currently connecting. You can use other subdomains, such as
   `blog.example.com`.
5. If this domain was successfully connected to another app and then deleted
   within the last hour, try again after at least one hour has passed. If you
   still see this exception after 6 hours, contact Support. For more information,
   see [Creating a support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") in the
   _AWS Support User Guide_.
6. If you manage your domain through Route 53, make sure to clean up any hosted
   zone CNAME or ALIAS records that point to the
   old CloudFront distribution.
7. After completing the preceding steps, remove the custom domain from
   Amplify Hosting and start over with the workflow to connect a custom
   domain in the Amplify console.

## I get an Additional Verification Required error

If you get an **Additional Verification Required**
error, this means that AWS Certificate Manager (ACM) requires additional information to process
this certificate request. This can happen as a fraud-protection measure, such as
when the domain ranks within the [Alexa top 1000 websites](https://aws.amazon.com/marketplace/pp/Amazon-Web-Services-Alexa-Top-Sites/B07QK2XWNV "https://aws.amazon.com/marketplace/pp/Amazon-Web-Services-Alexa-Top-Sites/B07QK2XWNV"). To provide the required information, use the
[Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") to contact
Support. If you don't have a support plan, post a new thread in the [ACM Discussion
Forum](https://forums.aws.amazon.com/forum.jspa?forumID=206 "https://forums.aws.amazon.com/forum.jspa?forumID=206").

###### Note

You cannot request a certificate for Amazon-owned domain names such as those
ending in amazonaws.com, cloudfront.net, or elasticbeanstalk.com.

## I get a 404 error on the CloudFront URL

To serve traffic, Amplify Hosting points to a CloudFront URL via a CNAME record. In
the process of connecting an app to a custom domain, the Amplify console displays
the CloudFront URL for the app. However, you cannot access your application directly using
this CloudFront URL. It returns a 404 error. Your application resolves only using the
Amplify app URL (for example,
`https://main.d5udybEXAMPLE.amplifyapp.com`, or your custom domain
(for example `www.example.com`).

Amplify needs to route requests to the correct deployed branch and uses the
hostname to do this. For example, you can configure the domain
`www.example.com` that points to the mainline branch of an app, but
also configure `dev.example.com` that points to the dev branch of the
same app. Therefore, you must visit your application based on it's configured
subdomains so that Amplify can route the requests accordingly.

## I get SSL certificate or HTTPS errors when visiting my domain

If you have Certificate Authority Authorization (CAA) DNS records configured with
your third-party DNS provider, AWS Certificate Manager (ACM) might not be able to update or
reissue intermediate certificates for your custom domain SSL certificate. To resolve
this, you need to add a CAA record to trust at least one of Amazon’s certificate
authority domains. The following procedure describes the steps you need to
perform.

###### To add a CAA record to trust an Amazon certificate authority

1.  Configure a CAA record with your domain provider to trust at least one of
    Amazon’s certificate authority domains. For more information about
    configuring the CAA record, see [Certification
    Authority Authorization (CAA) problems](../../../acm/latest/userguide/troubleshooting-caa.md "../../../acm/latest/userguide/troubleshooting-caa.md") in the
    _AWS Certificate Manager User Guide_.
2.  Use one of the following methods to update your SSL certificate:
    - Manually update using the Amplify console.

    ###### Note

    This method will cause down time for your custom
    domain.

        1. Sign in to the AWS Management Console and open the [Amplify
         console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
        2. Choose your app that you want to add a CAA record
         to.
        3. In the navigation pane, choose **App
         Settings**, **Domain
         management**.
        4. On the **Domain management** page, delete
         the custom domain.
        5. Connect your app to the custom domain again. This process
         issues a new SSL certificate and its intermediate
         certificates can now be managed by ACM.


        To reconnect your app to your custom domain, use one of
         the following procedures that corresponds to the domain
         provider you are using.




        	+ [Adding a custom domain managed by Amazon Route 53](to-add-a-custom-domain-managed-by-amazon-route-53.md "to-add-a-custom-domain-managed-by-amazon-route-53.md").
        	+ [Adding a custom domain managed by a third-party DNS provider](to-add-a-custom-domain-managed-by-a-third-party-dns-provider.md "to-add-a-custom-domain-managed-by-a-third-party-dns-provider.md").
        	+ [Updating DNS records for a domain managed by GoDaddy](to-add-a-custom-domain-managed-by-godaddy.md "to-add-a-custom-domain-managed-by-godaddy.md").

    - Contact Support to have your SSL certificate reissued.

## Path components not supported in domain redirects

Domain redirects only match the hostname portion. Path components in domain-based
source rules (e.g., `"https://domain.com/path"`) are not supported and
will cause the rule to be ignored without error. For more information, see [Redirects and rewrites example reference](redirect-rewrite-examples.md "redirect-rewrite-examples.md").

## I get a 400 error for cross account domain association

When initiating a DomainAssociation request for an Amplify app with a domain that is already or was previously associated with different Amplify App(s) in other AWS account(s) in the same region, this is considered a cross account domain association. If you get this error this means that you are attempting cross account domain association which requires manual verification. If you would like to proceed with a cross account domain association, please contact AWS support for assistance.
