# Filter IAM Access Analyzer findings

The default filtering for a findings page is to display all active findings. To view all
findings, choose **All** from the **Status** dropdown. To
view archived findings, choose **Archived**. To view resolved findings,
choose **Resolved**. When you first start using IAM Access Analyzer, there are no
archived findings.

Use filters to display only the findings that meet the specified property criteria. To
create a filter, select the property to filter on, then choose whether the property equals
or contains a value, then enter or choose a property value to filter on.

For a list of filter keys that you can use to create or update an archive rule, see [IAM Access Analyzer filter keys](access-analyzer-reference-filter-keys.md "access-analyzer-reference-filter-keys.md").

## Filtering resources with active

findings

You can view and filter active findings by resource for a maximum of one external
access analyzer and a maximum of one internal access analyzer.

###### To filter resources with active findings

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Resource analysis**.
3. To filter by resource name, type all or part of the name of the resource in
   the search box.
4. In the **Filter access type** dropdown, choose the access
   type:
   - **All types** – display resources with all
     types of access findings.
   - **Public access** – display only resources
     with public access findings.
   - **External access** – display only resources
     with external access findings.
   - **Internal access within organization** –
     display only resources with internal access findings.

5. In the **Filter resource type** dropdown, choose a resource
   type to display only resources of the selected type.

## Filtering external access

findings

###### To filter external access findings

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Analyzer settings** and then choose the external
   access analyzer in the **Analyzers** section.
3. Choose **View findings**.
4. Choose the search box to display a list of available properties.
5. Choose the property to use to filter the findings displayed.
6. Choose the value to match for the property. Only findings with that value in
   the finding are displayed.

For example, choose **Resource** as the property, then choose
**Resource:**, then type part or all of the name of a
bucket, then press Enter. Only findings for the bucket that matches the filter
criteria are displayed. To create a filter that displays only findings for
resources that allow public access, you can choose the **Public
access** property, then choose **Public access
=**, then choose **Public access = true**.

You can add additional properties to further filter the findings displayed. When you
add additional properties, only findings that match all conditions in the filter are
displayed. Defining a filter to display findings that match one property OR another
property is not supported. Choose **Clear filters** to clear any
filters you have defined and display all of the findings with the specified status for
your analyzer.

Some fields are displayed only when you are viewing findings for an analyzer with an
organization as its zone of trust.

The following properties are available for defining filters for external
access:

- **Public access** – To filter by findings for
  resources that allow public access, filter by **Public access**
  then choose **Public access: true**.
- **Resource** – To filter by resource, type all or part
  of the name of the resource.
- **Resource Type** – To filter by resource type, choose
  the type from the list displayed.
- **Resource Owner Account** – Use this property to
  filter by the account in the organization that owns the resource reported in the
  finding.
- **Resource Control Policy Restriction** – Use this
  property to filter by the type of restriction applied by an Organizations resource
  control policy (RCP). To learn more, see [Resource
  control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the AWS Organizations User Guide.
  - **Failed to evaluate RCP**: There was an error
    evaluating the RCP.
  - **Not applicable**: No RCP restricts this resource or
    principal. This also includes resources where RCPs are not yet
    supported.
  - **Applicable**: Your organization administrator has
    set restrictions through a RCP that impacts the resource or resource
    type. Contact your organization administrator for more details.

- **AWS Account** – Use this property to filter by
  AWS account that is granted access in the **Principal** section of a policy statement. To filter by
  AWS account, type all or part of the 12-digit AWS account ID, or all or part
  of the full account ARN of the external AWS user or role that has access to
  resources in the current account.
- **Canonical User** – To filter by canonical user, type
  the canonical user ID as defined for Amazon S3 buckets. To learn more, see [AWS Account
  Identifiers](../../../general/latest/gr/acct-identifiers.md "../../../general/latest/gr/acct-identifiers.md").
- **Federated User** – To filter by federated user, type
  all or part of the ARN of the federated identity. To learn more, see [Identity Providers and
  Federation](id_roles_providers.md "id_roles_providers.md").
- **Finding ID** – To filter by finding ID, type all or
  part of the finding ID.
- **Error** – To filter by error type, choose
  **Access Denied** or **Internal
  Error**.
- **Principal ARN** – Use this property to filter on the
  ARN of the principal (IAM user, role, or group) used in an **aws:PrincipalArn** condition key. To filter by
  Principal ARN, type all or part of the ARN of the IAM user, role, or group
  from an external AWS account reported in a finding.
- **Principal OrgID** – To filter by Principal OrgID,
  type all or part of the organization ID associated with the external principals
  that belong to the AWS organization specified as a condition in the finding.
  To learn more, see [AWS global
  condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **Principal OrgPaths** – To filter by Principal
  OrgPaths, type all or part of the ID for the AWS organization or
  organizational unit (OU) that allows access to all external principals that are
  account members of the specified organization or OU as a condition in the
  policy. To learn more, see [AWS global
  condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **Source Account** – To filter on Source Account, type
  all or part of the AWS account ID associated with the resources, as used in
  some cross-service permissions in AWS. To learn more, see [AWS global
  condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **Source ARN** – To filter by Source ARN, type all or
  part of the ARN specified as a condition in the finding. To learn more, see
  [AWS
  global condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **Source IP** – To filter by Source IP, type all or
  part of the IP address that allows external entities access to resources in the
  current account when using the specified IP address. To learn more, see [AWS global
  condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **Source OrgID** – To filter by Source OrgID, type all
  or part of the organization ID associated with the resources, as used in some
  cross-service permissions in AWS. To learn more, see [AWS global
  condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **Source OrgPaths** – To filter by Source OrgPaths,
  type all or part of the organizational unit (OU) associated with the resources,
  as used in some cross-service permission in AWS. To learn more, see [AWS global
  condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **Source VPC** – To filter by Source VPC, type all or
  part of the VPC ID that allows external entities access to resources in the
  current account when using the specified VPC. To learn more, see [AWS global
  condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **Source VPC ARN** – To filter by Source VPC ARN, type all or part of the VPC ARN that allows external entities access to resources in the current account when using the specified VPC.
  To learn more, see [AWS global
  condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **Source VPCE** – To filter by Source VPCE, type all
  or part of the VPC endpoint ID that allows external entities access to resources
  in the current account when using the specified VPC endpoint. To learn more, see
  [AWS
  global condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **VPCE Account** – To filter by VPCE Account, type all
  or part of the 12-digit AWS account ID that owns the the VPC endpoint external
  entities and allows external entities access to resources. To learn more, see
  [AWS
  global condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **VPCE OrgID** – To filter by VPCE OrgID, type all or
  part of the organization ID that owns the VPC endpoint external entities and
  allows external entities access to resources. To learn more, see [AWS global
  condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **VPCE OrgPaths** – To filter by VPCE OrgPaths, type
  all or part of the organizational unit (OU) that owns the VPC endpoint external
  entities and allows external entities access to resources. To learn more, see
  [AWS
  global condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **User ID** – To filter by User ID, type all or part
  of the user ID of the IAM user from an external AWS account who is allowed
  access to resource in the current account. To learn more, see [AWS global
  condition context keys](reference_policies_condition-keys.md "reference_policies_condition-keys.md").
- **KMS Key ID** – To filter by KMS key ID, type all
  or part of the key ID for the KMS key specified as a condition for
  AWS KMS-encrypted Amazon S3 object access in your current account.
- **Session Mode** – To filter by session mode for Amazon S3
  directory buckets (`ReadOnly` or `ReadWrite`, type all or
  part of the session mode. To learn more, see [CreateSession](../../../AmazonS3/latest/API/API_CreateSession.md "../../../AmazonS3/latest/API/API_CreateSession.md") in
  the Amazon Simple Storage Service API Reference.
- **Google Audience** – To filter by Google Audience,
  type all or part of the Google application ID specified as a condition for IAM
  role access in your current account. To learn more, see [IAM and
  AWS STS condition context keys](reference_policies_iam-condition-keys.md "reference_policies_iam-condition-keys.md").
- **Cognito Audience** – To filter by Amazon Cognito audience,
  type all or part of the Amazon Cognito identity pool ID specified as a condition for
  IAM role access in your current account. To learn more, see [IAM and
  AWS STS condition context keys](reference_policies_iam-condition-keys.md "reference_policies_iam-condition-keys.md").
- **Caller Account** – The AWS account ID of the
  account that owns or contains the calling entity, such as an IAM role, user,
  or account root user. This is used by services calling AWS KMS. To filter by
  caller account, type all or part of the AWS account ID.
- **Facebook App ID** – To filter by Facebook App ID,
  type all or part of the Facebook application ID (or site ID) specified as a
  condition to allow Login with Facebook federation access to an IAM role in
  your current account. To learn more, see the **id**
  section in [IAM and AWS STS condition context keys](reference_policies_iam-condition-keys.md#condition-keys-wif "reference_policies_iam-condition-keys.md#condition-keys-wif").
- **Amazon App ID** – To filter by Amazon App ID, type
  all or part of the Amazon application ID (or site ID) specified as a condition
  to allow Login with Amazon federation access to an IAM role in your current
  account. To learn more, see the **id** section in
  [IAM and AWS STS condition context keys](reference_policies_iam-condition-keys.md#condition-keys-wif "reference_policies_iam-condition-keys.md#condition-keys-wif").
- **Lambda Event Source Token** – To filter on Lambda
  Event Source Token passed in with Alexa integrations, type all or part of the
  token string.

## Filtering internal access

findings

###### To filter internal access findings

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Analyzer settings** and then choose the internal
   access analyzer in the **Analyzers** section.
3. Choose **View findings**.
4. Choose the search box to display a list of available properties.
5. Choose the property to use to filter the findings displayed.
6. Choose the value to match for the property. Only findings with that value in
   the finding are displayed.

For example, choose **Resource** as the property, then choose
**Resource:**, then type part or all of the name of a
bucket, then press Enter. Only findings for the bucket that matches the filter
criteria are displayed.

You can add additional properties to further filter the findings displayed. When you
add additional properties, only findings that match all conditions in the filter are
displayed. Defining a filter to display findings that match one property OR another
property is not supported. Choose **Clear filters** to clear any
filters you have defined and display all of the findings with the specified status for
your analyzer.

Some fields are displayed only when you are viewing findings for an analyzer with an
organization as its zone of trust.

The following fields are displayed only when you are viewing findings for an analyzer
that is monitoring internal access:

- **Resource** – To filter by resource, type all or part
  of the name of the resource.
- **Resource Type** – To filter by resource type, choose
  the type from the list displayed.
- **Resource Owner Account** – Use this property to
  filter by the account in the organization that owns the resource reported in the
  finding.
- **Finding id** – To filter by finding ID, type all or
  part of the finding ID.

## Filtering unused access

findings

###### To filter unused access findings

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Unused access** and then choose the analyzer in the
   **View analyzer** dropdown.
3. Choose the search box to display a list of available properties.
4. Choose the property to use to filter the findings displayed.
5. Choose the value to match for the property. Only findings with that value in
   the finding are displayed.

For example, choose **Findings type** as the property, then
choose **Findings type =**, then choose **Findings type
= Unused role**. Only findings with a type of **Unused
role** are displayed.

You can add additional properties to further filter the findings displayed. When you
add additional properties, only findings that match all conditions in the filter are
displayed. Defining a filter to display findings that match one property OR another
property is not supported. Choose **Clear filters** to clear any
filters you have defined and display all of the findings with the specified status for
your analyzer.

The following fields are displayed only when you are viewing findings for an analyzer
that is monitoring unused access:

- **Findings type** – To filter by finding type, filter
  by **Findings type** and then choose the type of
  finding.
- **Resource** – To filter by resource, type all or part
  of the name of the resource.
- **Resource Type** – To filter by resource type, choose
  the type from the list displayed.
- **Resource Owner Account** – Use this property to
  filter by the account in the organization that owns the resource reported in the
  finding.
- **Finding id** – To filter by finding ID, type all or
  part of the finding ID.
