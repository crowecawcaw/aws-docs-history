

# Step 3: Containerize
<a name="transform-containers-step-containerize"></a>

In this step, the AWS Transform AI agent analyzes your application source code and generates Docker artifacts. AWS Transform examines your application's structure, dependencies, and runtime requirements to produce appropriate Dockerfiles and related configuration files.

## What happens during containerization
<a name="transform-containers-containerize-process"></a>

The containerization agent performs the following tasks:

1. **Source code analysis** — AWS Transform examines your application's project files, dependencies, build configuration, and runtime requirements. AWS Transform also replaces hardcoded values (such as database IP addresses or DNS names), identifies environment variables, detects volumes, and attempts to redirect logs to standard output.

1. **Dockerfile generation** — Based on the analysis, AWS Transform generates a Dockerfile tailored to your application.

1. **Container image build and test** — AWS Transform builds the container image and runs a test to verify that the Dockerfile produces a working image. If the build fails, AWS Transform iterates on the Dockerfile automatically.

1. **Security analysis** — AWS Transform scans the generated artifacts for hardcoded values such as credentials, API keys, or other sensitive data, and flags any findings for your review.

If you provided multiple repositories or a monorepo with multiple services, the processes each service in parallel.

## Supported application types
<a name="transform-containers-containerize-supported"></a>

AWS Transform supports containerizing the following application types:
+ **.NET 7 and later** — Optimized containerization for .NET applications running on version 7 or later.
+ **General applications** — Containerization for applications built with any language or framework, including Java, Python, Node.js, Go, and others.
+ **Unsupported applications** — Windows, Xcode, or any proprietary build environments are not supported.

## What you need to do
<a name="transform-containers-containerize-user-actions"></a>

This step runs automatically. AWS Transform displays progress updates as it analyzes and containerizes each application. If AWS Transform encounters issues, it may ask you for clarification or additional information.

When containerization is complete, AWS Transform moves to the next step where you review the generated artifacts. The outputs are saved in the Artifact Store.