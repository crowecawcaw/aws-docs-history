

# Connecting to a Spark Connect session via API
<a name="interactive-sessions-spark-connect-connecting"></a>

Spark Connect provides a thin client interface that you can use to connect to AWS Glue interactive sessions from any environment that supports PySpark. Unlike Livy-based sessions, Spark Connect does not require a Jupyter kernel installation. You can connect directly from a Python script, a notebook, or an IDE such as VS Code.

This topic describes how to create a Spark Connect session, retrieve the connection endpoint, and connect from your local environment.

## Connecting with Boto3 SDK
<a name="spark-connect-pyspark"></a>

Use the AWS SDK for Python (Boto3) to create a session, get the Spark Connect endpoint, and connect using PySpark.

1. Install the required libraries.

   ```
   pip install boto3 "pyspark==3.5.6" pandas pyarrow grpcio grpcio-status
   ```

1. Create an AWS Glue Spark Connect session.

   ```
   import time
   import urllib.parse
   
   import boto3
   from pyspark.sql import SparkSession
   
   glue = boto3.client("glue", region_name="{{us-east-1}}")
   
   glue.create_session(
       Id="{{my-spark-connect-session}}",
       Role="arn:aws:iam::{{123456789012}}:role/{{GlueRole}}",
       Command={"Name": "glueetl"},
       GlueVersion="5.1",
       SessionType="SPARK_CONNECT",
       IdleTimeout=60,
       Timeout=60,
       DefaultArguments={"--language": "python"},
   )
   ```

1. Wait for the session to reach `READY` state. The session typically takes 20–30 seconds to reach `READY` state.

   ```
   session_id = "{{my-spark-connect-session}}"
   while True:
       status = glue.get_session(Id=session_id)["Session"]["Status"]
       if status == "READY":
           break
       time.sleep(10)
   ```

1. Retrieve the Spark Connect endpoint and build the authenticated remote URL.

   ```
   def get_remote_url(glue, session_id):
       """Get endpoint and construct the authenticated remote URL."""
       resp = glue.get_session_endpoint(SessionId=session_id)
       sc = resp["SparkConnect"]
       token = urllib.parse.quote(sc["AuthToken"], safe="")
       return f"{sc['Url']}:443/;use_ssl=true;x-aws-proxy-auth={token}", sc["AuthTokenExpirationTime"]
   
   remote, token_expiry = get_remote_url(glue, session_id)
   ```

   The `get_session_endpoint` response includes:
   + `Url` – The Spark Connect endpoint URL.
   + `AuthToken` – A temporary authentication token for the session.
   + `AuthTokenExpirationTime` – The time at which the token expires, represented as a Unix epoch timestamp.

1. Start the Spark session.

   ```
   spark = SparkSession.builder.remote(remote).getOrCreate()
   spark.version
   ```

1. (Optional) Set up automatic token refresh. The authentication token expires after the duration indicated by `AuthTokenExpirationTime`. Use a background thread to refresh the token before it expires.

   ```
   import threading
   
   def reconnect():
       global spark
       remote, token_expiry = get_remote_url(glue, session_id)
       spark = SparkSession.builder.remote(remote).getOrCreate()
   
       # Schedule next refresh 60 seconds before expiry
       expires_in = token_expiry - time.time()
       delay = max(expires_in - 60, 10)
       timer = threading.Timer(delay, reconnect)
       timer.daemon = True
       timer.start()
   
   # Schedule the first refresh
   expires_in = token_expiry - time.time()
   delay = max(expires_in - 60, 10)
   timer = threading.Timer(delay, reconnect)
   timer.daemon = True
   timer.start()
   ```

1. Read data from the AWS Glue Data Catalog.

   ```
   df = spark.read.table("{{my_database}}.{{my_table}}")
   df.show()
   ```

## Connecting with Spark utilities
<a name="spark-connect-spark-utils"></a>

If you use [Notebooks in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks-spark-connect.html), the `sagemaker-studio` Python library provides Spark utilities that simplify connecting to AWS Glue Spark Connect sessions.

1. Install the `sagemaker-studio` library.

   ```
   pip install sagemaker-studio
   ```

1. Initialize a Spark session using your AWS Glue Spark Connect connection.

   ```
   from sagemaker_studio import sparkutils
   
   spark = sparkutils.init(connection_name="{{my-glue-spark-connection}}")
   ```

1. Read data from the AWS Glue Data Catalog.

   ```
   df = spark.read.table("{{my_database}}.{{my_table}}")
   df.show()
   ```

For more information about the Spark utilities module, see [Spark Utilities](https://pypi.org/project/sagemaker-studio/#spark-utilities) in the `sagemaker-studio` library documentation.