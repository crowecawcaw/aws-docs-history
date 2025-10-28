# Running a Spark application with Apache Livy for Amazon EMR on EKS

Before you can run a Spark application with Apache Livy, make sure that you have completed the steps in
[Setting up Apache Livy for Amazon EMR on EKS](job-runs-apache-livy-setup.md "job-runs-apache-livy-setup.md")
and [Getting started with Apache Livy for Amazon EMR on EKS](job-runs-apache-livy-install.md "job-runs-apache-livy-install.md").

You can use Apache Livy to run two types of applications:

- Batch sessions – a type of Livy workload to submit Spark batch jobs.
- Interactive sessions – a type of Livy workload that provides a programmatic and visual interface to run Spark queries.

###### Note

Driver and executor pods from different sessions can communicate with each other. Namespaces don't guarantee any security between pods. Kubernetes doesn't allow
selective permissions on a subset of pods inside a given namespace.

## Running batch sessions

To submit a batch job, use the following command.

```
curl -s -k -H 'Content-Type: application/json' -X POST \
      -d '{
            "name": "my-session",
            "file": "entryPoint_location (S3 or local)",
            "args": ["argument1", "argument2", ...],
            "conf": {
                "spark.kubernetes.namespace": "`<spark-namespace>`",
                "spark.kubernetes.container.image": "public.ecr.aws/emr-on-eks/spark/emr-7.10.0:latest",
                "spark.kubernetes.authenticate.driver.serviceAccountName": "`<spark-service-account>`"
            }
          }' `<livy-endpoint>`/batches
```

To monitor your batch job, use the following command.

```
curl -s -k -H 'Content-Type: application/json' -X GET `<livy-endpoint>`/batches/my-session
```

## Running interactive sessions

To run interactive sessions with Apache Livy, see the following steps.

1. Make sure you have access to either a self-hosted or a managed Jupyter notebook, such as a
   SageMaker AI Jupyter notebook. Your jupyter notebook must
   have [sparkmagic](https://github.com/jupyter-incubator/sparkmagic/blob/master/README.md "https://github.com/jupyter-incubator/sparkmagic/blob/master/README.md") installed.
2. Create a bucket for Spark configuration `spark.kubernetes.file.upload.path`. Make sure the Spark service account
   has read and write access to the bucket. For more details on how to configure your spark service account, see Setting up
   access permissions with IAM roles for service accounts (IRSA)
3. Load sparkmagic in the Jupyter notebook with the command `%load_ext sparkmagic.magics`.
4. Run the command `%manage_spark` to set up your Livy endpoint with the Jupyter notebook. Choose the **Add Endpoints** tab, choose the configured auth type, add the Livy endpoint to the notebook, and then choose **Add endpoint**.
5. Run `%manage_spark` again to create the Spark context and then go to the **Create session**. Choose the Livy endpoint, specify a unique session name
   choose a language, and then add the following properties.

```
{
  "conf": {
    "spark.kubernetes.namespace": "`livy-namespace`",
    "spark.kubernetes.container.image": "public.ecr.aws/emr-on-eks/spark/emr-7.10.0:latest",
    "spark.kubernetes.authenticate.driver.serviceAccountName": "`<spark-service-account>`",
    "spark.kubernetes.file.upload.path": "`<URI_TO_S3_LOCATION_>`"
  }
}
```

6. Submit the application and wait for it to create the Spark context.
7. To monitor the status of the interactive session, run the following command.

```
curl -s -k -H 'Content-Type: application/json' -X GET `livy-endpoint`/sessions/my-interactive-session
```

## Monitoring Spark applications

To monitor the progress of your Spark applications with the Livy UI, use the link `http://<livy-endpoint>/ui`.
