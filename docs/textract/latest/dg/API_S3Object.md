# S3Object

The S3 bucket name and file name that identifies the document.

The AWS Region for the S3 bucket that contains the document must match the Region that
you use for Amazon Textract operations.

For Amazon Textract to process a file in an S3 bucket, the user must have
permission to access the S3 bucket and file.

## Contents

**Bucket**

The name of the S3 bucket. Note that the # character is not valid in the file
name.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 255.

Pattern: `[0-9A-Za-z\.\-_]*`

Required: No

**Name**

The file name of the input document. Image files may be in PDF, TIFF, JPEG, or PNG format.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `.*\S.*`

Required: No

**Version**

If the bucket has versioning enabled, you can specify the object version.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `.*\S.*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/S3Object.md "../../../goto/SdkForCpp/textract-2018-06-27/S3Object.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/S3Object.md "../../../goto/SdkForJavaV2/textract-2018-06-27/S3Object.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/S3Object.md "../../../goto/SdkForRubyV3/textract-2018-06-27/S3Object.md")
