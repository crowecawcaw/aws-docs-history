

# Getting started with embedded mode

Embedded mode runs the emulator in the same process as your tests. Each test gets its own emulator and its own data. This lets you run tests in parallel. Your code calls the emulator directly, not over the network. You don’t set an endpoint URL or a certificate.

Embedded mode works with the AWS SDK for Rust. Telemetry is on by default in embedded mode, as it is when the emulator runs on its own. To turn it off, see [Telemetry in AWS Emulator](telemetry.md).

## To add AWS Emulator to a Rust project
<a name="getting-started-embedded-add"></a>

Add the `aws-emulator-embedded` crate to the `[dev-dependencies]` section of your `Cargo.toml` file. This keeps the emulator out of the binary that you ship. You get the crate from GitHub. In the following example, `[dependencies]` holds the AWS SDK that your code uses. `[dev-dependencies]` adds the emulator.

```toml
[dependencies]
aws-config = "1"
aws-sdk-s3 = "1"

[dev-dependencies]
aws-emulator-embedded = { git = "https://github.com/aws/aws-emulator", rev = "<commit>" }
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
```

Replace `<commit>` with the commit of the release that you want to use. Each release on the [AWS Emulator releases page on GitHub](https://github.com/aws/aws-emulator/releases) names its commit. Pin to a commit rather than a tag, because a commit can’t move. For more information about versions, see [Versions and compatibility in AWS Emulator](versioning.md).

## To use embedded mode in a test
<a name="getting-started-embedded-use"></a>

1. Create an `AwsEmulatorEmbedded` object with `AwsEmulatorEmbedded::new(EmbeddedOptions::default())`. You can also call `AwsEmulatorEmbedded::default()`, which does the same thing.

1. When you build your SDK configuration, pass `emulator.http_client()` to `.http_client()`.

1. Set the Region to `us-east-1`, and pass `emulator.aws_credentials_provider()` to `.credentials_provider()`.

1. Create a service client from that configuration, and run your test.

Set the Region and the credentials provider as shown. If you leave them out, the SDK looks for them in your environment. If it doesn’t find them, your test fails.

The following example creates an Amazon S3 bucket, writes an object, and reads it back.

```rust
use aws_emulator_embedded::{AwsEmulatorEmbedded, EmbeddedOptions};
use aws_sdk_s3::primitives::ByteStream;

#[tokio::test]
async fn put_then_get_returns_the_body() {
    // Start an emulator for this test only. Its state is not shared with other tests.
    let emulator = AwsEmulatorEmbedded::new(EmbeddedOptions::default());

    // Send SDK requests to the emulator instead of to AWS.
    let config = aws_config::defaults(aws_config::BehaviorVersion::latest())
        .http_client(emulator.http_client())
        .region(aws_config::Region::new("us-east-1"))
        .credentials_provider(emulator.aws_credentials_provider())
        .load()
        .await;

    let s3 = aws_sdk_s3::Client::new(&config);

    // Use the client as you would against AWS.
    s3.create_bucket().bucket("emulator-demo-bucket").send().await.unwrap();
    s3.put_object()
        .bucket("emulator-demo-bucket")
        .key("k")
        .body(ByteStream::from_static(b"hi"))
        .send()
        .await
        .unwrap();

    let got = s3.get_object().bucket("emulator-demo-bucket").key("k").send().await.unwrap();
    assert_eq!(got.body.collect().await.unwrap().to_vec(), b"hi");
}
```

Each emulator that you create has its own state. All clients that you build from one emulator share its state. Two emulators never share state.

## To turn on authentication in embedded mode
<a name="getting-started-embedded-auth"></a>

Authentication is off by default in embedded mode. The emulator serves any request, signed or not. The credentials provider gives the SDK placeholder keys.

To make the emulator check signatures, set `Authentication::On` in `EmbeddedOptions`. Then API requests must be signed with the emulator’s credentials, or with access keys that you create in the emulator through IAM or AWS STS. Operations that AWS serves without a signature don’t need one. The emulator rejects other requests. In embedded mode, the emulator doesn’t write a credentials file.

```rust
use aws_emulator_embedded::{Authentication, AwsEmulatorEmbedded, EmbeddedOptions};

let emulator = AwsEmulatorEmbedded::new(
    EmbeddedOptions::default().authentication(Authentication::On),
);
```

Keep passing `emulator.aws_credentials_provider()` to your SDK configuration. With authentication on, the provider supplies the emulator’s credentials, and the SDK signs requests with them.