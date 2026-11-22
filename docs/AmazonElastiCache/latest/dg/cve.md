

# Common Vulnerabilities and Exposures (CVE): Security vulnerabilities addressed in ElastiCache

Common Vulnerabilities and Exposures (CVE) is a list of entries for publicly known cybersecurity vulnerabilities. Each entry is a link that contains an identification number, a description, and at least one public reference. You can find on this page a list of security vulnerabilities that have been addressed in ElastiCache, as well as CVEs that do not affect ElastiCache. 

We recommend that you always upgrade to the latest ElastiCache Valkey, Redis OSS or ElastiCache Memcached versions to be protected against known vulnerabilities. When operating an ElastiCache Serverless Cache, CVE fixes are automatically applied to your cache. When operating node-based clusters with Valkey or Redis OSS, ElastiCache exposes the PATCH component. For example, when using ElastiCache for Redis OSS version 6.2.6, the major version is 6, the minor version is 2, and the patch version is 6. PATCH versions are for backwards-compatible bug fixes, security fixes, and non-functional changes. 

## CVEs addressed in Amazon ElastiCache
<a name="cve-addressed"></a>

The following table lists Common Vulnerabilities and Exposures (CVEs) and the ElastiCache engine versions that address them. In the table, Yes means that the engine version addresses the CVE, and Not applicable means that the CVE does not affect that engine version. If a vulnerability does not have a CVE ID, the table lists its GitHub Security Advisory (GHSA) ID, which links to the advisory on the GitHub website. If your ElastiCache Valkey or Redis OSS cluster is running a version without the security fix, you can either upgrade to a more recent ElastiCache Valkey or Redis OSS version containing the fix, or if you are on a version containing the fix, ensure you have the latest service update applied by referring to [Managing service updates for node-based clusters](Self-Service-Updates.md#managing-updates). For more information about the supported ElastiCache engine versions and how to upgrade, see [Engine versions and upgrading in ElastiCache](engine-versions.md).

**Note**  
An asterisk (\*) in the following table indicates you must have the latest service update applied for the cluster running the version specified in order to address the security vulnerability. For more information about how to verify you have the latest service update applied for the version your cluster is running on, see [Managing service updates for node-based clusters](Self-Service-Updates.md#managing-updates).


| CVE | Valkey 9.1 | Valkey 9.0 | Valkey 8.2 | Valkey 8.1 | Valkey 8.0 | Valkey 7.2 | Redis OSS 7.1 | Redis OSS 7.0 | Redis OSS 6.2 | Redis OSS 6.0 | Redis OSS 5.0 | Redis OSS 4.0 | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| [GHSA-f4q9-j22m-xqq9 on the GitHub website](https://github.com/valkey-io/valkey/security/advisories/GHSA-f4q9-j22m-xqq9)\* | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2026-66373](https://www.cve.org/CVERecord?id=CVE-2026-66373)\* | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Not applicable | 
| [CVE-2026-25589](https://www.cve.org/CVERecord?id=CVE-2026-25589) | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | Not applicable | 
| [CVE-2026-25588](https://www.cve.org/CVERecord?id=CVE-2026-25588) | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | Not applicable | 
| [CVE-2026-25243](https://www.cve.org/CVERecord?id=CVE-2026-25243)\* | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | Not applicable | 
| [CVE-2026-23631](https://www.cve.org/CVERecord?id=CVE-2026-23631) | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | Not applicable | 
| [CVE-2026-23479](https://www.cve.org/CVERecord?id=CVE-2026-23479)\* | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | Not applicable | 
| [CVE-2025-67733](https://www.cve.org/CVERecord?id=CVE-2025-67733)\* | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | Not applicable | Not applicable | 
| [CVE-2025-49844](https://www.cve.org/CVERecord?id=CVE-2025-49844)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2025-49819](https://www.cve.org/CVERecord?id=CVE-2025-49819)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2025-48367](https://www.cve.org/CVERecord?id=CVE-2025-48367)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2025-46844](https://www.cve.org/CVERecord?id=CVE-2025-46844)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2025-46818](https://www.cve.org/CVERecord?id=CVE-2025-46818)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2025-46817](https://www.cve.org/CVERecord?id=CVE-2025-46817)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2025-32023](https://www.cve.org/CVERecord?id=CVE-2025-32023)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2025-27151](https://www.cve.org/CVERecord?id=CVE-2025-27151)\* | Not applicable | Not applicable | Not applicable | Yes | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | 
| [CVE-2025-21605](https://www.cve.org/CVERecord?id=CVE-2025-21605)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2024-46981](https://www.cve.org/CVERecord?id=CVE-2024-46981) | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2024-31449](https://www.cve.org/CVERecord?id=CVE-2024-31449)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2024-31228](https://www.cve.org/CVERecord?id=CVE-2024-31228)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2024-31227](https://www.cve.org/CVERecord?id=CVE-2024-31227)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2023-41056](https://www.cve.org/CVERecord?id=CVE-2023-41056)\* | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | 
| [CVE-2023-28425](https://www.cve.org/CVERecord?id=CVE-2023-28425)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Not applicable | Not applicable | Not applicable | Not applicable | 
| [CVE-2023-25155](https://www.cve.org/CVERecord?id=CVE-2023-25155) | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2023-22458](https://www.cve.org/CVERecord?id=CVE-2023-22458) | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2022-36021](https://www.cve.org/CVERecord?id=CVE-2022-36021)\* | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2022-35977](https://www.cve.org/CVERecord?id=CVE-2022-35977)\* | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2022-35951](https://www.cve.org/CVERecord?id=CVE-2022-35951)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Not applicable | Not applicable | Not applicable | Not applicable | 
| [CVE-2022-31144](https://www.cve.org/CVERecord?id=CVE-2022-31144)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Not applicable | Not applicable | Not applicable | Not applicable | 
| [CVE-2022-24834](https://www.cve.org/CVERecord?id=CVE-2022-24834)\* | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| [CVE-2021-41099](https://www.cve.org/CVERecord?id=CVE-2021-41099)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-32762](https://www.cve.org/CVERecord?id=CVE-2021-32762)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-32761](https://www.cve.org/CVERecord?id=CVE-2021-32761)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-32687](https://www.cve.org/CVERecord?id=CVE-2021-32687)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-32675](https://www.cve.org/CVERecord?id=CVE-2021-32675)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-32672](https://www.cve.org/CVERecord?id=CVE-2021-32672)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-32628](https://www.cve.org/CVERecord?id=CVE-2021-32628)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-32627](https://www.cve.org/CVERecord?id=CVE-2021-32627)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-32626](https://www.cve.org/CVERecord?id=CVE-2021-32626)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-32625](https://www.cve.org/CVERecord?id=CVE-2021-32625)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-29478](https://www.cve.org/CVERecord?id=CVE-2021-29478)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-29477](https://www.cve.org/CVERecord?id=CVE-2021-29477)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 
| [CVE-2021-21309](https://www.cve.org/CVERecord?id=CVE-2021-21309)\* | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Yes | Yes | Yes | Yes | Not applicable | Not applicable | 

## CVEs that do not affect Amazon ElastiCache
<a name="cve-not-affected"></a>

The following CVEs do not affect Amazon ElastiCache for Valkey or Redis OSS.
+ [CVE-2026-21864](https://www.cve.org/CVERecord?id=CVE-2026-21864)
+ [CVE-2026-21863](https://www.cve.org/CVERecord?id=CVE-2026-21863)
+ [CVE-2024-51741](https://www.cve.org/CVERecord?id=CVE-2024-51741)
+ [CVE-2023-45145](https://www.cve.org/CVERecord?id=CVE-2023-45145)
+ [CVE-2023-28856](https://www.cve.org/CVERecord?id=CVE-2023-28856)
+ [CVE-2022-24736](https://www.cve.org/CVERecord?id=CVE-2022-24736)
+ [CVE-2022-24735](https://www.cve.org/CVERecord?id=CVE-2022-24735)