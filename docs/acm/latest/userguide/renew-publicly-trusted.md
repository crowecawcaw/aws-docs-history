# Renew ACM public certificates

When issuing a managed, publicly trusted certificate, AWS Certificate Manager requires you to prove
that you are the domain owner. This happens by means of either [DNS validation](dns-validation.md "dns-validation.md") or [email validation](email-validation.md "email-validation.md"). When a certificate comes up for renewal, ACM uses the
same method that you chose earlier to re-validate your ownership. The following topics
describe how the renewal process works in each case.

###### Topics

- [Renewal for domains validated by
  DNS](dns-renewal-validation.md "dns-renewal-validation.md")
- [Renewal for email-validated
  domains](email-renewal-validation.md "email-renewal-validation.md")
- [Renewal for domains validated by
  HTTP](http-renewal-validation.md "http-renewal-validation.md")
