# Common Vulnerabilities and Exposures (CVE): Security vulnerabilities addressed in MemoryDB

Common Vulnerabilities and Exposures (CVE) is a list of entries for publicly known cybersecurity vulnerabilities.
Each entry is a link that contains an identification number, a description, and at least one public reference.
You can find on this page a list of security vulnerabilities that have been addressed in MemoryDB, as well as CVEs that do not affect MemoryDB.

We recommend that you always upgrade to the latest MemoryDB versions to be protected against known vulnerabilities. MemoryDB exposes the PATCH component. PATCH versions are for backwards-compatible bug fixes, security fixes, and non-functional changes.

## CVEs addressed in MemoryDB

The following table lists CVEs and the MemoryDB engine versions in which they are addressed. A checkmark (✓) indicates the CVE is addressed in that version. N/A indicates the CVE does not affect that engine version.

If your MemoryDB cluster is running a version without the security fix, you can either upgrade to a more recent version containing the fix, or if you are on a version
containing the fix, ensure you have the latest service update applied by referring to [Managing the service updates](managing-updates.md "managing-updates.md").
For more information about the supported MemoryDB engine versions and how to upgrade, see [Engine versions](engine-versions.md "engine-versions.md").

###### Note

An asterisk (\*) in the following table indicates you must have the latest service update applied for the cluster
running the version specified in order to address the security vulnerability.
For more information about how to verify you have the latest service update applied for the version your cluster is running on,
see [Managing the service updates](managing-updates.md "managing-updates.md").

| CVE                                                                                                                   | Valkey 7.3 | Valkey 7.2 | Redis OSS 7.1 | Redis OSS 7.0 | Redis OSS 6.2 |
| --------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- | ------------- | ------------- | ------------- |
| [CVE-2026-66373](https://www.cve.org/CVERecord?id=CVE-2026-66373 "https://www.cve.org/CVERecord?id=CVE-2026-66373")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2026-25589](https://www.cve.org/CVERecord?id=CVE-2026-25589 "https://www.cve.org/CVERecord?id=CVE-2026-25589")   | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2026-25588](https://www.cve.org/CVERecord?id=CVE-2026-25588 "https://www.cve.org/CVERecord?id=CVE-2026-25588")   | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2026-25243](https://www.cve.org/CVERecord?id=CVE-2026-25243 "https://www.cve.org/CVERecord?id=CVE-2026-25243")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2026-23631](https://www.cve.org/CVERecord?id=CVE-2026-23631 "https://www.cve.org/CVERecord?id=CVE-2026-23631")   | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2026-23479](https://www.cve.org/CVERecord?id=CVE-2026-23479 "https://www.cve.org/CVERecord?id=CVE-2026-23479")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2025-49844](https://www.cve.org/CVERecord?id=CVE-2025-49844 "https://www.cve.org/CVERecord?id=CVE-2025-49844")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2025-49819](https://www.cve.org/CVERecord?id=CVE-2025-49819 "https://www.cve.org/CVERecord?id=CVE-2025-49819")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2025-48367](https://www.cve.org/CVERecord?id=CVE-2025-48367 "https://www.cve.org/CVERecord?id=CVE-2025-48367")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2025-46844](https://www.cve.org/CVERecord?id=CVE-2025-46844 "https://www.cve.org/CVERecord?id=CVE-2025-46844")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2025-46818](https://www.cve.org/CVERecord?id=CVE-2025-46818 "https://www.cve.org/CVERecord?id=CVE-2025-46818")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2025-46817](https://www.cve.org/CVERecord?id=CVE-2025-46817 "https://www.cve.org/CVERecord?id=CVE-2025-46817")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2025-32023](https://www.cve.org/CVERecord?id=CVE-2025-32023 "https://www.cve.org/CVERecord?id=CVE-2025-32023")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2025-21605](https://www.cve.org/CVERecord?id=CVE-2025-21605 "https://www.cve.org/CVERecord?id=CVE-2025-21605")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2024-46981](https://www.cve.org/CVERecord?id=CVE-2024-46981 "https://www.cve.org/CVERecord?id=CVE-2024-46981")   | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2024-31449](https://www.cve.org/CVERecord?id=CVE-2024-31449 "https://www.cve.org/CVERecord?id=CVE-2024-31449")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2024-31228](https://www.cve.org/CVERecord?id=CVE-2024-31228 "https://www.cve.org/CVERecord?id=CVE-2024-31228")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2024-31227](https://www.cve.org/CVERecord?id=CVE-2024-31227 "https://www.cve.org/CVERecord?id=CVE-2024-31227")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2023-41056](https://www.cve.org/CVERecord?id=CVE-2023-41056 "https://www.cve.org/CVERecord?id=CVE-2023-41056")\* | ✓          | ✓          | ✓             | N/A           | N/A           |
| [CVE-2023-28425](https://www.cve.org/CVERecord?id=CVE-2023-28425 "https://www.cve.org/CVERecord?id=CVE-2023-28425")\* | N/A        | N/A        | ✓             | ✓             | N/A           |
| [CVE-2023-25155](https://www.cve.org/CVERecord?id=CVE-2023-25155 "https://www.cve.org/CVERecord?id=CVE-2023-25155")   | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2023-22458](https://www.cve.org/CVERecord?id=CVE-2023-22458 "https://www.cve.org/CVERecord?id=CVE-2023-22458")   | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2022-36021](https://www.cve.org/CVERecord?id=CVE-2022-36021 "https://www.cve.org/CVERecord?id=CVE-2022-36021")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2022-35977](https://www.cve.org/CVERecord?id=CVE-2022-35977 "https://www.cve.org/CVERecord?id=CVE-2022-35977")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2022-35951](https://www.cve.org/CVERecord?id=CVE-2022-35951 "https://www.cve.org/CVERecord?id=CVE-2022-35951")\* | N/A        | N/A        | ✓             | ✓             | N/A           |
| [CVE-2022-31144](https://www.cve.org/CVERecord?id=CVE-2022-31144 "https://www.cve.org/CVERecord?id=CVE-2022-31144")\* | N/A        | N/A        | ✓             | ✓             | N/A           |
| [CVE-2022-24834](https://www.cve.org/CVERecord?id=CVE-2022-24834 "https://www.cve.org/CVERecord?id=CVE-2022-24834")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2021-41099](https://www.cve.org/CVERecord?id=CVE-2021-41099 "https://www.cve.org/CVERecord?id=CVE-2021-41099")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2021-32762](https://www.cve.org/CVERecord?id=CVE-2021-32762 "https://www.cve.org/CVERecord?id=CVE-2021-32762")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2021-32761](https://www.cve.org/CVERecord?id=CVE-2021-32761 "https://www.cve.org/CVERecord?id=CVE-2021-32761")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2021-32687](https://www.cve.org/CVERecord?id=CVE-2021-32687 "https://www.cve.org/CVERecord?id=CVE-2021-32687")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2021-32675](https://www.cve.org/CVERecord?id=CVE-2021-32675 "https://www.cve.org/CVERecord?id=CVE-2021-32675")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2021-32672](https://www.cve.org/CVERecord?id=CVE-2021-32672 "https://www.cve.org/CVERecord?id=CVE-2021-32672")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2021-32628](https://www.cve.org/CVERecord?id=CVE-2021-32628 "https://www.cve.org/CVERecord?id=CVE-2021-32628")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2021-32627](https://www.cve.org/CVERecord?id=CVE-2021-32627 "https://www.cve.org/CVERecord?id=CVE-2021-32627")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2021-32626](https://www.cve.org/CVERecord?id=CVE-2021-32626 "https://www.cve.org/CVERecord?id=CVE-2021-32626")\* | ✓          | ✓          | ✓             | ✓             | ✓             |
| [CVE-2021-32625](https://www.cve.org/CVERecord?id=CVE-2021-32625 "https://www.cve.org/CVERecord?id=CVE-2021-32625")\* | N/A        | N/A        | ✓             | ✓             | ✓             |
| [CVE-2021-29478](https://www.cve.org/CVERecord?id=CVE-2021-29478 "https://www.cve.org/CVERecord?id=CVE-2021-29478")\* | N/A        | N/A        | ✓             | ✓             | ✓             |
| [CVE-2021-29477](https://www.cve.org/CVERecord?id=CVE-2021-29477 "https://www.cve.org/CVERecord?id=CVE-2021-29477")\* | N/A        | N/A        | ✓             | ✓             | ✓             |
| [CVE-2021-21309](https://www.cve.org/CVERecord?id=CVE-2021-21309 "https://www.cve.org/CVERecord?id=CVE-2021-21309")\* | N/A        | N/A        | ✓             | ✓             | ✓             |

## CVEs that do not affect MemoryDB

The following CVEs do not affect MemoryDB for Valkey or Redis OSS.

- [CVE-2026-21864](https://www.cve.org/CVERecord?id=CVE-2026-21864 "https://www.cve.org/CVERecord?id=CVE-2026-21864")
- [CVE-2026-21863](https://www.cve.org/CVERecord?id=CVE-2026-21863 "https://www.cve.org/CVERecord?id=CVE-2026-21863")
- [CVE-2024-51741](https://www.cve.org/CVERecord?id=CVE-2024-51741 "https://www.cve.org/CVERecord?id=CVE-2024-51741")
- [CVE-2023-45145](https://www.cve.org/CVERecord?id=CVE-2023-45145 "https://www.cve.org/CVERecord?id=CVE-2023-45145")
- [CVE-2023-28856](https://www.cve.org/CVERecord?id=CVE-2023-28856 "https://www.cve.org/CVERecord?id=CVE-2023-28856")
- [CVE-2022-24736](https://www.cve.org/CVERecord?id=CVE-2022-24736 "https://www.cve.org/CVERecord?id=CVE-2022-24736")
- [CVE-2022-24735](https://www.cve.org/CVERecord?id=CVE-2022-24735 "https://www.cve.org/CVERecord?id=CVE-2022-24735")
