# Updating DNS records for a domain managed by Cloudflare

If Cloudflare is your DNS provider, use the following instructions to update your DNS
records in the Cloudflare dashboard to finish connecting your Amplify app to your
Cloudflare domain. Cloudflare can also act as a reverse proxy to provide caching, security,
and performance features. Because Amplify verifies your DNS records before it issues an
SSL/TLS certificate, you must first add your records using Cloudflare's **DNS only** mode. After Amplify verifies your domain, you can
optionally enable the Cloudflare proxy for your domain records.

When you add a custom domain, Amplify configures both the root domain (also called the
apex or naked domain, for example **example.com**) and the
**www** subdomain (**www.example.com**) by default. Amplify also provides an option to
automatically redirect the root domain to the www subdomain. Because of this, you typically
add DNS records in Cloudflare for both the apex domain and the www subdomain.

###### Note

The apex domain is the part that commonly causes issues with third-party DNS
providers. DNS standards don't allow a CNAME record at the apex of a domain. Cloudflare
works around this limitation by automatically applying [CNAME
flattening](https://developers.cloudflare.com/dns/cname-flattening/ "https://developers.cloudflare.com/dns/cname-flattening/"). When you add a CNAME record for the apex domain (by using
**@** as the record name), Cloudflare flattens it to the
address records that are required at the apex, so you can point your root domain to the
Amplify domain without extra configuration.

###### To add a custom domain managed by Cloudflare

1. Before you can update your DNS records with Cloudflare, complete steps one through
   nine of the procedure [Adding a custom domain managed by a third-party DNS provider](to-add-a-custom-domain-managed-by-a-third-party-dns-provider.md "to-add-a-custom-domain-managed-by-a-third-party-dns-provider.md").
2. Log in to your Cloudflare account at [https://dash.cloudflare.com/](https://dash.cloudflare.com/ "https://dash.cloudflare.com/").
3. Choose the domain to add. In the left navigation pane, choose **DNS**, and then choose **Records**.
4. Create a CNAME record for each domain that Amplify is configuring. By default,
   this is the apex domain (for example, **example.com**)
   and the www subdomain (**www.example.com**). Repeat the
   following substeps to add a record for each one.

   1. Choose **Add record**.
   2. For **Type**, choose **CNAME**.
   3. For **Name**, enter the record name for the domain you're
      adding:

      - For the apex domain, enter **@**.
        Cloudflare automatically applies CNAME flattening at the apex, as
        described in the preceding note.
      - For the www subdomain, enter **www**.

   4. For **Target**, look at your DNS records in the Amplify
      console and enter the value. For example, if the Amplify console displays the
      domain for your app as **d111111abcdef8.cloudfront.net**, enter
      `d111111abcdef8.cloudfront.net`.
   5. For **Proxy status**, choose **DNS
      only** (the gray cloud).
   6. Choose **Save**.

5. Create the second CNAME record to point to the AWS Certificate Manager (ACM) validation server.
   A single validated ACM generates an SSL/TLS certificate for your domain.

   1. Choose **Add record**.
   2. For **Type**, choose **CNAME**.
   3. For **Name**, enter the subdomain. For example, if the DNS
      record in the Amplify console for verifying ownership of your subdomain is
      **\_c3e2d7eaf1e656b73f46cd6980fdc0e.example.com**, enter only
      `_c3e2d7eaf1e656b73f46cd6980fdc0e`.
   4. For **Target**, enter the ACM validation certificate value
      from the Amplify console. For example, **\_cjhwou20vhu2exampleuw20vuyb2ovb9.j9s73ucn9vy.acm-validations.aws**.
   5. For **Proxy status**, choose **DNS
      only** (the gray cloud).
   6. Choose **Save**.###### Important

You must keep the ACM validation record set to **DNS
only**. AWS relies on the accuracy of this CNAME record to
automatically renew your SSL/TLS certificate. If you proxy the certificate record,
certificate renewal fails, which can result in your domain becoming
unavailable. 6. Amplify verifies the records and adds your domain. While Amplify is verifying
your domain, all records must remain in **DNS only**
mode. Amplify reads the record values directly, and proxied records prevent
Amplify from reading the correct values.

###### Note

Verification of domain ownership and DNS propagation for third-party domains can
take up to 48 hours. For help resolving errors that occur, see [Troubleshooting custom
domains](custom-domain-troubleshoot-guide.md "custom-domain-troubleshoot-guide.md"). 7. (Optional) After Amplify verifies your domain, you can proxy your subdomain
records through Cloudflare.

    1. In the left navigation pane, choose **SSL/TLS**.
     On the **Overview** page, choose **Configure**, and then choose **Full
     (Strict)** as the encryption mode. This mode uses HTTPS end to end,
     works with the SSL/TLS certificate that Amplify provisions, and prevents
     redirect loops. Don't use **Flexible** mode, which
     uses HTTP between Cloudflare and Amplify and can cause redirect loops.
    2. Choose **DNS** > **Records**, and set the **Proxy status** to
     **Proxied** (the orange cloud) for your
     subdomain records. Keep the ACM validation record set to **DNS only**.

###### Note

The default Amplify certificate generated by AWS Certificate Manager (ACM) is valid for 13 months
and renews automatically as long as your app is hosted with Amplify. Amplify can't
renew the certificate if the CNAME verification record has been modified, deleted, or
proxied through Cloudflare. If this happens, you must delete and add the domain again in
the Amplify console.
