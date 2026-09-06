

# AWS Private CA template definitions
<a name="template-definitions"></a>

The following sections provide configuration details about supported AWS Private CA certificate templates. 

## BlankEndEntityCertificate\_APIPassthrough/V1 definition
<a name="BlankEndEntityCertificate_APIPassthrough"></a>

With blank end-entity certificate templates, you can issue end-entity certificates with only X.509 Basic constraints present. This is the simplest end-entity certificate that AWS Private CA can issue, but it can be customized using the API structure. The Basic constraints extension defines whether or not the certificate is a CA certificate. A blank end-entity certificate template enforces a value of FALSE for Basic constraints to ensure that an end-entity certificate is issued and not a CA certificate.

You can use blank passthrough templates to issue smart card certificates that require specific values for Key usage (KU) and Extended key usage (EKU). For example, Extended key usage may require Client Authentication and Smart Card Logon, and Key usage may require Digital Signature, Non Repudiation, and Key Encipherment. Unlike other passthrough templates, blank end-entity certificate templates allow the configuration of KU and EKU extensions, where KU can be any of the nine supported values (digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment, keyAgreement, keyCertSign, cRLSign, encipherOnly, and decipherOnly) and EKU can be any of the supported values (serverAuth, clientAuth, codesigning, emailProtection, timestamping, and OCSPSigning) plus custom extensions.


**BlankEndEntityCertificate\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | CA:FALSE | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

## BlankEndEntityCertificate\_APICSRPassthrough/V1 definition
<a name="BlankEndEntityCertificate_APICSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankEndEntityCertificate\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | CA:FALSE | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

## BlankEndEntityCertificate\_CriticalBasicConstraints\_APICSRPassthrough/V1 definition
<a name="BlankEndEntityCertificate_CriticalBasicConstraints_APICSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankEndEntityCertificate\_CriticalBasicConstraints\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, CA:FALSE | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration, API, or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankEndEntityCertificate\_CriticalBasicConstraints\_APIPassthrough/V1 definition
<a name="BlankEndEntityCertificate_CriticalBasicConstraints_APIPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankEndEntityCertificate\_CriticalBasicConstraints\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, CA:FALSE | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or API] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankEndEntityCertificate\_CriticalBasicConstraints\_CSRPassthrough/V1 definition
<a name="BlankEndEntityCertificate_CriticalBasicConstraints_CSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankEndEntityCertificate\_CriticalBasicConstraints\_CSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, CA:FALSE | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankEndEntityCertificate\_CSRPassthrough/V1 definition
<a name="BlankEndEntityCertificate_CSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankEndEntityCertificate\_CSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | CA:FALSE | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen0\_CSRPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen0_CSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen0\_CSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 0` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen0\_APICSRPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen0_APICSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen0\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 0` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen0\_APIPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen0_APIPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen0\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 0` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

### BlankSubordinateCACertificate\_PathLen1\_APIPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen1_APIPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen1\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 1` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen1\_CSRPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen1_CSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen1\_CSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 1` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen1\_APICSRPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen1_APICSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen1\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 1` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen2\_APIPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen2_APIPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen2\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 2` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen2\_CSRPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen2_CSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen2\_CSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 2` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen2\_APICSRPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen2_APICSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen2\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 2` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen3\_APIPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen3_APIPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen3\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 3` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen3\_CSRPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen3_CSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen3\_CSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 3` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### BlankSubordinateCACertificate\_PathLen3\_APICSRPassthrough/V1 definition
<a name="BlankSubordinateCACertificate_PathLen3_APICSRPassthrough"></a>

For general information about blank templates, see [BlankEndEntityCertificate\_APIPassthrough/V1 definition](#BlankEndEntityCertificate_APIPassthrough).


**BlankSubordinateCACertificate\_PathLen3\_APICSRPassthrough**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 3` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### CodeSigningCertificate/V1 definition
<a name="CodeSigningCertificate-V1"></a>

This template is used to create certificates for code signing. You can use code-signing certificates from AWS Private CA with any code-signing solution that is based on a private CA infrastructure. For example, customers using Code Signing for AWS IoT can generate a code-signing certificate with AWS Private CA and import it to AWS Certificate Manager. For more information, see [What Is Code Signing for AWS IoT?](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) and [Obtain and Import a Code Signing Certificate](https://docs.aws.amazon.com/signer/latest/developerguide/obtain-cert.html).


**CodeSigningCertificate/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | `CA:FALSE` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature | 
| Extended key usage | Critical, code signing | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\*CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### CodeSigningCertificate\_APICSRPassthrough/V1 definition
<a name="CodeSigningCertificate_APICSRPassthrough"></a>

This template extends CodeSigningCertificate/V1 to support API and CSR passthrough values.


**CodeSigningCertificate\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | `CA:FALSE` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature | 
| Extended key usage | Critical, code signing | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### CodeSigningCertificate\_APIPassthrough/V1 definition
<a name="CodeSigningCertificate_APIPassthrough"></a>

This template is identical to the `CodeSigningCertificate` template with one difference: In this template, AWS Private CA passes additional extensions through the API to the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the API.


**CodeSigningCertificate\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | `CA:FALSE` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature | 
| Extended key usage | Critical, code signing | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### CodeSigningCertificate\_CSRPassthrough/V1 definition
<a name="CodeSigningCertificate_CSRPassthrough-V1"></a>

This template is identical to the `CodeSigningCertificate` template with one difference: In this template, AWS Private CA passes additional extensions from the certificate signing request (CSR) into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the CSR.


**CodeSigningCertificate\_CSRPassthrough/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | `CA:FALSE` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature | 
| Extended key usage | Critical, code signing | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\*CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityCertificate/V1 definition
<a name="EndEntityCertificate-V1"></a>

This template is used to create certificates for end entities such as operating systems or web servers. 


**EndEntityCertificate/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web server authentication, TLS web client authentication | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\*CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityCertificate\_APICSRPassthrough/V1 definition
<a name="EndEntityCertificate_APICSRPassthrough"></a>

This template extends EndEntityCertificate/V1 to support API and CSR passthrough values.


**EndEntityCertificate\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web server authentication, TLS web client authentication | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityCertificate\_APIPassthrough/V1 definition
<a name="EndEntityCertificate_APIPassthrough"></a>

This template is identical to the `EndEntityCertificate` template with one difference: In this template, AWS Private CA passes additional extensions through the API to the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the API.


**EndEntityCertificate\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web server authentication, TLS web client authentication | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityCertificate\_CSRPassthrough/V1 definition
<a name="EndEntityCertificate_CSRPassthrough-V1"></a>

This template is identical to the `EndEntityCertificate` template with one difference: In this template, AWS Private CA passes additional extensions from the certificate signing request (CSR) into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the CSR.


**EndEntityCertificate\_CSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web server authentication, TLS web client authentication | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\*CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityClientAuthCertificate/V1 definition
<a name="EndEntityClientAuthCertificate-V1"></a>

This template differs from the `EndEntityCertificate` only in the Extended key usage value, which restricts it to TLS web client authentication.


**EndEntityClientAuthCertificate/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web client authentication | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\*CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityClientAuthCertificate\_APICSRPassthrough/V1 definition
<a name="EndEntityClientAuthCertificate_APICSRPassthrough"></a>

This template extends EndEntityClientAuthCertificate/V1 to support API and CSR passthrough values.


**EndEntityClientAuthCertificate\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web client authentication | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityClientAuthCertificate\_APIPassthrough/V1 definition
<a name="EndEntityClientAuthCertificate_APIPassthrough"></a>

This template is identical to the `EndEntityClientAuthCertificate` template with one difference. In this template, AWS Private CA passes additional extensions through the API into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the API.


**EndEntityClientAuthCertificate\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web client authentication | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityClientAuthCertificate\_CSRPassthrough/V1 definition
<a name="EndEntityClientAuthCertificate_CSRPassthrough-V1"></a>

This template is identical to the `EndEntityClientAuthCertificate` template with one difference. In this template, AWS Private CA passes additional extensions from the certificate signing request (CSR) into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the CSR.


**EndEntityClientAuthCertificate\_CSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web client authentication | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\*CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityServerAuthCertificate/V1 definition
<a name="EndEntityServerAuthCertificate-V1"></a>

This template differs from the `EndEntityCertificate` only in the Extended key usage value, which restricts it to TLS web server authentication.


**EndEntityServerAuthCertificate/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web server authentication | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\*CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityServerAuthCertificate\_APICSRPassthrough/V1 definition
<a name="EndEntityServerAuthCertificate_APICSRPassthrough"></a>

This template extends EndEntityServerAuthCertificate/V1 to support API and CSR passthrough values.


**EndEntityServerAuthCertificate\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web server authentication | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityServerAuthCertificate\_APIPassthrough/V1 definition
<a name="EndEntityServerAuthCertificate_APIPassthrough"></a>

This template is identical to the `EndEntityServerAuthCertificate` template with one difference. In this template, AWS Private CA passes additional extensions through the API into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the API.


**EndEntityServerAuthCertificate\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web server authentication | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### EndEntityServerAuthCertificate\_CSRPassthrough/V1 definition
<a name="EndEntityServerAuthCertificate_CSRPassthrough-V1"></a>

This template is identical to the `EndEntityServerAuthCertificate` template with one difference. In this template, AWS Private CA passes additional extensions from the certificate signing request (CSR) into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the CSR.


**EndEntityServerAuthCertificate\_CSRPassthrough/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | CA:`FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, key encipherment | 
| Extended key usage | TLS web server authentication | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\*CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### OCSPSigningCertificate/V1 definition
<a name="OCSPSigningCertificate-V1"></a>

This template is used to create certificates for signing OCSP responses. The template is identical to the `CodeSigningCertificate` template, except that the Extended key usage value specifies OCSP signing instead of code signing.


**OCSPSigningCertificate/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | `CA:FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature | 
| Extended key usage | Critical, OCSP signing | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\*CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### OCSPSigningCertificate\_APICSRPassthrough/V1 definition
<a name="OCSPSigningCertificate_APICSRPassthrough"></a>

This template extends the OCSPSigningCertificate/V1 to support API and CSR passthrough values.


**OCSPSigningCertificate\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | `CA:FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature | 
| Extended key usage | Critical, OCSP signing | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### OCSPSigningCertificate\_APIPassthrough/V1 definition
<a name="OCSPSigningCertificate_APIPassthrough"></a>

This template is identical to the `OCSPSigningCertificate` template with one difference. In this template, AWS Private CA passes additional extensions through the API into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the API.


**OCSPSigningCertificate\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | `CA:FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature | 
| Extended key usage | Critical, OCSP signing | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### OCSPSigningCertificate\_CSRPassthrough/V1 definition
<a name="OCSPSigningCertificate_CSRPassthrough-V1"></a>

This template is identical to the `OCSPSigningCertificate` template with one difference. In this template, AWS Private CA passes additional extensions from the certificate signing request (CSR) into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the CSR.


**OCSPSigningCertificate\_CSRPassthrough/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | `CA:FALSE` | 
| Authority key identifier | [SKI from CA certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature | 
| Extended key usage | Critical, OCSP signing | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\*CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### RootCACertificate/V1 definition
<a name="RootCACertificate-V1"></a>

This template is used to issue self-signed root CA certificates. CA certificates include a critical basic constraints extension with the CA field set to `TRUE` to designate that the certificate can be used to issue CA certificates. The template does not specify a path length ([pathLenConstraint](PcaTerms.md#terms-pathlength)) because this could inhibit future expansion of the hierarchy. Extended key usage is excluded to prevent use of the CA certificate as a TLS client or server certificate. No CRL information is specified because a self-signed certificate cannot be revoked.


**RootCACertificate/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE` | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, keyCertSign, CRL sign | 
| CRL distribution points | N/A | 

### RootCACertificate\_APIPassthrough/V1 definition
<a name="RootCACertificate_APIPassthrough"></a>

This template extends RootCACertificate/V1 to support API passthrough values.


**RootCACertificate\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE` | 
| Authority key identifier | [Passthrough from API] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, keyCertSign, CRL sign | 
| CRL distribution points\* | N/A | 

### BlankRootCACertificate\_APIPassthrough/V1 definition
<a name="BlankRootCACertificate_APIPassthrough"></a>

With blank root certificate templates, you can issue root certificates with only X.509 basic constraints present. This is the simplest root certificate that AWS Private CA can issue, but it can be customized using the API structure. The basic constraints extension defines whether or not the certificate is a CA certificate. A blank root certificate template enforces a value of `TRUE` for basic constraints to ensure that a root CA certificate is issued.

You can use blank passthrough root templates to issue root certificates that require specific values for key usage (KU). For example, key usage might require `keyCertSign` and `cRLSign`, but not `digitalSignature`. Unlike the other non-blank root passthrough certificate template, blank root certificate templates allow the configuration of the KU extension, where KU can be any of the nine supported values (`digitalSignature`, `nonRepudiation`, `keyEncipherment`, `dataEncipherment`, `keyAgreement`, `keyCertSign`, `cRLSign`, `encipherOnly`, and `decipherOnly`). 


**BlankRootCACertificate\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE` | 
| Subject key identifier | [Derived from CSR] | 

### BlankRootCACertificate\_PathLen0\_APIPassthrough/V1 definition
<a name="BlankRootCACertificate_PathLen0_APIPassthrough"></a>

For general information about blank root CA templates, see [BlankRootCACertificate\_APIPassthrough/V1 definition](#BlankRootCACertificate_APIPassthrough).


**BlankRootCACertificate\_PathLen0\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 0` | 
| Subject key identifier | [Derived from CSR] | 

### BlankRootCACertificate\_PathLen1\_APIPassthrough/V1 definition
<a name="BlankRootCACertificate_PathLen1_APIPassthrough"></a>

For general information about blank root CA templates, see [BlankRootCACertificate\_APIPassthrough/V1 definition](#BlankRootCACertificate_APIPassthrough).


**BlankRootCACertificate\_PathLen1\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 1` | 
| Subject key identifier | [Derived from CSR] | 

### BlankRootCACertificate\_PathLen2\_APIPassthrough/V1 definition
<a name="BlankRootCACertificate_PathLen2_APIPassthrough"></a>

For general information about blank root CA templates, see [BlankRootCACertificate\_APIPassthrough/V1 definition](#BlankRootCACertificate_APIPassthrough).


**BlankRootCACertificate\_PathLen2\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 2` | 
| Subject key identifier | [Derived from CSR] | 

### BlankRootCACertificate\_PathLen3\_APIPassthrough/V1 definition
<a name="BlankRootCACertificate_PathLen3_APIPassthrough"></a>

For general information about blank root CA templates, see [BlankRootCACertificate\_APIPassthrough/V1 definition](#BlankRootCACertificate_APIPassthrough).


**BlankRootCACertificate\_PathLen3\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 3` | 
| Subject key identifier | [Derived from CSR] | 

### SubordinateCACertificate\_PathLen0/V1 definition
<a name="SubordinateCACertificate_PathLen0-V1"></a>

This template is used to issue subordinate CA certificates with a path length of `0`. CA certificates include a critical basic constraints extension with the CA field set to `TRUE` to designate that the certificate can be used to issue CA certificates. Extended key usage is not included, which prevents the CA certificate from being used as a TLS client or server certificate.

For more information about certification paths, see [Setting Length Constraints on the Certification Path](https://docs.aws.amazon.com/privateca/latest/userguide/ca-hierarchy.html#length-constraints).


**SubordinateCACertificate\_PathLen0/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 0` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\*CRL distribution points are included in certificates that are issued with this template only if the CA is configured with CRL generation enabled.

### SubordinateCACertificate\_PathLen0\_APICSRPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen0_APICSRPassthrough"></a>

This template extends SubordinateCACertificate\_PathLen0/V1 to support API and CSR passthrough values.


**SubordinateCACertificate\_PathLen0\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 0` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### SubordinateCACertificate\_PathLen0\_APIPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen0_APIPassthrough"></a>

This template extends SubordinateCACertificate\_PathLen0/V1 to support API passthrough values.


**SubordinateCACertificate\_PathLen0\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 0` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### SubordinateCACertificate\_PathLen0\_CSRPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen0_CSRPassthrough-V1"></a>

This template is identical to the `SubordinateCACertificate_PathLen0` template with one difference: In this template, AWS Private CA passes additional extensions from the certificate signing request (CSR) into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the CSR.

**Note**  
A CSR that contains custom additional extensions must be created outside of AWS Private CA.


**SubordinateCACertificate\_PathLen0\_CSRPassthrough/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 0` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\*CRL distribution points are included in certificates issued with this template only if the CA is configured with CRL generation enabled.

### SubordinateCACertificate\_PathLen1/V1 definition
<a name="SubordinateCACertificate_PathLen1-V1"></a>

This template is used to issue subordinate CA certificates with a path length of `1`. CA certificates include a critical Basic constraints extension with the CA field set to `TRUE` to designate that the certificate can be used to issue CA certificates. Extended key usage is not included, which prevents the CA certificate from being used as a TLS client or server certificate.

For more information about certification paths, see [Setting Length Constraints on the Certification Path](https://docs.aws.amazon.com/privateca/latest/userguide/ca-hierarchy.html#length-constraints).


**SubordinateCACertificate\_PathLen1/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 1` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\*CRL distribution points are included in certificates issued with this template only if the CA is configured with CRL generation enabled.

### SubordinateCACertificate\_PathLen1\_APICSRPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen1_APICSRPassthrough"></a>

This template extends SubordinateCACertificate\_PathLen1/V1 to support API and CSR passthrough values.


**SubordinateCACertificate\_PathLen1\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 1` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### SubordinateCACertificate\_PathLen1\_APIPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen1_APIPassthrough"></a>

This template extends SubordinateCACertificate\_PathLen0/V1 to support API passthrough values.


**SubordinateCACertificate\_PathLen1\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 1` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### SubordinateCACertificate\_PathLen1\_CSRPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen1_CSRPassthrough-V1"></a>

This template is identical to the `SubordinateCACertificate_PathLen1` template with one difference: In this template, AWS Private CA passes additional extensions from the certificate signing request (CSR) into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the CSR.

**Note**  
A CSR that contains custom additional extensions must be created outside of AWS Private CA.


**SubordinateCACertificate\_PathLen1\_CSRPassthrough/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 1` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\*CRL distribution points are included in certificates issued with this template only if the CA is configured with CRL generation enabled.

### SubordinateCACertificate\_PathLen2/V1 definition
<a name="SubordinateCACertificate_PathLen2-V1"></a>

This template is used to issue subordinate CA certificates with a path length of 2. CA certificates include a critical Basic constraints extension with the CA field set to `TRUE` to designate that the certificate can be used to issue CA certificates. Extended key usage is not included, which prevents the CA certificate from being used as a TLS client or server certificate.

For more information about certification paths, see [Setting Length Constraints on the Certification Path](https://docs.aws.amazon.com/privateca/latest/userguide/ca-hierarchy.html#length-constraints).


**SubordinateCACertificate\_PathLen2/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 2` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\*CRL distribution points are included in certificates issued with this template only if the CA is configured with CRL generation enabled.

### SubordinateCACertificate\_PathLen2\_APICSRPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen2_APICSRPassthrough"></a>

This template extends SubordinateCACertificate\_PathLen2/V1 to support API and CSR passthrough values.


**SubordinateCACertificate\_PathLen2\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 2` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### SubordinateCACertificate\_PathLen2\_APIPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen2_APIPassthrough"></a>

This template extends SubordinateCACertificate\_PathLen2/V1 to support API passthrough values.


**SubordinateCACertificate\_PathLen2\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 2` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### SubordinateCACertificate\_PathLen2\_CSRPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen2_CSRPassthrough-V1"></a>

This template is identical to the `SubordinateCACertificate_PathLen2` template with one difference: In this template, AWS Private CA passes additional extensions from the certificate signing request (CSR) into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the CSR.

**Note**  
A CSR that contains custom additional extensions must be created outside of AWS Private CA.


**SubordinateCACertificate\_PathLen2\_CSRPassthrough/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 2` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\*CRL distribution points are included in certificates issued with this template only if the CA is configured with CRL generation enabled.

### SubordinateCACertificate\_PathLen3/V1 definition
<a name="SubordinateCACertificate_PathLen3-V1"></a>

This template is used to issue subordinate CA certificates with a path length of 3. CA certificates include a critical Basic constraints extension with the CA field set to `TRUE` to designate that the certificate can be used to issue CA certificates. Extended key usage is not included, which prevents the CA certificate from being used as a TLS client or server certificate.

For more information about certification paths, see [Setting Length Constraints on the Certification Path](https://docs.aws.amazon.com/privateca/latest/userguide/ca-hierarchy.html#length-constraints).


**SubordinateCACertificate\_PathLen3/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 3` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\*CRL distribution points are included in certificates issued with this template only if the CA is configured with CRL generation enabled.

### SubordinateCACertificate\_PathLen3\_APICSRPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen3_APICSRPassthrough"></a>

This template extends SubordinateCACertificate\_PathLen3/V1 to support API and CSR passthrough values.


**SubordinateCACertificate\_PathLen3\_APICSRPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 3` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### SubordinateCACertificate\_PathLen3\_APIPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen3_APIPassthrough"></a>

This template extends SubordinateCACertificate\_PathLen3/V1 to support API passthrough values.


**SubordinateCACertificate\_PathLen3\_APIPassthrough/V1**  

|  X509v3 Parameter  | Value | 
| --- | --- | 
| Subject alternative name | [Passthrough from API or CSR] | 
| Subject | [Passthrough from API or CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 3` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration] | 

\* CRL distribution points are included in the template only if the CA is configured with CRL generation enabled. 

### SubordinateCACertificate\_PathLen3\_CSRPassthrough/V1 definition
<a name="SubordinateCACertificate_PathLen3_CSRPassthrough-V1"></a>

This template is identical to the `SubordinateCACertificate_PathLen3` template with one difference: In this template, AWS Private CA passes additional extensions from the certificate signing request (CSR) into the certificate if the extensions are not specified in the template. Extensions specified in the template always override extensions in the CSR.

**Note**  
A CSR that contains custom additional extensions must be created outside of AWS Private CA.


**SubordinateCACertificate\_PathLen3\_CSRPassthrough/V1**  

|  X509v3 Parameter  |  Value  | 
| --- | --- | 
| Subject alternative name | [Passthrough from CSR] | 
| Subject | [Passthrough from CSR] | 
| Basic constraints | Critical, `CA:TRUE`, `pathlen: 3` | 
| Authority key identifier | [SKI from CA Certificate] | 
| Subject key identifier | [Derived from CSR] | 
| Key usage | Critical, digital signature, `keyCertSign`, CRL sign | 
| CRL distribution points\* | [Passthrough from CA configuration or CSR] | 

\*CRL distribution points are included in certificates issued with this template only if the CA is configured with CRL generation enabled.