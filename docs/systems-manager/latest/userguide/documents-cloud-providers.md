

# Specifying cloud providers for SSM documents

The cloud providers of an SSM document are metadata that declare which clouds the document runs on. The values are `AWS`, `Azure`, and `GCP`. Cloud providers apply to Automation runbooks. Use them to declare that a runbook works with Microsoft Azure or Google Cloud resources, in addition to or instead of AWS resources.

You set cloud providers when you create or update a runbook.

## How the Automation console uses cloud providers
<a name="documents-cloud-providers-why"></a>

The Automation console reads a runbook's cloud providers and adapts the **Execute automation** page:
+ The console offers the **Multi-account and Region** execution mode only when the runbook's cloud providers include `AWS`.
+ For a runbook whose cloud providers don't include `AWS`, the **Targets** list offers **Cloud Connector** and **Parameter Values**, and selects **Cloud Connector** for you.
+ For a Cloud Connector target, the console shows the filters for the runbook's cloud. If you choose a connector for a cloud that the runbook doesn't list, the console shows a warning, but you can still run the automation.
+ The runbook details on the **Execute automation** page show the runbook's **Cloud providers**.
+ The runbook picker and the Systems Manager **Documents** page show a **Cloud providers** column and filter.

## Rules for cloud providers
<a name="documents-cloud-providers-rules"></a>
+ A document can have 1 to 10 cloud providers, from the values `AWS`, `Azure`, and `GCP`. The values are case-sensitive.
+ Cloud providers are stored per document version as metadata, not in the document content.
+ A new document created without cloud providers is treated as `AWS`. An update that doesn't specify cloud providers copies the value from the latest version. Changing only the cloud providers creates a new document version.
+ The `DescribeDocument`, `ListDocuments`, and `ListDocumentVersions` operations return cloud providers. The `GetDocument` operation doesn't.

## Setting cloud providers with the AWS CLI
<a name="documents-cloud-providers-cli"></a>

Use the `cloud-providers` parameter with the `create-document` and `update-document` commands. In the following commands, replace {{MyRunbook}} and the content file with your own information.

------
#### [ Linux & macOS ]

```sh
aws ssm create-document \
    --name "{{MyRunbook}}" \
    --document-type "Automation" \
    --content file://MyRunbook.json \
    --cloud-providers "Azure"

aws ssm update-document \
    --name "{{MyRunbook}}" \
    --document-version '$LATEST' \
    --content file://MyRunbook.json \
    --cloud-providers "AWS" "Azure"
```

------
#### [ Windows ]

```sh
aws ssm create-document ^
    --name "{{MyRunbook}}" ^
    --document-type "Automation" ^
    --content file://MyRunbook.json ^
    --cloud-providers "Azure"

aws ssm update-document ^
    --name "{{MyRunbook}}" ^
    --document-version "$LATEST" ^
    --content file://MyRunbook.json ^
    --cloud-providers "AWS" "Azure"
```

------
#### [ PowerShell ]

```powershell
New-SSMDocument `
    -Name "{{MyRunbook}}" `
    -DocumentType "Automation" `
    -Content (Get-Content -Raw MyRunbook.json) `
    -CloudProvider "Azure"

Update-SSMDocument `
    -Name "{{MyRunbook}}" `
    -DocumentVersion "`$LATEST" `
    -Content (Get-Content -Raw MyRunbook.json) `
    -CloudProvider "AWS","Azure"
```

------

## Viewing cloud providers
<a name="documents-cloud-providers-view"></a>

To view a runbook's cloud providers with the command line, run the `describe-document` command and read the `CloudProviders` field in the output.

```sh
aws ssm describe-document --name "{{MyRunbook}}"
```

In the Systems Manager console, the details of a document on the **Documents** page include a **Cloud providers** field, and the documents list has a **Cloud providers** column.

## Searching by cloud provider
<a name="documents-cloud-providers-search"></a>

Use the `CloudProviders` filter with the `list-documents` command to find documents by cloud. The filter matches a document that has any of the values you specify. Documents without stored cloud providers match `AWS`.

```sh
aws ssm list-documents --filters Key=CloudProviders,Values=Azure
```

For more ways to search for SSM documents, see [Searching for SSM documents](ssm-documents-searching.md).

## Errors
<a name="documents-cloud-providers-errors"></a>

Setting cloud providers can return the following errors:
+ `CloudProviders must contain at least one cloud provider.`
+ `CloudProviders must not contain duplicate values.`
+ `<value> is not a supported cloud provider. Supported values: AWS, Azure, GCP`