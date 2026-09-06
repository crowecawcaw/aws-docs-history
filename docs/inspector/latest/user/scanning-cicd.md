

# Integrating Amazon Inspector scans into your CI/CD pipeline
<a name="scanning-cicd"></a>

 The Amazon Inspector CI/CD integration utilizes the Amazon Inspector SBOM Generator and Amazon Inspector Scan API to produce vulnerability reports for container images. The Amazon Inspector SBOM Generator creates a software bill of materials (SBOM) for archives, container images, directories, local systems, and compiled Go and Rust binaries. The Amazon Inspector Scan API scans the SBOM to create a report with details about detected vulnerabilities. You can integrate Amazon Inspector container image scans with your CI/CD pipeline to scan for software vulnerabilities and produce vulnerability reports, which allow you to investigate and remediate risks before deployment. To set up your CI/CD integration, you can use plugins or create a custom CI/CD integration using the Amazon Inspector SBOM Generator and Amazon Inspector Scan API. 

**Topics**
+ [Plugin integration](#plugin-integration)
+ [Custom integration](#custom-integration)
+ [Setting up an AWS account to use the Amazon Inspector CI/CD integration](configure-cicd-account.md)
+ [Amazon Inspector Dockerfile checks](dockerfile-checks.md)
+ [Creating a custom CI/CD pipeline integration with Amazon Inspector Scan](cicd-custom.md)
+ [Using Amazon Inspector with GitHub actions](cicd-inspector-github-actions.md)
+ [Using the Amazon Inspector Jenkins plugin](cicd-jenkins.md)
+ [Using CodeCatalyst actions with Amazon Inspector](cicd-inspector-codecatalyst-actions.md)
+ [Using Amazon Inspector Scan actions with CodePipeline](cicd-inspector-codepipeline-actions.md)
+ [Using the Amazon Inspector TeamCity plugin](cicd-teamcity.md)
+ [Using Amazon Inspector with GitLab components](cicd-inspector-gitlab-components.md)

## Plugin integration
<a name="plugin-integration"></a>

Amazon Inspector provides plugins for supported CI/CD solutions. You can install these plugins from their respective marketplaces and then use them to add Amazon Inspector Scans as a build step in your pipeline. The plugin build step runs the Amazon Inspector SBOM generator on the image you supply, and then runs the Amazon Inspector Scan API on the generated SBOM.

The following is an overview of how an Amazon Inspector CI/CD integration works through plugins:

1. You configure an AWS account to allow access to the Amazon Inspector Scan API. For instructions, see [Setting up an AWS account to use the Amazon Inspector CI/CD integration](configure-cicd-account.md).

1. You install the Amazon Inspector plugin from the marketplace.

1. You install and configure the Amazon Inspector SBOM Generator binary. For instructions, see [Amazon Inspector SBOM Generator](sbom-generator.md).

1. You add Amazon Inspector Scans as a build step in your CI/CD pipeline and configure the scan.

1. When you run a build, the plugin takes your container image as input and then runs the Amazon Inspector SBOM Generator on the image to generate a CycloneDX compatible SBOM.

1. From there, the plugin sends the generated SBOM to an Amazon Inspector Scan API endpoint which assesses each SBOM component for vulnerabilities.

1. The Amazon Inspector Scan API response is transformed into a vulnerability report in CSV, SBOM JSON, and HTML formats. The report contains details about any vulnerabilities that Amazon Inspector found.

### Supported CI/CD solutions
<a name="supported-plugins"></a>

Amazon Inspector currently supports the following CI/CD solutions. For complete instructions on setting up the CI/CD integration using a plugin, select the plugin for your CI/CD solution:
+ [GitHub actions](https://docs.aws.amazon.com/inspector/latest/user/cicd-inspector-github-actions.html)
+ [Jenkins plugin](cicd-jenkins.md)
+ [TeamCity plugin](cicd-teamcity.md)

## Custom integration
<a name="custom-integration"></a>

If Amazon Inspector does not provide plugins for your CI/CD solution, you can create your own custom CI/CD integration using a combination of the Amazon Inspector SBOM Generator and the Amazon Inspector Scan API. You can also use a custom integration to fine-tune scans using the options available through Amazon Inspector SBOM Generator. 

The following is an overview of how a custom Amazon Inspector CI/CD integration works:

1. You configure an AWS account to allow access to the Amazon Inspector Scan API. For instructions, see [Setting up an AWS account to use the Amazon Inspector CI/CD integration](configure-cicd-account.md).

1. You install and configure the Amazon Inspector SBOM Generator binary. For instructions, see [Amazon Inspector SBOM Generator](sbom-generator.md).

1. You use the Amazon Inspector SBOM Generator to generate a CycloneDX compatible SBOM for your container image.

1. You use the Amazon Inspector Scan API on the generated SBOM to produce a vulnerability report.

For instructions on setting up a custom integration, see [Creating a custom CI/CD pipeline integration with Amazon Inspector Scan](cicd-custom.md).