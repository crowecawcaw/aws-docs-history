

# Amazon Inspector Security Research
<a name="security-research"></a>

 Amazon Inspector Security Research is a continuous monitoring program that identifies malicious packages published to public package registries. Software supply chain attacks targeting open-source ecosystems are a growing threat, and malicious packages are frequently removed from upstream registries only after they have been downloaded by unsuspecting developers. Amazon Inspector Security Research helps protect your applications by detecting these packages, publishing advisories, and incorporating this intelligence into Amazon Inspector findings so that workloads consuming a known-malicious package are surfaced automatically. 

 Supported public package registries: 
+ **npm** – the Node.js package registry ([npmjs.com](https://www.npmjs.com))
+ **PyPI** – the Python Package Index ([pypi.org](https://pypi.org))
+ **RubyGems** – the Ruby package registry ([rubygems.org](https://rubygems.org))
+ **crates.io** – the Rust package registry ([crates.io](https://crates.io))

## Research methodology
<a name="research-methodology"></a>

 The Amazon Inspector security research team combines automated detection pipelines with expert analyst review to identify malicious packages across supported registries. Each package that meets the Amazon Inspector criteria for a malicious determination receives an Amazon Inspector advisory with an `IN-MAL` identifier. Amazon Inspector findings use these advisories, so customers are notified when their workloads consume an affected package. No customer action is required to benefit from this research – detections are applied automatically. 

 Amazon Inspector is a contributing partner in the [Open Source Security Foundation (OpenSSF)](https://openssf.org/) [Malicious Packages Repository](https://github.com/ossf/malicious-packages). Amazon Inspector also submits advisories to this open dataset, giving the broader open-source community access to the same threat intelligence that Amazon Inspector uses to protect AWS customers. Advisories that also meet the OpenSSF criteria are published in the repository with a `MAL` identifier, which Amazon Inspector records as an alias of the `IN-MAL` identifier. Advisories that meet only the Amazon Inspector criteria keep the `IN-MAL` identifier alone. Both kinds of advisory are used in Amazon Inspector findings. 

 As of 2026-11-11, Amazon Inspector is credited in 196,691 of the 240,400 records (81.8%) in the OpenSSF Malicious Packages Repository, making it the largest contributor to the dataset. 

## Detection summary
<a name="detection-summary"></a>

 The following tables summarize the advisories issued by Amazon Inspector Security Research across all supported registries. Each package is counted once, whether its advisory has only an `IN-MAL` identifier or both an `IN-MAL` and a `MAL` identifier. Periods are based on the date Amazon Inspector issued the advisory. 

**Note**  
**Last updated:** 2026-11-11 22:04:14 UTC

### Lifetime totals by registry
<a name="lifetime-totals"></a>


| Registry | Lifetime packages identified | 
| --- | --- | 
| npm | 196,132 | 
| PyPI | 609 | 
| RubyGems | 77 | 
| crates.io | 1 | 
| Total | 196,819 | 

### Recent activity by registry
<a name="recent-activity"></a>


| Period | Window (UTC) | npm | PyPI | RubyGems | crates.io | Total | 
| --- | --- | --- | --- | --- | --- | --- | 
| This week | 2026-11-09 .. 2026-11-15 | 2 | 2 | 0 | 1 | 5 | 
| Last week | 2026-11-02 .. 2026-11-08 | 35 | 19 | 9 | 0 | 63 | 
| This month | 2026-11 | 44 | 22 | 10 | 1 | 77 | 
| Last month | 2026-10 | 518 | 148 | 67 | 0 | 733 | 

## Recent malicious package reports
<a name="recent-malicious-packages"></a>

 The following table lists the ten most recent advisories issued by Amazon Inspector Security Research, ordered by the date Amazon Inspector issued the advisory. The advisory ID is the OpenSSF `MAL` identifier when the advisory has one, and the Amazon Inspector `IN-MAL` identifier otherwise. 


| Package name | Advisory ID | Registry | Published date | 
| --- | --- | --- | --- | 
| aurum-pay | MAL-2026-19147 | PyPI | 2026-11-11 | 
| mock-data-sdk | MAL-2026-19143 | npm | 2026-11-10 | 
| lwd-uri-util | MAL-2026-19058 | crates.io | 2026-11-10 | 
| logger-libs | MAL-2026-18778 | PyPI | 2026-11-09 | 
| @ethersphere/bee-js | MAL-2026-18773 | npm | 2026-11-09 | 
| bundyfed | MAL-2026-18770 | PyPI | 2026-11-08 | 
| super-color | MAL-2026-18768 | PyPI | 2026-11-08 | 
| supercolor-tui | MAL-2026-18767 | PyPI | 2026-11-08 | 
| fcefi-wdojs-util | MAL-2026-19142 | npm | 2026-11-08 | 
| rcp-ndcg | MAL-2026-18658 | PyPI | 2026-11-08 | 

## Related resources
<a name="security-research-related-resources"></a>

 The following AWS Security Blog posts provide additional context on Amazon Inspector Security Research and recent supply chain threat campaigns: 
+  [Amazon identifies North Korean hacker group behind open-source supply chain attacks](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/) 
+  [Amazon Inspector detects over 150,000 malicious packages linked to token farming campaign](https://aws.amazon.com/blogs/security/amazon-inspector-detects-over-150000-malicious-packages-linked-to-token-farming-campaign/) 
+  [Defending against supply chain attacks like Chalk/Debug and the Shai-Hulud worm](https://aws.amazon.com/blogs/security/defending-against-supply-chain-attacks-like-chalk-debug-and-the-shai-hulud-worm/) 
+  [What AWS Security learned from responding to recent npm supply chain threat campaigns](https://aws.amazon.com/blogs/security/what-aws-security-learned-from-responding-to-recent-npm-supply-chain-threat-campaigns/) 