# Import design documents

Design documents provide additional architectural context that the next generation of Resilience Hub uses during
failure mode assessments. You can upload design documents stored in Amazon S3 as input sources for
your service.

###### To import a design document (console)

1. Open the Next generation Resilience Hub console and navigate to your service.
2. Choose the **Assessments** tab.
3. Choose **Failure mode guidance**.
4. Choose **Add more** from Architecture design files.
5. Enter the Amazon S3 URL of your design document.
6. Choose **Save design file**.

###### To import a design document (AWS CLI)

- Run the following command:

```

aws resiliencehubv2 create-input-source \
  --service-arn "`service-arn`" \
  --resource-configuration '{"designFileS3Url": "s3://`bucket`/`path/to/design-doc.pdf`"}'

```

Supported design document formats include PDF, Markdown, and plain text files. The AI
assessment engine uses these documents to understand your intended architecture and identify
gaps between design intent and actual implementation.
