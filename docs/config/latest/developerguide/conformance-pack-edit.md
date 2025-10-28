# Editing Conformance Packs for AWS Config

You can use the AWS Config console or the AWS CLI to edit your conformance packs.

Editing Conformance Packs (Console)

1. To edit a conformance pack, select the conformance pack from the table.
2. Choose **Actions** and then choose
   **Edit**.
3. On the **Edit conformance pack** page, you can edit the
   template details, sample template, conformance pack, and parameters section.

You cannot change the name of the conformance pack. 4. Choose **Save changes**.

The conformance pack is displayed with the AWS Config rules.

Editing Conformance Packs (AWS CLI)
If you are editing a conformance pack that you added previously, use the same `PutConformancePack` command that you use when deploying a conformance pack.

1. Open a command prompt or a terminal window.
2. Enter one of the following commands to deploy a conformance pack named
   `MyConformancePack`. The template source is either an
   Amazon S3 URI, a template that you upload, or an AWS Systems Manager document (SSM
   document).

**Amazon S3 URI**

```
aws configservice put-conformance-pack
--conformance-pack-name MyConformancePack
--template-s3-uri "s3://`amzn-s3-demo-bucket`/`templateName`.yaml"
--delivery-s3-bucket `amzn-s3-demo-bucket`
```

**YAML template from your local directory**

```
aws configservice put-conformance-pack
--conformance-pack-name MyConformancePack
--template-body `template body`
```

**AWS Systems Manager Document (Systems Manager Document)**

```
aws configservice put-conformance-pack
--conformance-pack-name MyConformancePack
--template-ssm-document-details DocumentName=`SSMDocumentName`,DocumentVersion=`SSMDocumentVersion`
--delivery-s3-bucket `amzn-s3-demo-bucket`
```

3. Press Enter to run the command.

You should see output similar to the following.

```
{
    "conformancePackArn": "arn:aws:config:us-west-2:`AccountID`:conformance-pack/MyConformancePack1/`conformance-pack-ID`"
}

```

###### Note

For more information on creating a YAML template for a conformance pack, see
[Custom Conformance
Pack](custom-conformance-pack.md "custom-conformance-pack.md").
