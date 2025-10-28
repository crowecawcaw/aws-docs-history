# Using Amazon Inspector with GitLab components

You can use Amazon Inspector with [GitLab CI/CD components](https://docs.gitlab.com/ee/ci/components/ "https://docs.gitlab.com/ee/ci/components/") to add Amazon Inspector vulnerability scans to your GitLab projects.
This leverages the [Amazon Inspector SBOM Generator](sbom-generator.md "sbom-generator.md") and [Amazon Inspector Scan API](../../v2/APIReference/API_Operations_Inspector_Scan.md "../../v2/APIReference/API_Operations_Inspector_Scan.md") to produce detailed reports at the end of your build, so you can investigate and remediate risk before deployment.
Amazon Inspector vulnerability scans can be configured to pass or fail workflows based on the number and severity of vulnerabilities detected.
You can view the latest version of the Amazon Inspector component on the [GitLab website](https://gitlab.com/guided-explorations/ci-components/aws/amazon-inspector "https://gitlab.com/guided-explorations/ci-components/aws/amazon-inspector").
For information about how to integrate Amazon Inspector Scan into your CI/CD pipeline, see [Integrating Amazon Inspector scans into your CI/CD pipeline](scanning-cicd.md "scanning-cicd.md").
For a list of operating systems and programming languages that Amazon Inspector supports, see [Supported operating systems and programming languages](supported.md "supported.md").
