# Attaching a certificate to an email identity

Before you can attach a certificate to an email identity, you must meet the following
prerequisites:

- A verified email identity.
- An S/MIME certificate imported into ACM that meets the requirements described
  in [S/MIME certificate considerations](send-email-authentication-smime.md#send-email-authentication-smime-certificate-considerations "send-email-authentication-smime.md#send-email-authentication-smime-certificate-considerations").

## Importing your certificate into ACM

You import your S/MIME certificate, private key, and certificate chain into ACM.
After import, you can select the certificate in the Amazon SES console. For
instructions on importing a certificate, see [Importing certificates into ACM](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md").

## Attaching a certificate

When you attach a certificate, you associate an ACM certificate with a From
address under an email identity. The From address must align with the Subject
Alternative Name (SAN) in the certificate. This comparison is case-sensitive. The
From address must also belong to the email identity.

You can attach a certificate using either the Amazon SES console or the AWS CLI.

###### To attach a certificate to an email identity

1. Open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane, under **Configuration**,
   choose **Identities**.
3. In the list of identities, choose the verified identity that you want
   to configure.

   1. If the **Status** is
      _Unverified_, complete the procedures in [Creating and verifying identities in Amazon SES](creating-identities.md "creating-identities.md") to verify the
      identity.

4. On the **Authentication** tab of the identity details page, in the
   **Email certificates** container, choose
   **Attach certificate**.
5. In the **Email certificate details** container, enter
   the From address that this certificate is for.
6. Select a certificate from the ACM certificate list. The list
   shows certificates that are compatible with this email identity and
   From address.
7. Choose **Save changes**.
   The following example attaches a certificate to a domain email identity for a
   specific sender address. In the AWS CLI, use the
   `associate-email-identity-certificate` command.

```
aws sesv2 associate-email-identity-certificate \
    --email-identity `example.com` \
    --from-address `sender@example.com` \
    --certificate-arn `arn:aws:acm:us-east-1:123456789012:certificate/abcd1234-abcd-1234-abcd-abcd12345678`
```

For a domain email identity, the `--from-address` parameter is required
and must match an email address in the certificate SAN. For an email-address identity,
you can omit `--from-address`.

To view attached certificates and their status, use the following command:

```
aws sesv2 list-email-identity-certificates \
    --email-identity `example.com`
```

For more information about the associate-email-identity-certificate
command, see [associate-email-identity-certificate](../../../cli/latest/reference/sesv2/associate-email-identity-certificate.md "../../../cli/latest/reference/sesv2/associate-email-identity-certificate.md") in the AWS CLI Command
Reference.

## Monitoring certificate status changes with Amazon EventBridge

Amazon SES emits an event to Amazon EventBridge when a certificate association status changes to
`ACTIVE`, `DEPROVISIONING`, or `FAILED`. You can use
these events to automate responses, for example alerting when a certificate enters
`FAILED` status.

## Removing a certificate

###### To remove a certificate using the console

1. Open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. Open the **Email certificates** table on the email
   identity's **Authentication** tab.
3. Select the certificate.
4. Choose **Delete**.

To remove a certificate using the AWS CLI, run the following command:

```
aws sesv2 disassociate-email-identity-certificate \
    --email-identity `example.com` \
    --from-address `sender@example.com`
```

Removing the certificate from the email identity does not delete it from ACM.
Amazon SES stops signing messages from that From address after you remove the
certificate.

###### One certificate per From address

You cannot attach more than one certificate to a From address. To
replace a certificate, you must first remove the existing one, unless it
is already `DEPROVISIONING`.

###### Identity deletion restriction

You cannot delete an email identity while it still has attached
certificates.
