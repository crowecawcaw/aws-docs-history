# Supported systems

Application Signals is supported and tested on Amazon EKS, native Kubernetes, Amazon ECS, and Amazon EC2. The instructions for
enabling Application Signals on Amazon EC2 should work on any platform that supports the CloudWatch agent and
AWS Distro for OpenTelemetry.

###### Topics

- [Java compatibility](#CloudWatch-Application-Signals-supportmatrix-java "#CloudWatch-Application-Signals-supportmatrix-java")
- [.NET compatibility](#CloudWatch-Application-Signals-supportmatrix-dotnet "#CloudWatch-Application-Signals-supportmatrix-dotnet")
- [PHP compatibility](#php-compatibility "#php-compatibility")
- [Ruby compatibility](#ruby-compatibility "#ruby-compatibility")
- [Python compatibility](#CloudWatch-Application-Signals-supportmatrix-python "#CloudWatch-Application-Signals-supportmatrix-python")
- [Node.js compatibility](#CloudWatch-Application-Signals-supportmatrix-node "#CloudWatch-Application-Signals-supportmatrix-node")
- [GoLang compatibility](#golang-compatibility "#golang-compatibility")
- [Runtime version support matrix](#rumtime-version-matix "#rumtime-version-matix")
- [Known issues](#AppSignals-Issues "#AppSignals-Issues")

## Java compatibility

Application Signals supports Java applications, and supports the same Java
libraries and frameworks as the AWS Distro for
OpenTelemetry does. For more information, see
[Supported libraries, frameworks, application servers, and JVMs](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md "https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md").

## .NET compatibility

Application Signals supports the same .NET libraries and frameworks as the AWS Distro for OpenTelemetry does. For more information, see
[Supported instrumentations](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/metapackages/auto-instrumentations-node#supported-instrumentations "https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/metapackages/auto-instrumentations-node#supported-instrumentations").

Application Signals supports .NET applications that are running on x86-64 or ARM64 CPUs, and supports the Linux x64, Linux ARM64, and Microsoft Windows Server 2022 x64.

###### Note

The AWS Distro for Open Telemetry (ADOT) SDK for .NET does not support AWS SDK for .NET V4. Use AWS SDK .NET V3 for full Application Signals support.

## PHP compatibility

Application Signals supports PHP applications with OpenTelemetry Zero Code instrumentation. There is no AWS Distro for Open Telemetry (ADOT) SDK available for this purpose. You should use the standard OpenTelemetry Instrumentation SDK
with [Transaction Search](AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.md "AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.md") enabled. To start using zero code instrumentation in PHP, follow these steps from the OpenTelemetry PHP Instrumentation docs, [PHP zero-code instrumentation](https://opentelemetry.io/docs/zero-code/php/ "https://opentelemetry.io/docs/zero-code/php/") .
Automatic instrumentation is available for a number of commonly used PHP libraries. For more information, see [OpenTelemetry registry](https://packagist.org/search/?query=open-telemetry%3Dinstrumentation "https://packagist.org/search/?query=open-telemetry%3Dinstrumentation").

## Ruby compatibility

Application Signals supports Ruby applications with OpenTelemetry Zero Code instrumentation. There is no AWS Distro for Open Telemetry (ADOT) SDK available for this purpose. You should use the standard OpenTelemetry Instrumentation SDK
with [Transaction Search](AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.md "AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.md") enabled. To start using zero code instrumentation in Ruby, follow these steps from the OpenTelemetry Ruby Instrumentation docs, [Ruby zero-code instrumentation](https://opentelemetry.io/docs/languages/ruby/getting-started/#instrumentation "https://opentelemetry.io/docs/languages/ruby/getting-started/#instrumentation") . For a list of released instrumentation libraries, see [Registry](https://opentelemetry.io/ecosystem/registry/?language=rubycomponent=instrumentation "https://opentelemetry.io/ecosystem/registry/?language=rubycomponent=instrumentation").

## Python compatibility

Application Signals supports the same libraries and frameworks as the AWS Distro for
OpenTelemetry does. For more information, see **Supported packages** at
[opentelemetry-python-contrib](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation/README.md "https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation/README.md").

Before you enable Application Signals for your Python applications, be aware of the following considerations.

- In some containerized applications, a missing `PYTHONPATH` environment variable can sometimes
  cause the application to fail to start. To resolve this, ensure that you set the `PYTHONPATH` environment variable
  to the location of your application’s working directory. This is due to a known issue with OpenTelemetry auto-instrumentation.
  For more information about this issue, see
  [Python autoinstrumentation setting of PYTHONPATH is not compliant](https://github.com/open-telemetry/opentelemetry-operator/issues/2302 "https://github.com/open-telemetry/opentelemetry-operator/issues/2302").
- For Django applications, there are additional required configurations, which are outlined
  in the [OpenTelemetry Python documentation](https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html "https://opentelemetry-python.readthedocs.io/en/latest/examples/django/README.html").
  - Use the `--noreload` flag to prevent automatic reloading.
  - Set the `DJANGO_SETTINGS_MODULE` environment variable to the location of your Django
    application’s `settings.py` file. This ensures that OpenTelemetry can correctly access and integrate with your Django settings.

## Node.js compatibility

Application Signals supports the same Node.js
libraries and frameworks as the AWS Distro for
OpenTelemetry does. For more information, see
[Supported instrumentations](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main "https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main").

### Known limitations about Node.js with ESM

The AWS Distro for Opentelemetry Node.js supports two module systems: ECMAScript Modules (ESM) and CommonJS (CJS). To enable Application Signals, we
recommend that you use the CJS module format because OpenTelemetry JavaScript’s support of ESM is experimental and a work in progress.
For more details, see [ECMAScript Modules vs. CommonJS](https://github.com/open-telemetry/opentelemetry-js/blob/eb3ca4fb07ee31c62093f5fcec56575573c902ce/doc/esm-support.md "https://github.com/open-telemetry/opentelemetry-js/blob/eb3ca4fb07ee31c62093f5fcec56575573c902ce/doc/esm-support.md") on GitHub.

To determine if your application is using CJS and not ESM, ensure that your application does not fulfill the conditions to enable ESM. For more information
about these conditions, see [Enabling](https://nodejs.org/api/esm.html#enabling "https://nodejs.org/api/esm.html#enabling") in the Node.js documentation.

The AWS Distro for Opentelemetry Node.js provides limited support for ESM based on OpenTelemetry JavaScript’s experimental support for ESM. This means the following:

- The Node.js version must be 18.19.0 or later.
- The Node.js application that you want to instrument must include `@aws/aws-distro-opentelemetry-node-autoinstrumentation`
  and `@opentelemetry/instrumentation` as dependencies.
- The Node.js application that you want to instrument must start with the following node option:

```
NODE_OPTIONS=' --import @aws/aws-distro-opentelemetry-node-autoinstrumentation/register --experimental-loader=@opentelemetry/instrumentation/hook.mjs'
```

To enable Application Signals with Node.js ESM module format, we provide the different setup for different platforms:

- **Amazon EKS** – [Setting up a Node.js application with the ESM module format](CloudWatch-Application-Signals-Enable-EKS.md#EKS-NodeJs-ESM "CloudWatch-Application-Signals-Enable-EKS.md#EKS-NodeJs-ESM")
- **Amazon ECS with sidecar strategy** – [Setting up a Node.js application with the ESM module format](CloudWatch-Application-Signals-ECS-Sidecar.md#ECS-NodeJs-ESM "CloudWatch-Application-Signals-ECS-Sidecar.md#ECS-NodeJs-ESM")
- **Amazon ECS with daemon strategy** – [Setting up a Node.js application with the ESM module format](CloudWatch-Application-Signals-ECS-Daemon.md#ECSDaemon-NodeJs-ESM "CloudWatch-Application-Signals-ECS-Daemon.md#ECSDaemon-NodeJs-ESM")
- **Amazon ECS with AWS CDK**
- **Amazon EC2** – [Setting up a Node.js application with the ESM module format](CloudWatch-Application-Signals-Enable-EC2Main.md#EC2-NodeJs-ESM "CloudWatch-Application-Signals-Enable-EC2Main.md#EC2-NodeJs-ESM")
- **Kubernetes** – [Setting up a Node.js application with the ESM module format](CloudWatch-Application-Signals-Enable-KubernetesMain.md#Kubernetes-NodeJs-ESM "CloudWatch-Application-Signals-Enable-KubernetesMain.md#Kubernetes-NodeJs-ESM")

## GoLang compatibility

Application Signals supports GoLang applications with OpenTelemetry Zero Code instrumentation. There is no AWS Distro for Open Telemetry (ADOT) SDK available for this purpose. You should use the standard OpenTelemetry Instrumentation SDK
with [Transaction Search](AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.md "AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.md") enabled. To start using zero code instrumentation in GoLang, follow these steps from the OpenTelemetry GoLang Instrumentation docs,
[Getting Started with OpenTelemetry Go Automatic Instrumentation](https://github.com/open-telemetry/opentelemetry-go-instrumentation/blob/main/docs/getting-started.md "https://github.com/open-telemetry/opentelemetry-go-instrumentation/blob/main/docs/getting-started.md") .

### Implementation considerations GoLang instrumentation

Learn about important implementation details for using GoLang instrumentation. This guidance explains how to implement explicit context propagation in GoLang applications and set up Application Signals.
Properly implementing GoLang instrumentation helps you track and analyze your application's performance effectively.

#### Instrumenting the AWS SDK

The Golang auto-instrumentation library does not support AWS SDK instrumentation out of the box. You must use the `otelaws` library instrumentation along with the auto-instrumentation agent:

1. Install the required dependency:

```
go get go.opentelemetry.io/contrib/instrumentation/github.com/aws/aws-sdk-go-v2/otelaws
```

2. Add the following line to the application:

```
otelaws.AppendMiddlewares(&cfg.APIOptions)
```

3. Create subsequent AWS clients with the previous `aws.Config` object:

```
s3Client := s3.NewFromConfig(cfg)
```

The following example will generate spans for AWS calls and integrates with auto-instrumentation.

```
func handleRequest(ctx context.Context) error {
    cfg, err := config.LoadDefaultConfig(ctx)
    if err != nil {
        return err
    }

    // Add OpenTelemetry instrumentation middleware to the AWS config
    otelaws.AppendMiddlewares(&cfg.APIOptions)

    // Create S3 client with the instrumented config
    s3Client := s3.NewFromConfig(cfg)

    // Now any operations with this client will be traced
    // with the context from the upstream call
    _, err = s3Client.ListBuckets(ctx, &s3.ListBucketsInput{})
    return err
}
```

For information on configuring the auto-instrumentation executable, see [Configuration methods](https://github.com/open-telemetry/opentelemetry-go-instrumentation/blob/main/docs/configuration.md "https://github.com/open-telemetry/opentelemetry-go-instrumentation/blob/main/docs/configuration.md").

#### Instrumenting HTTP calls

HTTP calls can split traces when Context isn't passed between requests – HTTP clients must use `NewRequestWithContext()` instead of `NewRequest()` to ensure ensures the downstream service uses the same context. When both services have instrumentation agents, the spans connect with the same trace ID to provide end-to-end visibility.

```
func makeDownstreamCall(ctx context.Context, url string) ([]byte, error) {
    client := &http.Client{}

    // Create request with context from the upstream call
    req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
    if err != nil {
        return nil, err
    }

    // Execute the request
    resp, err := client.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()
}
```

#### Instrumenting SQL calls

SQL spans may become disconnected from their parent span, causing client calls to be inferred as server spans. This occurs when SQL calls do not receive the context from their upstream handlers. Standard SQL calls like `Query` and `Exec` use `context.Background()`
by default, not the context of the upstream caller. Replace standard SQL calls with their context-aware equivalents:

- Use `QueryContext` instead of `Query`
- Use `ExecContext` instead of `Exec`

These methods Pass the upstream request context to the DB calls, maintaining proper trace continuity.

```
func queryDatabase(ctx context.Context, db *sql.DB, userID string) (*sql.Rows, error) {
    // This breaks the trace context
    // row := db.Query("SELECT name FROM users WHERE id = $1", userID)

    // This passes the context from the upstream call for trace continuity
    rows, err := db.QueryContext(ctx, "SELECT name FROM users WHERE id = $1", userID)

    return rows, error
}
```

###### Note

The `db.system` attribute is not currently supported for SQL calls. This limitation affects CloudWatch's ability to accurately identify database clients. As a result, dependencies will display **UnknownRemoteService** instead of the
name of the DB client making the query.

#### Resource detectors

Go auto-instrumentation does not currently support configuring resource detectors at runtime. The OpenTelemetry community is working on a feature to configure resource detectors using environment variables. Look for this feature in a future update.
In the meantime, you can use the CloudWatch Agent with auto-instrumentation to automatically generate host resource attributes.

## Runtime version support matrix

| Language | Runtime version                                                                                                                                                     |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Java     | JVM versions 8, 11, 17, 21, and 23                                                                                                                                  |
| Python   | Python versions 3.9 and higher are supported                                                                                                                        |
| .NET     | Release 1.6.0 and below supports .NET 6, 8, and .NET Framework 4.6.2 and higher<br>Release 1.7.0 and higher supports .NET 8, 9, and .NET Framework 4.6.2 and higher |
| Node.js  | Node.js versions 14, 16, 18, 20, and 22                                                                                                                             |
| PHP      | PHP versions 8.0 and higher                                                                                                                                         |
| Ruby     | CRuby >= 3.1, JRuby >= 9.3.2.0, or TruffleRuby >= 22.1                                                                                                              |
| GoLang   | Golang versions 1.18 and higher                                                                                                                                     |

## Known issues

The runtime metrics collection in the Java SDK release v1.32.5 is known to not work with applications using JBoss Wildfly. This issue extends to the
Amazon CloudWatch Observability EKS add-on, affecting versions `2.3.0-eksbuild.1` through `2.6.0-eksbuild.1`. The issue is fixed in Java SDK release `v1.32.6` and the Amazon CloudWatch Observability EKS add-on version `v3.0.0-eksbuild.1`.

If you are impacted, either upgrade the Java SDK version or disable your runtime metrics collection by adding the
environment variable `OTEL_AWS_APPLICATION_SIGNALS_RUNTIME_ENABLED=false` to your application.
