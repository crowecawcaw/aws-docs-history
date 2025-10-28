#

Converting a script or notebook into an AWS Glue job

There are two ways you can convert a script or notebook into an AWS Glue job:

- Use **nbconvert** to convert your Jupyter `.ipynb` notebook document file into a
  `.py` file. For more information, see
  [nbconvert: Convert Notebooks to other formats](https://nbconvert.readthedocs.io/en/latest/ "https://nbconvert.readthedocs.io/en/latest/").
- Upload the file to AWS Glue Studio Notebooks.
  - In the AWS Glue Studio console, choose **Jobs** from the navigation menu.
  - In the **Create job** section, choose **Jupyter Notebook**.
  - In the **Options** section, choose **Upload and edit an existing notebook**.
  - Select **Choose file** to upload an `.ipynb` file.
