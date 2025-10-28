#

Step 3. Validate and troubleshoot custom visual transforms in AWS Glue Studio

AWS Glue Studio validates the JSON config file before custom visual transforms are loaded into AWS Glue Studio.
Validation includes:

- Presence of required fields
- JSON format validation
- Incorrect or invalid parameters
- Presence of both the .py and .json files in the same Amazon S3 path
- Matching filenames for the .py and .json

If validation succeeds, the transform is listed in the list of available **Actions** in the visual editor.
If a custom icon has been provided, it should be visible beside the **Action**.

If validation fails, AWS Glue Studio does not load the custom visual transform.
