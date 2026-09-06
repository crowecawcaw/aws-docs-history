

# Transferring a domain from Amazon Route 53 to another registrar
<a name="domain-transfer-from-route-53"></a>

When you transfer a domain from Amazon Route 53 to another registrar, you get some information from Route 53 and provide it to the new registrar. The new registrar will do the rest.

**Important**  
If you're currently using Route 53 as your DNS service provider and you also want to transfer DNS service to another provider, be aware that the following Route 53 features don't have direct parallels with features provided by other DNS service providers. You'll need to work with the new DNS service provider to determine how to achieve comparable functionality:  
Alias records. For more information, see [Choosing between alias and non-alias records](resource-record-sets-choosing-alias-non-alias.md).
Routing policies other than the simple routing policy. For more information, see [Choosing a routing policy](routing-policy.md).
Health checks that are associated with records. For more information, see [Configuring DNS failover](dns-failover-configuring.md).

Most domain registrars enforce requirements on transferring a domain to another registrar. The primary purpose of these requirements is to prevent the owners of fraudulent domains from repeatedly transferring the domains to different registrars. Requirements vary, but the following requirements are typical: 
+  You must have registered the domain with the current registrar or transferred registration for the domain to the current registrar at least 14 days ago.
+ The domain cannot have any of the following domain name status codes:
  + pendingDelete
  + pendingTransfer
  + redemptionPeriod
  + clientTransferProhibited
  + serverTransferProhibited

For a current list of domain name status codes and an explanation of what each code means, go to the [ICANN website](https://www.icann.org/) and search for **epp status codes**. (Search on the ICANN website; web searches sometimes return an old version of the document.)

**Note**  
If you want to transfer your domain to another domain registrar but the AWS account that the domain is registered with is closed, suspended, or terminated, you can contact AWS Support for help. Domains cannot be transferred within the first 14 days of registration. For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md).

**Note**  
If the new registrar requires a REG-ID code, you can contact AWS Support for help. For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md).<a name="domain-transfer-from-route-53-procedure"></a>

**To transfer a domain from Route 53 to another registrar**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Registered domains**.

1. Choose the name of the domain that you want to transfer to another registrar.

1. On the *domain name* page, check the value of **Domain name status code**. If it is one of the following values, you can't currently transfer the domain: 
   + pendingDelete
   + pendingTransfer
   + redemptionPeriod
   + clientTransferProhibited
   + serverTransferProhibited

   For a current list of domain name status codes and an explanation of what each code means, go to the [ICANN website](https://www.icann.org/) and search for **epp status codes**. (Search on the ICANN website; web searches sometimes return an old version of the document.)

   If the value of **Domain name status code** is **serverTransferProhibited**, you can contact AWS Support for free to learn what you must do so you can transfer the domain. For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md).

1. If the value of **Transfer lock** is **On**, choose **Turn off transfer lock** from the **Actions** dropdown.

1. *All domains except .be, .co.za, .ru, .uk, .co.uk, .me.uk, and .org.uk domains* – On the *domain name* page, choose **Transfer to another registrar** from the **Transfer out** dropdown. 

    In the **Transfer to another registrar** dialog box, choose **Copy** to copy the authorization code for the domain transfer. You'll provide this value to your registrar later in this procedure.
**Note**  
For .eu domains, you can also generate the auth code by using the "My.eu" panel at the registry: [https://my.eurid.eu/](https://my.eurid.eu/).

   *.be, .co.za, .es, .ru, .uk, .co.uk, .me.uk, and .org.uk domains* – Do the following:  
**.be domains**  
Get the authorization code from the registry for .be domains at [DNS Belgium website](https://www.dnsbelgium.be/en/transfer-code).  
**.co.za domains**  
You don't need to get an authorization code to transfer a .co.za domain to another registrar.  
**.ru domains**  
Get the authorization code from the registry for .ru domains at [https://www.nic.ru/en/auth/recovery/](https://www.nic.ru/en/auth/recovery/):  

   1. Choose the option to recover credentials by domain name.

   1. Enter your domain name, and choose **Continue**.

   1. Follow the on-screen prompts to get access to the RU-CENTER admin page.

   1. In the **Manage your account** section, choose **Domain transfer**.

   1. Confirm the transfer with REGRU-RU.  
**.uk, .co.uk, .me.uk, and .org.uk domains**  
Change the IPS tag to the value for the new registrar:  

   1. Go to the [Find a Registrar](http://www.nominet.uk/registrar-list/) page on the Nominet website, and find the IPS tag for the new registrar. (Nominet is the registry for .uk, .co.uk, .me.uk, and .org.uk domains.)

   1. On the **Registered Domains >** *domain name* page, select the **Transfer out**, drop-down, then **Update IPS Tag**, and specify the value that you got in step 6a.

   1. Choose **Update**.
**Note**  
You can also update the IPS tag on the Nominet console. For instructions, see [Switch the registrar](https://theukdomain.uk/help-centre/can-i-switch-the-registrar-i-have-my-domain-registered-with/).

1. If you're not currently using Route 53 as the DNS service provider for your domain, skip to step 10.

   If you are currently using Route 53 as the DNS service provider for the domain, perform the following steps:

   1. Choose **Hosted Zones.**

   1. Choose the name of the hosted zone for your domain. The domain and the hosted zone have the same name.

   1. *If you want to continue using Route 53 as the DNS service provider for the domain:* Get the names of the four name servers that Route 53 assigned to your hosted zone. For more information, see [Getting the name servers for a public hosted zone](GetInfoAboutHostedZone.md).

      *If you do not want to continue using Route 53 as the DNS service provider for the domain:* Make note of the settings for all of your records except the NS and SOA records. For Route 53–specific features such as alias records, you'll need to work with your new DNS service provider to determine how to achieve comparable functionality.

1. If you're transferring DNS service to another provider, use the methods that are provided by the new DNS service to perform the following tasks:
   + Create a hosted zone
   + Create records that reproduce the functionality of your Route 53 records
   + Get the name servers that the new DNS service assigned to your hosted zone

1. Use the process that is provided by the new registrar to request a transfer of the domain.

   *All domains except .co.za, .uk, .co.uk, .me.uk, and .org.uk domains* – You'll be prompted to enter the authorization code that you got from the Route 53 console in step 6 of this procedure.

1. If you still want to use Route 53 as your DNS service provider, use the process that is provided by the new registrar to specify the names of the Route 53 name servers that you got in step 7. If you want to use another DNS service provider, specify the names of the name servers that the new provider gave you when you created a new hosted zone in step 8.

1. Act on the confirmation email:  
**All domains except .jp domains**  
Route 53 sends a confirmation email to the registrant contact for the domain:  
   + Depending on the TLD, the confirmation email includes a link from one of the following domains. Use this link to approve or reject the transfer.
     + registrar.amazon
     + domainnameverification.net
     + emailverification.info
     + key-systems.net
   + If you don't take action, the transfer will proceed automatically on the specified date.  
**.jp domains**  
Route 53 sends a confirmation email to the registrant contact for the domain from address *noreply@domainnameverification.net* or *noreply@emailverification.info* with a link to confirm the transfer:  
   + Use this link to approve or reject the transfer. You will need to provide the domain authorization code that you obtained in step 7.
   + If you don't take action, the transfer will be canceled on the specified date.
In addition you might receive an email from WIXI.jp. You can ignore this email.

1. If the registrar that you're transferring the domain to reports that the transfer failed, contact that registrar for more information. When you transfer a domain to another registrar, all status updates go to the new registrar, so Route 53 has no information about why a transfer failed.

   If the new registrar reports that the transfer failed because the authorization code that you got from Route 53 isn't valid, open a case with AWS Support. (You don't need a support contract, and there's no fee.) For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md).
**Note**  
Authorization codes generated by Gandi are valid for about 5 days. If your transfer attempt occurs after this period, it might fail due to an expired code.

1. If you transferred DNS service to another DNS service provider, you can delete the records in the hosted zone and delete the hosted zone after DNS resolvers stop responding to DNS queries with the names of Route 53 name servers. This typically takes two days, the amount of time that DNS resolvers commonly cache the names of name servers for a domain.
**Important**  
If you delete the hosted zone while DNS resolvers are still responding to DNS queries with the names of Route 53 name servers, your domain will become unavailable on the internet.

   After you delete the hosted zone, Route 53 will stop billing you the monthly charge for a hosted zone. For more information, see the following documentation:
   + [Deleting records](resource-record-sets-deleting.md)
   + [Deleting a public hosted zone](DeleteHostedZone.md)
   + [Route 53 Pricing](https://aws.amazon.com/route53/pricing)