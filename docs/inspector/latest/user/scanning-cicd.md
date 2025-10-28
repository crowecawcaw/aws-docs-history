# Integrating Amazon Inspector scans into your CI/CD pipeline

The Amazon Inspector CI/CD integration utilizes the Amazon Inspector SBOM Generator and Amazon Inspector Scan API to produce vulnerability reports for container images.
The Amazon Inspector SBOM Generator creates a software bill of materials (SBOM) for archives, container images, directories, local systems, and compiled Go and Rust binaries.
The Amazon Inspector Scan API scans the SBOM to create a report with details about detected vulnerabilities.
You can integrate Amazon Inspector container image scans with your CI/CD pipeline to scan for software vulnerabilities and produce vulnerability reports, which allow you to investigate and remediate risks before deployment.
To set up your CI/CD integration, you can use plugins or create a custom CI/CD integration using the Amazon Inspector SBOM Generator and Amazon Inspector Scan API.

###### Topics

- [Plugin integration](#plugin-integration "#plugin-integration")
- [Custom integration](#custom-integration "#custom-integration")
- [Setting up an AWS account to use the Amazon Inspector CI/CD integration](configure-cicd-account.md "configure-cicd-account.md")
- [Amazon Inspector Dockerfile checks](dockerfile-checks.md "dockerfile-checks.md")
- [Creating a custom CI/CD pipeline integration with Amazon Inspector Scan](cicd-custom.md "cicd-custom.md")
- [Using the Amazon Inspector Jenkins plugin](cicd-jenkins.md "cicd-jenkins.md")
- [Using the Amazon Inspector TeamCity plugin](cicd-teamcity.md "cicd-teamcity.md")
- [Using Amazon Inspector with GitHub actions](cicd-inspector-github-actions.md "cicd-inspector-github-actions.md")
- [Using Amazon Inspector with GitLab components](cicd-inspector-gitlab-components.md "cicd-inspector-gitlab-components.md")
- [Using CodeCatalyst actions with Amazon Inspector](cicd-inspector-codecatalyst-actions.md "cicd-inspector-codecatalyst-actions.md")
- [Using Amazon Inspector Scan actions with CodePipeline](cicd-inspector-codepipeline-actions.md "cicd-inspector-codepipeline-actions.md")

## Plugin integration

Amazon Inspector provides plugins for supported CI/CD solutions. You can install these plugins
from their respective marketplaces and then use them to add Amazon Inspector Scans as a build step in
your pipeline. The plugin build step runs the Amazon Inspector SBOM generator on the image you
supply, and then runs the Amazon Inspector Scan API on the generated SBOM.

The following is an overview of how an Amazon Inspector CI/CD integration works through
plugins:

1. You configure an AWS account to allow access to the Amazon Inspector Scan API. For
   instructions, see [Setting up an AWS account to use the Amazon Inspector CI/CD integration](configure-cicd-account.md "configure-cicd-account.md").
2. You install the Amazon Inspector plugin from the marketplace.
3. You install and configure the Amazon Inspector SBOM Generator binary. For instructions, see [Amazon Inspector SBOM Generator](sbom-generator.md "sbom-generator.md").
4. You add Amazon Inspector Scans as a build step in your CI/CD pipeline and configure the
   scan.
5. When you run a build, the plugin takes your container image as input and then
   runs the Amazon Inspector SBOM Generator on the image to generate a CycloneDX compatible
   SBOM.
6. From there, the plugin sends the generated SBOM to an Amazon Inspector Scan API endpoint
   which assesses each SBOM component for vulnerabilities.
7. The Amazon Inspector Scan API response is transformed into a vulnerability report in CSV,
   SBOM JSON, and HTML formats. The report contains details about any
   vulnerabilities that Amazon Inspector found.

### Supported CI/CD solutions

Amazon Inspector currently supports the following CI/CD solutions. For complete instructions
on setting up the CI/CD integration using a plugin, select the plugin for your CI/CD
solution:

- [Jenkins plugin](cicd-jenkins.md "cicd-jenkins.md")
- [TeamCity plugin](cicd-teamcity.md "cicd-teamcity.md")
- [GitHub actions](cicd-inspector-github-actions.md "cicd-inspector-github-actions.md")

## Custom integration

If Amazon Inspector does not provide plugins for your CI/CD solution, you can create your own
custom CI/CD integration using a combination of the Amazon Inspector SBOM Generator and the Amazon Inspector Scan API. You can
also use a custom integration to fine-tune scans using the options available through
Amazon Inspector SBOM Generator.

The following is an overview of how a custom Amazon Inspector CI/CD integration works:

1. You configure an AWS account to allow access to the Amazon Inspector Scan API. For
   instructions, see [Setting up an AWS account to use the Amazon Inspector CI/CD integration](configure-cicd-account.md "configure-cicd-account.md").
2. You install and configure the Amazon Inspector SBOM Generator binary. For instructions, see [Amazon Inspector SBOM Generator](sbom-generator.md "sbom-generator.md").
3. You use the Amazon Inspector SBOM Generator to generate a CycloneDX compatible SBOM
   for your container image.
4. You use the Amazon Inspector Scan API on the generated SBOM to produce a vulnerability
   report.

For instructions on setting up a custom integration, see [Creating a custom CI/CD pipeline integration with Amazon Inspector Scan](cicd-custom.md "cicd-custom.md").
