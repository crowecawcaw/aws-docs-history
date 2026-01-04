# LSREL03-BP02 Implement tiered storage and recovery

strategies

Adopt a tiered approach to storage and retrieval, balancing cost,
durability, and recovery speed. Critical research datasets should be
stored in durable, retrievable formats, while less frequently
accessed archives can be stored in lower-cost, long-term archival
tiers.

**Desired outcome:**

- Cost-effective storage of large volumes of research data.
- Ability to retrieve datasets reliably within regulatory or
  operational timelines.
- Long-term durability and reproducibility for clinical trial and
  research data.

**Common anti-patterns:**

- Treating each dataset equally, leading to unnecessary costs or
  slow recovery.
- Archiving data without defining retrieval timelines or
  compliance-related needs.
- Failing to test retrieval procedures, risking failed restores
  during audits.

**Benefits of establishing this best
practice:**

- Reduces storage costs without sacrificing durability.
- Provides scalable recovery aligned with business and
  compliance-related needs.
- Improved preparation for regulatory audits or re-analysis of
  research and clinical data.
- Supports sustainable scaling of data management as volumes grow
  exponentially.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Classify datasets by criticality, regulatory requirements, and
access frequency. Assign storage tiers accordingly, with active
datasets kept on performant storage and archival datasets
transitioned to lower-cost tiers. Lifecycle automation reduces
human error and improves adherence to retention schedules.
Recovery workflows must be tested periodically to confirm that
timelines can be met during regulatory audits or scientific
reviews.

### Implementation steps

1. Store frequently accessed datasets in Amazon S3 Standard,
   then transition infrequently accessed data to Amazon Glacier Flexible Retrieval or enable Amazon S3
   Intelligent-Tiering.
2. Archive rarely accessed datasets with Amazon Glacier Deep
   Archive for the lowest-cost, long-term retention.
3. Use S3 Lifecycle Policies to automate transitions across
   tiers.
4. Implement recovery workflows using AWS Step Functions to
   orchestrate retrieval steps, and align with regulatory
   timelines and audit needs.

## Resources

**Related best practices:**

- Business continuity planning for research data
- Backup validation and recovery testing
- Risk-based classification of clinical and research datasets
