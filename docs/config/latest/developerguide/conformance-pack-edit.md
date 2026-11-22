

# Editing Conformance Packs for AWS Config

You can use the AWS Config console or the AWS CLI to edit your conformance packs. For a managed conformance pack, you can change the resource scope, parameters, and tags. You can't change the name, the source, or the conformance pack type. To change the source or the type, delete the conformance pack and deploy it again.

------
#### [ Editing Conformance Packs (Console) ]

1. To edit a conformance pack, select the conformance pack from the table.

1. Choose **Actions** and then choose **Edit**.

1. For a custom conformance pack, on the **Edit conformance pack** page, you can edit the template details, sample template, conformance pack, and parameters section. You can't change the name of the conformance pack.

   For a managed conformance pack, on the **Edit conformance pack settings** page, update the **Resource scope**, **Parameters**, and **Tags**. Choose **Next**, and then review your changes on the **Review and save** page.

1. Choose **Save changes**.

   The conformance pack is displayed with the AWS Config rules.

------
#### [ Editing Conformance Packs (AWS CLI) ]

If you are editing a conformance pack that you added previously, use the same `PutConformancePack` command that you use when deploying a conformance pack.

1. Open a command prompt or a terminal window.

1. Run one of the following commands to update a conformance pack named **MyConformancePack**.

   **Managed conformance pack**

   ```
   aws configservice put-conformance-pack
   --conformance-pack-name MyConformancePack
   --source SourceIdentifier={{AWS-WAF_V10}}
   --scope TagKey={{environment}},TagValue={{staging}}
   ```

   For the `source` parameter, specify the same value as the existing conformance pack. Also specify every setting that you want to keep. If you omit a setting, it's removed. For example, if you omit the `scope` parameter, the tag scope is removed from the conformance pack.

   For a custom conformance pack, the template source is either an Amazon S3 URI, a template that you upload, or an AWS Systems Manager document (SSM document).

   **Amazon S3 URI**

   ```
   aws configservice put-conformance-pack
   --conformance-pack-name MyConformancePack
   --template-s3-uri "s3://{{amzn-s3-demo-bucket}}/{{templateName}}.yaml"
   --delivery-s3-bucket {{amzn-s3-demo-bucket}}
   ```

   **YAML template from your local directory**

   ```
   aws configservice put-conformance-pack
   --conformance-pack-name MyConformancePack
   --template-body {{template body}}
   ```

   **AWS Systems Manager Document (Systems Manager Document)**

   ```
   aws configservice put-conformance-pack
   --conformance-pack-name MyConformancePack
   --template-ssm-document-details DocumentName={{SSMDocumentName}},DocumentVersion={{SSMDocumentVersion}}
   --delivery-s3-bucket {{amzn-s3-demo-bucket}}
   ```

1. Press Enter to run the command.

   You should see output similar to the following.

   ```yaml
   {
       "conformancePackArn": "arn:aws:config:us-west-2:{{AccountID}}:conformance-pack/MyConformancePack/{{conformance-pack-ID}}"
   }
   ```

**Note**  
For more information on creating a YAML template for a conformance pack, see [Custom Conformance Pack](https://docs.aws.amazon.com/config/latest/developerguide/custom-conformance-pack.html).

------