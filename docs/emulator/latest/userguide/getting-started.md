

# Getting started with AWS Emulator
<a name="getting-started"></a>

You can get started with AWS Emulator in four ways. Choose the path that fits how you work, your operating system, and how you test:
+  **With an AI coding agent** – Install the `aws-emulator` skill, and ask your agent to install, start, and connect the emulator for you. You need an AI coding agent and the AWS CLI version 2.35.0 or later. For more information, see [Getting started with an AI coding agent](getting-started-agent.md).
+  **Linux package** – Install the emulator from an RPM or Debian package and run it as a local process. Use this path on Linux. For more information, see [Getting started on Linux](getting-started-linux.md).
+  **Docker** – Build a container image that installs the emulator, and run it as a local container. Use this path on Windows and macOS, or on Linux when you prefer containers. For more information, see [Getting started with Docker](getting-started-docker.md).
+  **Embedded mode** – Run the emulator inside your Rust test process. Use this path when you want per-test isolated state and parallelism. For more information, see [Getting started with embedded mode](getting-started-embedded.md).

The Linux and Docker paths start a local process that listens for HTTPS requests on port 9297 of `127.0.0.1`. You point the AWS CLI or your AWS SDK at that endpoint by setting environment variables. For more information, see [Pointing your AWS SDK at AWS Emulator](point-sdk-to-emulator.md).

Before you begin, complete the prerequisites in [Setting up AWS Emulator](setting-up.md).

**Topics**
+ [Setting up](setting-up.md)
+ [With an AI coding agent](getting-started-agent.md)
+ [Linux](getting-started-linux.md)
+ [Docker](getting-started-docker.md)
+ [Embedded mode](getting-started-embedded.md)
+ [Point your SDK at the emulator](point-sdk-to-emulator.md)
+ [Checking your project](check-project.md)