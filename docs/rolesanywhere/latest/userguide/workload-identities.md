# Mapping identities to your workloads with

IAM Roles Anywhere

A key element to using IAM Roles Anywhere is managing how identities are assigned to workloads.
Certificates are issued to compute instances (servers, containers), in which the
identity is encoded as the `Subject` of the certificate. The subject may be
a simple Common Name (CN), a Fully Qualified Distinguished Name (FQDN), that contains information
about organizational structure, or a simple hostname. Alternatively, a standard such as
[SPIFFE](https://spiffe.io "https://spiffe.io") could be used to create a hierarchical namespace for
the workload identities.

IAM Roles Anywhere lets the workload use the certificate to obtain temporary credentials instead of
issuing Access Key IDs and Secret Access Keys, and the identity in the subject is encoded in the
session credentials in a way that can be used in resource policies. For example, if a certificate
has a `Subject` with `CN=Alice`, the value is added to the session as
a `PrincipalTag`: `aws:PrincipalTag/x509Subject/CN`.

The fields Subject, Issuer and Subject Alternative Name (SAN) are extracted from x509 tickets
and used as elements of the PrincipalTags. Tags that start with the prefix x509Subject are usually
followed by the suffix /CN used to identify the subject’s common name. Tags starting with the prefix
x509Issuer are usually followed by /C, /O, /OU, /ST, /L, and /CN in order to identify the issuer’s country,
organization, organization unit, state, locality and common name respectively. Tags starting with
x509SAN prefix are followed by /DNS, /URI or /CN to identify the subject alternative name’s DNS, URI
or common name of the subject alternative name respectively. These are some of the different ways x509 fields are
implemented as PrincipalTags for use in identity mapping.
