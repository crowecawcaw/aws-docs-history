# Export a model card

Follow these steps to export a model card.

1. Go to the Amazon SageMaker Model Card console.
2. Choose the name of the model card you want to export.
3. In the model card overview, choose **Actions** and then
   **Export PDF**.
4. Enter an S3 URI or browse available S3 buckets for your model card
   PDF.
5. If your model card exports successfully, you can either choose
   **Download PDF** in the resulting banner or download
   your PDF directly from Amazon S3.
   You can export a model card in the SageMaker Python SDK by specifying an S3 output path and export your model card PDF to it with the following
   commands:

```
s3_output_path = f"s3://`{bucket}`/`{prefix}`/export"
pdf_s3_url = `my_card`.export_pdf(s3_output_path=s3_output_path).delete()
```
