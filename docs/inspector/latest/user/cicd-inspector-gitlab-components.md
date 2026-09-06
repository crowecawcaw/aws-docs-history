

# Using Amazon Inspector with GitLab components
<a name="cicd-inspector-gitlab-components"></a>

**Note**  
 The Amazon Inspector GitLab component is not officially supported by Amazon. It is maintained and provided as open-source by GitLab. 

 You can use Amazon Inspector with [GitLab CI/CD components](https://docs.gitlab.com/ee/ci/components/) to add Amazon Inspector vulnerability scans to your GitLab projects. This leverages the [Amazon Inspector SBOM Generator](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html) and [Amazon Inspector Scan API](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Operations_Inspector_Scan.html) to produce detailed reports at the end of your build, so you can investigate and remediate risk before deployment. Amazon Inspector vulnerability scans can be configured to pass or fail workflows based on the number and severity of vulnerabilities detected. You can view the latest version of the Amazon Inspector component on the [GitLab website](https://gitlab.com/guided-explorations/ci-components/aws/amazon-inspector). For information about how to integrate Amazon Inspector Scan into your CI/CD pipeline, see [Integrating Amazon Inspector scans into your CI/CD pipeline](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html). For a list of operating systems and programming languages that Amazon Inspector supports, see [Supported operating systems and programming languages](https://docs.aws.amazon.com/inspector/latest/user/supported.html). 