AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# What is AWS HealthOmics?

AWS HealthOmics is a HIPAA-eligible service that accelerates clinical diagnostic testing, drug discovery,
and agriculture research by fully managing the complex infrastructure behind your bioinformatics workflows.
HealthOmics supports industry-standard workflow languages (WDL, Nextflow, CWL) and seamlessly scales bioinformatics
infrastructure to support data from tens of thousands of tests per day—all with predictable cost per-sample.
HealthOmics handles the technical complexities like managing compute resources and maintaining workflow engines
so you can focus entirely on scientific breakthroughs.

###### Topics

- [Important notice](#important-notice "#important-notice")
- [HealthOmics features](#healthomics-feature-overview "#healthomics-feature-overview")
- [HealthOmics concepts](#concepts "#concepts")
- [Related services](#related-services "#related-services")
- [How to access HealthOmics](#acessing-healthomics "#acessing-healthomics")
- [Regions and endpoints for AWS HealthOmics](#endpoints "#endpoints")
- [Learn more](#healthomics-resources "#healthomics-resources")

## Important notice

HealthOmics is intended only for the transferring, storing, formatting, or displaying of data, and for the
provision of infrastructure and configuration support for managing workflows. HealthOmics isn't a substitute for
professional medical advice, diagnosis, or treatment, and isn't intended to cure, treat, mitigate, prevent, or
diagnose any disease or health condition. You are responsible for instituting human review as part of any use of
AWS HealthOmics, including in association with any third-party product intended to inform clinical
decision-making.

## HealthOmics features

**Primary use cases for HealthOmics:**

- _Clinical diagnostics_ – Build and scale diagnostic
  testing workflows with predictable costs and fully managed infrastructure that grows with your
  testing volume.
- _Drug discovery_ – Accelerate therapeutic research
  by orchestrating biological foundation models at scale, enabling rapid iteration across millions
  of potential candidates.
- _Agricultural research_ – Enhance crop traits like
  drought tolerance and pest resistance through AI-powered workflows that improve food security
  and agricultural productivity.

**Key benefits of HealthOmics:**

- _Scalability_ – Scale workflows across 100,000+
  concurrent vCPUs to support tens of thousands of tests daily with zero infrastructure management
  and predictable cost-per sample.
- _Focus on science, not infrastructure_ – Use
  familiar workflow languages and APIs while AWS automatically handles infrastructure
  orchestration and data management behind the scenes.
- _Maintain compliance_ – Comprehensive audit
  trails, data provenance tracking, and HIPAA-eligible infrastructure designed for clinical
  workflows—all out-of-the-box—support development of solutions that meet regulatory
  requirements.

HealthOmics consists of three main components:

- [HealthOmics
  workflows](private-workflows.md "private-workflows.md") — Run bioinformatics computations on automatically provisioned
  and scaled infrastructure.
- [HealthOmics
  storage](sequence-stores.md "sequence-stores.md") — Store and share petabytes of genomics data efficiently at
  a low cost per gigabase.
- [HealthOmics
  analytics](omics-analytics.md "omics-analytics.md") — Prepare genomics data for multiomics and multimodal analyses.

Use these components independently or combine them for an end-to-end solution.

## HealthOmics concepts

This topic covers definitions for key concepts and terms that are specific to HealthOmics, to help you understand the
terminology of HealthOmics used this guide.

###### Topics

- [Workflows](#workflows-concepts "#workflows-concepts")
- [Storage](#sequence-store-concepts "#sequence-store-concepts")
- [Analytics](#variant-store-concepts "#variant-store-concepts")

### Workflows

With HealthOmics Workflows, you can process and analyze your genomics data.

- _Workflow_ – The overall definition of an end to end
  process including parameters and references to tools. Workflow definitions can be expressed as WDL,
  Nextflow, or CWL. Each created workflow has a unique identifier.
- _Run_ – A single invocation of a workflow.
  An individual run uses your defined input data and produces an output. Each created run has a unique
  identifier.
- _Task_ – The individual processes within a run. HealthOmics
  Workflows use these defined compute specifications to run your task. Each task has a unique identifier.
- _Run group_ – A group of runs for which you can set the
  max vCPU, max duration, or max concurrent runs to help limit the compute resources used per run. You can
  specify and configure priorities for your runs within a run group. For example, you can specify
  that a high priority run will be performed before one that's lower priority, creating a priority queue. It
  is optional to use a Run Group, and each Run Group has a unique identifier.

### Storage

Data storage is separated into sequence stores, for your genomics sequences and
related information, and a reference store, for all of your reference genomes. The
following terms describe the implementations that are specific to HealthOmics.

- _Sequence store_ – A data store for
  the storage of genomics files. You can have one or more sequence stores
  within HealthOmics. Access permissions and AWS KMS encryption can be set on a
  sequence store to control who has access to the data.
- _Read set_ – A read set is an abstraction of genomics
  reads, which are stored in FASTQ, BAM, or CRAM formats. Read sets can be imported into sequence stores and
  annotated with metadata. You can apply permissions to read sets using attribute based access control (ABAC).
- _Reference_ – A genome reference is
  used with reads to identify where in a genome a specific read, or group of
  reads, is mapped to. These are in FASTA format and stored in the reference
  store.
- _Reference store_ – A data store
  for the storage of reference genomes. You can have a single reference store
  in each account and region.

### Analytics

You can transform and analyze your genomics data with HealthOmics Analytics.
Create a variant store or annotation store to include additional information for
your queries.

- _Variant store_ – data store that
  stores variant data at a population scale. Variant stores support both
  genomic Variant Call Format (gVCF) and VCF inputs.
- _Annotation store_ – A data store
  representing an annotation database, such as one from a TSV/CSV, VCF, or
  General Feature Format (GFF3) file. Annotation Stores are mapped to the same
  coordinate system as variant stores during an import.

## Related services

The following services work with HealthOmics.

- Amazon Elastic Container Registry – Each private workflow uses an Amazon ECR image (in a private Amazon ECR repository) to contain
  all executables, libraries, and scripts required to run the workflow.
- Amazon Simple Storage Service – Amazon S3 provides file storage for Store and Workflow data.
- AWS Lake Formation – Lake Formation manages data access to your Analytics data stores.
- Amazon Athena – Use Athena to perform queries on your Variant stores.
- Amazon SageMaker AI – Use SageMaker AI to run HealthOmics tasks using Jupyter notebooks.
- [GitHub connections](../../../codepipeline/latest/userguide/connections-github.md "../../../codepipeline/latest/userguide/connections-github.md")
  – Use connections to connect your external code respoitories to your HealthOmics workflows.

## How to access HealthOmics

You can access AWS HealthOmics features using the management console, CLI, SDKs or API.

- AWS Management Console – Provides a web interface that you can use to access HealthOmics.
- AWS Command Line Interface (AWS CLI) – Provides commands for a broad set of AWS services, including AWS HealthOmics, and is
  supported on Windows, macOS, and Linux. For more information about installing the AWS CLI, see [AWS Command Line Interface](https://aws.amazon.com/cli/ " https://aws.amazon.com/cli/").
- AWS SDKs – AWS provides SDKs (Software Development Kits) that consist of libraries
  and sample code for various programming languages and platforms (including Java, Python, Ruby, .NET,
  iOS, and Android). The SDKs provide a convenient way to use HealthOmics
  programmatically. For more information, see the [AWS SDK Developer Center](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").
- AWS API – You can use API operations to access and manage HealthOmics programmatically. For more
  information, see the [HealthOmics API
  Reference](../api/Welcome.md "../api/Welcome.md").

## Regions and endpoints for AWS HealthOmics

For a full list of regions and endpoints, see the [AWS General Reference](../../../general/latest/gr/healthomics-quotas.md "../../../general/latest/gr/healthomics-quotas.md").

In addition to the AWS regions that are active by default, there are also
_Opt-in Regions_ which need to be activated. To learn more about
how to activate or deactivate a Region, see [Specify which AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone") in the AWS Account
Management guide.

## Learn more

Learn more about HealthOmics from these workshops and tutorials:

- HealthOmics workshop – [HealthOmics end to end workshop](https://catalog.workshops.aws/amazon-omics-end-to-end/en-US "https://catalog.workshops.aws/amazon-omics-end-to-end/en-US")
- AWS genomics resources – [Public Amazon ECR
  repositories](https://gallery.ecr.aws/aws-genomics?page=1 "https://gallery.ecr.aws/aws-genomics?page=1") related to genomics
- Python tutorials – [Jupyter notebook tutorials](https://github.com/aws-samples/amazon-omics-tutorials "https://github.com/aws-samples/amazon-omics-tutorials") on GitHub, covering HealthOmics storage, analytics, and workflows

Become familiar with additional HealthOmics tools that AWS provides:

- WDL linter – [HealthOmics linter for
  WDL](https://gallery.ecr.aws/aws-genomics/healthomics-linter "https://gallery.ecr.aws/aws-genomics/healthomics-linter")
- Nextflow linter – [HealthOmics linter for Nextflow](https://gallery.ecr.aws/aws-genomics/linter-rules-for-nextflow "https://gallery.ecr.aws/aws-genomics/linter-rules-for-nextflow")
- HealthOmics Amazon ECR helper tool – [Amazon ECR helper tool for HealthOmics](https://github.com/aws-samples/amazon-ecr-helper-for-aws-healthomics "https://github.com/aws-samples/amazon-ecr-helper-for-aws-healthomics")
- HealthOmics tools on GitHub – [Tools for working with HealthOmics](https://github.com/awslabs/amazon-omics-tools "https://github.com/awslabs/amazon-omics-tools") (Transfer manager, URI parser, Omics rerun, Run analyzer).
