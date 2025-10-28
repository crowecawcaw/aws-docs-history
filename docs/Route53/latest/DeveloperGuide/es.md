# .es (Spain)

[Return to index](registrar-tld-list.md#index "registrar-tld-list.md#index")

**Domain purchase or transfer**

###### Important

You currently can purchase new .es domain names or transfer
.es domains to Route 53 . The contact type for the registrant
contact has no restriction. Admin / Tech / Billing contact type must be a **person**.

**Lease period for registration and renewal**

One to five years.

**Restrictions**

Open to the public, for those who have an interest in or
connection with Spain.

As of 2016, the .ES domain registrants must provide a registrant contact email. If you
haven't provided this information, you need to do so at the current
registrar before you transfer your domain to Route 53.

You will need the following information:

- ESNIC identifier similar to `AAAA0-ESNIC-F0`.
- If you don't know your ESNIC identifier, you can get it from the current registrar. You can
  find your registrar at: [https://www.dominios.es/en](https://www.dominios.es/en "https://www.dominios.es/en").

Depending on whether you remember your password at the registrar, or not, you can follow one of the following procedures to update
your registrant email:

- If you remember you password, sign in at [https://www.nic.es/sgnd/login.action](https://www.nic.es/sgnd/login.action "https://www.nic.es/sgnd/login.action") by using
  you ESNIC identifies and password.

After you have signed in, you can edit the registrant email contact by choosing the
**Edit** tab on the registry
page.

- If you forgot your password, browse to [https://www.nic.es/sgnd/peticion/editCorreo.action?request_locale=en](https://www.nic.es/sgnd/peticion/editCorreo.action?request_locale=en "https://www.nic.es/sgnd/peticion/editCorreo.action?request_locale=en").

Fill out the form with your ESNIC identifier, your new and valid registrant email
contact. Then, validate the form by choosing
**Processing without eID/Certificate**,
and upload the requested identity document.

**Privacy protection**

Not supported.

**Domain locking to prevent unauthorized transfers**

Supported

**Internationalized domain names**

Supported.

**Authorization code required for transfers**

Yes

The .es registry manages the authorization code with a time-to-live and it might become
expired. You can refresh the auth code by removing the transfer lock
(clientTransferProhibited) status from your domain if it is present.
If the domain has no transfer lock, you can refresh the auth code by
turning it on first, and then off.

**DNSSEC**

Supported for domain registration. For more information, see [Configuring DNSSEC for a domain](domain-configure-dnssec.md "domain-configure-dnssec.md").

**Deadlines for renewing and restoring domains**

- Renewal is possible: Until 6 days before the expiration
  date
- Late renewal with Route 53 is possible: No
- Domain is deleted from Route 53: 6 days before
  expiration
- Restoration with the registry is possible: Between 6 days
  before and 4 days after expiration
- Domain is deleted from the registry: 4 days after
  expiration
