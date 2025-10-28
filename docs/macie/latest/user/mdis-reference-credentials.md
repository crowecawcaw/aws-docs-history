# Managed data identifiers for credentials data

Amazon Macie can detect multiple types of sensitive credentials data by using managed data
identifiers. The topics on this page specify each type and provide information about the managed
data identifier that's designed to detect the data. Each topic provides the following
information:

- Managed data identifier ID – Specifies the unique
  identifier (ID) for the managed data identifier that's designed to detect the data. When you [create a
  sensitive data discovery job](discovery-jobs-create.md "discovery-jobs-create.md") or [configure settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md"), you can use
  this ID to specify whether you want Macie to use the managed data identifier when it analyzes data.
- Supported countries and regions – Indicates which countries or
  regions the applicable managed data identifier is designed for. If the managed data identifier isn't
  designed for a particular country or region, this value is _Any_.
- Keyword required – Specifies whether detection
  requires a keyword to be in proximity of the data. If a keyword is required, the topic also
  provides examples of required keywords. For information about how Macie uses
  keywords when it analyzes data, see [Keyword requirements](managed-data-identifiers-keywords.md "managed-data-identifiers-keywords.md").
- Comments – Provides any relevant details that might
  affect your choice of managed data identifier or your investigation into reported occurrences of
  the sensitive data. The details include information such as supported standards, syntax
  requirements, and exceptions.
  The topics are listed in alphabetical order by sensitive data type.

###### Sensitive data types

- [AWS secret access key](#mdis-reference-AWS-CREDENTIALS "#mdis-reference-AWS-CREDENTIALS")
- [Google Cloud API key](#mdis-reference-GCP-API-key "#mdis-reference-GCP-API-key")
- [HTTP Basic Authorization header](#mdis-reference-HTTP_BASIC_AUTH_HEADER "#mdis-reference-HTTP_BASIC_AUTH_HEADER")
- [JSON Web
  Token (JWT)](#mdis-reference-JSON_WEB_TOKEN "#mdis-reference-JSON_WEB_TOKEN")
- [OpenSSH private key](#mdis-reference-OPENSSH_PRIVATE_KEY "#mdis-reference-OPENSSH_PRIVATE_KEY")
- [PGP private key](#mdis-reference-PGP_PRIVATE_KEY "#mdis-reference-PGP_PRIVATE_KEY")
- [Public-Key Cryptography Standard (PKCS)
  private key](#mdis-reference-PKCS "#mdis-reference-PKCS")
- [PuTTY private key](#mdis-reference-PUTTY_PRIVATE_KEY "#mdis-reference-PUTTY_PRIVATE_KEY")
- [Stripe API key](#mdis-reference-Stripe_API_key "#mdis-reference-Stripe_API_key")

## AWS secret access key

**Managed data identifier ID:** AWS_CREDENTIALS

**Supported countries and regions:** Any

**Keyword required:** Yes. Keywords include: _aws_secret_access_key, credentials, secret access key, secret key,
set-awscredential_

**Comments:** Macie doesn't report occurrences of the following character
sequences, which are commonly used as fictitious examples:
`je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY` and
`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.

## Google Cloud API key

**Managed data identifier ID:** GCP_API_KEY

**Supported countries and regions:** Any

**Keyword required:** Yes. Keywords include: _G_PLACES_KEY,
GCP api key, GCP key, google cloud key, google-api-key, google-cloud-apikeys, GOOGLEKEY,
X-goog-api-key_

**Comments:** Macie can detect only the string (`keyString`)
component of a Google Cloud API key. Support doesn't include detection of the ID or display name
component of a Google Cloud API key.

## HTTP Basic Authorization header

**Managed data identifier ID:** HTTP_BASIC_AUTH_HEADER

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** Detection requires a complete header, including the field name
and authentication scheme directive, as specified by [RFC 7617](https://tools.ietf.org/html/rfc7617 "https://tools.ietf.org/html/rfc7617"). For example: `Authorization:
 Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==` and `Proxy-Authorization: Basic
 dGVzdDoxMjPCow==`.

## JSON Web Token (JWT)

**Managed data identifier ID:** JSON_WEB_TOKEN

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** Macie can detect JSON Web Tokens (JWTs) that comply with the
requirements specified by [RFC 7519](https://tools.ietf.org/html/rfc7519 "https://tools.ietf.org/html/rfc7519") for
JSON Web Signature (JWS) structures. The tokens can be signed or unsigned.

## OpenSSH private key

**Managed data identifier ID:** OPENSSH_PRIVATE_KEY

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** None

## PGP private key

**Managed data identifier ID:** PGP_PRIVATE_KEY

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** None

## Public-Key Cryptography Standard (PKCS) private

key

**Managed data identifier ID:** PKCS

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** None

## PuTTY private key

**Managed data identifier ID:** PUTTY_PRIVATE_KEY

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** Macie can detect PuTTY private keys that use the following
standard headers and header sequence: `PuTTY-User-Key-File`, `Encryption`,
`Comment`, `Public-Lines`, `Private-Lines`, and
`Private-MAC`. The header values can contain alphanumeric characters, hyphens
(`‐`), and newline characters (`\n` or `\r`).
`Public-Lines` and `Private-Lines` values can also contain forward slashes
(`/`), plus signs (`+`), and equal signs (`=`).
`Private-MAC` values can also contain plus signs (`+`). Support doesn’t
include detection of private keys with header values that contain other characters, such as
spaces or underscores (`_`). Support also doesn’t include detection of private keys
that include custom headers.

## Stripe API key

**Managed data identifier ID:** STRIPE_CREDENTIALS

**Supported countries and regions:** Any

**Keyword required:** No

**Comments:** Macie doesn't report occurrences of the following character
sequences, which are commonly used in Stripe code examples:
`sk_test_4eC39HqLyjWDarjtT1zdp7dc` and
`pk_test_TYooMQauvdEDq54NiTphI7jx`.
