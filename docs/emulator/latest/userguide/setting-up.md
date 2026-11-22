

# Setting up AWS Emulator

Before you start, check the following. The prerequisites depend on how you run the emulator. You don’t need an AWS account to download or run the emulator.
+  **An AWS SDK or the AWS CLI** – You use the emulator through the AWS CLI or an AWS SDK, the same way that you use AWS.
+  **AI coding agent path** – An AI coding agent, such as Kiro, Cursor, or Claude Code, and the AWS CLI version 2.35.0 or later to install the `aws-emulator` skill. For more information, see [Getting started with an AI coding agent](getting-started-agent.md).
+  **Linux package path** – A 64-bit Linux system on x86\_64 or Arm (aarch64) with glibc 2.17 or later, such as Amazon Linux 2 or Amazon Linux 2023. It must be able to install RPM or Debian packages. To check your glibc version, run `ldd --version`. For more information, see [Getting started on Linux](getting-started-linux.md).
+  **Docker path** – Any system that runs Docker, including Windows, macOS, and Linux. On macOS and Windows, use this path. The emulator runs natively only on Linux. For more information, see [Getting started with Docker](getting-started-docker.md).
+  **Embedded mode** – A Rust toolchain with Cargo, a C compiler, and the AWS SDK for Rust. For more information, see [Getting started with embedded mode](getting-started-embedded.md).

## Review the license
<a name="setting-up-license"></a>

The source code is in the [AWS Emulator repository on GitHub](https://github.com/aws/aws-emulator). The source code is under the CC0 1.0 Universal (CC0 1.0) public domain dedication, except the code in the `vendor/` directory, which is under the Apache License 2.0. For the full terms, see the license files in the repository.