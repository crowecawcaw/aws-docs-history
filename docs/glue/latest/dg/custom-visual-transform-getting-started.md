#

Getting started with custom visual transforms

To create a custom visual transform, you go through the following steps.

- Step 1. Create a JSON config file
- Step 2. Implement the transform logic
- Step 3. Validate the custom visual transform
- Step 4. Update the custom visual transform as needed
- Step 5. Use the custom visual transform in AWS Glue Studio

Get started by setting up the Amazon S3 bucket and continue to **Step 1. Create a JSON config file.**

##

Prerequisites

Customer-supplied transforms reside within a customer AWS account. That account owns the transforms and
therefore has all permissions to view (search and use), edit, or delete them.

In order to use a custom transform in AWS Glue Studio, you will need to create and upload two files to the
Amazon S3 assets bucket in that AWS account:

- **Python file** – contains the transform function
- **JSON file** – describes the transform. This is also known as the config
  file that is required to define the transform.

In order to pair the files together, use the same name for both. For example:

- myTransform.json
- myTransform.py

Optionally, you can give your custom visual transform a custom icon by providing a **SVG file** containing
the icon. In order to pair the files together, use the same name for the icon:

- myTransform.svg

AWS Glue Studio will automatically match them using their respective file names. File names cannot be the same for any existing module.

##

Recommended convention for transform file name

AWS Glue Studio will import your file as module (for example, `import myTransform`) in your job script.
Therefore, your file name must follow the same naming rules set for python variable names (identifiers). Specifically,
they must start with either a letter or an underscore and then be composed entirely of letters, digits, and/or underscores.

###### Note

Ensure your transform file name is not conflicting with existing loaded python modules (for example, `sys, array, copy` etc.)
to avoid unexpected runtime issues.

##

Setting up the Amazon S3 bucket

Transforms you create are stored in Amazon S3 and is owned by your AWS account. You create new custom visual transforms by simply
uploading files (json and py) to the Amazon S3 assets folder where all job scripts are currently stored
(for example, `s3://aws-glue-assets-<accountid>-<region>/transforms`). If using a custom icon, upload it as well.
By default, AWS Glue Studio will read all .json files from the /transforms folder in the same S3 bucket.
