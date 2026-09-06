

# AWS Systems Manager in AWS GovCloud (US)
<a name="govcloud-ssm"></a>

Use AWS Systems Manager to organize, monitor, and automate management tasks on your AWS resources.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS Systems Manager differs
<a name="govcloud-sys-diffs"></a>

The following differences apply to AWS Systems Manager:
+ The following Systems Manager capabilities are not yet available for the AWS GovCloud (US) Regions:
  + Change Manager
  +  Incident Manager 
+ The following Systems Manager features are not yet available for the AWS GovCloud (US) Regions:
  + In the [Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html) tool, third-party packages are not available.
  + In the [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html) tool, integration with AWS Cost Explorer functionality is not available.
  + In the [Explorer](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer.html) tool, delegated administrator support for Explorer is not available.
  + In the [OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) tool, [markdown support](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-creating-OpsItems-console.html) is not available in the **OpsItem** description field in the console.
  + In the [Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) tool, support for Quick Setup patch policy configurations is not available.
  + In the [Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html) tool, support for AWS Organizations is not available.
  + In the [State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) tool, support for viewing association histories is not available.
+  Amazon Elastic Compute Cloud resource scheduling is not available.

Other differences:
+ Some Automation runbooks and SSM Command documents are not available for the AWS GovCloud (US) Regions.
+ SSM Agent for AWS GovCloud (US) can be downloaded from the following locations:

  ```
  https://amazon-ssm-us-gov-east-1.s3.us-gov-east-1.amazonaws.com/latest/windows_amd64/AmazonSSMAgentSetup.exe
  ```

```
https://amazon-ssm-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/latest/windows_amd64/AmazonSSMAgentSetup.exe
```

## Documentation
<a name="govcloud-sys-docs"></a>
+  [AWS Systems Manager documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) 

## Export-controlled content
<a name="govcloud-ssm-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ The following AWS Systems Manager metadata fields are not permitted to contain export-controlled data:
  + Document names
  + Parameter Store parameter names
  + Patch group names (that is, the value of the Patch Group tag)