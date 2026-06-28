# Amazon Inspector Security Research

Amazon Inspector Security Research is a continuous monitoring program that identifies malicious packages published to public package registries. Software supply chain attacks targeting open-source ecosystems are a growing threat, and malicious packages are frequently removed from upstream registries only after they have been downloaded by unsuspecting developers. Amazon Inspector Security Research helps protect your applications by detecting these packages, publishing advisories, and incorporating this intelligence into Amazon Inspector findings so that workloads consuming a known-malicious package are surfaced automatically.

Supported public package registries:

- **NPM** – the Node.js package registry ([npmjs.com](https://www.npmjs.com "https://www.npmjs.com"))
- **PyPI** – the Python Package Index ([pypi.org](https://pypi.org "https://pypi.org"))

## Research methodology

The Amazon Inspector security research team combines automated detection pipelines with expert analyst review to identify malicious packages across supported registries. Each confirmed malicious package is assigned a MAL-ID, documented as a public advisory, and integrated into Amazon Inspector findings so that customers are notified when their workloads consume affected packages. No customer action is required to benefit from this research – detections are applied automatically.

Amazon Inspector is a contributing partner in the [Open Source Security Foundation (OpenSSF)](https://openssf.org/ "https://openssf.org/") [Malicious Packages Repository](https://github.com/ossf/malicious-packages "https://github.com/ossf/malicious-packages"). Advisories produced by Amazon Inspector Security Research are published to this open dataset, giving the broader open-source community access to the same threat intelligence that Amazon Inspector uses to protect AWS customers. The MAL-ID assigned to each advisory is compatible with the OpenSSF advisory format.

## Detection summary

The following tables summarize malicious package detections by Amazon Inspector Security Research across all supported registries.

###### Note

**Last updated:** 2026-05-13 21:00:00 UTC

### Lifetime totals by registry

| Registry  | Lifetime packages identified |
| --------- | ---------------------------- |
| NPM       | 188,538                      |
| PyPI      | 12                           |
| **Total** | **188,550**                  |

### Recent activity by registry

| Period     | Window (UTC)             | NPM | PyPI | Total |
| ---------- | ------------------------ | --- | ---- | ----- |
| This week  | 2026-05-11 .. 2026-05-17 | 61  | 12   | 73    |
| Last week  | 2026-05-04 .. 2026-05-10 | 84  | 0    | 84    |
| This month | 2026-05                  | 180 | 12   | 192   |
| Last month | 2026-04                  | 619 | 0    | 619   |

## Recent malicious package reports

The following table lists the ten most recent malicious package advisories published by Amazon Inspector Security Research, ordered by published date.

| Package name             | MAL-ID        | Registry | Detection date |
| ------------------------ | ------------- | -------- | -------------- |
| d4rktg                   | MAL-2026-3688 | PyPI     | 2026-05-13     |
| @dropout-ai/runtime      | MAL-2026-3683 | NPM      | 2026-05-13     |
| amino.fix                | MAL-2026-3686 | PyPI     | 2026-05-13     |
| @gusmano/reext           | MAL-2026-3684 | NPM      | 2026-05-12     |
| always-updates           | MAL-2026-3685 | PyPI     | 2026-05-12     |
| @a91082900/test\_package | MAL-2026-3680 | NPM      | 2026-05-12     |
| kaggle-runner            | MAL-2026-3693 | PyPI     | 2026-05-12     |
| 88q                      | MAL-2026-3676 | NPM      | 2026-05-12     |
| 66o                      | MAL-2026-3674 | NPM      | 2026-05-12     |
| 6cc                      | MAL-2026-3675 | NPM      | 2026-05-12     |

## Related resources

The following AWS Security Blog posts provide additional context on Amazon Inspector Security Research and recent supply chain threat campaigns:

- [Amazon Inspector detects over 150,000 malicious packages linked to token-farming campaign](https://aws.amazon.com/blogs/security/amazon-inspector-detects-over-150000-malicious-packages-linked-to-token-farming-campaign/ "https://aws.amazon.com/blogs/security/amazon-inspector-detects-over-150000-malicious-packages-linked-to-token-farming-campaign/")
- [Defending against supply chain attacks like chalk, debug, and the Shai-Hulud worm](https://aws.amazon.com/blogs/security/defending-against-supply-chain-attacks-like-chalk-debug-and-the-shai-hulud-worm/ "https://aws.amazon.com/blogs/security/defending-against-supply-chain-attacks-like-chalk-debug-and-the-shai-hulud-worm/")
- [What AWS Security learned from responding to recent npm supply chain threat campaigns](https://aws.amazon.com/blogs/security/what-aws-security-learned-from-responding-to-recent-npm-supply-chain-threat-campaigns/ "https://aws.amazon.com/blogs/security/what-aws-security-learned-from-responding-to-recent-npm-supply-chain-threat-campaigns/")
