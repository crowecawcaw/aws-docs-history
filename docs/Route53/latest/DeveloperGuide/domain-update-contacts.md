# Updating contact information and ownership for

a domain

For the administrative and technical contacts for a domain, you can change all contact
information without having to authorize the changes. For more information, see [Updating contact information for a
domain](#domain-update-contacts-basic "#domain-update-contacts-basic").

For the registrant contact, you can change most values without having to authorize the
changes. However, for some TLDs, changing the owner of a domain requires authorization.
For more information, see the applicable topic.

###### Topics

- [What triggers a domain
  ownership change?](#domain-update-contacts-who-is-domain-owner "#domain-update-contacts-who-is-domain-owner")
- [TLDs that require special processing
  to change the owner](#domain-update-contacts-tlds "#domain-update-contacts-tlds")
- [Updating contact information for a
  domain](#domain-update-contacts-basic "#domain-update-contacts-basic")
- [Changing the owner of
  a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form")

## What triggers a domain

ownership change?

###### Important

The contact you list as the registrant will have certain rights as the
Registered Name Holder of the domain name, under the [ICANN Transfer Policy](https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en "https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en"). Most domains will be deleted upon closure of
your AWS account (for more information, see [My AWS account is closed or permanently
closed, and my domain is registered with Route 53](troubleshooting-account-closed.md "troubleshooting-account-closed.md")), however if a domain
remains in a closed account, the contact you listed as the registrant may have
the ability to request a transfer of the domain name to an external registrar.
Therefore, it is important that the registrant contact you list is either
yourself or another person you trust to act responsibly.

The following changes to registrant contact information trigger the domain
ownership change process:

**For Person contact type**

Changing the **First Name** or **Last
Name** fields triggers an ownership change.

**For non-Person contact types (Company, Association, Public Body)**

Changing the **Organization** field triggers an
ownership change.

**Additional triggers (all contact types)**

Depending on your domain's TLD requirements, other contact field
changes might also trigger the ownership change process,
including:

- Changes to the registrant email address
- Changes to other identifying information fields

The specific fields that trigger ownership changes vary by TLD and are
determined by the domain registry's policies.

###### Warning

**Service interruption risk:** When an ownership
change is triggered, you will receive an authorization email. If you don't
respond to this email within 3-15 days (depending on your TLD), your domain
registration will be cancelled as required by ICANN, which will interrupt your
website and email services.

Always ensure you can access the registrant contact email address before
making any contact changes.

Note the following about changing the owner of a domain:

- For some TLDs, there's a fee to change the owner of a domain. To determine
  whether there's a fee for the TLD for your domain, see the "Change Ownership
  Price" column in [Amazon Route 53 Pricing for Domain Registration](https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf "https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf").

###### Note

You can't use AWS credits to pay the fee, if any, to change the
owner of a domain.

- For some TLDs, when you change the owner of a domain, we send an
  authorization email to the email address for the registrant contact. The
  registrant contact must follow the instructions in the email to authorize
  the change.
- For some TLDs, you need to fill out a Change of Domain Ownership Form and
  provide proof of identity so that an Amazon Route 53 support engineer can update
  the values for you. If the TLD for your domain requires a Change of Domain
  Ownership form, the console displays a message that links to a form for
  opening a support case. For more information, see [Changing the owner of
  a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form").

## TLDs that require special processing

to change the owner

When you change the owner of a domain, the registries for some TLDs require
special processing. If you're changing the owner for any of the following domains,
perform the applicable procedure. If you're changing the owner for any other domain,
you can change the owner yourself, either programmatically or using the Route 53
console. See [Updating contact information for a
domain](#domain-update-contacts-basic "#domain-update-contacts-basic").

The following TLDs require special processing to change the owner of the
domain:

[.be](#be-special "#be-special"), [.cl](#cl-special "#cl-special"), [.com.br](#com.br-special "#com.br-special"), [.es](#es-special "#es-special"), [.fi](#fi-special "#fi-special"), [.ru](#ru-special "#ru-special"), [.se](#se-special "#se-special"), [.sh](#sh-special "#sh-special")

**.be**

You must get a transfer code from the registry for .be domains, and
then open a case with AWS Support.

- To get the transfer code, see [https://www.dnsbelgium.be/en/manage-your-domain-name/change-holder#transfer](https://www.dnsbelgium.be/en/manage-your-domain-name/change-holder#transfer "https://www.dnsbelgium.be/en/manage-your-domain-name/change-holder#transfer"),
  and follow the prompts.
- To open a case, see [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").

**.cl**

You must complete and submit a form to AWS Support. See [Changing the owner of
a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form").

**.com.ar**

You must complete and submit a form to AWS Support. See [Changing the owner of
a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form").

**.com.br**

You must complete and submit a form to AWS Support. See [Changing the owner of
a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form").

**.es**

You must complete and submit a form to AWS Support. See [Changing the owner of
a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form").

**.fi**

Initiate the owner change on the Route 53 console. After you have
initiated the change, you will receive a **Holder
transfer key** from
*fi-domain-tech@traficom.fi* email address. After
you receive the key, open a support case with AWS Support, and share
the key code with us. See [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").

**.qa**

You must complete and submit a form to AWS Support. See [Changing the owner of
a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form").

**.ru**

You must complete and submit a form to AWS Support. See [Changing the owner of
a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form").

**.se**

You must complete and submit a form to AWS Support. See [Changing the owner of
a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form").

**.sh**

You must complete and submit a form to AWS Support. See [Changing the owner of
a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form").

## Updating contact information for a

domain

To update contact information for a domain, perform the following procedure.

###### Warning

**Service interruption risk:** If your contact
changes trigger the owner change process, you will receive an authorization
email. If you don't respond to this email within 3-15 days (depending on your
TLD), your domain registration will be cancelled as required by ICANN, which
will interrupt your website and email services.

Ensure you can access the registrant contact email address before making any
contact changes.

### Before updating domain

contacts

Before making any changes to your domain's registrant contact information,
complete this checklist:

1. **☐ Verify email access** - Confirm you
   can receive email at the current registrant email address
2. **☐ Understand owner change triggers** -
   Review [What triggers a domain
   ownership change?](#domain-update-contacts-who-is-domain-owner "#domain-update-contacts-who-is-domain-owner") to
   understand what changes might trigger the owner change process
3. **☐ Plan for potential downtime** - If
   owner change is triggered, you have 3-15 days to respond to the
   authorization email or your domain will be cancelled

###### To update contact information

for a domain

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Registered
   domains**.
3. Choose the name of the domain that you want to update contact information
   for.
4. In the **Contact information** tab, choose
   **Edit**.
5. If you don't have access to the email address for the registrant contact,
   perform the following steps. If you have access to the email address for the
   registrant contact, skip to step 6.
   1. Change _only_ the email address for the
      registrant contact. Don't change any other values for any of the
      contacts for the domain. If you also want to change other values,
      you change them later in the process.

   Choose **Save changes**.

   To verify the new email address, we send a verification email to
   the new address (if required for the TLD). You must choose the link
   in the email to verify that the new email address is valid. If
   verification is required, and you don't verify the new email
   address, Route 53 suspends the domain as required by ICANN.

   If you need to resend the verification email, navigate to the
   **Registered domains** page, choose the radio
   button next to the domain name you updated, and choose the name of
   the domain that you're updating. On the **Verify your email
   to avoid domain suspension** alert, choose
   **Send email again**. 2. If you want to change other values for the registrant, admin,
   tech, or billing contacts for the domain, return to step 1 and
   repeat the procedure.

6. Update the applicable values. You can also choose **Copy
   registrant contact** to automatically fill in the same
   information you entered for the registrant contact. For more information,
   see [Values that you specify when you register or transfer a domain](domain-register-values-specify.md "domain-register-values-specify.md").

Depending on the TLD for your domain and the values that you're changing,
the console might display the following message:

"To change the registrant name or organization, open a case."

If you see that message, skip the rest of this procedure and see [Changing the owner of
a domain when the registry requires a Change of Domain Ownership form](#domain-update-contacts-domain-ownership-form "#domain-update-contacts-domain-ownership-form") for more
information. 7. Choose **Save**. 8. If you changed the domain owner, as described in [What triggers a domain
ownership change?](#domain-update-contacts-who-is-domain-owner "#domain-update-contacts-who-is-domain-owner"), we send
email to the registrant contact for the domain. The email asks for
authorization for the change of owner.

If we don't receive authorization for the change within 3 to 15 days,
depending on the top-level domain, we must cancel the request as required by
ICANN.

The email comes from one of the following email addresses.

| TLDs               | Email address that authorization email comes from                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| .fr                | nic@nic.fr                                                                                                                                      |
| .com.au<br>.net.au | noreply@emailverification.info                                                                                                                  |
| All others         | One of the following email addresses:<br>• noreply@registrar.amazon<br>• noreply@domainnameverification.net<br>• noreply@emailverification.info |

9. If you encounter issues while updating contact information, you can
   contact AWS Support for free. For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").

For information about the API you can use to update the contact information, see
[UpdateDomainContact](../APIReference/API_domains_UpdateDomainContact.md "../APIReference/API_domains_UpdateDomainContact.md").

## Changing the owner of

a domain when the registry requires a Change of Domain Ownership form

If the registry for your domain requires you to complete a Change of Domain
Ownership and submit the form to AWS Support, perform the following procedure. To
determine whether you need to perform this procedure, see the following
topics:

- To determine whether the value you're changing is considered a change of
  owner, see [What triggers a domain
  ownership change?](#domain-update-contacts-who-is-domain-owner "#domain-update-contacts-who-is-domain-owner").
- To determine whether a Change of Domain Ownership form is required for
  your domain, see [TLDs that require special processing
  to change the owner](#domain-update-contacts-tlds "#domain-update-contacts-tlds").

###### To change

the owner of a domain when the registry requires a Change of Domain Ownership
form

1. See the introduction to this topic to determine whether the registry for
   your domain requires special processing to change the owner of the domain.
   If so, and if a Change of Domain Ownership form is required, continue with
   this procedure.

If no Change of Domain Ownership form is required, perform the procedure
in the applicable topic instead. 2. Download the [Change of Domain Ownership Form](samples/ChangeOfOwnerForm.md "samples/ChangeOfOwnerForm.md"). The file is compressed into a
.zip file. 3. Fill out the form. 4. For the registrant contact for the former owner of the domain
_and_ for the new owner, get a copy of a signed proof
of identity (identity card, driver's license, passport, or other legal proof
of identity).

In addition, if a legal entity is listed as the registrant organization,
gather the following information for the former owner of the domain
_and_ for the new owner:

    * Proof that the organization that the domain is registered to
     exists.
    * Proof that the representatives for the former owner and the new
     owner are authorized to act on the organization's behalf. This
     document must be a certified legal document that contains both the
     name of the organization and the names of the representatives as
     signing officers (for example, CEO, President, or Executive
     Director).

5. Scan the Change of Domain Ownership form and the required proof. Save the
   scanned documents in a common format, such as a .pdf file or a .png
   file.
6. Using the AWS account that the domain is currently registered to, sign
   in to the [AWS Support Center](https://console.aws.amazon.com/support/cases#/create?issueType=customer-service&serviceCode=service-domains&categoryCode=change-of-ownership "https://console.aws.amazon.com/support/cases#/create?issueType=customer-service&serviceCode=service-domains&categoryCode=change-of-ownership").

###### Important

You must sign in either by using the root account or by using a user
that has been granted IAM permissions in one or more of the following
ways:

    * The user is assigned the
     **AdministratorAccess** managed
     policy.
    * The user is assigned the
     **AmazonRoute53DomainsFullAccess** managed
     policy.
    * The user is assigned the
     **AmazonRoute53FullAccess** managed
     policy.If you don't sign in either by using the root account or by using a

user that has the required permissions, we can't update the domain
owner. This requirement prevents unauthorized users from changing the
owner of a domain. 7. Specify the following values:

**Regarding**

Accept the default value of **Account and
billing**.

**Service**

Accept the default value of
**Domains**.

**Category**

Accept the default value of **Change of
Ownership**.

**Severity**

Accept the default value of **General question**.

Choose **Next step: Additional
information**

**Subject**

Specify Change the owner of a domain.

**Description**

Provide the following information:

    * Domain that you want to change the owner for
    * [12-digit account ID](../../../general/latest/gr/acct-identifiers.md#FindingYourAccountIdentifiers "../../../general/latest/gr/acct-identifiers.md#FindingYourAccountIdentifiers") of the AWS account
     that the domain is registered to

**Add attachment**

Upload the documents that you scanned in step 5.

**Contact method**

Specify a contact method and enter the applicable
values. 8. Choose **Submit**.

An AWS Support engineer reviews the information that you provided and
updates the settings. The engineer will either contact you when the update
is finished or contact you for more information.
