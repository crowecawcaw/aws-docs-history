# Enabling hybrid post-quantum TLS

AWS SDKs and tools have cryptographic capabilities and configuration that differ across language and runtime.
There are three ways that an AWS SDK or tool currently provides PQ TLS support:

###### Topics

- [SDKs with PQ TLS enabled by default](#pq-tls-default "#pq-tls-default")
- [Opt-in PQ TLS support](#pq-tls-opt-in "#pq-tls-opt-in")
- [SDKs that rely on System OpenSSL](#pq-tls-open-ssl "#pq-tls-open-ssl")
- [AWS SDKs and tools not planning to support PQ TLS](#pq-tls-nosupport "#pq-tls-nosupport")

## SDKs with PQ TLS enabled by default

###### Note

As of 6-Nov-2025, AWS SDK and its underlying CRT libraries
for MacOS and Windows uses system libraries for TLS, so PQ TLS capabilities on those platforms is
generally determined by system-level support.

### AWS SDK for Go

The AWS SDK for Go uses Golang’s own TLS implementation provided by its standard library.
Golang supports and prefers PQ TLS as of v1.24,
so AWS SDK for Go users can enable PQ TLS by simply upgrading Golang to v1.24

### AWS SDK for JavaScript (browser)

The AWS SDK for JavaScript (browser) uses the browser’s TLS stack,
so the SDK will negotiate PQ TLS if the browser runtime supports and prefers it.
Firefox launched support for PQ TLS in v132.0. Chrome announced support for PQ TLS in v131.
Edge supports opt-in PQ TLS in v120 for desktop and 140 for Android.

### AWS SDK for Node.js

As of Node.js v22.20 (LTS) and v24.9.0, Node.js statically links and bundles OpenSSL 3.5.
This means that PQ TLS is enabled and preferred by default for those and subsequent versions.

### AWS SDK for Kotlin

The Kotlin SDK supports and prefers PQ TLS on Linux as of v1.5.78.
Because AWS SDK for Kotlin’s CRT-based client relies on system libraries for TLS on MacOS and Windows,
support for PQ TLS will depend on those underlying system libraries.

### AWS SDK for Rust

The AWS SDK for Rust distributes distinct packages (known as “crates” in the Rust ecosystem) for each service client. These are all managed in a consolidated GitHub repository, but each service
client follows its own version and release cadence. The consolidated SDK released PQ TLS preference on 8/29/25, so any individual service
client version released after that date will support and prefer PQ TLS by default.

You can determine the minimum version supporting PQ TLS for a particular service client by
navigating to the relevant crates.io version URL (for example,
AWS Payment Cryptography's is [here](https://crates.io/crates/aws-sdk-paymentcryptography/versions "https://crates.io/crates/aws-sdk-paymentcryptography/versions"))
and finding the first version published after 29-Aug-25. Any service client version published after 29-Aug-25
will have PQ TLS enabled and preferred by default.

## Opt-in PQ TLS support

### AWS SDK for C++

By default, the C++ SDK uses platform-native clients like libcurl and WinHttp.
Libcurl generally relies on system OpenSSL for TLS,
so PQ TLS is only enabled by default if system OpenSSL is ≥ v3.5.
You can override this default in C++ SDK v1.11.673 or later, and
opt-in to the AwsCrtHttpClient which supports and enables PQ TLS by default.

Notes on Building for Opt-In PQ TLS You can fetch the SDK’s
CRT dependencies with [this script](https://github.com/aws/aws-sdk-cpp/blob/main/prefetch_crt_dependency.sh "https://github.com/aws/aws-sdk-cpp/blob/main/prefetch_crt_dependency.sh").
Building the SDK from source is
described [here](../../../sdk-for-cpp/v1/developer-guide/sdk-from-source.md "../../../sdk-for-cpp/v1/developer-guide/sdk-from-source.md")
and [here](https://github.com/aws/aws-sdk-cpp/tree/main?tab=readme-ov-file#building-from-source "https://github.com/aws/aws-sdk-cpp/tree/main?tab=readme-ov-file#building-from-source"),
but note that you may need a few additional CMake flags:

```

  `-DUSE_CRT_HTTP_CLIENT=ON \
 -DUSE_TLS_V1_2=OFF \
 -DUSE_TLS_V1_3=ON \
 -DUSE_OPENSSL=OFF \`
```

### AWS SDK for Java

As of v2, AWS SDK for Java provides an AWS Common Runtime (AWS CRT) HTTP Client that
can be configured to perform PQ TLS. As of v2.35.11, the AwsCrtHttpClient enables and prefers PQ TLS by default wherever it’s used.

## SDKs that rely on System OpenSSL

Several AWS SDKs and tools depend on the system's libcrypto/libssl library for TLS.
The system library most often used is OpenSSL.
OpenSSL enabled PQ TLS support in version 3.5, so the easiest way to
configure these SDKs and tools for PQ TLS is to use it on an
operating system distribution that has at least OpenSSL 3.5 installed.

You can also configure a Docker container to use OpenSSL 3.5 to enable PQ TLS on any
system that supports Docker. See Post-quantum TLS in Python for an example of setting this up for Python.

### AWS CLI

PQ TLS support with the [AWS CLI installer](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") is coming soon.
To enable immediately, you can use alternative installers for the AWS CLI, which varies by operating system, and can enable PQ TLS.

For MacOS, install the AWS CLI via [Homebrew](https://brew.sh/ "https://brew.sh/") and ensure that your Homebrew-vended OpenSSL is upgraded to version 3.5+.
You can do this with “brew install openssl@3.6” and validate with “brew list | grep openssl”.

For Ubuntu or Debian Linux: ensure the Linux distribution you are using has OpenSSL 3.5+ installed as system OpenSSL.
Then, install the AWS CLI using apt or [PyPI](https://pypi.org/project/awscliv2/ "https://pypi.org/project/awscliv2/"). With these prerequisites,
the AWS CLI vended by apt or PyPI will be configured to negotiate PQ-TLS.
For step-by-step instructions to validate the installation, see [github repository](https://github.com/aws-samples/sample-post-quantum-tls-python/ "https://github.com/aws-samples/sample-post-quantum-tls-python/")
and accompanying [blog post](https://aws.amazon.com/blogs/security/post-quantum-tls-in-python/ "https://aws.amazon.com/blogs/security/post-quantum-tls-in-python/").

### AWS SDK for PHP

The AWS SDK for PHP relies on system libssl/libcrypto.
To use PQ TLS, use this SDK on an operating system distribution that has at least OpenSSL 3.5 installed.

### AWS SDK for Python (Boto3)

The AWS SDK for Python (Boto3) relies on system libssl/libcrypto.
To use PQ TLS, use this SDK on an operating system distribution that has at least OpenSSL 3.5 installed.

### AWS SDK for Ruby

The AWS SDK for Ruby relies on system libssl/libcrypto.
To use PQ TLS, use this SDK on an operating system distribution that has at least OpenSSL 3.5 installed.

## AWS SDKs and tools not planning to support PQ TLS

There are currently no plans to support the following language SDKs and tools:

- AWS SDK for .NET
- AWS SDK for Swift
- AWS Tools for Windows PowerShell
