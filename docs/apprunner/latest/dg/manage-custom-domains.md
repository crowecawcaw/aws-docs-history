# Managing custom domain names for an App Runner service

When you create an AWS App Runner service, App Runner allocates a domain name for it. This is a subdomain in the `awsapprunner.com` domain that's
owned by App Runner. You can use the domain name to access the web application that's running in your service.

###### Note

To augment the security of your App Runner applications, the _\*.awsapprunner.com_ domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). For further security, we recommend that you use cookies with a `__Host-`
prefix if you ever need to set sensitive cookies in the default domain name for your App Runner applications.
This practice will help to defend your domain against cross-site request
forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla Developer Network.

If you own a domain name, you can associate it to your App Runner service. After App Runner validates your new domain, you can use your domain to access your
application in addition to the App Runner domain. You can associate up to five custom domains.

###### Note

You can optionally include the `www` subdomain of your domain. However, this is currently only supported by the API. The App Runner console
doesn't support including `www` subdomain of your domain.

###### Note

AWS App Runner doesn't support using Route 53 private hosted zones. Private hosted zones
customize domain name resolution for Amazon VPC traffic. For more information about private hosted zones, see [Working with private hosted zones](../../../Route53/latest/DeveloperGuide/hosted-zones-private.md "../../../Route53/latest/DeveloperGuide/hosted-zones-private.md") in the Route 53
documentation.

## Associate (link) a custom domain to your service

When you associate a custom domain to your service, you must add the CNAME records and DNS target records to your DNS server. The following sections
provide information on CNAME records and DNS target records and how to use them.

###### Note

If you're using Amazon Route 53 as your DNS provider, App Runner automatically configures your custom domain with the required certificate validation and DNS
records to link to your App Runner web application. This happens when you use the App Runner console to link your custom domain to your service. The [Manage custom domains](#manage-custom-domains.manage "#manage-custom-domains.manage") topic that follows provides more information.

### CNAME records

When you associate a custom domain with your service, App Runner provides you with a set of certificate validation records for certificate validation. You
must add these certificate validation records to your Domain Name System (DNS) server. Add the certificate validation records, provided by App Runner, to your
DNS server. This way, App Runner can validate that you own or control the domain.

###### Note

To auto-renew your custom domain certificates, ensure that you don't delete the certificate validation records from your DNS server. For
information about how to resolve issues that are related to the renewal of the certificate, see [Custom domain certificate renewal](manage-custom-domain-troubleshoot.md#certificate-renewal.troubleshoot "manage-custom-domain-troubleshoot.md#certificate-renewal.troubleshoot").

App Runner uses ACM to verify the domain. If you're using CAA records in your DNS records, make sure that at least one CAA record references
`amazon.com`. Otherwise, ACM can't verify the domain and successfully create your domain.

If you receive errors related to CAA, see the following links to learn how to resolve them:

- [Certification Authority Authorization (CAA) problems](../../../acm/latest/userguide/troubleshooting-caa.md "../../../acm/latest/userguide/troubleshooting-caa.md")
- [How do I resolve CAA errors for issuing or renewing
  an ACM certificate?](https://aws.amazon.com/premiumsupport/knowledge-center/acm-troubleshoot-caa-errors/ "https://aws.amazon.com/premiumsupport/knowledge-center/acm-troubleshoot-caa-errors/")
- [Custom domain names](manage-custom-domain-troubleshoot.md "manage-custom-domain-troubleshoot.md")

###### Note

If you're using Amazon Route 53 as your DNS provider, App Runner automatically configures your custom domain with the required certificate validation and DNS
records to link to your App Runner web application. This happens when you use the App Runner console to link your custom domain to your service. The [Manage custom domains](#manage-custom-domains.manage "#manage-custom-domains.manage") topic that follows provides more information.

### DNS target records

Add the DNS target records to your DNS server to target the App Runner domain. Add one record for the custom domain, and another for the `www`
subdomain, if you chose this option. Then, wait for the custom domain status to become **Active** in the App Runner console. This typically
takes several minutes, but might take up to 24—48 hours (1—2 days). When your custom domain is validated, App Runner starts routing traffic from
this domain to your web application.

###### Note

For better compatibility with App Runner services, we recommend that you use Amazon Route 53 as your DNS provider. If you don't use Amazon Route 53 to manage your
public DNS records, contact your DNS provider to find out how to add records.

If you're using Amazon Route 53 as your DNS provider, you can add either CNAME or alias record for _subdomain_. For _root
domain_, ensure that you use the alias record.

You can purchase a domain name from Amazon Route 53 or another provider. To purchase a domain name with Amazon Route 53, see [Registering a new domain](../../../Route53/latest/DeveloperGuide/domain-register.md "../../../Route53/latest/DeveloperGuide/domain-register.md"), in the _Amazon Route 53 Developer Guide_.

For instructions on how to configure a DNS target in Route 53, see [Routing traffic to your resources](../../../Route53/latest/DeveloperGuide/dns-routing-traffic-to-resources.md "../../../Route53/latest/DeveloperGuide/dns-routing-traffic-to-resources.md"), in
the _Amazon Route 53 Developer Guide_.

For instructions on how to configure a DNS target on other registrars, such as GoDaddy, Shopify, Hover and so on, refer to their specific
documentation on adding DNS Target records.

### Specify a domain to associate with your App Runner service

You can specify a domain to associate with your App Runner service in the following ways:

- _A root domain_ – DNS has some inherent limitations which might block you from creating CNAME records for the root
  domain name. For example, if your domain name is `example.com`, you can create a CNAME record that routes traffic for
  `acme.example.com` to your App Runner service. However, you can't create a CNAME record that routes traffic for `example.com` to
  your App Runner service. To create a root domain, ensure that you add an alias record.

An alias record is specific to Route 53 and has the following advantages over CNAME records:

    + Route 53 provides you with more flexibility as alias records can be created for root domain or subdomain. For example, if your domain name is
     `example.com`, you can create a record that routes requests for `example.com` or `acme.example.com` to your
     App Runner service.
    + It is more cost efficient. This is because Route 53 doesn't charge for requests that use an alias record to route traffic.

- _A subdomain_ – For example, `login.example.com` or `admin.login.example.com`. You can optionally
  also associate the `www` subdomain as part of the same operation. You can add either CNAME or alias record for subdomain.
- _A wildcard_ – For example, `*.example.com`. You can't use the `www` option in this case. You can
  specify a wildcard only as the immediate subdomain of a root domain and only on its own. These aren't valid specifications:
  `login*.example.com`, `*.login.example.com`. This wildcard specification associates all immediate subdomains, and doesn't
  associate the root domain itself. The root domain must be associated in a separate operation.

A more specific domain association overrides a less specific one. For example, `login.example.com` overrides `*.example.com`.
The certificate and CNAME of the more specific association are used.

The following example shows how you can use multiple custom domain associations:

1. Associate `example.com` with the home page of your service. Enable the `www` to associate
   `www.example.com`.
2. Associate `login.example.com` with the login page of your service.
3. Associate `*.example.com` with a custom "not found" page.

## Disassociate (unlink) a custom domain

You can disassociate (unlink) a custom domain from your App Runner service. When you unlink a domain, App Runner stops routing traffic from this domain to your
web application.

###### Note

You must delete the records for the domain you disassociated from your DNS server.

App Runner internally creates certificates that track domain validity. These certificates are stored in AWS Certificate Manager (ACM). App Runner doesn't delete these
certificates for 7 days after a domain is disassociated from your service or after the service is deleted.

## Manage custom domains

Manage custom domains for your App Runner service using one of the following methods:

###### Note

For better compatibility with App Runner services, we recommend that you use Amazon Route 53 as your DNS provider. If you don't use Amazon Route 53 to manage your
public DNS records, contact your DNS provider to find out how to add records.

If you're using Amazon Route 53 as your DNS provider, you can add either CNAME or alias record for _subdomain_. For _root
domain_, ensure that you use alias record.

App Runner console

###### To associate (link) a custom domain using the App Runner console

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Services**, and then choose your App Runner service.

The console displays the service dashboard with a **Service overview**.

![App Runner service dashboard page showing Activity list](images/console-dashboard.png) 3. On the service dashboard page, choose the **Custom domains** tab.

The console shows the custom domains that are associated with your service, or **No custom domains**.

![The Custom domains tab on the App Runner service dashboard page, showing no associated custom domains](images/service-dashboad-domains-empty.png)

![The Custom domains tab on the App Runner service dashboard page, showing one custom domain pending association.](images/service-dashboad-domains-one-pending.png) 4. On the **Custom domains** tab, choose **Link domain**. 5. The **Link custom domain** page displays.

    * If your custom domain is registered with Amazon Route 53, select **Amazon Route 53** for **Domain
     registrar**.


    	1. Select the **Domain name** from the drop-down list. This list displays the name of your Route 53 domain names and the
    	 hosted zone id.


    	###### Note

    	You must first create a Route 53 domain using the Amazon Route 53 service from the same AWS account that you use to manage your other
    	 App Runner resources.
    	2. Select the **DNS record type**.
    	3. Choose **Link domain**.
    ![The Link custom domain page, showing Amazon Route 53 as the selected domain provider.](images/service-domains-link-r53.png)

    ###### Note

    If App Runner displays an error message stating that the automatic configuration attempt failed, you can proceed by configuring the DNS
     records manually. This issue can arise if the same domain name was previously unlinked from a service, without the DNS provider records
     that point to the service being deleted afterward. In this case App Runner is blocked from automatically overwriting these records. To finish
     the DNS configuration, skip the remainder of the steps in this procedure and then follow the instructions in [Configure an Amazon Route 53 alias record](manage-custom-domains-route53.md "manage-custom-domains-route53.md").
    * If your custom domain is registered with another domain registrar, select **Non–Amazon** for
     **Domain registrar**.


    	1. Enter the **Domain name**.
    	2. Choose **Link domain**.

![The Link custom domain page, showing non–Amazon as the selected domain provider.](images/service-domains-link-non-amzn.png) 6. The **Configure DNS** page displays.

    * If Amazon Route 53 is your DNS provider, then this step is optional.


    At this point App Runner has automatically configured your Route 53 domain with the required certificate validation and DNS records.


    ###### Note

    If this same domain name was previously unlinked from a service, without the DNS provider records that point to the service being
     deleted afterward, the automatic configuration that App Runner attempted could have failed. To work around this issue and complete the DNS
     association, proceed with steps **(1)** and **(2)** on the **Configure DNS** page to
     copy the current target and certificate records to the DNS provider.


    	1. Copy the certificate validation records and DNS target records, and add them to your DNS server. App Runner can then validate that you own
    	 or control the domain.


    	###### Note

    	To auto-renew your custom domain certificates, make sure not to delete the certificate validation records from your DNS
    	 server.




    		+ For more information about **Configure certificate validation**, see [DNS Validation](../../../acm/latest/userguide/dns-validation.md "../../../acm/latest/userguide/dns-validation.md") in the
    		 *[AWS Certificate Manager User Guide](../../../acm/latest/userguide.md "../../../acm/latest/userguide.md")*.
    		+ For information about how to **Configure DNS target** with Amazon Route 53 alias record, see [Configure Amazon Route 53 alias record for your target DNS](manage-custom-domains-route53.md "manage-custom-domains-route53.md").
    * If you're using a DNS provider other than Amazon Route 53, follow these steps.


    	1. Copy the certificate validation records and DNS target records, and add them to your DNS server. App Runner can then validate that you own
    	 or control the domain.


    	###### Note

    	To auto-renew your custom domain certificates, make sure not to delete the certificate validation records from your DNS
    	 server.




    		+ For more information about **Configure certificate validation**, see [DNS Validation](../../../acm/latest/userguide/dns-validation.md "../../../acm/latest/userguide/dns-validation.md") in the
    		 *[AWS Certificate Manager User Guide](../../../acm/latest/userguide.md "../../../acm/latest/userguide.md")*.
    		+ For instructions on how to configure a DNS target on other registrars, such as GoDaddy, Shopify, Hover and so on, refer to their
    		 specific documentation on adding DNS Target.

![The Configure DNS page, showing certificate validation and DNS target records to add to your DNS.](images/custom-domain-configure.png) 7. Choose **Close**

The console shows the dashboard again. The **Custom domains** tab has a new tile showing the domain that you just linked in
the **Pending certificate DNS validation** status.

![The Custom domains tab on the App Runner service dashboard page, showing a custom domain tile](images/service-dashboad-domains-tile.png) 8. When the domain status changes to **Active**, verify that the domain works for routing traffic by browsing to it.

![The Custom domains tab on the App Runner service dashboard page, showing a custom domain tile](images/service-dashboad-domains-tile-active.png)

###### Note

For instructions on how to troubleshoot errors related to custom domain, see [Custom domain names](manage-custom-domain-troubleshoot.md "manage-custom-domain-troubleshoot.md").

###### To disassociate (unlink) a custom domain using the App Runner console

1. On the **Custom domains** tab, select the tile for the domain you want to disassociate, and then choose **Unlink
   domain**.
2. In the **Unlink domain** dialog, verify the action by choosing **Unlink domain**.

###### Note

You must delete the records for the domain that you disassociated from your DNS server.

App Runner API or AWS CLI
To associate a custom domain with your service using the App Runner API or AWS CLI, call the [AssociateCustomDomain](../api/API_AssociateCustomDomain.md "../api/API_AssociateCustomDomain.md") API action. When the call succeeds, a [CustomDomain](../api/API_CustomDomain.md "../api/API_CustomDomain.md") object is
returned that describes the custom domain that's being associated with your service. The object shows a `CREATING` status and contains a
list of [CertificateValidationRecord](../api/API_CertificateValidationRecord.md "../api/API_CertificateValidationRecord.md") objects. The call also returns the target
alias that you can use to configure the DNS target. These are records that you can add to your DNS.

To disassociate a custom domain from your service using the App Runner API or AWS CLI, call the [DisassociateCustomDomain](../api/API_DisassociateCustomDomain.md "../api/API_DisassociateCustomDomain.md") API action. When the call succeeds, a [CustomDomain](../api/API_CustomDomain.md "../api/API_CustomDomain.md") object is returned that describes the custom domain that's being disassociated from
your service. The object shows a `DELETING` status.

###### Topics

- [Configure Amazon Route 53 alias record for your target DNS](manage-custom-domains-route53.md "manage-custom-domains-route53.md")
