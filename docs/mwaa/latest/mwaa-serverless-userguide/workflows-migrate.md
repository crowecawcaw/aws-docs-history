# Convert Python DAG to YAML definition

Amazon MWAA Serverless provides a Python to YAML DAG converter tool that helps convert you Python based DAG to YAML based definition that is ready to create a Amazon MWAA Serverless workflow. Refer to the following steps to convert your Python based DAGs to YAML based definition using AWS CLI:

CLI

1. Install the library ([dag-converter](https://pypi.org/project/python-to-yaml-dag-converter-mwaa-serverless/ "https://pypi.org/project/python-to-yaml-dag-converter-mwaa-serverless/")):

```

pip install python-to-yaml-dag-converter-mwaa-serverless

```

2. (Optional) If your Python DAG files are in S3, copy them locally:

```

aws s3 cp s3://source-bucket/dags/source.py/ `my-local-folder/`source`.py`

```

3. Run following command. This tool only converts Python based DAG files and provides an output file ``dag_id`.yml`

```

dag-converter convert `my-local-folder/source.py` --output `/output_yaml/destination`

```

###### Important

A single Python DAG file can potentially create multiple YAML definitions workflows. 4. Move the YAML workflow to an Amazon S3 location.

```
aws s3 cp /`output_yaml`/`dag_id`.yml s3://`destination-bucket`/dags/`ddag_id`.yml
```

5. Refer to [Workflows](workflows.md "workflows.md") for steps to create Amazon MWAA Serverless workflows
