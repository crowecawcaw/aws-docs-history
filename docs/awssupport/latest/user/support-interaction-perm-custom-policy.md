# Option 2: Create a custom policy with minimum required permissions

You can explicitly allow-list specific actions instead of using wildcards. The following are the required permissions for support interactions, case creation, and case management:

```


{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "support:AddAttachmentsToSet",
        "support:AddCommunicationToCase",
        "support:CreateCase",
        "support:DescribeAttachment",
        "support:DescribeCaseAttributes",
        "support:DescribeCases",
        "support:DescribeCommunication",
        "support:DescribeCommunications",
        "support:DescribeCreateCaseOptions",
        "support:DescribeIssueTypes",
        "support:DescribeServices",
        "support:DescribeSeverityLevels",
        "support:DescribeSupportedLanguages",
        "support:DescribeSupportLevel",
        "support:GetInteraction",
        "support:InitiateCallForCase",
        "support:ListInteractionEntries",
        "support:ListInteractions",
        "support:InitiateChatForCase",
        "support:PutCaseAttributes",
        "support:ResolveCase",
        "support:ResolveInteraction",
        "support:SearchForCases",
        "support:StartInteraction",
        "support:UpdateInteraction",
        "support-console:GetAccountState",
        "support-console:GetAccountGovCloudEnabled",
        "support-console:GetCaseDraft",
        "support-console:CreateCaseDraft",
        "support-console:DeleteCaseDraft",
        "support-console:GetBanner",
        "support-console:DescribeDynamicHelp",
        "support-console:CreateContact",
      ],
      "Resource": "*"
    }
  ]
}

```

###### Note

Using a custom policy requires ongoing maintenance as AWS Support releases new features. For more information about the Support Center Console API operations, see [Adding IAM policies for the Support Center Console API operations](support-console-access-control.md "support-console-access-control.md"). For more information about each of the Support API operations, see [Manage access to AWS Support Center](accessing-support.md "accessing-support.md").
