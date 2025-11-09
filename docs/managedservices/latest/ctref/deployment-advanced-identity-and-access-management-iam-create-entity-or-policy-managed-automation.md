# Identity and Access Management (IAM) | Create Entity or Policy (Managed Automation)

Create Identity and Access Management (IAM) user, role, or policy.

**Full classification:** Deployment | Advanced stack components | Identity and Access Management (IAM) | Create entity or policy (managed automation)

## Change Type Details

|                             |                           |
| --------------------------- | ------------------------- |
| Change type ID              | ct-3dpd8mdd9jn1r          |
| Current version             | 1.0                       |
| Expected execution duration | 240 minutes               |
| AWS approval                | Required                  |
| Customer approval           | Not required if submitter |
| Execution mode              | Manual                    |

## Additional Information

### Create IAM entity or policy (Managed Automation)

![](images/guiIamResourceCreateRrCT.png)
How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.
2. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the
   **Choose by category** view.
   - **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the
     **Run RFC** page. Note that you cannot choose an older CT version with quick create.

   To sort CTs, use the **All change types** area in either the **Card** or **Table** view.
   In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable,
   a **Create with older version** option appears next to the **Create RFC** button.
   - **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to
     **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

3. On the **Run RFC** page, open the CT name area to see the CT details box.
   A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the
   **Additional configuration** area to add information about the RFC.

In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure
optional execution parameters, open the **Additional configuration** area. 4. When finished, click **Run**. If there are no errors, the **RFC successfully created**
page displays with the submitted RFC details, and the initial **Run output**. 5. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status.
Optionally, cancel the RFC or create a copy of it with the options at the top of the page.
How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or
   Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc`
   command with the two files as input. Both methods are described here.
2. Submit the RFC: `aws amscm submit-rfc --rfc-id `ID`` command with the returned RFC ID.

Monitor the RFC: `aws amscm get-rfc --rfc-id `ID`` command.
To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value=`CT_ID`
```

###### Note

You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the
change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the
RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the
[AMS Change Management API Reference](../ApiReference-cm/API_CreateRfc.md "../ApiReference-cm/API_CreateRfc.md").

###### Note

When pasting in a policy document, note that the RFC only accepts policy pastes up to 20,480 characters. If your file has more than 20,480 characters, create a service request to upload the
policy and then refer to that service request in the RFC that you open for IAM.

_INLINE CREATE_:

Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-3dpd8mdd9jn1r" --change-type-version "1.0" --title "`TestIamCreate`" --execution-parameters "{\"UseCase\":\"`IAM_RESOURCE_DETAILS`\",\"IAM Role\":[{\"RoleName\":\"`ROLE_NAME`\",\"TrustPolicy\":\"`TRUST_POLICY`\",\"RolePermissions\":\"`ROLE_PERMISSIONS`\"}],\"Operation\":\"Create\"}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a file; example names it CreateIamResourceParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-3dpd8mdd9jn1r" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateIamResourceParams.json
```

2. Modify and save the CreateIamResourceParams file; example creates an IAM Role with policy documents pasted inline.

```
{
  "UseCase": "`IAM_RESOURCE_DETAILS`",
  "IAM Role": [
    {
      "RoleName": "`codebuild_ec2_test_role`",
      "TrustPolicy": {
        "Version": "`2008-10-17`",
        "Statement": [
          {
            "Effect": "`Allow`",
            "Principal": {
              "Service": "`codebuild.amazonaws.com`"
            },
            "Action": "`sts:AssumeRole`"
          }
        ]
      },
      "RolePermissions": {
        "Version": "`2012-10-17`",
        "Statement": [
          {
            "Effect": "`Allow`",
            "Action": [
              "`ec2:DescribeInstanceStatus`"
            ],
            "Resource": "`*`"
          }
        ]
      }
    }
  ],
  "Operation": "Create"
}
```

3. Output the RFC template JSON file to a file named CreateIamResourceRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateIamResourceRfc.json
```

4. Modify and save the CreateIamResourceRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion": "1.0",
"ChangeTypeId": "ct-3dpd8mdd9jn1r",
"Title": "`Create IAM Role`"
}
```

5. Create the RFC, specifying the CreateIamResourceRfc file and the CreateIamResourceParams file:

```
aws amscm create-rfc --cli-input-json file://CreateIamResourceRfc.json  --execution-parameters file://CreateIamResourceParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.

- After an IAM role is provisioned in your account, you must onboard the role in your federation solution.
- When pasting in a policy document, note that the RFC only accepts policy pastes up to 20,480 characters. If your policy has more
  than 20,480 characters, create a service request to upload the policy, and then refer to that service request in the RFC that you open for IAM.
- This is a manual change type (an AMS operator must review and run the CT), which means that the RFC can take longer
  to run and you might have to communicate with AMS through the RFC details page correspondance option. Additionally, if you schedule a manual change type RFC,
  be sure to allow at least 24 hours, if approval does not happen before the scheduled start time, the RFC is rejected automatically.
- For information about AWS Identity and Access Management, see
  [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") and for policy information, see
  [Managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md").
  For information about AMS permissions, see
  [Deploying IAM resources](../userguide/deploy-iam-resources.md "../userguide/deploy-iam-resources.md").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-3dpd8mdd9jn1r](schemas.md#ct-3dpd8mdd9jn1r-schema-section "schemas.md#ct-3dpd8mdd9jn1r-schema-section").

## Example: Required Parameters

```
{
  "UseCase": "Use case...",
  "Operation": "Create"
}
```

## Example: All Parameters

```
{
  "UseCase": "Use case...",
  "IAM User": [
    {
      "UserName": "user-a",
      "AccessType": "Console access",
      "AddPermissionsAsInlinePolicy": "No",
      "UserPermissionPolicyName": "policy",
      "UserPermissions": "Power User permissions",
      "Tags": [
        {
          "Key": "foo",
          "Value": "bar"
        },
        {
          "Key": "testkey",
          "Value": "testvalue"
        }
      ]
    }
  ],
  "IAM Role": [
    {
      "RoleName": "role-b",
      "AddPermissionsAsInlinePolicy": "No",
      "InstanceProfile": "No",
      "TrustPolicy": "Trust policy example",
      "RolePermissionPolicyName": "TestPolicy1",
      "RolePermissions": "Role permissions example",
      "ManagedPolicyArns": [
        "arn:aws:iam::123456789012:policy/policy01",
        "arn:aws:iam::123456789012:policy/policy02"
      ],
      "Path": "/",
      "Tags": [
        {
          "Key": "foo",
          "Value": "bar"
        },
        {
          "Key": "testkey",
          "Value": "testvalue"
        }
      ]
    }
  ],
  "IAM Policy": [
    {
      "PolicyName": "policy1",
      "PolicyDocument": "Policy document example 1",
      "Path": "/",
      "RelatedResources": [
        "resourceA",
        "resourceB"
      ],
      "CreatePolicyAsInlinePolicy": "No"
    },
    {
      "PolicyName": "policy2",
      "PolicyDocument": "Policy document example 2",
      "Path": "/",
      "RelatedResources": [
        "resourceC",
        "resourceD"
      ],
      "CreatePolicyAsInlinePolicy": "Yes"
    }
  ],
  "Operation": "Create",
  "Priority": "Medium"
}

```
