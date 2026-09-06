

# Apache Airflow Parameter Support
<a name="supported-airflow-parameters"></a>

 Amazon MWAA Serverless leverages Apache Airflow as its workflow orchestration engine and supports YAML workflow definitions that are build using allowlisted [Supported operators](operators.md). To provide the serverless experience using these operators, Amazon MWAA Serverless supports a limited set of [Apache Airflow parameters](https://airflow.apache.org/docs/apache-airflow/3.0.6/core-concepts/params.html). While building your workflow definitions, we recommend you to refer to the follwoing paramter support: 

**Topics**
+ [DAG level parameters that Amazon MWAA Serverless will validate](#dag-object-attributes-validation)
+ [Task level parameters that Amazon MWAA Serverless will validate](#task-object-attributes-validation)
+ [DAG level paramters that are not supported by Amazon MWAA Serverless](#dag-object-attributes-not-supported)
+ [Task level paratmers that are not suppored by Amazon MWAA Serverless](#base-operator-attributes-not-supported)
+ [AWS base operator attributes](#aws-base-operator-attributes)

## DAG level parameters that Amazon MWAA Serverless will validate
<a name="dag-object-attributes-validation"></a>

 The following table lists the supported Apache Airflow DAG level parameters that are subject to validation by Amazon MWAA Serverless during a create or update of workflow. 


| Parameter | Validation Rule | Default Value | 
| --- | --- | --- | 
| dag\_id | Must be a valid, non-empty string |  | 
| schedule | Must be a valid CRON expression format |  | 
| start\_date | Must be in the future |  | 
| end\_date | Must be after or equal to start\_date |  | 
| max\_active\_runs | Must be smaller than account limit. Please refer to [Quotas for Amazon MWAA Serverless](mwaa-serverless-quotas.md) | 16 | 

## Task level parameters that Amazon MWAA Serverless will validate
<a name="task-object-attributes-validation"></a>

 The following table lists the Apache Airflow Task level parameters that are are subject to validation by Amazon MWAA Serverless during a task execution. 


| Parameter | Validation Rule | Default Value | 
| --- | --- | --- | 
| task\_id | Must be a valid string |  | 
| retries | Must be between 0 to 3 | 1 | 
| retry\_delay | Must be between 0 to 300 seconds | 300 seconds | 
| execution\_timeout | Maximum 3600 seconds | 3600 seconds | 

## DAG level paramters that are not supported by Amazon MWAA Serverless
<a name="dag-object-attributes-not-supported"></a>

 The following table lists the Apache Airflow DAG level parameters that are not supported by Amazon MWAA Serverless and will be ignored. 


| Parameter | 
| --- | 
| dag\_id | 
| template\_searchpath | 
| template\_undefined | 
| user\_defined\_macros | 
| user\_defined\_filters | 
| catchup | 
| access\_control | 
| jinja\_environment\_kwargs | 
| render\_template\_as\_native\_obj | 
| tags | 
| owner\_links | 
| auto\_register | 
| fail\_fast | 
| dag\_display\_name | 
| depends\_on\_past | 
| email\_on\_failure | 
| email\_on\_retry | 
| description | 
| max\_consecutive\_failed\_dag\_runs | 
| dagrun\_timeout | 
| sla\_miss\_callback | 
| on\_failure\_callback | 
| on\_success\_callback | 
| is\_paused\_upon\_creation | 

## Task level paratmers that are not suppored by Amazon MWAA Serverless
<a name="base-operator-attributes-not-supported"></a>

 The following table lists the Apache Airflow Task level parameters that are not supported by Amazon MWAA Serverless and will be ignored. 


| Parameter | 
| --- | 
| email\_on\_retry | 
| email\_on\_failure | 
| retry\_exponential\_backoff | 
| depends\_on\_past | 
| ignore\_first\_depends\_on\_past | 
| wait\_for\_downstream | 
| priority\_weight | 
| sla | 
| max\_active\_tis\_per\_dag | 
| max\_active\_tis\_per\_dagrun | 
| task\_concurrency | 
| resources | 
| run\_as\_user | 
| executor\_config | 
| doc | 
| doc\_md | 
| doc\_rst | 
| doc\_json | 
| doc\_yaml | 
| task\_display\_name | 
| logger\_name | 
| allow\_nested\_operators | 
| inlets | 
| outlets | 
| map\_index\_template | 
| email | 
| owner | 
| max\_retry\_delay | 
| on\_execute\_callback | 
| on\_failure\_callback | 
| on\_success\_callback | 
| on\_retry\_callback | 
| on\_skipped\_callback | 
| wait\_for\_past\_depends\_before\_skipping | 
| do\_xcom\_push | 
| multiple\_outputs | 
| start\_date | 
| end\_date | 
| weight\_rule | 
| queue | 
| pool | 
| pool\_slots | 
| pre\_execute | 
| post\_execute | 
| trigger\_rule | 
| executor | 
| task\_group | 
| deferrable | 

## AWS base operator attributes
<a name="aws-base-operator-attributes"></a>


| Parameter | Amazon MWAA | Amazon MWAA Serverless | 
| --- | --- | --- | 
| aws\_conn\_id | Supported | Controlled by service | 
| verify | Supported | Not supported | 
| botocore\_config | Supported | Not supported | 
| region\_name | Supported | Gets Region from environment | 