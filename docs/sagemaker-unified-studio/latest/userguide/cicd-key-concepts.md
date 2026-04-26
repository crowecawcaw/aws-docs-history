# Key concept

## Manifest

The manifest file (`manifest.yaml`) is the single source of truth for your application. It declares what resources your application uses, which Amazon SageMaker Unified Studio projects to deploy into, and how configurations differ across stages. Data teams own the manifest. DevOps teams do not need to modify it.

## Stages and targets

Each stage in the manifest (for example, `dev`, `test`, `prod`) maps to a separate Amazon SageMaker Unified Studio project and domain. Stages can span different AWS accounts and Regions. The CLI substitutes stage-specific configurations at deploy time, so the same application definition works across all environments.

## Bundles

A bundle is an immutable, versioned archive produced by reading from a **source target** (typically your development environment). The `bundle` command packages your application code, workflow definitions, and resolved configurations from the source into a self-contained artifact.

The `deploy` command then deploys the bundle contents to a **destination target** (for example, test or production). This separation means:

- **Source → Bundle:** `aws-smus-cicd-cli bundle` reads from your source(dev) project and creates the artifact
- **Bundle → Destination:** `aws-smus-cicd-cli deploy` deploys the artifact into the target project

The same bundle is promoted across stages without rebuilding, supporting immutable artifacts, audit trails, and controlled promotion through quality gates.

## Catalog support

The CLI supports catalog asset management as part of the deployment process. You can define business metadata, including glossaries, glossary terms, assets, and data products, in your manifest. During deployment, the CLI automatically searches for assets in the catalog, creates subscription requests for required access, and waits for subscription approval before proceeding.
