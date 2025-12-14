# ADVCOST05-BP01 Use cost efficient data types and

configurations for collaborative data environments

Use efficient storage formats and streamlined query configurations to reduce unnecessary data scanning, duplication, and transfer costs in collaborative analytics environments.

## Implementation guidance

- Use parquet or columnar formats with partitioning and compress datasets.
- Use standard SQL for lightweight or well-partitioned datasets.
- Avoid unnecessary cross-joins or full table scans.
- Use same-Region AWS Clean Rooms collaborations to minimize inter-Region transfer costs.

## Key AWS services

- AWS Clean Rooms

## Resources

- [Data
  formats for AWS Clean Rooms](../../../clean-rooms/latest/userguide/data-formats.md "../../../clean-rooms/latest/userguide/data-formats.md")
- [Data Analytics Lens](../analytics-lens/best-practice-10.md "../analytics-lens/best-practice-10.md")
