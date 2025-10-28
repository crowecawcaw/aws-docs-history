# Creating issues with

suggestions and a linked AWS resource from AWS Systems Manager

A Systems Manager Automation Document can automatically create a
Jira issue with the fields set to have a linked AWS resource and up to
three suggested remediation documents.

To install this automation document, download and extract the [JSM Connector Create Remediation Issue Automation and IT Lifecycle
Demo.zip](https://servicecatalogconnector.s3.amazonaws.com/JSDConnector-create-remediation-issue-automation-and-it-lifecycle-demo.zip "https://servicecatalogconnector.s3.amazonaws.com/JSDConnector-create-remediation-issue-automation-and-it-lifecycle-demo.zip") that contains two files:

- _JSMConnector-CreateRemediationIssue.ssmdoc.yaml_
- _JSMConnector-function.zip_

###### Follow these steps

1. Upload the file _JSMConnector-function.zip_ to a bucket. In the
   following command, replace ${BUCKET} with the appropriate
   bucket:

```

aws s3 cp JSMConnector-function.zip s3://${BUCKET}/function.zip

```

2. Create the Systems Manager Automation Document, called
   **JSMConnector-CreateRemediationIssue**, with the
   contents from the file *JSMConnector-CreateRemediationIssue.ssmdoc.yam*l and an
   attachment _Key=SourceUrl,Values=s3://${BUCKET}/_, using the bucket
   name from the previous step as ${BUCKET}. The following command
   replaces ${BUCKET}):

```
aws ssm create-document --name "JSMConnector-CreateRemediationIssue" --content "file://JSMConnector-CreateRemediationIssue.ssmdoc.yaml" --document-type "Automation" --document-format "YAML" --attachments "Key=SourceUrl,Values=s3://${BUCKET}/"

```

Once installed, enter the parameters and run it. Note that it
requires many of the same parameters, as described previously to connect
to Jira.

You should then see an issue in Jira with AWS Config information and the
suggested remediation shown.
