# LSOPS10-BP01 Reproducibility

Build technology products with infrastructure as code so you can
rebuild them if needed. In archive documents, store the structure of
your products. Store data in a format that is simple to archive,
such as Iceberg.

**Desired outcome:** Maintain a
history of changes made in the IT environment and methods to
programmatically create environments when needed.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:** In addition to being ready to close at project
conclusion, this practice eases movement from test to production and
verifies that testing is performed on the exact architecture that
will be deployed. Additionally, it becomes more straightforward to
reproduce the environment in the event that certain components are
needed after project conclusion.

## Implementation guidance

Establish a robust infrastructure as code framework using
industry-standard tools and practices. This foundation fosters
consistent, repeatable deployments while maintaining complete
version control and documentation.

Implement comprehensive documentation practices that automatically
capture infrastructure configurations, dependencies, and changes.
This system should integrate with version control and provide
clear rebuild instructions.

Establish structured change control procedures that maintain
infrastructure stability while enabling necessary updates. This
process should include proper documentation, testing, and approval
workflows.

### Implementation steps

1. Create an infrastructure as code foundation:

- Establish version-controlled repository for infrastructure
  code and configurations.
- Implement automated CI/CD pipelines for infrastructure
  deployment using AWS CodeBuild.
- Create standardized templates for common infrastructure
  components. Consider AWS CloudFormation and StackSets.

1. Develop a documentation framework:

- Develop comprehensive documentation covering the
  infrastructure components.
- Create automated documentation generation for code and
  configurations. Consider Amazon Q.

1. Implement archive management:

- Implement versioned archive system for infrastructure code.
  Amazon S3 Versioning can be used to retain multiple versions
  of documents.
- Create automated backup procedures for configuration files
  using AWS Backup. Establish a clear tagging system for
  archived components.

## Resources

**Related documents::**

- [Best
  Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md")

**Related examples:**

- [Generating
  documentation with Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/doc-generation.md "../../../amazonq/latest/qdeveloper-ug/doc-generation.md")

**Related tools:**

- [Amazon Q](https://aws.amazon.com/q/ "https://aws.amazon.com/q/")
- [Amazon S3 Versioning](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md")
- [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/")
- [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/")
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") (with drift detection)
