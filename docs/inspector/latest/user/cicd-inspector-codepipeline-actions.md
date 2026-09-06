

# Using Amazon Inspector Scan actions with CodePipeline
<a name="cicd-inspector-codepipeline-actions"></a>

 You can use Amazon Inspector with AWS CodePipeline by adding vulnerability scans to your workflows. This integration leverages the Amazon Inspector SBOM Generator and Amazon Inspector Scan API to produce detailed reports at the end of your build. The integration helps you investigate and remediate risk before deployment. The `InspectorScan` action is a managed compute action in CodePipeline that automates detecting and fixing security vulnerabilities in your open source code. You can use this action with application source code in your third-party repository, such as GitHub or Bitbucket Cloud, or with images for container applications. For more information, see [InspectorScan invoke action reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-InspectorScan.html) in the *AWS CodePipeline User Guide*. 