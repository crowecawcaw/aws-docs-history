

# Lambda Event Function runtimes

AWS Lambda Event Functions (previously known as Lambda functions) support multiple languages through the use of *runtimes*. A runtime provides an environment for a specific language. It passes invocation events, context information, and responses between Lambda and the function. You can use runtimes that Lambda provides, or build your own as a [customer-managed runtime](runtimes-customer-managed.md). For information about open-source runtimes, see [Open-source repositories](runtimes-open-source.md). For runtimes that Lambda Web Functions use, see [Lambda Web Function runtimes](web-functions-runtimes.md). 

Lambda is agnostic to your choice of runtime. For simple functions, interpreted languages like Python and Node.js offer the fastest performance. For functions with more complex computation, compiled languages like Java are often slower to initialize but run quickly in the Lambda handler. Choice of runtime is also influenced by developer preference and language familiarity.

Each major programming language release has a separate runtime, with a unique *runtime identifier*, such as `nodejs24.x` or `python3.14`. To configure a function to use a new major language version, you need to change the runtime identifier. AWS Lambda can't guarantee backward compatibility between major versions. So, you must make this change yourself.

 For a [function defined as a container image](images-create.md), you choose a runtime and the Linux distribution when you create the container image. To change the runtime, you create a new container image.

When you use a .zip file archive for the deployment package, you choose a runtime when you create the function. To change the runtime, you can [update your function's configuration](configuration-function-zip.md). The runtime is paired with one of the Amazon Linux distributions. The underlying execution environment provides additional libraries and [environment variables](configuration-envvars.md) that you can access from your function code.

Lambda invokes your function in an [execution environment](lambda-runtime-environment.md). The execution environment provides a secure and isolated runtime environment that manages the resources required to run your function. Lambda re-uses the execution environment from a previous invocation if one is available, or it can create a new execution environment. 

To use languages that compile to a native binary, such as [Go](lambda-golang.md) or [Rust](lambda-rust.md), use an [OS-only runtime](#runtimes-provided). To use other languages or language versions, or to customize a runtime, we recommend that you create a [customer-managed runtime](runtimes-customer-managed.md). You can also include a runtime in your function's deployment package or in a [layer](chapter-layers.md), with an OS-only runtime. This approach is called [bring your own language (BYOL)](runtimes-custom.md). In both cases, the runtime uses the Lambda [runtime API](runtimes-api.md) to get invocation events and send responses.

## Supported runtimes
<a name="runtimes-supported"></a>

The following table lists the supported Lambda runtimes for Event Functions and projected deprecation dates. After a runtime is deprecated, you're still able to create and update functions for a limited period. For more information, see [Runtime use after deprecation](runtime-support-policy.md#runtime-deprecation-levels). The table provides the currently forecasted dates for runtime deprecation, based on our [Runtime deprecation](runtime-support-policy.md). These dates are provided for planning purposes and are subject to change.

**Important**  
Amazon Linux 2 reached its scheduled end of life on June 30, 2026. Lambda runtimes and container base images for Java 8 (AL2), Java 11 (AL2), Java 17 (AL2), Python 3.10, Python 3.11, and provided.al2 will continue to receive patches for [critical and selected important](https://alas.aws.amazon.com/faqs.html) Amazon Linux 2 security issues, in addition to language runtime patches, until the deprecation dates shown in the following table and in the [deprecated runtimes](runtime-support-policy.md#runtimes-deprecated) table.  
We recommend customers upgrade to an Amazon Linux 2023-based runtime as soon as possible. For customers upgrading to Java 21 or Java 25, you can use [AWS Transform custom](https://docs.aws.amazon.com/transform/latest/userguide/custom.html) to assist with these upgrades. For customers unable to upgrade their Java version, we provide Amazon Linux 2023-based runtimes for Java 8, Java 11, and Java 17 that follow the AL2023 deprecation schedule.


| Name | Identifier | Operating system | Deprecation date | Block function create | Block function update | 
| --- | --- | --- | --- | --- | --- | 
| Node.js 26 | `nodejs26.x` | Amazon Linux 2023 |  Apr 30, 2029  |  Jun 1, 2029  |  Jul 1, 2029  | 
| Node.js 24 | `nodejs24.x` | Amazon Linux 2023 |  Apr 30, 2028  |  Jun 1, 2028  |  Jul 1, 2028  | 
| Node.js 22 | `nodejs22.x` | Amazon Linux 2023 |  May 30, 2027  |  Jul 29, 2027  |  Aug 31, 2027  | 
| Python 3.15 | `python3.15` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 
| Python 3.14 | `python3.14` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 
| Python 3.13 | `python3.13` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 
| Python 3.12 | `python3.12` | Amazon Linux 2023 |  Oct 31, 2028  |  Nov 30, 2028  |  Jan 10, 2029  | 
| Python 3.11 | `python3.11` | Amazon Linux 2 |  Jun 30, 2027  |  Jul 29, 2027  |  Aug 31, 2027  | 
| Java 25 | `java25` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 
| Java 21 | `java21` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 
| Java 17 | `java17.al2023` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 
| Java 11 | `java11.al2023` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 
| Java 8 | `java8.al2023` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 
| Java 17 | `java17` | Amazon Linux 2 |  Jun 30, 2027  |  Jul 29, 2027  |  Aug 31, 2027  | 
| Java 11 | `java11` | Amazon Linux 2 |  Jun 30, 2027  |  Jul 29, 2027  |  Aug 31, 2027  | 
| Java 8 | `java8.al2` | Amazon Linux 2 |  Jun 30, 2027  |  Jul 29, 2027  |  Aug 31, 2027  | 
| .NET 10 | `dotnet10` | Amazon Linux 2023 |  Nov 14, 2028  |  Dec 14, 2028  |  Jan 15, 2029  | 
| Ruby 4.0 | `ruby4.0` | Amazon Linux 2023 |  Mar 31, 2029  |  Apr 30, 2029  |  May 31, 2029  | 
| Ruby 3.4 | `ruby3.4` | Amazon Linux 2023 |  Mar 31, 2028  |  Apr 30, 2028  |  May 31, 2028  | 
| Ruby 3.3 | `ruby3.3` | Amazon Linux 2023 |  Mar 31, 2027  |  Jul 29, 2027  |  Aug 31, 2027  | 
| OS-only Runtime | `provided.al2023` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 

**Note**  
For new AWS Regions, Lambda doesn't support runtimes that are set to be deprecated within the next 6 months.

Lambda keeps managed runtimes and their corresponding container base images up to date with patches and support for minor version releases. For more information, see [Understanding how Lambda manages runtime updates](runtimes-update.md).

To interact with other AWS services and resources from your function, you can use one of the AWS SDKs. The Node.js, Python, and Ruby runtimes include a version of the AWS SDK. However, we recommend that you always include the SDK modules your code uses, along with any dependencies, in your function's deployment package or in a [Lambda layer](chapter-layers.md). This approach gives you full control of your dependencies. It also maximizes [backward compatibility](runtimes-update.md#runtime-update-compatibility) during automatic runtime updates.

We recommend that you use the runtime-included SDK version only when you can't include additional packages in your deployment. For example, when you create your function using the Lambda console code editor or using inline function code in an CloudFormation template.

Lambda periodically updates the versions of the AWS SDKs included in the Node.js, Python, and Ruby runtimes. To determine the version of the AWS SDK included in the runtime you're using, see the following sections:
+ [Runtime-included SDK versions (Node.js)](lambda-nodejs.md#nodejs-sdk-included)
+ [Runtime-included SDK versions (Python)](lambda-python.md#python-sdk-included)
+ [Runtime-included SDK versions (Ruby)](lambda-ruby.md#ruby-sdk-included)

Lambda continues to support the Go programming language after deprecation of the Go 1.x runtime. Use an [OS-only runtime](#runtimes-provided), such as `provided.al2023`. For more information, see [Building Lambda Event Functions with Go](lambda-golang.md) and [Migrating AWS Lambda functions from the Go1.x runtime to the custom runtime on Amazon Linux 2](https://aws.amazon.com/blogs/compute/migrating-aws-lambda-functions-from-the-go1-x-runtime-to-the-custom-runtime-on-amazon-linux-2/) on the *AWS Compute Blog*.

All supported Lambda runtimes support both x86\_64 and arm64 architectures. For customer-managed runtimes, the runtime publisher chooses the supported architectures.

## New runtime releases
<a name="runtimes-future"></a>

Lambda provides managed runtimes for new language versions only when the release reaches the long-term support (LTS) phase of the language's release cycle. For example, for the [Node.js release cycle](https://nodejs.org/en/about/previous-releases), when the release reaches the Active LTS phase.

Before the release reaches the long-term support phase, it remains in development and can still be subject to breaking changes. Lambda applies runtime updates automatically by default, so breaking changes to a runtime version could stop your functions from working as expected.

Lambda doesn't provide managed runtimes for language versions which aren't scheduled for LTS release.

To use a language version before Lambda provides a managed runtime for it, or a version that Lambda doesn't plan to support, you can create a [customer-managed runtime](runtimes-customer-managed.md).

The following list shows the target launch month for upcoming Lambda runtimes. These dates are indicative only and subject to change.
+ **Node.js 26** - November 2026
+ **Python 3.15** - November 2026

For information about how Lambda deprecates runtimes and a list of deprecated runtimes, see [Runtime deprecation](runtime-support-policy.md).

## OS-only runtimes
<a name="runtimes-provided"></a>

Lambda provides [managed runtimes](#runtimes-supported) for Java, Python, Node.js, .NET, and Ruby. An OS-only runtime (the `provided` runtime family) includes the operating system but no language runtime. Lambda patches the operating system in OS-only runtimes, in the same way as for other managed runtimes.

### Using an OS-only runtime for compiled languages
<a name="runtimes-provided-native"></a>

Languages such as Go, Rust, Swift, and C\+\+ compile ahead of time (AOT) to a native executable binary, which doesn't require a separate language runtime. These languages need only an operating system environment in which the binary can run. You can also use OS-only runtimes to deploy binaries compiled with .NET Native AOT and Java GraalVM Native Image.

You must include a runtime interface client in your binary. The runtime interface client calls the [Lambda runtime API](runtimes-api.md) to retrieve function invocations, and then calls your function handler. Lambda provides runtime interface clients for [Rust](lambda-rust.md), [Go](golang-package.md#golang-package-mac-linux), [.NET Native AOT](dotnet-native-aot.md), [Swift](https://github.com/awslabs/swift-aws-lambda-runtime) (experimental), and [C\+\+](https://github.com/awslabs/aws-lambda-cpp) (experimental).

You must compile your binary for a Linux environment and for the same instruction set architecture that you plan to use for the function (x86\_64 or arm64).

### Customizing or adding a language runtime
<a name="runtimes-provided-customize"></a>

To use a language or language version that Lambda doesn't provide a managed runtime for, or to add shared components to a runtime, we recommend that you create a [customer-managed runtime](runtimes-customer-managed.md). Customer-managed runtimes have the following benefits:
+ **Central runtime management** – You manage the runtime as a separate resource, independently of the functions that use it. You control the runtime contents, patching, and lifecycle, including deprecation.
+ **Updates at scale** – You roll out a runtime update by updating a runtime alias. Functions that use the alias pick up the update at their next cold start, without you redeploying each function.

You can build a customer-managed runtime from a Lambda base image or an OS-only base image, or with a third-party runtime. For more information, see [Comparing customer-managed runtimes to other deployment models](runtimes-customer-managed.md#runtimes-customer-managed-compare) and [Building runtime images](cmr-building-images.md).

You can also include the language runtime in your function's deployment package or in a [layer](chapter-layers.md), and use it with an OS-only runtime. This approach is called bring your own language (BYOL). With BYOL, you update the runtime separately in each function, so it can be a good choice when you have only a small number of functions. Third-party runtimes such as [Bref](https://bref.sh/) for PHP use this approach. For more information, see [Supporting a new programming language for AWS Lambda Event Functions](runtimes-custom.md).

### Supported OS-only runtimes
<a name="runtimes-provided-list"></a>

Lambda supports the following OS-only runtimes:


| Name | Identifier | Operating system | Deprecation date | Block function create | Block function update | 
| --- | --- | --- | --- | --- | --- | 
| OS-only Runtime | `provided.al2023` | Amazon Linux 2023 |  Jun 30, 2029  |  Jul 31, 2029  |  Aug 31, 2029  | 

The Amazon Linux 2023 (`provided.al2023`) runtime provides several advantages over Amazon Linux 2, including a smaller deployment footprint and updated versions of libraries such as `glibc`.

The `provided.al2023` runtime uses `dnf` as the package manager instead of `yum`, which is the default package manager in Amazon Linux 2. For more information about the differences between `provided.al2023` and `provided.al2`, see [Introducing the Amazon Linux 2023 runtime for AWS Lambda](https://aws.amazon.com/blogs/compute/introducing-the-amazon-linux-2023-runtime-for-aws-lambda/) on the AWS Compute Blog.