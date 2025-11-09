# AWS CodeCommit in AWS GovCloud (US)

AWS CodeCommit is a fully-managed source control service that hosts secure Git-based repositories. It makes it easy for teams to collaborate on code in a secure and highly scalable ecosystem. CodeCommit eliminates the need to operate your own source control system or worry about scaling its infrastructure. You can use CodeCommit to securely store anything from source code to binaries, and it works seamlessly with your existing Git tools.

## How AWS CodeCommit differs for AWS GovCloud (US)

- The old console experience is not available in the AWS GovCloud (US) Regions. The documentation reflects the new console experience.
- Since AWS GovCloud (US); operates as isolated regions, you cannot share or use CodeCommit repositories and resources with other services outside of the Regions. For example, you cannot use a CodeCommit repository in AWS GovCloud (US-West) as the source for a pipeline in CodePipeline that is not in the AWS GovCloud (US-West) Region.
- All policy statements must refer to the GovCloud ARNs for the AWS GovCloud (US) Regions. For example, policies for Amazon SNS notifications, CloudWatch Events rules, and trigger resources must use the AWS GovCloud (US) ARNs for those services. For more information, see [Amazon Resource Names (ARNs) in AWS GovCloud](../ug-west/using-govcloud-arns.md "../ug-west/using-govcloud-arns.md").
- All IAM users and service roles must exist in the AWS GovCloud (US) Regions.

## Documentation for AWS CodeCommit

[AWS CodeCommit documentation](../../../codecommit/latest/userguide.md "../../../codecommit/latest/userguide.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Repository name
- Repository description
- Branch name
- Trigger name
- SNS topic name
- AWS Lambda topic name
