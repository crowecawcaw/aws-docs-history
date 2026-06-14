# Developing with Amazon S3 using the AWS SDKs

AWS software development kits (SDKs) are available for many popular programming languages. Each SDK provides an API, code examples, and documentation that make it easier for developers to build applications in their preferred language.

###### Note

You can use AWS Amplify for end-to-end fullstack development of web and mobile apps. Amplify Storage seamlessly integrates file storage and management capabilities into frontend web and mobile apps, built on top of Amazon S3. For more information, see [Storage](https://docs.amplify.aws/react/build-a-backend/storage/ "https://docs.amplify.aws/react/build-a-backend/storage/") in the Amplify user guide.

| SDK documentation                                                                         | Code examples                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [AWS SDK for C++](../../../sdk-for-cpp.md "../../../sdk-for-cpp.md")                      | [AWS SDK for C++ code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp")                          |
| [AWS CLI](../../../cli.md "../../../cli.md")                                              | [AWS CLI code examples](../../../code-library/latest/ug/cli_2_code_examples.md "../../../code-library/latest/ug/cli_2_code_examples.md")                                                |
| [AWS SDK for Go](../../../sdk-for-go.md "../../../sdk-for-go.md")                         | [AWS SDK for Go code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2 "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2")                         |
| [AWS SDK for Java](../../../sdk-for-java.md "../../../sdk-for-java.md")                   | [AWS SDK for Java code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2 "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2")                   |
| [AWS SDK for JavaScript](../../../sdk-for-javascript.md "../../../sdk-for-javascript.md") | [AWS SDK for JavaScript code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3 "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3") |
| [AWS SDK for Kotlin](../../../sdk-for-kotlin.md "../../../sdk-for-kotlin.md")             | [AWS SDK for Kotlin code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin")                 |
| [AWS SDK for .NET](../../../sdk-for-net.md "../../../sdk-for-net.md")                     | [AWS SDK for .NET code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3 "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3")               |
| [AWS SDK for PHP](../../../sdk-for-php.md "../../../sdk-for-php.md")                      | [AWS SDK for PHP code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php")                          |
| [AWS Tools for PowerShell](../../../powershell.md "../../../powershell.md")               | [Tools for PowerShell code examples](../../../code-library/latest/ug/powershell_4_code_examples.md "../../../code-library/latest/ug/powershell_4_code_examples.md")                     |
| [AWS SDK for Python (Boto3)](../../../pythonsdk.md "../../../pythonsdk.md")               | [AWS SDK for Python (Boto3) code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python")         |
| [AWS SDK for Ruby](../../../sdk-for-ruby.md "../../../sdk-for-ruby.md")                   | [AWS SDK for Ruby code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby")                       |
| [AWS SDK for Rust](../../../sdk-for-rust.md "../../../sdk-for-rust.md")                   | [AWS SDK for Rust code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1 "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1")                   |
| [AWS SDK for SAP ABAP](../../../sdk-for-sapabap.md "../../../sdk-for-sapabap.md")         | [AWS SDK for SAP ABAP code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap")           |
| [AWS SDK for Swift](../../../sdk-for-swift.md "../../../sdk-for-swift.md")                | [AWS SDK for Swift code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift")                    |

For specific examples, see [Code examples for Amazon S3 using AWS SDKs](service_code_examples.md "service_code_examples.md").

## SDK Programming interfaces

Each AWS SDK provides one or more programmatic interfaces for working with Amazon S3. Each SDK provides a low-level interface for Amazon S3, with methods that closely resemble API operations. Some SDKs provide high-level interfaces for Amazon S3, that are abstractions intended to simplify common use cases.

For example, when you perform a multipart upload by using the low-level API operations,
you use an operation to initiate the upload, another operation to upload parts, and a final
operation to complete the upload. A high-level multipart upload API operation lets you to do
all of the operations required for upload in a single API call. For examples, see [Uploading an
object using multipart upload](../userguide/mpu-upload-object.md "../userguide/mpu-upload-object.md") in the _Amazon S3 User Guide_.

Low-level API operations allow greater control over the upload. We recommend that you use the low-level API operations if you need to pause and resume uploads, vary part sizes during the upload, or begin uploads when you don't know the size of the data in advance.
