

# .de (Germany)
<a name="de"></a>

[Return to index](registrar-tld-list.md#index)

**Lease period for registration and renewal**  
One year.

**Restrictions**  
Open to the public, with some restrictions:  
+ You must reside in Germany or have an administrative contact (physical person) who resides in Germany and has an address other than a P.O. box.
+ During registration, the DNS (A, MX, and CNAME) of the domain name must be correctly configured so that it can pass the registry's zone check. Three servers of two different C classes are required.
+ If you're using a DNS service other than Route 53, the name servers for the domain must pass a check to make sure that they're correctly configured. To determine whether the name servers for your domain will pass the check, see [https://www.denic.de/en/service/tools/nast/](https://www.denic.de/en/service/tools/nast/).
+ You must provide contact information that meets registry validation requirements. Invalid or incorrectly formatted contact details can cause domain renewals to fail.

**Privacy protection**  
Not supported.

**Domain locking to prevent unauthorized transfers**  
Not supported. We recommend that you prevent unauthorized transfers by restricting access to the [RetrieveDomainAuthCode](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RetrieveDomainAuthCode.html) API action. (When you restrict access to this Route 53 API, you also restrict who can generate an authorization code using the Route 53 console, AWS SDKs, and other programmatic methods.) For more information, see [Identity and access management in Amazon Route 53](security-iam.md).

**Internationalized domain names**  
Supported.

**Authorization code required for transfers**  
Yes

**DNSSEC**  
Supported for domain registration. For more information, see [Configuring DNSSEC for a domain](domain-configure-dnssec.md).

**Deadlines for renewing and restoring domains**  
+ Renewal is possible: Until the expiration date
+ Late renewal with Route 53 is possible: No
+ Domain is deleted from Route 53: On the expiration date
+ Restoration with the registry is possible: Only if you deleted the domain. Expired .de domains can't be restored. See the following note.
+ Domain is deleted from the registry: After the restoration period ends.

**Note**  
How you recover a .de domain depends on its status with DENIC, the registry for .de.  
If you deleted the domain and it's within DENIC's redemption grace period, you can recover the domain by [restoring it](domain-restore-expired.md).
If the domain expires, it leaves Route 53 and enters DENIC's TRANSIT status. DENIC mails the domain holder a letter with an authorization code. If you don't receive it, you can request a new code from DENIC. Within the period stated in the letter, you can recover the domain by [transferring it back to Route 53](domain-transfer-to-route-53.md) using that code.