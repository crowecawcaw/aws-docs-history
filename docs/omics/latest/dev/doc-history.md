

# Document history for the HealthOmics User Guide
<a name="doc-history"></a>

The following table describes the documentation releases for HealthOmics.

| Change | Description | Date | 
| --- |--- |--- |
| [New Feature](#doc-history) | HealthOmics added support for Nextflow profiles from API, which lets you select environment-specific configuration at runtime using the `engineSettings` parameter. To learn more, see [Use Nextflow profiles](https://docs.aws.amazon.com/omics/latest/dev/workflow-definition-nextflow.html#nextflow-profiles). | June 1, 2026 | 
| [New Feature](#doc-history) | HealthOmics added support for batch runs, which let you submit up to 100,000 workflow runs in a single API request. To learn more, see [Batch runs in HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflows-batch.html). | March 20, 2026 | 
| [AWS HealthOmics variant stores and annotation stores are no longer open to new customers.](#doc-history) | AWS HealthOmics variant stores and annotation stores are no longer open to new customers. For more information, see [AWS HealthOmics variant store and annotation store availability change](https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html). | November 7, 2025 | 
| [AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting November 7th, 2025.](#doc-history) | AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting November 7th, 2025. If you would like to use variant stores or annotation stores, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS HealthOmics variant store and annotation store availability change](https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html). | October 7, 2025 | 
| [New Features](#doc-history) | HealthOmics added support for workflows to synchronize a private Amazon ECR repository with an upstream registry. To learn more, see [Container images for private workflows in HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html). | August 28, 2025 | 
| [New README and repository integration features](#doc-history) | Added support for creating workflows from [external code repositories](https://docs.aws.amazon.com/omics/latest/dev/setting-up-omics-repository.html) and [README files](https://docs.aws.amazon.com/omics/latest/dev/workflows-readme.html). | July 24, 2025 | 
| [New Features](#doc-history) | HealthOmics added support for Nextflow automatic parameter interpolation. To learn more, see [Parameter template files for HealthOmics workflows](https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html). | June 27, 2025 | 
| [New Features](#doc-history) | HealthOmics added support for workflows to interpolate the run parameters from a WDL workflow definition file. To learn more, see [Parameter template files for HealthOmics workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html). | May 30, 2025 | 
| [New Features](#doc-history) | HealthOmics added support for workflow versioning. To learn more, see [Workflow versioning in HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html). | April 18, 2025 | 
| [New Features](#doc-history) | HealthOmics added elastic throughput for dynamic run storage. To learn more, see [Run storage types in HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html). | April 16, 2025 | 
| [New Features](#doc-history) | HealthOmics added attribute based access controls for Sequence Store S3 locations, and the abilty to synchronize up to five read-set tags to a Sequence Store S3 object. To learn more, see [Creating a HealthOmics sequence store](https://docs.aws.amazon.com/omics/latest/dev/create-sequence-store.html). | November 22, 2024 | 
| [New Features](#doc-history) | HealthOmics added support for call caching, also known as resume, for private workflows. To learn more, see [ Call caching](https://docs.aws.amazon.com/omics/latest/dev/workflows-call-caching.html). | November 20, 2024 | 
| [New Features](#doc-history) | HealthOmics added new API fields to help you map between sequence store input jobs and read sets.  | August 29, 2024 | 
| [New Features](#doc-history) | HealthOmics added support for managing Nextflow versions. To learn more, see [ Nextflow versions](https://docs.aws.amazon.com/omics/latest/dev/workflows-lang-versions.html#workflows-lang-versions-nextflow). | August 14, 2024 | 
| [New Features](#doc-history) | HealthOmics added support for shared workflows and dynamic run storage. | April 30, 2024 | 
| [New Features](#doc-history) | HealthOmics added support for Amazon S3 access to reference and sequence stores, and support for SHA256 ETags. | April 15, 2024 | 
| [New Features](#doc-history) | HealthOmics added entity tags (ETags) for sequence stores. | October 6, 2023 | 
| [New Features](#doc-history) | HealthOmics added annotation store versioning and analytic store sharing. | August 15, 2023 | 
| [New Features](#doc-history) | HealthOmics added Common Workflow Language (CWL) as a supported language for HealthOmics workflows. | June 30, 2023 | 
| [New Features](#doc-history) | HealthOmics added new Ready2Run workflows, GPU support for workflows, data parsing for annotation stores, direct upload into HealthOmics storage, and integration with EventBridge. | May 15, 2023 | 
| [New managed policy](#doc-history) | HealthOmics added a new managed policy that provides full access. To learn more, see [AWS managed policies](https://docs.aws.amazon.com/omics/latest/dev/security-iam-awsmanpol.html?icmpid=docs_omics_rss). | February 23, 2023 | 
| [New managed policy](#doc-history) | HealthOmics added a new managed policy that limits access to read only. To learn more, see [AWS managed policies](https://docs.aws.amazon.com/omics/latest/dev/security-iam-awsmanpol.html?icmpid=docs_omics_rss). | November 29, 2022 | 
| [Initial release](#doc-history) | Initial release of the HealthOmics User Guide | November 29, 2022 | 