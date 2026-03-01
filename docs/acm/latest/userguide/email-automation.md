# Automate AWS Certificate Manager email validation

Email-validated ACM certificates normally require manual action
by the domain owner. Organizations dealing with large numbers of email-validated
certificates may prefer to create a parser that can automate the required responses.
To assist customers using email validation, the information in this section
describes the templates used for domain validation email messages and the workflow
involved in completing the validation process.

## Validation email templates

Validation email messages have one of the two following
formats, depending on whether a new certificate is being requested or an
existing certificate is being renewed. The content of the highlighted strings
should be replaced with values that are specific to the domain being
validated.

### Validating a new certificate

Email template text:

```
Greetings from Amazon Web Services,

We received a request to issue an SSL/TLS certificate for `requested_domain`.

Verify that the following domain, AWS account ID, and certificate identifier correspond
to a request from you or someone in your organization.

Domain: `fqdn`
AWS account ID: `account_id`
AWS Region name: `region_name`
Certificate Identifier: `certificate_identifier`

To approve this request, go to Amazon Certificate Approvals
(https://`region_name`.acm-certificates.amazon.com/approvals?code=validation_code&context=validation_context)
and follow the instructions on the page.

This email is intended solely for authorized individuals for `fqdn`. To express any concerns
about this email or if this email has reached you in error, forward it along with a brief
explanation of your concern to validation-questions@amazon.com.

Sincerely,
Amazon Web Services
```

### Validating a certificate for renewal

Email template text:

```
Greetings from Amazon Web Services,

We received a request to issue an SSL/TLS certificate for `requested_domain`.
This email is a request to validate ownership of the domain in order to renew
the existing, currently in use, certificate. Certificates have defined
validity periods and email validated certificates, like this one, require you
to re-validate for the certificate to renew.

Verify that the following domain, AWS account ID, and certificate identifier
correspond to a request from you or someone in your organization.

Domain: `fqdn`
AWS account ID: `account_id`
AWS Region name: `region_name`
Certificate Identifier: `certificate_identifier`

To approve this request, go to Amazon Certificate Approvals at
https://`region_name`.acm-certificates.amazon.com/approvals?code=$validation_code&context=$validation_context
and follow the instructions on the page.

This email is intended solely for authorized individuals for `fqdn`. You can see
more about how AWS Certificate Manager validation works here -
https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html.
To express any concerns about this email or if this email has reached you in
error, forward it along with a brief explanation of your concern to
validation-questions@amazon.com.

Sincerely,
Amazon Web Services

--
Amazon Web Services, Inc. is a subsidiary of Amazon.com, Inc. Amazon.com is a
registered trademark of Amazon.com, Inc.

This message produced and distributed by Amazon Web Services, Inc.,
410 Terry Ave. North, Seattle, WA 98109-5210.

(c)2015-2022, Amazon Web Services, Inc. or its affiliates. All rights reserved.
Our privacy policy is posted at https://aws.amazon.com/privacy
```

Once you receive a new validation message from AWS, we recommend that you
use it as the most up-to-date and authoritative template for your parser.
Customers with message parsers designed before November, 2020, should note the
following changes that may have been made to the template:

- The email subject line now reads "`Certificate request for
`domain name``" instead of
`"Certificate approval for `domain
name``".
- The `AWS account ID` is now presented without dashes or
  hyphens.
- The `Certificate Identifier` now presents the entire
  certificate ARN instead of a shortened form, for example,
  `arn:aws:acm:us-east-1:000000000000:certificate/3b4d78e1-0882-4f51-954a-298ee44ff369`
  rather than
  `3b4d78e1-0882-4f51-954a-298ee44ff369`.
- The certificate approval URL now contains
  `acm-certificates.amazon.com` instead of
  `certificates.amazon.com`.
- The approval form opened by clicking the certificate approval URL now
  contains the approval button. The name of the approval button div is now
  `approve-button` instead of
  `approval_button`.
- Validation messages for both newly requested certificates and renewing
  certificates have the same email format.

## Validation workflow

This section provides information about the renewal workflow for
email-validated certificates.

- When the ACM console processes a multi-domain certificate request,
  it sends validation email messages to the domain name or the validation
  domain that you specify when you request a public certificate. The
  domain owner needs to validate an email message for each domain before
  ACM can issue the certificate. For more information, see [Using Email to Validate
  Domain Ownership](email-validation.md "email-validation.md").
- Email validation for multi-domain certificate requests using the ACM
  API or CLI results in an email message being sent by each requested
  domain, even if the request includes subdomains of other domains in the
  request. The domain owner needs to validate an email message for each of
  these domains before ACM can issue the certificate.

If you resend emails for an existing certificate through the ACM
console, emails will be sent to the validation domain specified in the
original certificate request, or the exact domain if no validation
domain was specified. To receive validation emails at a different
domain, you can request a new certificate, specifying the validation
domain that you want to use for validation. Alternatively, you can call
[ResendValidationEmail](../APIReference/API_ResendValidationEmail.md "../APIReference/API_ResendValidationEmail.md") with the
`ValidationDomain` parameter using the API, SDK, or CLI.
However, the validation domain specified in the
`ResendValidationEmail` request is only used for that
call and is not saved to the certificate Amazon Resource Name (ARN) for
future validation emails. You must call
`ResendValidationEmail` each time you wish to receive a
validation email at a domain name that was not specified in the original
certificate request.

###### Note

Prior to November, 2020, customers needed to validate only the
apex domain and ACM would issue a certificate that also covered
any subdomains. Customers with message parsers designed before that
time should note the change to the email validation workflow.

- With the ACM API or CLI, you can force all validation email messages
  for a multi-domain certificate request to be sent to the apex domain. In
  the API, use the `DomainValidationOptions` parameter of the
  [RequestCertificate](../APIReference/API_RequestCertificate.md "../APIReference/API_RequestCertificate.md") action to specify a value for
  `ValidationDomain`, which is a member of the [DomainValidationOption](../APIReference/API_DomainValidationOption.md "../APIReference/API_DomainValidationOption.md") type. In the CLI, use the
  **--domain-validation-options** parameter of the
  [request-certificate](../../../cli/latest/reference/acm/request-certificate.md "../../../cli/latest/reference/acm/request-certificate.md") command to specify a value for
  `ValidationDomain`.
