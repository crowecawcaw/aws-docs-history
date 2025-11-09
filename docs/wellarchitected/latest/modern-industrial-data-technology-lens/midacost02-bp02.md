# MIDACOST02-BP02 Implement manufacturing-aware resource decommissioning process

Systematically remove unused resources while preserving critical manufacturing data,
maintaining production system integrity, and complying with industrial requirements. This
involves careful consideration of dependencies between manufacturing systems, data retention
requirements, and proper archival procedures before resource removal.

**Desired outcome:** Systematic removal of unused resources
while preserving critical manufacturing data, maintaining production system integrity, and
complying with industrial requirements.

**Common anti-patterns:**

- Decommissioning resources without checking their connection to active production
  lines
- Failing to preserve quality control and compliance data before resource removal
- Not considering seasonal manufacturing patterns when identifying unused resources
- Decommissioning without checking impact on OT or IT integrated systems
- Removing resources without validating manufacturing regulatory requirements
- Failing to archive production performance data and custom configuration settings
  before decommissioning
- Not considering maintenance and repair history requirements

**Benefits of establishing this Best Practice:**

- Reduced costs from unnecessary resource retention
- Minimized risk of accidental data loss
- Clear process for resource retirement
- Compliance with data governance requirements

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Establish formal processes for identifying and safely decommissioning resources in your
manufacturing setup that are no longer needed, while meeting data preservation requirements
and managing dependencies.

### Implementation steps

1. Create decommissioning criteria based on:
   - Resource utilization thresholds
   - Business value assessment
   - Data retention requirements

2. Establish approval workflows.
3. Document dependencies and impact analysis.
4. Create backup and archival procedures.
5. Implement verification steps post-decommissioning.
6. Consider manufacturing-specific decommissioning criteria:
   - Production line changeovers
   - End of product lifecycle
   - Equipment replacement cycles
   - Historical data retention for quality compliance and machine learning

## Key AWS services

- AWS Backup
- Amazon S3 Lifecycle policies
- AWS Organizations
- Amazon CloudWatch
- AWS Glue Data Catalog

## Resources

**Related documents:**

- [Amazon Simple Storage Service: Examples of S3 Lifecycle configurations](../../../AmazonS3/latest/userguide/lifecycle-configuration-examples.md "../../../AmazonS3/latest/userguide/lifecycle-configuration-examples.md")
- [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md")
- [Detecting unusual spend with AWS Cost Anomaly Detection](../../../cost-management/latest/userguide/manage-ad.md "../../../cost-management/latest/userguide/manage-ad.md")
