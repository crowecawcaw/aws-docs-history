# Searching for a finding or entity in Detective

With the Amazon Detective search function, you can search for a finding or entity. From the search
results, you can navigate to an entity profile or a finding overview. If your search returns more
than 10,000 results, only the top 10,000 results are displayed. Changing the sorting order changes
the returned results.

You can export your search results to a comma-separated values (.csv) file. This file
contains the data returned in the search page. The data is exported in comma-separated values (CSV) format. The file name of the exported data follows the pattern detective-page-panel-yyyy-mm-dd.csv format. You can enrich your security investigations by manipulating the data using other AWS services, third-party applications, or spreadsheet programs that support CSV import.

###### Note

If an export is currently in progress, wait until the export is complete before you try to export additional data.

## Completing the search

To complete the search, choose the type of entity to search for. Then provide the exact
identifier or identifier with wildcard characters `*` or `?`. To search for
a range of IP addresses, you can also use CIDR or dot notations. See the following example search
strings.

For IP addresses:

- `1.0.*.*`
- `1.0.133.*`
- `1.0.0.0/16`
- `0.239.48.198/31`

For all other types of entities:

- `Admin`
- `ad*`
- `ad*n`
- `ad*n*`
- `adm?n`
- `a?m*`
- `*min`

For each entity type, the following identifiers are supported:

- For Findings, the finding identifier or finding Amazon Resource Name (ARN).
- For AWS accounts, the account ID.
- For AWS roles and AWS users, either the principal ID, the name, or the ARN.
- For Container clusters, the cluster name or ARN.
- For Container images, the repository or the full digest of the container image.
- For container Pods or Tasks, the pod name or the UID of the pod.
- For EC2 instances, the instance identifier or the ARN.
- For Finding group, the finding group identifier.
- For IP addresses, the address in CIDR or dot notation.
- For Kubernetes subjects (service accounts or users), the name.
- For a role session, you can use any of the following values to search:
  - Role session identifier.

  The role session identifier uses the format
  ``<rolePrincipalID>`:`<sessionName>``.

  Here is an example: `AROA12345678910111213:MySession`.
  - Role session ARN
  - Session name
  - Principal ID of the role that was assumed
  - Name of the role that was assumed

- For S3 buckets, the bucket name or bucket ARN.
- For federated users, the principal ID or the user name. The principal ID is either
  ``<identityProvider>`:`<username>``
  or
  ``<identityProvider>`:`<audience>`:`<username>``.
- For user agents, the user agent name.

###### To search for a finding or entity

1. Sign in to the AWS Management Console. Then open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the navigation pane, choose **Search**.
3. From the **Choose type** menu, choose the type of item you're looking
   for.

Note that when you choose **User**, you can search for either an AWS
user or a federated user.

**Examples from your data** contains a sample set of identifiers of the
selected type that are in your behavior graph data. To display the profile for one of the
examples, choose its identifier. 4. Enter the exact identifier or an identifier with wildcard characters to search for.

The search is case insensitive. 5. Choose **Search** or press **Enter**.

## Using the search results

When you complete the search, Detective displays a list of up to 10,000 matching results. For
searches that use a unique identifier, there is only one matching result.

From the results, to navigate to the entity profile or finding overview, choose the
identifier.

For findings, roles, users, and EC2 instances, the search results include the associated
account. To navigate to the profile for the account, choose the account identifier.

## Troubleshooting the search

If Detective does not find the finding or entity, first check that you entered the correct
identifier. If the identifier is correct, you can also check the following.

- **Does the finding or entity belong to an enabled member account in
  your behavior graph?** If the associated account was not invited to the behavior
  graph as a member account, then the behavior graph does not contain data for that
  account.

If an invited member account did not accept the invitation, then the behavior graph does
not contain data for that account.

- **For a finding, is the finding archived?** Detective does not
  receive archived findings from Amazon GuardDuty.
- **Did the finding or entity occur before Detective began to ingest data
  into your behavior graph?** If the finding or entity is not present in the data that
  Detective ingests, then the behavior graph does not contain data for it.
- **Is the finding or entity from the correct Region?** Each
  behavior graph is specific to an AWS Region. A behavior graph does not contain data from
  other Regions.
