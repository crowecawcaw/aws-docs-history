# The resources section of the CfCT manifest

file

This topic describes the **resources** section of the CfCT manifest file,
where you'll define the resources that are required for your customizations. This section of
the CfCT manifest file begins at the keyword **resources** and continues to the
end of the file.

The **resources** section of the manifest file specifies the AWS CloudFormation
StackSets, or AWS Organizations SCPs and RCPs, which CfCT deploys automatically through the code pipeline. You
can list OUs, accounts, and Regions to deploy stack instances.

Stack instances are deployed at the account level instead of the OU level. SCPs and RCPs are
deployed at the OU level. For more information, see [Build your own
customizations](cfcn-byo-customizations.md "cfcn-byo-customizations.md").

The following example template describes the possible entries that are available for
the **resources** section of the manifest file.

```
resources: # List of resources
  - name: [String]
    resource_file: [String] [Local File Path, S3 URI, S3 URL]
    deployment_targets: # account and/or organizational unit names
      accounts: # array of strings, [0-9]{12}
        - 012345678912
        - AccountName1
      organizational_units: #array of strings
        - OuName1
        - OuName2
    deploy_method: scp | stack_set | rcp
    parameters: # List of parameters [SSM, Alfred, Values]
      - parameter_key: [String]
        parameter_value: [String]
    export_outputs: # list of ssm parameters to store output values
      - name: /org/member/test-ssm/app-id
        value: $[output_ApplicationId]
    regions: #list of strings
    - [String]
```

**The remainder of this topic gives detailed definitions for the
keywords shown in the previous code example.**

**name** – The name that is associated with the
AWS CloudFormation StackSets.
The string you provide assigns a more user-friendly name for a stack
set.

- **Type:** String
- **Required:** Yes
- **Valid Values:** a-z, A-Z, 0-9, and an underscore (\_).
  Any other character is automatically replaced with an underscore (\_).
  **description** – The description for the
  resource.

- **Type:** String
- **Required:** No

**resource_file** – This file can be specified as the
relative location to the manifest file, an Amazon S3 URI or URL that points to an AWS CloudFormation template
or AWS Organizations service control policy in JSON for creating AWS CloudFormation resources, SCPs, or RCPs.

- **Type:** String
- **Required:** Yes

1. The following example shows the `resource_file`, given as a relative
   location to the resource file inside the configuration package.

```
resources:
  - name: SecurityRoles
    resource_file: templates/custom-security.template
```

2. The following example shows the resource file given as an Amazon S3 URI

```
resources:
  - name: SecurityRoles
    resource_file: s3://`amzn-s3-demo-bucket`/[key-name]
```

3. The following example shows the resource file given as an Amazon S3 HTTPS URL

```
resources:
  - name: SecurityRoles
    resource_file: https://bucket-name.s3.Region.amazonaws.com/key-name
```

###### Note

If you provide an Amazon S3 URL, verify that the bucket policy allows read access for
the AWS Control Tower management account from which you are deploying CfCT. If you provide an
Amazon S3 HTTPS URL, verify that the path uses dot notation. For example,
`S3.us-west-1`. CfCT does not support endpoints that contain a dash
between S3 and the Region, such as `S3‐us-west-2`. 4. The following example shows an Amazon S3 bucket policy and an ARN where resources are
stored.

```
{
   "Version": "2012-10-17",
   "Statement": [
       {
        "Effect": "Allow",
        "Principal": {"AWS": "arn:aws:iam::`AccountId`:root"},
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::`my-bucket`/*”
       }
   ]
}


```

You'll replace the `AccountId` variable shown in the
example with the AWS account ID for the management account that is deploying CfCT. For
more examples, refer to [Bucket policy
examples](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md") in the Amazon Simple Storage Service User Guide.
**parameters** – Specifies the name and value for
AWS CloudFormation parameters.

- **Type:** MapList
- **Required:** No
  The parameters section contains pairs of key/value parameters. The following pseudo
  template outlines the **parameters** section.

```
parameters:
  - parameter_key: [String]
    parameter_value: [String]
```

- **parameter_key** – The key associated with the
  parameter.
  - **Type:** String
  - **Required:** Yes (under parameters
    property)
  - **Valid Values:** a-z, A-Z, and 0-9

- **parameter_value** – The input value associated
  with the parameter.

      + **Type:** String
      + **Required:** Yes (under parameters property)

  **deploy_method** – The deployment method for
  deploying resource(s) into the account. Currently, **deploy_method**
  supports deploying resources using the `stack_set` option for resource deployment
  through AWS CloudFormation StackSets, the `scp` option if you are deploying SCPs, or the `rcp` option if you are deploying RCPs.

- **Type:** String
- **Valid Values:**
  `stack_set` | `scp` | `rcp`
- **Required:** Yes
  **deployment_targets** – List of accounts or
  Organizational Units (OUs), into which CfCT will deploy the AWS CloudFormation resources, specified as
  **accounts** or **organizational_units**.

###### Note

If you want to deploy an SCP or RCP, the target must be an OU, not an account.

- **Type:** List of string `account name` or
  `account number` to indicate that this resource will be deployed into the
  given account list, or `OU names` to indicate that this resource will be
  deployed into the given OU list.
- **Required:** At least one of
  **accounts** or **organizational_units**

      + **accounts:**


      **Type:** List of string `account name`
       or `account number` to indicate that this resource will be deployed into
       the given account list.
      + **organizational\_units:**


      **Type:** List of string `OU names` to
       indicate that this resource will be deployed into a given OU list. If you provide an
       OU that doesn’t contain accounts and the **accounts** property is
       not added, CfCT only creates the stack set.


      ###### Note

      The organization’s management account ID is not an allowed value. CfCT does
       not support deploying stack instances into the organization’s management
       account, by default. If you have a special use case, see [Root OU](cfct-root-ou.md "cfct-root-ou.md").

  **export_outputs** – List of name/value pairs that
  denote SSM parameter keys. These SSM parameter keys allow you to store template outputs into
  the SSM parameter store. The output is intended for reference by other resources, defined
  earlier in the manifest file.

```
export_outputs: # List of SSM parameters
  - name: [String]
    value: [String]
```

- **Type:** List of **name** and
  **value** key pairs. The **name** contains the
  `name` string of an SSM parameter store key, and **value**
  contains the parameter's `value` string.
- **Valid Values:** Any string or the
  `$[output_`CfnOutput-Logical-ID`]` variable
  where `CfnOutput-Logical-ID` corresponds to the template output
  variable. For more information about the Outputs section in an AWS CloudFormation template, see
  [**Outputs**](../../../AWSCloudFormation/latest/UserGuide/outputs-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/outputs-section-structure.md") in the _AWS CloudFormation User
  Guide_.
- **Required:** No
  For example, the following code snippet stores the template `VPCID` output
  variable into the SSM parameter key that's named
  `/org/member/audit/vpc_id`.

```
export_outputs: # List of SSM parameters
  - name: /org/member/audit/VPC-ID
    value: $[output_VPCID]
```

###### Note

The **export_outputs** key name may contain a value other than
`output`. For example, if the **name** is
`/org/environment-name`, the **value** may be
`production`.

**regions** – List of Regions in which CfCT will
deploy the AWS CloudFormation stack instances.

- **Type:** Any list of AWS commercial Region names, to
  indicate that this resource will be deployed into the given Region list. If this keyword
  does not exist in the manifest file, the resources are deployed in the home Region
  only.
- **Required:** No
