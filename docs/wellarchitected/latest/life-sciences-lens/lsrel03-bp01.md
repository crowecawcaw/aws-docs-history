# LSREL03-BP01 Digitize and modernize archival of research

data

Replace legacy storage formats such as tapes, optical disks, or
local hard drives with digital storage strategies that provide
redundancy, immutability, and verifiable integrity. Centralized
digital archives keep data accessible, protected from degradation,
and adhere to long-term retention requirements.

**Desired outcome:**

- Research and clinical data remains intact and accessible for
  extended periods.
- Immutable archives block tampering or accidental deletion.
- Metadata supports efficient search and retrieval for audits or
  scientific review.

**Common anti-patterns:**

- Relying on physical tapes or local servers with no periodic
  validation.
- Storing critical data without metadata, making retrieval
  inefficient.
- Keeping data in non-standard formats that hinder long-term
  usability.

**Benefits of establishing this best
practice:**

- Improved durability and accessibility compared to physical
  archives.
- Reduced operational costs and manual overhead of physical
  storage.
- Simplified adherence to regulatory audits through traceable,
  verifiable archives.
- Supports reproducibility by keeping datasets intact and usable
  over decades.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Long-term storage strategies should prioritize immutability and
regulatory alignment. Establish centralized digital archives with
policies that enforce retention and stop premature deletion.
Periodically validate archived datasets with integrity checks and
maintain metadata to verify that datasets are searchable and
contextualized. Migrating legacy media into durable repositories
reduces the risk of data degradation and provides consistent
access across global research teams.

### Implementation steps

1. Digitize and migrate legacy media into Amazon S3 with Object
   Lock to enforce immutability.
2. Use Amazon Glacier Vault Lock to apply retention rules.
3. Migrate large historical datasets efficiently with AWS
   DataSync.
4. Schedule automated integrity checks with Amazon S3 Inventory
   and log validation results into AWS Audit Manager for audit
   tracking.
5. Maintain searchable metadata indexes using Amazon DynamoDB
   or Amazon OpenSearch Service to enable rapid dataset
   retrieval during audits or scientific reviews.

## Resources

**Related best practices:**

- Data integrity validation for regulatory adherence
- Metadata management and data cataloging
- Lifecycle management policies for long-term research data
