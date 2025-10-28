# Using the Apache Airflow REST API

Amazon Managed Workflows for Apache Airflow (Amazon MWAA) supports interacting with your Apache Airflow environments directly using the Apache Airflow REST API for environments running Apache Airflow v2.4.3 and later. This lets you access and manage your Amazon MWAA environments programmatically, providing a standardized way to invoke data orchestration workflows, manage your DAGs, and monitor the status of various Apache Airflow components such as the metadata database, triggerer, and scheduler.

To support scalability while using the Apache Airflow REST API, Amazon MWAA provides you with the option to horizontally scale webserver capacity to handle increased demand, whether from REST API requests, command line interface (CLI) usage, or more concurrent Apache Airflow user interface (UI) users. For more information about how Amazon MWAA scales webservers, refer to [Configuring Amazon MWAA webserver automatic scaling](mwaa-web-server-autoscaling.md "mwaa-web-server-autoscaling.md").

You can use the Apache Airflow REST API to implement the following use cases for your environments:

- **Programmatic access** – You can now start Apache Airflow DAG runs, manage datasets, and retrieve the status of various components such as the metadata database, triggerers, and schedulers without relying on the Apache Airflow UI or CLI.
- **Integrate with external applications and microservices** – REST API support you can use to build custom solutions that integrate your Amazon MWAA environments with other systems. For example, you can start workflows in response to events from external systems, such as completed database jobs or new user sign-ups.
- **Centralized monitoring** – You can build monitoring dashboards that aggregate the status of your DAGs across multiple Amazon MWAA environments, enabling centralized monitoring and management.
  For more information about the Apache Airflow REST API, refer to the [Apache Airflow REST API Reference](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html "https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html").

By using `InvokeRestApi`, you can access the Apache Airflow REST API using AWS credentials. Alternatively, you can also access it by obtaining a webserver access token and then using the token to call it.

If you encounter an error with the message `Update your environment to use InvokeRestApi` while using the `InvokeRestApi` operation, it indicates that you need to update your Amazon MWAA environment. This error occurs when your Amazon MWAA environment is not compatible with the latest changes related to the `InvokeRestApi` feature. To resolve this issue, update your Amazon MWAA environment to incorporate the necessary changes for the `InvokeRestApi` feature.

The `InvokeRestApi` operation has a default timeout duration of 10 seconds. If the operation does not complete within this 10-second timeframe, it is automatically terminated, and an error is raised. Ensure that your REST API calls are designed to complete within this timeout period to avoid encountering errors.

To support scalability while using the Apache Airflow REST API, Amazon MWAA provides you with the option to horizontally scale web server capacity to handle increased demand, whether from REST API requests, command line interface (CLI) usage, or more concurrent Apache Airflow user interface (UI) users. For more information about how Amazon MWAA scales web servers, refer to [Configuring Amazon MWAA webserver automatic scaling](mwaa-web-server-autoscaling.md "mwaa-web-server-autoscaling.md").

You can use the Apache Airflow REST API to implement the following use cases for your environments:

- **Programmatic access** – You can now start Apache Airflow DAG runs, manage datasets, and retrieve the status of various components such as the metadata database, triggerers, and schedulers without relying on the Apache Airflow UI or CLI.
- **Integrate with external applications and microservices** – REST API support you can use to build custom solutions that integrate your Amazon MWAA environments with other systems. For example, you can start workflows in response to events from external systems, such as completed database jobs or new user sign-ups.
- **Centralized monitoring** – You can build monitoring dashboards that aggregate the status of your DAGs across multiple Amazon MWAA environments, enabling centralized monitoring and management.
  For more information about the Apache Airflow REST API, refer to [The Apache Airflow REST API Reference](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html "https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html").

By using `InvokeRestApi`, you can access the Apache Airflow REST API using AWS credentials. Alternatively, you can also access it by obtaining a web server access token and then using the token to call it.

- If you encounter an error with the message `Update your environment to use InvokeRestApi` while using the `InvokeRestApi` operation, it indicates that you need to update your Amazon MWAA environment. This error occurs when your Amazon MWAA environment is not compatible with the latest changes related to the `InvokeRestApi` feature. To resolve this issue, update your Amazon MWAA environment to incorporate the necessary changes for the `InvokeRestApi` feature.
- The `InvokeRestApi` operation has a default timeout duration of 10 seconds. If the operation does not complete within this 10-second timeframe, it is automatically terminated, and an error is raised. Ensure that your REST API calls are designed to complete within this timeout period to avoid encountering errors.

###### Important

The response payload size cannot exceed 6 MB. Your `RestApi` fails if this limit is exceeded.

Use the following examples to make API calls to the Apache Airflow REST API and start a new DAG run:

###### Topics

- [Granting access to the Apache Airflow REST API: airflow:InvokeRestApi](#granting-access-MWAA-Enhanced-REST-API "#granting-access-MWAA-Enhanced-REST-API")
- [Calling the Apache Airflow REST API](#listing-DAGs-creating-variables-using-restapi-script "#listing-DAGs-creating-variables-using-restapi-script")
- [Creating a webserver session token and calling the Apache Airflow REST API](#create-web-server-session-token "#create-web-server-session-token")

## Granting access to the Apache Airflow REST API: `airflow:InvokeRestApi`

To access the Apache Airflow REST API using AWS credentials, you must grant the `airflow:InvokeRestApi` permission in your IAM policy. In the following policy sample, specify the `Admin`, `Op`, `User`, `Viewer`, or `Public` role in `{airflow-role}` to customize the level of user access. For more information, refer to [Default Roles](https://airflow.apache.org/docs/apache-airflow/1.10.6/security.html?highlight=ldap#default-roles "https://airflow.apache.org/docs/apache-airflow/1.10.6/security.html?highlight=ldap#default-roles") in the _Apache Airflow reference guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowMwaaRestApiAccess",
 "Effect": "Allow",
 "Action": "airflow:InvokeRestApi",
 "Resource": [
 "arn:aws:airflow:`us-east-1`:`111122223333`:role/{your-environment-name}/{airflow-role}"
 ]
 }
 ]
}`

```

###### Note

While configuring a private webserver, the `InvokeRestApi` action cannot be invoked from outside of a Virtual Private Cloud (VPC). You can use the `aws:SourceVpc` key to apply more granular access control for this operation. For more information, refer to [aws:SourceVpc](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpc "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpc").

## Calling the Apache Airflow REST API

This following sample script covers how to use the Apache Airflow REST API to list the available DAGs in your environment and how to create an Apache Airflow variable:

```
import boto3

  env_name = "MyAirflowEnvironment"

  def list_dags(client):
    request_params = {
      "Name": env_name,
      "Path": "/dags",
      "Method": "GET",
      "QueryParameters": {
        "paused": False
      }
    }
  response = client.invoke_rest_api(
    **request_params
  )

  print("Airflow REST API response: ", response['RestApiResponse'])

  def create_variable(client):
    request_params = {
      "Name": env_name,
      "Path": "/variables",
      "Method": "POST",
      "Body": {
        "key": "test-restapi-key",
        "value": "test-restapi-value",
        "description": "Test variable created by MWAA InvokeRestApi API",
      }
    }
  response = client.invoke_rest_api(
    **request_params
  )

  print("Airflow REST API response: ", response['RestApiResponse'])

  if __name__ == "__main__":
    client = boto3.client("mwaa")
    list_dags(client)
    create_variable(client)
```

## Creating a webserver session token and calling the Apache Airflow REST API

To create a webserver access token, use the following Python function. This function first calls the Amazon MWAA API to obtain a web login token. The web login token, which expires after 60 seconds, is then exchanged for a web _session_ token, which lets you access the webserver and use the Apache Airflow REST API. If you require more than 10 transactions per second (TPS) of throttling capacity, you can use this method to access the Apache Airflow REST API.

The session token expires after 12 hours.

###### Tip

Key changes in the following code samples from Apache Airflow v2 to v3 are:

- REST API path changed from `/api/v1` to `/api/v2`
- Login path changed from `/aws_maa/login` to `/pluginsv2/aws_mwaa/login`
- Response from login `response.cookies["_token"]` contains token information that you must use for subsequent API calls
- For a REST API call, you must pass `jwt_token` information in headers as:

```
headers = {
  "Authorization": f"Bearer {jwt_token}",
  "Content-Type": "application/json"
}
```

Apache Airflow v3

```
def get_token_info(region, env_name):
  logging.basicConfig(level=logging.INFO)

  try:
    # Initialize MWAA client and request a web login token
    mwaa = boto3.client('mwaa', region_name=region)
    response = mwaa.create_web_login_token(Name=env_name)

    # Extract the web server hostname and login token
    web_server_host_name = response["WebServerHostname"]
    web_token = response["WebToken"]

    # Construct the URL needed for authentication
    login_url = f"https://{web_server_host_name}/pluginsv2/aws_mwaa/login"
    login_payload = {"token": web_token}

    # Make a POST request to the MWAA login url using the login payload
    response = requests.post(
      login_url,
      data=login_payload,
      timeout=10
    )

    # Check if login was successful
    if response.status_code == 200:

    # Return the hostname and the session cookie
    return (
      web_server_host_name,
      response.cookies['_token']
    )
    else:
      # Log an error
      logging.error("Failed to log in: HTTP %d", response.status_code)
      return None
      except requests.RequestException as e:

      # Log any exceptions raised during the request to the MWAA login endpoint
      logging.error("Request failed: %s", str(e))
      return None
      except Exception as e:

      # Log any other unexpected exceptions
      logging.error("An unexpected error occurred: %s", str(e))
      return None
```

Apache Airflow v2

```
def get_session_info(region, env_name):
  logging.basicConfig(level=logging.INFO)

  try:
      # Initialize MWAA client and request a web login token
      mwaa = boto3.client('mwaa', region_name=region)
      response = mwaa.create_web_login_token(Name=env_name)

      # Extract the web server hostname and login token
      web_server_host_name = response["WebServerHostname"]
      web_token = response["WebToken"]

      # Construct the URL needed for authentication
      login_url = f"https://{web_server_host_name}/aws_mwaa/login"
      login_payload = {"token": web_token}

      # Make a POST request to the MWAA login url using the login payload
      response = requests.post(
          login_url,
          data=login_payload,
          timeout=10
      )

      # Check if login was succesfull
      if response.status_code == 200:

          # Return the hostname and the session cookie
          return (
              web_server_host_name,
              response.cookies["session"]
          )
      else:
          # Log an error
          logging.error("Failed to log in: HTTP %d", response.status_code)
          return None
  except requests.RequestException as e:
       # Log any exceptions raised during the request to the MWAA login endpoint
      logging.error("Request failed: %s", str(e))
      return None
  except Exception as e:
      # Log any other unexpected exceptions
      logging.error("An unexpected error occurred: %s", str(e))
      return None
```

After authentication is complete, you have the credentials to start sending requests to the API endpoints. In the example in the following section, use the endpoint `dags/{dag_name}/dagRuns`.

Apache Airflow v3

```
def trigger_dag(region, env_name, dag_id):
						"""
						Triggers a DAG in a specified MWAA environment using the Airflow REST API.

						Args:
						region (str): AWS region where the MWAA environment is hosted.
						env_name (str): Name of the MWAA environment.
						dag_id (str): ID of the DAG to trigger.
						"""

						logging.info(f"Attempting to trigger DAG {dag_id} in environment {env_name} at region {region}")

						# Retrieve the web server hostname and token for authentication
						try:
						web_server_host_name, jwt_token = get_token_info(region, env_name)
						if not jwt_token:
						logging.error("Authentication failed, no jwt token retrieved.")
						return
						except Exception as e:
						logging.error(f"Error retrieving token info: {str(e)}")
						return

						# Prepare headers and payload for the request
						request_headers = {
						"Authorization": f"Bearer {jwt_token}",
						"Content-Type": "application/json" # Good practice to include, even for GET
						}

						# sample request body input
						json_body = {"logical_date": "2025-09-17T14:15:00Z"}

						# Construct the URL for triggering the DAG
						url = f"https://{web_server_host_name}/api/v2/dags/{dag_id}/dagRuns"

						# Send the POST request to trigger the DAG
						try:
						response = requests.post(url, headers=request_headers, json=json_body)
						# Check the response status code to determine if the DAG was triggered successfully
						if response.status_code == 200:
						logging.info("DAG triggered successfully.")
						else:
						logging.error(f"Failed to trigger DAG: HTTP {response.status_code} - {response.text}")
						except requests.RequestException as e:
						logging.error(f"Request to trigger DAG failed: {str(e)}")

						if __name__ == "__main__":
						logging.basicConfig(level=logging.INFO)

						# Check if the correct number of arguments is provided
						if len(sys.argv) != 4:
						logging.error("Incorrect usage. Proper format: python script_name.py {region} {env_name} {dag_id}")
						sys.exit(1)

						region = sys.argv[1]
						env_name = sys.argv[2]
						dag_id = sys.argv[3]

						# Trigger the DAG with the provided arguments
						trigger_dag(region, env_name, dag_id)
```

Apache Airflow v2

```
def trigger_dag(region, env_name, dag_name):
						"""
						Triggers a DAG in a specified MWAA environment using the Airflow REST API.

						Args:
						region (str): AWS region where the MWAA environment is hosted.
						env_name (str): Name of the MWAA environment.
						dag_name (str): Name of the DAG to trigger.
						"""

						logging.info(f"Attempting to trigger DAG {dag_name} in environment {env_name} at region {region}")

						# Retrieve the web server hostname and session cookie for authentication
						try:
						web_server_host_name, session_cookie = get_session_info(region, env_name)
						if not session_cookie:
						logging.error("Authentication failed, no session cookie retrieved.")
						return
						except Exception as e:
						logging.error(f"Error retrieving session info: {str(e)}")
						return

						# Prepare headers and payload for the request
						cookies = {"session": session_cookie}
						json_body = {"conf": {}}

						# Construct the URL for triggering the DAG
						url = f"https://{web_server_host_name}/api/v1/dags/{dag_id}/dagRuns"

						# Send the POST request to trigger the DAG
						try:
						response = requests.post(url, cookies=cookies, json=json_body)
						# Check the response status code to determine if the DAG was triggered successfully
						if response.status_code == 200:
						logging.info("DAG triggered successfully.")
						else:
						logging.error(f"Failed to trigger DAG: HTTP {response.status_code} - {response.text}")
						except requests.RequestException as e:
						logging.error(f"Request to trigger DAG failed: {str(e)}")

						if __name__ == "__main__":
						logging.basicConfig(level=logging.INFO)

						# Check if the correct number of arguments is provided
						if len(sys.argv) != 4:
						logging.error("Incorrect usage. Proper format: python script_name.py {region} {env_name} {dag_name}")
						sys.exit(1)

						region = sys.argv[1]
						env_name = sys.argv[2]
						dag_name = sys.argv[3]

						# Trigger the DAG with the provided arguments
						trigger_dag(region, env_name, dag_name)

```
