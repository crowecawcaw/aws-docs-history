# Research and Engineering Studio support policy

Research and Engineering Studio (RES) supports multiple releases concurrently. RES uses a `YYYY.mm.patch`
version scheme, where `YYYY.mm` represents a major release. `YYYY` represents
the year, `mm` represents the month of release and `patch` indicates an
incremental release. Each RES release has a scheduled End of Support Life (EOSL) date that is the
last day of the `mm` month in year `YYYY`+1. For example, the EOSL date for
2025.09 is September 30, 2026. After the EOSL date, no further support or maintenance is provided for
that release.

New features, performance improvements, security updates, and bug fixes are included in new major
version releases (`YYYY.mm`). For critical issues, AWS provides fixes through patch
releases, but only for releases that have not reached EOSL.

In-place updates are supported only between patch releases within the same major release (for
example, from 2024.04.01 to 2024.04.02). To use updates from a new major RES version, you need to
perform a new installation of that version. To ensure you have access to the latest features and
security updates, we recommend keeping your RES installation up-to-date with the most recent
release.

If you're running a version approaching its end of supported life (EOSL) date, please plan to
upgrade to a newer version to maintain support and access to the latest improvements. For detailed
instructions on upgrading RES, please [refer to our documentation](update-the-product.md "update-the-product.md").
If you have any questions or need assistance with upgrading, please contact AWS Support.

| Research and Engineering Studio version | End of support (EOSL) date |
| --------------------------------------- | -------------------------- |
| 2023.11.x                               | 11/30/2024                 |
| 2024.01.x                               | 1/31/2025                  |
| 2024.04.x                               | 4/30/2025                  |
| 2024.06.x                               | 6/30/2025                  |
| 2024.08.x                               | 8/31/2025                  |
| 2024.10.x                               | 10/31/2025                 |
| 2024.12.x                               | 12/31/2025                 |
| 2025.03.x                               | 3/30/2026                  |
| 2025.06.x                               | 6/30/2026                  |
| 2025.09.x                               | 9/30/2026                  |

###### Important

You are responsible for patching your infra / VDI hosts after deployment.
