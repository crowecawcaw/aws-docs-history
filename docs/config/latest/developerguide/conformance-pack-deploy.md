# Deploying Conformance Packs for AWS Config

You can use the AWS Config console or the AWS CLI to deploy your conformance packs.

Deploy Conformance Packs (Console)
On the **Conformance packs** page, you can deploy a conformance pack for
an account in a Region. You can also edit and delete the deployed conformance pack.

You can deploy a conformance pack using AWS Config sample templates or your own custom
template. For instructions on how to create personalized conformance packs, see
[Custom Conformance
Pack](custom-conformance-pack.md "custom-conformance-pack.md").

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Navigate to the **Conformance packs** page and choose
   **Deploy conformance pack**.
3. On the **Specify template** page, either choose a sample
   template or use an existing template. For more information, see [Conformance Pack
   Sample Templates.](conformancepack-sample-templates.md "conformancepack-sample-templates.md")
   - If you choose **Use sample template**, select a
     **Sample template** from the dropdown list of
     sample templates.

   For information about the contents of each template, see Conformance
   Pack Sample Templates.
   - If you choose **Template is ready**, specify the
     template source. It is either an Amazon S3 URI, an AWS Systems Manager document (SSM
     document), or a template that you upload.

   If your template is more than 50 KB, upload it to the S3 bucket and
   select that S3 bucket location. For example:
   s3://`bucketname/prefix`.

   ###### Important

   Choose **Template is ready** if you created your
   conformance pack YAML file from scratch based on [Custom
   Conformance Pack](custom-conformance-pack.md "custom-conformance-pack.md").

4. Choose **Next**.
5. On the **Specify conformance pack details** page, enter the
   name for your conformance pack.

The conformance pack name must be a unique name with a maximum of 256
alphanumeric characters. The name can contain hyphens but cannot contain spaces. 6. Optional: Add a parameter.

Parameters are defined in your template and help you manage and organize your
resources. 7. Choose **Next**. 8. On the **Review and deploy** page, review all of the
information.

You can edit the template details and conformance pack details by choosing
**Edit**. 9. Choose **Deploy conformance pack**.

AWS Config displays the conformance pack on the conformance pack page with the
appropriate status.

If your conformance pack deployment fails, check your permissions, verify that
you did the prerequisite steps, and try
again.
Or you can contact AWS Support.

To deploy a **conformance pack using sample template with
remediations**, see the [A. Prerequisites for Using a Conformance
Pack With Remediation](cpack-prerequisites.md#cpack-prerequisites-remediations "cpack-prerequisites.md#cpack-prerequisites-remediations") and then use the preceding
procedure.

To deploy a **conformance pack with one or more AWS Config rules**, see the
[B. Prerequisites for Using a
Conformance Pack With One or More Custom AWS Config Rules](cpack-prerequisites.md#cpack-prerequisites-oneormorerules "cpack-prerequisites.md#cpack-prerequisites-oneormorerules").

Deploy Conformance Packs (AWS CLI)

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
