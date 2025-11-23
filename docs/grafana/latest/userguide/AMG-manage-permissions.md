# Amazon Managed Grafana permissions and policies for AWS data

sources

Amazon Managed Grafana offers three permission modes:

- Service-managed permissions for current account
- Service-managed permissions for organizations
- Customer-managed permissions
  When you create a workspace, you choose which permission mode to use. You can also change
  this later if you want.

In either of the service-managed permission modes, Amazon Managed Grafana creates roles and policies
that are needed to access and discover AWS data sources in your account or organization.
You can then edit these policies in the IAM console if you choose.

## Service-managed permissions for a single

account

In this mode, Amazon Managed Grafana creates a role called
**AmazonGrafanaServiceRole-`random-id`**.
Amazon Managed Grafana then attaches a policy to this role for each AWS service that you select to
access from the Amazon Managed Grafana workspace.

**CloudWatch**

Amazon Managed Grafana attaches the AWS managed policy
**AmazonGrafanaCloudWatchAccess**.

###### Note

For workspaces that used CloudWatch before the
**AmazonGrafanaCloudWatchAccess**
managed policy was created,
Amazon Managed Grafana created a customer-managed policy with the name
**AmazonGrafanaCloudWatchPolicy-`random-id`**.

**Amazon OpenSearch Service**

Amazon Managed Grafana creates a customer-managed policy with the name
**AmazonGrafanaOpenSearchPolicy-`random-id`**.
The Get/Post permissions are needed for data source access. The
List/Describe permissions are used by Amazon Managed Grafana for data source discovery,
but they aren’t required for the data source plugin to work. The contents of
the policy are as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "es:ESHttpGet",
 "es:DescribeElasticsearchDomains",
 "es:ListDomainNames"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "es:ESHttpPost",
 "Resource": [
 "arn:aws:es:*:*:domain/*/_msearch*",
 "arn:aws:es:*:*:domain/*/_opendistro/_ppl"
 ]
 }
 ]
}`

```

**AWS IoT SiteWise**

Amazon Managed Grafana attaches the AWS managed policy
**AWSIoTSiteWiseReadOnlyAccess**.

**Amazon Redshift**

Amazon Managed Grafana attaches the AWS managed policy
**AmazonGrafanaRedshiftAccess**.

**Amazon Athena**

Amazon Managed Grafana attaches the AWS managed policy
**AmazonGrafanaAthenaAccess**.

**Amazon Managed Service for Prometheus**

Amazon Managed Grafana creates a customer-managed policy with the name
**AmazonGrafanaPrometheusPolicy-`random-id`**.
The List/Describe permissions are used by Amazon Managed Grafana for data source
discovery, they aren’t required for the plugin to work. The contents of the
policy are as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aps:ListWorkspaces",
 "aps:DescribeWorkspace",
 "aps:QueryMetrics",
 "aps:GetLabels",
 "aps:GetSeries",
 "aps:GetMetricMetadata"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Amazon SNS**

Amazon Managed Grafana creates a customer-managed policy with the name
**AmazonGrafanaSNSPolicy-`random-id`**.
The policy restricts you to only using SNS topics in your account that start
with the string `grafana`. This is not necessary if you create
your own policy. The contents of the policy are as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sns:Publish"
 ],
 "Resource": [
 "arn:aws:sns:*:`111122223333`:grafana*"
 ]
 }
 ]
}`

```

**Timestream**

Amazon Managed Grafana attaches the AWS managed policy
**AmazonTimestreamReadOnlyAccess**.

**X-Ray**

Amazon Managed Grafana attaches the AWS managed policy
**AWSXrayReadOnlyAccess**.

## Service-managed permissions for an

organization

This mode is supported only for workspaces created in management accounts or
delegated administrator accounts in an organization. Delegated administrator accounts
can create and administer stack sets for the organization. For more information about
delegated administrator accounts, see [Register a delegated administrator](../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.md").

###### Note

Creating resources such as Amazon Managed Grafana workspaces in the management account of an
organization is against AWS security best practices.

In this mode, Amazon Managed Grafana creates all the IAM roles that are necessary to access AWS
resources in other accounts in your AWS organization. In each account in the
Organizational Units that you select, Amazon Managed Grafana creates a role called
**AmazonGrafanaOrgMemberRole-`random-id`**.
This role creation is performed through an integration with AWS CloudFormation StackSets.

This role has a policy attached for each AWS data source that you select to
use in the workspace. For the contents of these data policies, see [Service-managed permissions for a single
account](#AMG-service-managed-account "#AMG-service-managed-account") .

Amazon Managed Grafana also creates a role called
**AmazonGrafanaOrgAdminRole-`random-id`**
in the organization's management account. This role allows the Amazon Managed Grafana workspace
permission to access other accounts in the organization. AWS service notification
channel policies also get attached to this role. Use the **AWS Data
Source** menu in your workspace to quickly provision data sources for each
account that your workspace can access

To use this mode, you must enable CloudFormation Stacksets as a trusted service in your AWS
organization. For more information, see [Enable trusted access with AWS Organizations](../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.md").

Here is the content of the
**AmazonGrafanaStackSet-`random-id`**
stack set:

```
Parameters:
  IncludePrometheusPolicy:
    Description: Whether to include Amazon Prometheus access in the role
    Type: String
    AllowedValues:
      - true
      - false
    Default: false
  IncludeAESPolicy:
    Description: Whether to include Amazon Elasticsearch access in the role
    Type: String
    AllowedValues:
      - true
      - false
    Default: false
  IncludeCloudWatchPolicy:
    Description: Whether to include CloudWatch access in the role
    Type: String
    AllowedValues:
      - true
      - false
    Default: false
  IncludeTimestreamPolicy:
    Description: Whether to include Amazon Timestream access in the role
    Type: String
    AllowedValues:
      - true
      - false
    Default: false
  IncludeXrayPolicy:
    Description: Whether to include AWS X-Ray access in the role
    Type: String
    AllowedValues:
      - true
      - false
    Default: false
  IncludeSitewisePolicy:
    Description: Whether to include AWS IoT SiteWise access in the role
    Type: String
    AllowedValues:
      - true
      - false
    Default: false
  IncludeRedshiftPolicy:
    Description: Whether to include Amazon Redshift access in the role
    Type: String
    AllowedValues:
      - true
      - false
    Default: false
  IncludeAthenaPolicy:
    Description: Whether to include Amazon Athena access in the role
    Type: String
    AllowedValues:
      - true
      - false
    Default: false
  RoleName:
    Description: Name of the role to create
    Type: String
  AdminAccountId:
    Description: Account ID of the Amazon Grafana org admin
    Type: String
Conditions:
  addPrometheus: !Equals [!Ref IncludePrometheusPolicy, true]
  addAES: !Equals [!Ref IncludeAESPolicy, true]
  addCloudWatch: !Equals [!Ref IncludeCloudWatchPolicy, true]
  addTimestream: !Equals [!Ref IncludeTimestreamPolicy, true]
  addXray: !Equals [!Ref IncludeXrayPolicy, true]
  addSitewise: !Equals [!Ref IncludeSitewisePolicy, true]
  addRedshift: !Equals [!Ref IncludeRedshiftPolicy, true]
  addAthena: !Equals [!Ref IncludeAthenaPolicy, true]

Resources:
  PrometheusPolicy:
    Type: AWS::IAM::Policy
    Condition: addPrometheus
    Properties:
      Roles:
       - !Ref GrafanaMemberServiceRole
      PolicyName: AmazonGrafanaPrometheusPolicy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action:
              - aps:QueryMetrics
              - aps:GetLabels
              - aps:GetSeries
              - aps:GetMetricMetadata
              - aps:ListWorkspaces
              - aps:DescribeWorkspace
            Resource: '*'

  AESPolicy:
    Type: AWS::IAM::Policy
    Condition: addAES
    Properties:
      Roles:
       - !Ref GrafanaMemberServiceRole
      PolicyName: AmazonGrafanaElasticsearchPolicy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Sid: AllowReadingESDomains
            Effect: Allow
            Action:
              - es:ESHttpGet
              - es:ESHttpPost
              - es:ListDomainNames
              - es:DescribeElasticsearchDomains
            Resource: '*'

  CloudWatchPolicy:
    Type: AWS::IAM::Policy
    Condition: addCloudWatch
    Properties:
      Roles:
       - !Ref GrafanaMemberServiceRole
      PolicyName: AmazonGrafanaCloudWatchPolicy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Sid: AllowReadingMetricsFromCloudWatch
            Effect: Allow
            Action:
              - cloudwatch:DescribeAlarmsForMetric
              - cloudwatch:DescribeAlarmHistory
              - cloudwatch:DescribeAlarms
              - cloudwatch:ListMetrics
              - cloudwatch:GetMetricStatistics
              - cloudwatch:GetMetricData
              - cloudwatch:GetInsightRuleReport
            Resource: "*"
          - Sid: AllowReadingLogsFromCloudWatch
            Effect: Allow
            Action:
              - logs:DescribeLogGroups
              - logs:GetLogGroupFields
              - logs:StartQuery
              - logs:StopQuery
              - logs:GetQueryResults
              - logs:GetLogEvents
            Resource: "*"
          - Sid: AllowReadingTagsInstancesRegionsFromEC2
            Effect: Allow
            Action:
              - ec2:DescribeTags
              - ec2:DescribeInstances
              - ec2:DescribeRegions
            Resource: "*"
          - Sid: AllowReadingResourcesForTags
            Effect: Allow
            Action:
              - tag:GetResources
            Resource: "*"
  GrafanaMemberServiceRole:
    Type: 'AWS::IAM::Role'
    Properties:
      RoleName: !Ref RoleName
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS: !Sub arn:aws:iam::${AdminAccountId}:root
            Action:
              - 'sts:AssumeRole'
      Path: /service-role/
      ManagedPolicyArns:
        - !If [addTimestream, arn:aws:iam::aws:policy/AmazonTimestreamReadOnlyAccess, !Ref AWS::NoValue]
        - !If [addXray, arn:aws:iam::aws:policy/AWSXrayReadOnlyAccess, !Ref AWS::NoValue]
        - !If [addSitewise, arn:aws:iam::aws:policy/AWSIoTSiteWiseReadOnlyAccess, !Ref AWS::NoValue]
        - !If [addRedshift, arn:aws:iam::aws:policy/service-role/AmazonGrafanaRedshiftAccess, !Ref AWS::NoValue]
        - !If [addAthena, arn:aws:iam::aws:policy/service-role/AmazonGrafanaAthenaAccess, !Ref AWS::NoValue]
```

Here is the content of
**AmazonGrafanaOrgAdminPolicy-`random-id`**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "organizations:ListAccountsForParent",
 "organizations:ListOrganizationalUnitsForParent"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalOrgID": "o-`organizationId`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "arn:aws:iam::*:role/service-role/AmazonGrafanaOrgMemberRole-`random-Id`"
 }]
}`

```

## Customer-managed permissions

If you choose to use customer-managed permissions, you specify an existing IAM role
in your account when you create an Amazon Managed Grafana workspace. The role must have a trust
policy which trusts `grafana.amazonaws.com`.

The following is an example of such a policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "grafana.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For that role to access AWS data sources or notification channels in that account,
it must have the permissions in the policies listed earlier in this section. For
example, to use the CloudWatch data source, it must have the permissions in the CloudWatch policy
listed in [Service-managed permissions for a single
account](#AMG-service-managed-account "#AMG-service-managed-account") .

The `List` and `Describe` permissions in the policies for Amazon
OpenSearch Service and Amazon Managed Service for Prometheus shown in [Service-managed permissions for a single
account](#AMG-service-managed-account "#AMG-service-managed-account") are only needed for the data source
discovery and provisioning to work correctly. They aren’t needed if you just want to set
up these data sources manually.

**Cross-account access**

When a workspace is created in account 111111111111, a role in account 1111111111111
must be supplied. For this example, call this role
_WorkspaceRole_. To access data in account 999999999999, you must
create a role in account 999999999999. Call that
_DataSourceRole_. You must then establish a trust relationship
between _WorkspaceRole_ and _DataSourceRole_. For
more information about establishing trust between two roles, see [IAM Tutorial:
Delegate access across AWS accounts using IAM roles](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md").

_DataSourceRole_ needs to contain the policy statements listed
earlier in this section for each data source that you want to use. After the trust
relationship is established, you can specify the ARN of
_DataSourceRole_ (arn:aws:iam::999999999999:role:DataSourceRole)
in the **Assume Role ARN** field on the data source configuration page
of any AWS data source in your workspace. The data source then accesses account
999999999999 with the permissions that are defined in
_DataSourceRole_.
