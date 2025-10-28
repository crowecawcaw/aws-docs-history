# Using Amazon Inspector with GitHub actions

You can use Amazon Inspector with [GitHub actions](https://github.com/features/actions "https://github.com/features/actions") to add Amazon Inspector vulnerability scans to your GitHub workflows.
This leverages the [Amazon Inspector SBOM Generator](sbom-generator.md "sbom-generator.md") and [Amazon Inspector Scan API](../../v2/APIReference/API_Operations_Inspector_Scan.md "../../v2/APIReference/API_Operations_Inspector_Scan.md") to produce detailed reports at the end of your build, so you can investigate and remediate risk before deployment.
Amazon Inspector vulnerability scans can be configured to pass or fail workflows based on the number and severity of vulnerabilities detected.
You can view the latest version of the Amazon Inspector action on the [GitHub website](https://github.com/aws-actions/vulnerability-scan-github-action-for-amazon-inspector "https://github.com/aws-actions/vulnerability-scan-github-action-for-amazon-inspector").
For information about how to integrate Amazon Inspector Scan into your CI/CD pipeline, see [Integrating Amazon Inspector scans into your CI/CD pipeline](scanning-cicd.md "scanning-cicd.md").
For a list of operating systems and programming languages that Amazon Inspector supports, see [Supported operating systems and programming languages](supported.md "supported.md").
