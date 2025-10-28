# Set up to use AWS Certificate Manager

With AWS Certificate Manager (ACM) you can provision and manage SSL/TLS certificates for your
AWS based websites and applications. You use ACM to create or import and then manage
a certificate. You must use other AWS services to deploy the certificate to your
website or application. For more information about the services integrated with ACM,
see [Services integrated with ACM](acm-services.md "acm-services.md"). The following sections
discuss the steps you need to perform before using ACM.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [Register a domain name for ACM](#setup-domain "#setup-domain")
- [(Optional) Configure a CAA record](#setup-caa "#setup-caa")

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Register a domain name for ACM

A fully qualified domain name (FQDN) is the unique name of an organization or
individual on the Internet followed by a top-level domain extension such as
`.com` or `.org`. If you do not already have a registered
domain name, you can register one through Amazon Route 53 or dozens of other commercial
registrars. Typically you go to the registrar's website and request a domain name.
Domain name registration usually lasts for a set period of time such as one or two
years before it must be renewed.

For more information about registering domain names with Amazon Route 53, see [Registering Domain Names Using
Amazon Route 53](../../../Route53/latest/DeveloperGuide/registrar.md "../../../Route53/latest/DeveloperGuide/registrar.md") in the _Amazon Route 53 Developer Guide_.

## (Optional) Configure a CAA record

A CAA record specifies which certificate authorities (CAs) are allowed to issue
certificates for a domain or subdomain. Creating a CAA record for use with ACM
helps to prevent the wrong CAs from issuing certificates for your domains. A CAA
record isn't a substitute for the security requirements that are specified by your
certificate authority, such as the requirement to validate that you're the owner of
a domain.

After ACM validates your domain during the certificate request process, it
checks for the presence of a CAA record to make sure it can issue a certificate for
you. Configuring a CAA record is optional.

Use the following values when you configure your CAA record:

**flags**

Specifies whether the value of the **tag** field is supported by ACM. Set this value to
**0**.

**tag**

The **tag** field can be one of the
following values. Note that the **iodef** field is currently ignored.

**issue**

Indicates that the ACM CA that you specify in the
**value** field is
authorized to issue a certificate for your domain or
subdomain.

**issuewild**

Indicates that the ACM CA that you specified in the
**value** field is
authorized to issue a wildcard certificate for your domain
or subdomain. A wildcard certificate applies to the domain
or subdomain and all of its subdomains. Note that if you
plan to use HTTP validation, this setting won't apply
because HTTP validation doesn't support wildcard
certificates. Use DNS or email validation instead for
wildcard certificates.

**value**

The value of this field depends on the value of the **tag** field. You must enclose this value in
quotation marks ("").

When **tag** is **issue**

The **value** field contains
the CA domain name. This field can contain the name of a CA
other than an Amazon CA. However, if you do not have a CAA
record that specifies one of the following four Amazon CAs,
ACM cannot issue a certificate to your domain or
subdomain:

- amazon.com
- amazontrust.com
- awstrust.com
- amazonaws.com

The **value** field can also
contain a semicolon (;) to indicate that no CA should be
permitted to issue a certificate for your domain or
subdomain. Use this field if you decide at some point that
you no longer want a certificate issued for a particular
domain.

When **tag** is **issuewild**

The **value** field is the
same as that for when **tag**
is **issue** except that the
value applies to wildcard certificates.

When there is an **issuewild** CAA record present that does not
include an ACM CA value, then no wild cards can be issued
by ACM. If there is no **issuewild** present, but there is an **issue** CAA record for ACM, then
wild cards may be issued by ACM.

###### Example CAA Record Examples

In the following examples, your domain name comes first followed by the record
type (CAA). The **flags** field is always 0. The
**tags** field can be **issue** or **issuewild**. If the
field is **issue** and you type the domain name of
a CA server in the **value** field, the CAA record
indicates that your specified server is permitted to issue your requested
certificate. If you type a semicolon ";" in the **value** field, the CAA record indicates that no CA is permitted to
issue a certificate. The configuration of CAA records varies by DNS provider.

###### Important

If you plan to use HTTP validation with CloudFront, you don't need to configure
**issuewild** records because HTTP
validation doesn't support wildcard certificates. For wildcard certificates,
use DNS or email validation instead.

```
**Domain**       **Record type**  **Flags**  **Tag**      **Value**
example.com.   CAA            0        issue      "SomeCA.com"
```

```
**Domain**       **Record type**  **Flags**  **Tag**      **Value**
example.com.   CAA            0        issue      "amazon.com"
```

```
**Domain**       **Record type**  **Flags**  **Tag**      **Value**
example.com.   CAA            0        issue      "amazontrust.com"
```

```
**Domain**       **Record type**  **Flags**  **Tag**      **Value**
example.com.   CAA            0        issue      "awstrust.com"
```

```
**Domain**       **Record type**  **Flags**  **Tag**      **Value**
example.com.   CAA            0        issue      "amazonaws.com"
```

```
**Domain**       **Record type**  **Flags**  **Tag**      **Value**
example.com    CAA            0        issue      ";"
```

For more information about how to add or modify DNS records, check with your DNS
provider. Route 53 supports CAA records. If Route 53 is your DNS provider, see [CAA Format](../../../Route53/latest/DeveloperGuide/ResourceRecordTypes.md#CAAFormat "../../../Route53/latest/DeveloperGuide/ResourceRecordTypes.md#CAAFormat") for
more information about creating a record.
