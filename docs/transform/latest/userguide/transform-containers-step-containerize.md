# Step 3: Containerize

In this step, the AWS Transform AI agent analyzes your application source code and
generates Docker artifacts. The agent examines your application's structure,
dependencies, and runtime requirements to produce appropriate Dockerfiles and related
configuration files.

## What happens during containerization

The containerization agent performs the following tasks:

1. **Source code analysis** — The agent examines
   your application's project files, dependencies, build configuration, and runtime requirements.
   The agent also replaces hardcoded value (i.e database ip/dns), identify environment variables,
   detect volumes and attempt to redirect log to the standard output.
2. **Dockerfile generation** — Based on
   the analysis, the agent generates a Dockerfile tailored to your application.
   If an existing Dockerfile is present, the agent can reuse it with
   modifications, or generate a new one based on your preferences.
3. **Container image build and test** —
   The agent builds the container image and runs a test to verify that the
   Dockerfile produces a working image. If the build fails, the agent
   iterates on the Dockerfile automatically.
4. **Security analysis** — The agent
   scans the generated artifacts for hardcoded values such as credentials,
   API keys, or other sensitive data, and flags any findings for your
   review.

If you provided multiple repositories or a monorepo with multiple services, the
agent processes each service in parallel.

## Supported application types

AWS Transform supports containerizing the following application types:

- **.NET 7 and later** — Optimized
  containerization for .NET applications running on version 7 or later.
- **General applications** —
  Containerization for applications built with any language or framework,
  including Java, Python, Node.js, Go, and others.
- **Unsupported applications** —
  Windows, Xcode, or any prorietary build environments are not supported.

## What you need to do

This step runs automatically. The agent displays progress updates as it analyzes
and containerizes each application. If the agent encounters issues, it may ask you
for clarification or additional information.

When containerization is complete, the agent moves to the next step where you
review the generated artifacts. The outputs of the agent are saved in the Artifact Store
