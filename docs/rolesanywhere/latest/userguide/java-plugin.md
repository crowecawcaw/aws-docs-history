# Get temporary security credentials with the IAM Roles Anywhere plugin for the AWS SDK for Java

The IAM Roles Anywhere plugin for the AWS SDK for Java integrates IAM Roles Anywhere credential
resolution into any AWS SDK for Java v2 service client. Unlike the standalone
credential helper tool, which runs out of process, the plugin runs in the same
JVM as your application.
The SDK client signs each IAM Roles Anywhere `CreateSession` request with the
supplied X.509 credentials and refreshes the returned session credentials before
they expire. It applies them to subsequent AWS API calls with no additional code.

## Add the plugin as a dependency

The plugin is published to Maven Central under the following coordinates:

Group ID
`software.amazon.rolesanywhere.plugin`

Artifact ID
`roles-anywhere-java`

For the current version, release notes, and signature verification instructions,
see the plugin's page on the
[Maven Central](https://central.sonatype.com/artifact/software.amazon.rolesanywhere.plugin/roles-anywhere-java "https://central.sonatype.com/artifact/software.amazon.rolesanywhere.plugin/roles-anywhere-java")
website and the
[roles-anywhere-java](https://github.com/aws-sdk-plugin/roles-anywhere-java "https://github.com/aws-sdk-plugin/roles-anywhere-java")
repository on the GitHub website.

The plugin targets a minimum Java 8 runtime. The plugin follows its own release
cadence, independent of the AWS SDK for Java. Consult the plugin's release
notes for the SDK versions each release supports.

## Attach the plugin to an SDK client

Add the plugin to any AWS SDK for Java v2 service client builder using
`addPlugin`. The plugin resolves IAM Roles Anywhere credentials using the
trust anchor, profile, and role you configure, and supplies them to the client
for the lifetime of the client.

```

    S3Client s3 = S3Client.builder()
        .addPlugin(RolesAnywherePlugin.builder()
            .trustAnchorArn("arn:aws:rolesanywhere:us-east-1:123456789012:trust-anchor/example")
            .profileArn("arn:aws:rolesanywhere:us-east-1:123456789012:profile/example")
            .roleArn("arn:aws:iam::123456789012:role/example")
            .build())
        .build();

```

The preceding example uses the plugin's default source of X.509 key material.
The plugin also accepts customer-supplied key material through a service
provider interface, so it composes with keys held in a file, in a Java
`KeyStore`, or behind a JCE provider. For the full configuration
surface, the SPI, and worked examples, see the
[plugin README](https://github.com/aws-sdk-plugin/roles-anywhere-java#readme "https://github.com/aws-sdk-plugin/roles-anywhere-java#readme")
on the GitHub website.

## When to use the plugin

Use the plugin when your workload is a Java application on the AWS SDK for
Java v2, and you want IAM Roles Anywhere credentials resolved in process. The plugin
removes the need to spawn a subprocess or configure
`credential_process`.

Instead, see [Get temporary security credentials](credential-helper.md "credential-helper.md")
when your workload is not on the JVM. The credential helper is also the better
choice when you need to share credentials across multiple tools on the same host.
Choose it when you prefer to keep signing key material out of the application
process.
