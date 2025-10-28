# Restoring an expired or deleted domain

If you don't renew a domain before the end of the late-renewal period or if you accidentally
delete the domain, for some registries for top-level domains (TLDs), you can restore the
domain before it becomes available for others to register.

When a domain is deleted or it passes the end of the late-renewal period, it no longer appears in the Amazon Route 53 console.

###### Important

The price for restoring a domain is typically higher and sometimes much higher than the price
for registering or renewing a domain. For the current price for restoring a domain,
see the Restoration Price column in [Amazon Route 53 Pricing for Domain Registration](https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf "https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf").

You can't use AWS credits to pay the fee for restoring an expired domain.

###### To try to restore domain registration when a domain is deleted or the

late-renewal period has expired

1. Determine whether the TLD registry for the domain supports restoring domains and, if so, the period
   during which restoration is allowed.
   1. Go to [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md").

   ###### Important

   For generic TLD domains that are deleted within the first 5 days after registration, the
   standard 30-day redemption period (to check for the actual redemption period number of days,
   see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md")) does not apply. Instead, these domains become immediately
   available for new registration. 2. Find the TLD for your domain, and review the values in the Deadlines for renewing and
   restoring domains section.###### Important

We forward restoration requests to Gandi, which processes the requests during business hours
Monday through Friday. Gandi is based in Paris, where the time is UTC/GMT +1 hour. As a result, depending on when you submit
your request, in rare cases it can take a week or more for a request to be processed. 2. Review the price for restoring a domain, which is often higher and sometimes much higher than
the price for registering or renewing a domain. In [Amazon Route 53 Pricing for Domain Registration](https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf "https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf"), find the TLD for your
domain (such as .com) and check the price in the Restoration Price column. If
you still want to restore the domain, make note of the price; you'll need it in
a later step. 3. Using the AWS account that the domain was registered to, sign in to the
[AWS Support Center](https://console.aws.amazon.com/support/cases#/create?issueType=customer-service&serviceCode=service-domains&categoryCode=restoration "https://console.aws.amazon.com/support/cases#/create?issueType=customer-service&serviceCode=service-domains&categoryCode=restoration"). 4. Specify the following values:

**Regarding**
Accept the default value of **Account and billing**.

**Service**
Accept the default value of **Domains**.

**Category**
Accept the default value of **Restoration**.

**Severity**
Accept the default value of **General question**.

Choose **Next step: Additional information**

**Subject**

Enter **Restore an expired domain** or **Restore a deleted domain**.

**Description**
Provide the following information:

    * The domain that you want to restore
    * The [12-digit account ID](../../../general/latest/gr/acct-identifiers.md#FindingYourAccountIdentifiers "../../../general/latest/gr/acct-identifiers.md#FindingYourAccountIdentifiers")
     of the AWS account that the domain was registered to
    * Confirmation that you agree to the price for restoring the domain. Use the following text:


    **"I agree to the price of $\_\_\_\_ for restoring my domain."**


    Replace the blank with the price that you found in step 2.

**Contact method**
Specify a contact method and enter the applicable values. 5. Choose **Submit**. 6. When we learn whether we were able to restore your domain, an AWS Support representative
will contact you. In addition, if we were able to restore your domain, the domain will reappear in the console.
The expiration date depends on whether the domain expired or was accidentally deleted:

**The domain expired**
The new expiration date is usually one or two years (depending on the TLD) after the old expiration date.

###### Note

The new expiration date is not calculated from the date that the domain was restored.

**The domain was accidentally deleted**
The expiration date typically doesn't change.
