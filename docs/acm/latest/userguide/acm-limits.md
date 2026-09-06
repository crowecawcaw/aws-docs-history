

# Quotas
<a name="acm-limits"></a>

The following AWS Certificate Manager (ACM) service quotas apply to each AWS region per each AWS account. 

To see what quotas can be adjusted, see the [ACM quotas table](https://docs.aws.amazon.com/general/latest/gr/acm.html#limits_acm) in the *AWS General Reference Guide*. To request quota increases, create a case at the [Support Center](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-acm). 

## General quotas
<a name="general-limits"></a>

**Topics**



| Item | Default quota | 
| --- | --- | 
| Number of ACM certificatesExpired and revoked certificates continue to count toward this total.<br />Certificates signed by a CA from AWS Private CA do not count toward this total.<br />Certificates issued through ACME do not count toward this total. | 2500 | 
| Number of ACM certificates per year (last 365 days)You can request up to twice your quota of ACM certificates per year, region, and account. For example, if your quota is 2,500, you can request up to 5,000 ACM certificates per year in a given region and account. You can only have 2,500 certificates at any given time. To request 5,000 certificates in a year, you must delete 2,500 during the year to stay within the quota. If you need more than 2,500 certificates at any given time, you must contact the **[Support Center](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-acm)**. <br />Certificates signed by a CA from AWS Private CA do not count toward this total.<br />Certificates issued through ACME do not count toward this total. | 5,000 | 
| Number of imported certificates | 2,500 | 
| Number of imported certificates per year (last 365 days) | 5,000 | 
| Number of domain names per ACM certificateThe default quota is 10 domain names for each ACM certificate. Your quota may be greater. <br />The first domain name that you submit is included as the subject common name (CN) of the certificate. All names are included in the Subject Alternative Name extension. <br />You can request up to 100 domain names. To request an increase to your quota, create a request in the Service Quotas console for the ACM service. Before creating a case, however, make sure you understand how adding more domain names can create more administrative work for you if you use email validation. For more information, see [Domain validation](acm-bestpractices.md#best-practices-validating). <br />The quota for the number of domain names per ACM certificate applies only to certificates that are provided by ACM. This quota does not apply to certificates that you import into ACM. The following sections apply only to ACM certificates. | 10 | 
| Number of domain names per ACME-issued certificateCertificates issued through ACME can include up to 100 domain names. This quota is fixed and cannot be increased. | 100 | 
| Number of Private CAsACM is integrated with AWS Private Certificate Authority (AWS Private CA). You can use the ACM console, AWS CLI, or ACM API to request private certificates from an existing private certificate authority (CA) hosted by AWS Private CA. These certificates are managed within the ACM environment and have the same restrictions as public certificates issued by ACM. For more information, see [Request a private certificate in AWS Certificate Manager](gs-acm-request-private.md). You can also issue private certificates by using the standalone AWS Private CA service. For more information, see [Issue a Private End-Entity Certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PcaIssueCert.html).A private CA that has been deleted will count towards your quota until the end of its restoration period. For more information, see [Deleting Your Private CA](https://docs.aws.amazon.com/acm-pca/latest/userguide/PCADeleteCA.html). | 200 | 
| Number of Private Certificates per CA (lifetime) | 1,000,000 | 
| Number of ACME endpointsThe maximum number of ACME endpoints per AWS account per region. | 50 | 
| Number of external account bindings per ACME endpoint | 1,000 | 
| Number of domain validations per ACME endpoint | 1,500 | 

## API rate quotas
<a name="api-rate-limits"></a>

The following quotas apply to the ACM API for each region and account. ACM throttles API requests at different quotas depending on the API operation. Throttling means that ACM rejects an otherwise valid request because the request exceeds the operation's quota for the number of requests per second. When a request is throttled, ACM returns a `ThrottlingException` error. The following table lists each API operation and the quota at which ACM throttles requests for that operation. 

**Note**  
In addition to the API actions listed in the table below, ACM can also call the external `IssueCertificate` action from AWS Private CA. For up-to-date rate quota information on `IssueCertificate`, see the [endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/acm-pca.html#limits_acm-pca) for AWS Private CA.

**Requests-per-second quota for each ACM API operation**

Per-operation request rate quotas for ACME certificate automation are tiered: read operations at 30 requests per second per account, write operations at 20 requests per second per account, and domain validation mutation operations (Create/Update/Delete AcmeDomainValidation) at 5 requests per second per account.



| API call | Requests per second | 
| --- | --- | 
| AddTagsToCertificate | 5 | 
| CreateAcmeDomainValidation | 5 | 
| CreateAcmeEndpoint | 20 | 
| CreateAcmeExternalAccountBinding | 20 | 
| DeleteAcmeDomainValidation | 5 | 
| DeleteAcmeEndpoint | 20 | 
| DeleteAcmeExternalAccountBinding | 20 | 
| DeleteCertificate | 10 | 
| DescribeAcmeAccount | 30 | 
| DescribeAcmeDomainValidation | 30 | 
| DescribeAcmeEndpoint | 30 | 
| DescribeAcmeExternalAccountBinding | 30 | 
| DescribeCertificate | 10 | 
| ExportCertificate | 10 | 
| GetAccountConfiguration | 1 | 
| GetAcmeExternalAccountBindingCredentials | 30 | 
| GetCertificate | 10 | 
| ImportCertificate | 1 | 
| ListAcmeAccounts | 30 | 
| ListAcmeDomainValidations | 30 | 
| ListAcmeEndpoints | 30 | 
| ListAcmeExternalAccountBindings | 30 | 
| ListCertificates | 8 | 
| ListTagsForCertificate | 10 | 
| ListTagsForResource | 5 | 
| PutAccountConfiguration | 1 | 
| RemoveTagsFromCertificate | 5 | 
| RenewCertificate | 5 | 
| RequestCertificate | 5 | 
| ResendValidationEmail | 1 | 
| RevokeAcmeAccount | 20 | 
| RevokeAcmeExternalAccountBinding | 20 | 
| SearchCertificates | 5 | 
| TagResource | 5 | 
| UntagResource | 5 | 
| UpdateAcmeDomainValidation | 5 | 
| UpdateAcmeEndpoint | 20 | 
| UpdateCertificateOptions | 5 | 

For more information, see [AWS Certificate Manager API Reference](https://docs.aws.amazon.com/acm/latest/APIReference/).

## ACME protocol request rate quotas
<a name="acme-protocol-rate-limits"></a>

The following quotas apply to requests that ACME clients send to an ACME endpoint over the ACME protocol. These quotas are separate from the ACM API request rate quotas in the preceding section. Per-operation request rate quotas for the ACME protocol are tiered: read operations at 25 requests per second per account, write operations at 20 requests per second per account, and certificate operations (FinalizeOrder, RevokeCertificate) at 1 request per second per account. When a request exceeds the quota, the endpoint returns a rate limit error.

**Requests-per-second quota for each ACME protocol operation**



| Operation | Requests per second | 
| --- | --- | 
| ChangeAccountKey | 20 | 
| FinalizeOrder | 1 | 
| GetCertificate | 25 | 
| GetDirectory | 25 | 
| GetOrder | 25 | 
| ListOrders | 25 | 
| ManageAccount | 20 | 
| ManageAuthorization | 25 | 
| NewAccount | 20 | 
| NewNonce | 25 | 
| NewOrder | 20 | 
| RevokeCertificate | 1 | 