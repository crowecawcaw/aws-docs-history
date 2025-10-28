# MLOE-04: Establish ML roles and responsibilities

Understand the roles, responsibilities, ownership, and required
interactions across teams to maximize overall effectiveness. An
ML project typically consists of multiple roles, with defined
tasks and responsibilities for each. In many cases, the
separation of roles and responsibilities is not clear and there
is overlap.

## Implementation plan

- **Establish cross-functional teams
  with roles and responsibilities** - Enterprises
  often struggle getting started with their first
  enterprise-grade ML platform. This is partly due to the ML
  platform architecture having many components. Complexities
  around data science, data management, and model and
  operational governance also contribute to this struggle.
  Building an enterprise ML platform requires the
  collaboration of different cross-functional teams. The
  different personas from the different teams should each have
  a different role and responsibilities. They all should
  contribute in the build-out, usage, and operation of an ML
  platform.
  [Structure
  your ML organization to support your defined business outcomes](../framework/ops-02.md "../framework/ops-02.md"). Examples of ML technical roles and
  responsibilities with their definitions include:
  - **Domain expert** - Has
    valuable functional knowledge and understanding of the
    environment that the ML problem must be framed in.
    Helps ML engineers and data scientists with developing
    and validating assumptions and hypotheses. Engages
    early in the ML lifecycle and stays in close contact
    with the engineering owners throughout the evaluation
    phase.
  - **Data engineer** -
    Transforms data into a consumable format for machine
    learning and data science analysis.
  - **Data scientist** -
    Employs machine learning, statistical modeling, and
    artificial intelligence to derive insights from the
    data.
  - **ML engineer** - Turns
    reference implementations of ML models developed by
    data scientists into production-ready software.
  - **MLOps engineer** -
    Builds and manages automation pipelines to
    operationalize the ML platform and ML pipelines for
    fully or partially automated CI/CD pipelines. These
    pipelines automate building Docker images, model
    training, and model deployment. MLOps engineers also
    have a role in overall platform governance such as
    data and model lineage, as well as infrastructure and
    model monitoring.
  - **IT auditor** -
    Responsible for analyzing system access activities,
    identifying anomalies and violations, preparing audit
    reports for audit findings, and recommending
    remediations.
  - **Model risk manager**
  * Responsible for ensuring machine learning models
    meet various external and internal control
    requirements. These requirements include: model
    inventory, model explainability, model performance
    monitoring, and model lifecycle management.
  - **Cloud security
    engineer** - Responsible for creating,
    configuring, and managing the cloud accounts, and the
    resources in the accounts. Works with other security
    functions, such as identity and access management, to
    set up the required users, roles, and policies to
    grant users and services permissions to perform
    various operations in the cloud accounts. On the
    governance front, cloud security engineer implements
    governance controls such as resource tagging, audit
    trail, and other preventive and detective controls to
    meet both internal requirements and external
    regulations.

- **Enable easy mechanisms to control
  access and grant permissions for various ML
  roles** – Appropriate user access controls are
  essential for governance; they enable practitioners to
  access the tools they need to do their jobs, while
  ensuring data privacy and security.
  - Avoid the use of one-time methods for managing access
    policies for large teams which contain multiple roles
    for performing various ML activities, such as data
    preparation, training, and model monitoring.
  - Use Amazon SageMaker AI Role Manager to make it easier
    for administrators to control access and define
    permissions for users. Administrators can select and
    edit prebuilt templates based on various user roles
    and responsibilities. The tool then automatically
    creates the access policies with the necessary
    permissions within minutes, reducing the time and
    effort to onboard and manage users over time.

## Documents

- [Personas
  for an ML platform](../../../whitepapers/latest/build-secure-enterprise-ml-platform/personas-for-an-ml-platform.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/personas-for-an-ml-platform.md")
- [AWS MLOps Framework](https://aws.amazon.com/solutions/implementations/aws-mlops-framework/ "https://aws.amazon.com/solutions/implementations/aws-mlops-framework/")
- [Why
  should you use MLOps?](../../../sagemaker/latest/dg/sagemaker-projects-why.md "../../../sagemaker/latest/dg/sagemaker-projects-why.md")
- [Amazon SageMaker AI Role Manager](../../../sagemaker/latest/dg/role-manager.md "../../../sagemaker/latest/dg/role-manager.md")

## Blogs

- [Architecting
  Persona-centric Data Platform with on-premises Data Sources](https://aws.amazon.com/blogs/architecture/architecting-persona-centric-data-platform-with-on-premises-data-sources/ "https://aws.amazon.com/blogs/architecture/architecting-persona-centric-data-platform-with-on-premises-data-sources/")
- [Define
  customized permissions in minutes with Amazon SageMaker AI Role Manager](https://aws.amazon.com/blogs/machine-learning/define-customized-permissions-in-minutes-with-amazon-sagemaker-role-manager/ "https://aws.amazon.com/blogs/machine-learning/define-customized-permissions-in-minutes-with-amazon-sagemaker-role-manager/")
- [New
  ML Governance Tools for Amazon SageMaker AI – Simplify Access Control and Enhance Transparency Over Your ML Projects](https://aws.amazon.com/blogs/aws/new-ml-governance-tools-for-amazon-sagemaker-simplify-access-control-and-enhance-transparency-over-your-ml-projects/ "https://aws.amazon.com/blogs/aws/new-ml-governance-tools-for-amazon-sagemaker-simplify-access-control-and-enhance-transparency-over-your-ml-projects/")
