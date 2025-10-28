# DescribeCertificates

Returns a list of certificate authority (CA) certificates provided by Amazon DocumentDB for this AWS account.

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**CertificateIdentifier**

The user-supplied certificate identifier. If this parameter is specified, information for only the specified certificate is returned. If this parameter is omitted, a list of up to `MaxRecords` certificates is returned. This parameter is not case sensitive.

Constraints

- Must match an existing `CertificateIdentifier`.

Type: String

Required: No

**Filters.Filter.N**

This parameter is not currently supported.

Type: Array of [Filter](API_Filter.md "API_Filter.md") objects

Required: No

**Marker**

An optional pagination token provided by a previous `DescribeCertificates` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.

Type: String

Required: No

**MaxRecords**

The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.

Default: 100

Constraints:

- Minimum: 20
- Maximum: 100

Type: Integer

Required: No

## Response Elements

The following elements are returned by the service.

**Certificates.Certificate.N**

A list of certificates for this AWS account.

Type: Array of [Certificate](API_Certificate.md "API_Certificate.md") objects

**Marker**

An optional pagination token provided if the number of records retrieved is greater than `MaxRecords`. If this parameter is specified, the marker specifies the next record in the list. Including the value of `Marker` in the next call to `DescribeCertificates` results in the next page of certificates.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**CertificateNotFound**

`CertificateIdentifier` doesn't refer to an existing certificate.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-2014-10-31/DescribeCertificates.md "../../../goto/cli2/docdb-2014-10-31/DescribeCertificates.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/docdb-2014-10-31/DescribeCertificates.md "../../../goto/DotNetSDKV3/docdb-2014-10-31/DescribeCertificates.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DescribeCertificates.md "../../../goto/SdkForCpp/docdb-2014-10-31/DescribeCertificates.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeCertificates.md "../../../goto/SdkForGoV2/docdb-2014-10-31/DescribeCertificates.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeCertificates.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DescribeCertificates.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeCertificates.md "../../../goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeCertificates.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeCertificates.md "../../../goto/SdkForKotlin/docdb-2014-10-31/DescribeCertificates.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeCertificates.md "../../../goto/SdkForPHPV3/docdb-2014-10-31/DescribeCertificates.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-2014-10-31/DescribeCertificates.md "../../../goto/boto3/docdb-2014-10-31/DescribeCertificates.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeCertificates.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DescribeCertificates.md")
