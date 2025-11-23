# Version upgrades for the CfCT manifest

For information about the latest version of _Customizations for
AWS Control Tower_ (CfCT), see the [`CHANGELOG.md` file](https://github.com/aws-solutions/aws-control-tower-customizations/blob/master/CHANGELOG.md "https://github.com/aws-solutions/aws-control-tower-customizations/blob/master/CHANGELOG.md") in the GitHub repository.

###### Warning

Version 2.2.0 of _Customizations for AWS Control Tower_ (CfCT)
introduced a CfCT manifest schema (version _2021-03-15_) to
align with related AWS service APIs. The manifest schema allows a single manifest.yaml
file to manage supported resources (CloudFormation templates, SCPs, and RCPs) through decoupled DevOps
workflows.

We strongly recommend that you update the CfCT manifest schema from version _2020-01-01_ to version _2021-03-15_ or later.

CfCT continues to support version _2021-03-15_ and
_2020-01-01_ of the `manifest.yaml` file. No
changes to your existing configuration are required. However, version _2020-01-01_ is at **End of Support**. We no
longer provide updates or add enhancements to version _2020-01-01_. The Root OU and nested OU features aren't supported in version
_2020-01-01_.

**Deprecated properties in CfCT manifest version _2021-03-15:_**

```
organization_policies
policy_file
apply_to_accounts_in_ou

cloudformation_resources
template_file
deploy_to_account
deploy_to_ou
ssm_parameters
```

## Mandatory CfCT upgrade steps

When you upgrade to the CfCT manifest schema version _2021-03-15_ version, here are the changes you must make to update your files.
The next sections outline mandatory and recommended changes for the transition.

###### Organizations polices

1. Move the SCPs or RCPs under **organization_policies** under new property
   **resources**.
2. Change the **policy_file** property to new property
   **resource_file.**
3. Change the **apply_to_accounts_in_ou** to new property
   **deployment_targets**. The OU list should be defined under
   sub-property **organizational_units**. The
   **accounts** sub-property is not supported for organizations
   policies.
4. Add a new property **deploy_method** with the value
   **scp** or **rcp**.

###### CloudFormation resources

1. Move the CloudFormation resources under
   **cloudformation_resources** under new property
   **resources**.
2. Change the **template_file** property to new property
   **resource_file**.
3. Change the **deploy_to_ou** to new property
   **deployment_targets**. The OU list should be defined under
   sub-property **organizational_units**.
4. Change the **deploy_to_accounts** to new property
   **deployment_targets**. The account list should be defined under
   sub-property **accounts**.
5. Change the **ssm_parameters** property to new property
   **export_outputs**.

## Highly recommended CfCT upgrade steps

###### CloudFormation parameters

1. Change the **parameter_file** property to new property
   **parameters**.
2. Remove the file path in the value of the **parameter_file**
   property.
3. Copy the parameter key and parameter value from the existing parameter JSON file
   into the new format for the **parameters** property. This would help
   you manage them in the manifest file.

###### Note

The **parameter_file** property is supported in CfCT manifest version
_2021-03-15_.
