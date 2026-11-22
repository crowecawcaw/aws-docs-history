

# Pointing your AWS SDK at AWS Emulator

To use AWS Emulator, you configure the AWS CLI or your AWS SDK to send requests to the emulator instead of to AWS. When you run the emulator as a local process (Linux or Docker), you set environment variables. When you run it embedded in Rust tests, you replace the SDK HTTP client. For embedded mode, see [Getting started with embedded mode](getting-started-embedded.md).

## How the emulator handles credentials and HTTPS
<a name="point-sdk-credentials"></a>

When you run AWS Emulator as a local process, by default it requires API requests to be signed with Signature Version 4 (SigV4), like AWS does. Signature checks protect you from requests that a web page or another local program sends to the emulator without your knowledge. For which keys the emulator accepts and the errors that it returns, see [Credentials and authentication](cli-reference.md#cli-reference-credentials). For how this protects your machine, see [What we do](security.md#security-what-we-do).

When the emulator starts, it generates a new access key ID and secret access key. It writes them, a `config` file for your SDK, and its certificate (`ca.pem`, and `truststore.p12` for Java) to a subdirectory of `~/.aws/emulator/` named for its port, for example `~/.aws/emulator/9297/`. The keys work only with this run of the emulator. For what each file contains and when it’s deleted, see [Local files](cli-reference.md#cli-reference-files).

To turn off signature checks, start the emulator with `--auth off` (`-a off`). The emulator then serves every request and doesn’t write the `emulator_credentials` file. Before you use this option, see [What you do](security.md#security-what-you-do).

## To point your SDK at a local emulator
<a name="point-sdk-env"></a>

1. Start the emulator. For more information, see [Getting started with AWS Emulator](getting-started.md).

1. In the shell where you run your code, set the following environment variables. If you use a port other than 9297, replace `9297` in each value.

    **macOS and Linux** 

   ```bash
   export AWS_ENDPOINT_URL=https://127.0.0.1:9297
   export AWS_SHARED_CREDENTIALS_FILE=~/.aws/emulator/9297/emulator_credentials
   export AWS_CONFIG_FILE=~/.aws/emulator/9297/config
   export AWS_CA_BUNDLE=~/.aws/emulator/9297/ca.pem
   export AWS_EC2_METADATA_DISABLED=true
   export AWS_DISABLE_HOST_PREFIX_INJECTION=true
   export AWS_REGION=us-east-1
   export AWS_DEFAULT_REGION=us-east-1
   ```

    **Windows PowerShell** 

   ```powershell
   $env:AWS_ENDPOINT_URL = "https://127.0.0.1:9297"
   $env:AWS_SHARED_CREDENTIALS_FILE = "$env:USERPROFILE\.aws\emulator\9297\emulator_credentials"
   $env:AWS_CONFIG_FILE = "$env:USERPROFILE\.aws\emulator\9297\config"
   $env:AWS_CA_BUNDLE = "$env:USERPROFILE\.aws\emulator\9297\ca.pem"
   $env:AWS_EC2_METADATA_DISABLED = "true"
   $env:AWS_DISABLE_HOST_PREFIX_INJECTION = "true"
   $env:AWS_REGION = "us-east-1"
   $env:AWS_DEFAULT_REGION = "us-east-1"
   ```

    `AWS_EC2_METADATA_DISABLED` stops your SDK from asking the Amazon EC2 instance metadata service for credentials. This keeps your SDK from using real credentials when you test on an EC2 instance.

    `AWS_DISABLE_HOST_PREFIX_INJECTION` stops the AWS CLI and the AWS SDK for Python (Boto3) from adding a prefix to the host name of the endpoint. For other SDKs, see [Host names that your SDK changes](#point-sdk-host-names).

   Setting `AWS_CONFIG_FILE` replaces your own AWS config file for that shell. Settings that you keep there, such as retry or Amazon S3 settings, don’t apply while you test against the emulator. The emulator writes its `config` file again each time it starts, so don’t add your settings to it. Instead, copy the file, add your settings to the copy, and set `AWS_CONFIG_FILE` to the copy. If you change the emulator’s port, make the copy again.

   Use one Region for all your requests. To test several Regions, run one emulator for each Region. For more information, see [Limitations](what-is-service.md#what-is-limits).

    `AWS_CA_BUNDLE` makes the AWS CLI, Boto3, and the AWS SDK for Go trust the emulator’s certificate. It also works when the emulator runs in Docker, where the certificate path in `config` is a path in the container.

1. Unset any variables that can supply real AWS credentials. Environment variables take precedence over the credentials file. If you leave them set, your SDK signs requests with your real credentials, and the emulator rejects those requests.

    **macOS and Linux** 

   ```bash
   unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN AWS_PROFILE
   ```

    **Windows PowerShell** 

   ```powershell
   Remove-Item Env:AWS_ACCESS_KEY_ID, Env:AWS_SECRET_ACCESS_KEY, Env:AWS_SESSION_TOKEN, Env:AWS_PROFILE -ErrorAction SilentlyContinue
   ```

1. If your SDK doesn’t read `AWS_CA_BUNDLE`, set the variable for your language from the table in [Trusting the emulator certificate in each SDK](#point-sdk-ca).

1. (Optional) Check that the emulator is ready. The health check returns HTTP 200 with the body `ok`. It uses the same port as the API, over HTTPS.

   ```bash
   curl --cacert ~/.aws/emulator/9297/ca.pem https://127.0.0.1:9297/__admin/health
   ```

   In a script, you can wait for the emulator before you run your tests. The following loop tries once per second, for up to 30 seconds.

   ```bash
   for i in $(seq 30); do
     curl -sf --cacert ~/.aws/emulator/9297/ca.pem https://127.0.0.1:9297/__admin/health && break
     sleep 1
   done
   ```

1. Run your code. Your SDK reads the variables that you set, so your code needs no endpoint or credentials. For example, the following Python code lists the Amazon S3 buckets in the emulator.

   ```python
   import boto3
   
   s3 = boto3.client("s3")
   print(s3.list_buckets()["Buckets"])
   ```

**Important**  
Make sure that your tests send requests to the emulator, not to AWS. If `AWS_ENDPOINT_URL` isn’t set in the shell that runs your tests, your code calls AWS with whatever credentials it finds. Set the variables in the same script that runs your tests, and don’t keep real credentials in the environment of your test jobs.

## Host names that your SDK changes
<a name="point-sdk-host-names"></a>

The emulator serves all services on one endpoint, `https://127.0.0.1:9297`. For some requests, your SDK changes the host name of the endpoint before it sends the request. A request that goes to a different host name doesn’t reach the emulator.
+  **Host prefixes** – For some operations, the SDK adds a prefix to the host name. For example, it adds `data-` for AWS Cloud Map `DiscoverInstances`, `sync-` for AWS Step Functions `StartSyncExecution`, and `stream-` for Amazon CloudWatch Logs `StartLiveTail`. The request then goes to a host such as `data-127.0.0.1`, which doesn’t exist. To prevent this, turn off host prefix injection in your SDK, as shown in the following table.
+  **Amazon S3** – The endpoint is an IP address. So your SDK puts the bucket name in the path of each Amazon S3 request, not in the host name. The emulator doesn’t accept requests that put the bucket name in the host name. Keep `127.0.0.1` in `AWS_ENDPOINT_URL`. If you use `localhost` instead, the AWS SDKs for JavaScript, Java, and Go put the bucket name in the host name by default.
+  **Amazon S3 Control** – Your SDK always puts your account ID in the host name of an Amazon S3 Control request, such as `000000000000.127.0.0.1`. You can’t turn this off, so Amazon S3 Control requests don’t reach the emulator.


| SDK | How to turn off host prefix injection | 
| --- | --- | 
|  AWS CLI | Set `AWS_DISABLE_HOST_PREFIX_INJECTION` to `true`. | 
|  AWS SDK for Python (Boto3) | Set `AWS_DISABLE_HOST_PREFIX_INJECTION` to `true`, or create the client with `Config(inject_host_prefix=False)`. | 
|  AWS SDK for JavaScript v3 | Create the client with `disableHostPrefix: true`. | 
|  AWS SDK for Java 2.x | Set `SdkAdvancedClientOption.DISABLE_HOST_PREFIX_INJECTION` to `true` in the client override configuration. | 

Set `AWS_DISABLE_HOST_PREFIX_INJECTION` only in the shell where you use the emulator. On AWS, operations that use a host prefix fail when the variable is set. For example, Cloud Map `DiscoverInstances` returns `UnknownOperationException`.

The following example uses the AWS CLI to find the instances of a Cloud Map service. Without `AWS_DISABLE_HOST_PREFIX_INJECTION`, the AWS CLI sends the request to `data-127.0.0.1`, and the request fails.

```
$ aws servicediscovery discover-instances --namespace-name my-namespace --service-name my-service
Could not connect to the endpoint URL: "https://data-127.0.0.1:9297/"
```

With `AWS_DISABLE_HOST_PREFIX_INJECTION` set to `true`, the request reaches the emulator, and the emulator returns the instances that you registered.

```
$ export AWS_DISABLE_HOST_PREFIX_INJECTION=true
$ aws servicediscovery discover-instances --namespace-name my-namespace --service-name my-service \
    --query 'Instances[].{InstanceId: InstanceId, Attributes: Attributes}'
[
    {
        "InstanceId": "my-instance",
        "Attributes": {
            "AWS_INSTANCE_IPV4": "10.0.0.1"
        }
    }
]
```

## To check that you’re using the emulator
<a name="point-sdk-verify"></a>

To confirm that your shell sends requests to the emulator, run the following command.

```bash
aws sts get-caller-identity
```

The emulator uses one account, `000000000000`. If you reach the emulator, the output shows `Account` as `000000000000` and `Arn` as `arn:aws:iam::000000000000:user/emulator`. If you see your own account ID, your requests go to AWS. Check the variables in [To point your SDK at a local emulator](#point-sdk-env).

## Trusting the emulator certificate in each SDK
<a name="point-sdk-ca"></a>

The emulator serves HTTPS with its own certificate. The AWS CLI and some SDKs read the certificate from `AWS_CA_BUNDLE`, which you set in [To point your SDK at a local emulator](#point-sdk-env). Others need an extra setting. The following table lists the setting for each client.


| Client | Extra setting for HTTPS | 
| --- | --- | 
|  AWS CLI version 2 | None. Reads `AWS_CA_BUNDLE`. | 
|  AWS SDK for Python (Boto3) | None. Reads `AWS_CA_BUNDLE`. | 
|  AWS SDK for Go v2 | None. Reads `AWS_CA_BUNDLE`. | 
|  AWS SDK for JavaScript v3 (Node.js) |  `NODE_EXTRA_CA_CERTS` set to the path of `ca.pem`, for example `~/.aws/emulator/9297/ca.pem`  | 
|  AWS SDK for Java 2.x |  `JAVA_TOOL_OPTIONS` set to use the emulator’s `truststore.p12`. For more information, see [To trust the emulator certificate in Java](#point-sdk-ca-java). | 
|  AWS SDK for Rust |  `SSL_CERT_FILE` set to the path of `ca.pem`, for example `~/.aws/emulator/9297/ca.pem`  | 
|  AWS SDK for .NET |  `SSL_CERT_FILE` set to the path of `ca.pem`, for example `~/.aws/emulator/9297/ca.pem`  | 

The emulator creates a new certificate each time it starts. Settings that point to the path of `ca.pem` or `truststore.p12` keep working. If you copy or import the certificate, repeat that step after each start.

On Windows, you might need to import `ca.pem` into the Windows certificate store, depending on your SDK.

If your code must also reach other HTTPS servers, including AWS, see [Reaching the emulator and other HTTPS servers from one process](#point-sdk-ca-both).

### To trust the emulator certificate in Java
<a name="point-sdk-ca-java"></a>

Java doesn’t read `ca.pem`. Instead, the emulator writes the same certificate to `truststore.p12`, a PKCS12 trust store without a password, in the same folder as `ca.pem`. To use it, point the Java virtual machine (JVM) at it. For example, set `JAVA_TOOL_OPTIONS` in the shell that runs your tests. If you use a port other than 9297, replace `9297` in the path.

 **macOS and Linux** 

```bash
export JAVA_TOOL_OPTIONS="-Djavax.net.ssl.trustStore=$HOME/.aws/emulator/9297/truststore.p12 -Djavax.net.ssl.trustStoreType=PKCS12"
```

 **Windows PowerShell** 

```powershell
$env:JAVA_TOOL_OPTIONS = "-Djavax.net.ssl.trustStore=$env:USERPROFILE\.aws\emulator\9297\truststore.p12 -Djavax.net.ssl.trustStoreType=PKCS12"
```

Every JVM that you start from that shell reads `JAVA_TOOL_OPTIONS`, including build tools such as Gradle and Maven. To limit the setting to your tests, pass the same options to the test JVM only. For example, use `jvmArgs` in a Gradle `test` task, or `argLine` in the Maven Surefire plugin.

This trust store replaces the JVM’s default trust store, so calls to other HTTPS servers, including AWS, fail with `PKIX path building failed`. To reach both, see [Reaching the emulator and other HTTPS servers from one process](#point-sdk-ca-both).

### Reaching the emulator and other HTTPS servers from one process
<a name="point-sdk-ca-both"></a>

Most of the settings in [Trusting the emulator certificate in each SDK](#point-sdk-ca) replace the certificates that your code trusts by default, so your code then trusts only the emulator. This applies to `ca_bundle`, `AWS_CA_BUNDLE`, `SSL_CERT_FILE`, and the Java trust store. `NODE_EXTRA_CA_CERTS` in Node.js is the exception. It adds `ca.pem` to the certificates that Node.js trusts by default.

If your code must reach the emulator and other HTTPS servers, including AWS, from the same process, add `ca.pem` to the certificates that your code already trusts. For example, use a certificate bundle that contains your system’s certificates and `ca.pem`, or a copy of your Java Development Kit (JDK) trust store that also contains `ca.pem`. The emulator creates a new certificate each time it starts, so update the trust store after each start.