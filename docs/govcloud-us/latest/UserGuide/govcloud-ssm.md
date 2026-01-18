# AWS Systems Manager in AWS GovCloud (US)

Use AWS Systems Manager to organize, monitor, and automate management tasks on your AWS resources.

## How AWS Systems Manager differs for AWS GovCloud (US)

The implementation of Systems Manager is different for the AWS GovCloud (US) Regions in the following ways:

- The following Systems Manager capabilities are not yet available for the AWS GovCloud (US) Regions:
  - Change Manager
  - Incident Manager

- The following Systems Manager features are not yet available for the AWS GovCloud (US) Regions:
  - In the [Distributor](../../../systems-manager/latest/userguide/distributor.md "../../../systems-manager/latest/userguide/distributor.md") tool, third-party packages are not available.
  - In the [Application Manager](../../../systems-manager/latest/userguide/application-manager.md "../../../systems-manager/latest/userguide/application-manager.md") tool, integration with AWS Cost Explorer functionality is not available.
  - In the [Explorer](../../../systems-manager/latest/userguide/Explorer.md "../../../systems-manager/latest/userguide/Explorer.md") tool, delegated administrator support for Explorer is not available.
  - In the [OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md") tool, [markdown support](../../../systems-manager/latest/userguide/OpsCenter-creating-OpsItems-console.md "../../../systems-manager/latest/userguide/OpsCenter-creating-OpsItems-console.md") is not available in the **OpsItem** description field in the console.
  - In the [Patch Manager](../../../systems-manager/latest/userguide/patch-manager.md "../../../systems-manager/latest/userguide/patch-manager.md") tool, support for Quick Setup patch policy configurations is not available.
  - In the [Quick Setup](../../../systems-manager/latest/userguide/systems-manager-quick-setup.md "../../../systems-manager/latest/userguide/systems-manager-quick-setup.md") tool, support for AWS Organizations is not available.
  - In the [State Manager](../../../systems-manager/latest/userguide/systems-manager-state.md "../../../systems-manager/latest/userguide/systems-manager-state.md") tool, support for viewing association histories is not available.

- Amazon Elastic Compute Cloud resource scheduling is not available.

Other differences:

- Some Automation runbooks and SSM Command documents are not available for the AWS GovCloud (US) Regions.
- SSM Agent for AWS GovCloud (US) can be downloaded from the following locations:

```
 https://amazon-ssm-us-gov-east-1.s3.us-gov-east-1.amazonaws.com/latest/windows_amd64/AmazonSSMAgentSetup.exe
```

```
https://amazon-ssm-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/latest/windows_amd64/AmazonSSMAgentSetup.exe
```

## Documentation for AWS Systems Manager

[AWS Systems Manager documentation](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- The following AWS Systems Manager metadata fields are not permitted to contain export-controlled data:
  - Document names
  - Parameter Store parameter names
  - Patch group names (that is, the value of the Patch Group tag)
