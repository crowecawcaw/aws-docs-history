# Using Slurm REST API for job management in AWS PCS

## Slurm REST API overview

The Slurm REST API provides programmatic access to cluster management functions through HTTP requests. Understanding these key characteristics will help you effectively use the API with AWS PCS:

- **Access Protocol**: The API uses HTTP (not HTTPS) for communication within your cluster's private network.
- **Connection Details**: Access the API using your cluster's private IP address and the `slurmrestd` port (typically 6820). The full base URL format is `http://`<privateIpAddress>`:6820`.
- **API Versioning**: The API version corresponds to your Slurm installation. For Slurm 25.05, use version **v0.0.43**. The version number changes with each Slurm release. You can find the currently supported API versions in the [Slurm release notes](https://slurm.schedmd.com/release_notes.html "https://slurm.schedmd.com/release_notes.html").
- **URL Structure**: The URL structure for the Slurm REST API is `http://`<privateIpAddress>`:`<port>`/`<api-version>`/`<endpoint>``. Detailed usage information for REST API endpoints can be found in the [Slurm documentation](https://slurm.schedmd.com/rest_api.html "https://slurm.schedmd.com/rest_api.html").

## Prerequisites

Before using the Slurm REST API, ensure you have:

- **Cluster configuration**: AWS PCS cluster with Slurm 25.05+ and REST API enabled.
- **Authentication**: Valid JWT token with proper user identity claims.
- **Network access**: Connectivity within your cluster's VPC with a security group allowing port 6820.

## Procedure

###### To submit a job using the REST API

1. Create a job submission request with the required parameters:

```
{
  "job": {
    "name": "my-job",
    "partition": "compute",
    "nodes": 1,
    "tasks": 1,
    "script": "#!/bin/bash\necho 'Hello from Slurm REST API'"
  }
}
```

2. Submit the job using an HTTP POST request:

```
curl -X POST \
  -H "Authorization: Bearer `<jwt>`" \
  -H "Content-Type: application/json" \
  -d '`<job-json>`' \
  https://`<privateIpAddress>`:6820/slurm/v0.0.43/job/submit
```

3. Note the job ID returned in the response for monitoring purposes.

###### To monitor job status

1. Get information about a specific job:

```
curl -X GET -H "Authorization: Bearer `<jwt>`" \
    https://`<privateIpAddress>`:6820/slurm/v0.0.43/job/`<job-id>`
```

2. List all jobs for the authenticated user:

```
curl -X GET -H "Authorization: Bearer `<jwt>`" \
    https://`<privateIpAddress>`:6820/slurm/v0.0.43/jobs
```

###### To cancel a job

- Send a DELETE request to cancel a specific job:

```
curl -X DELETE -H "Authorization: Bearer `<jwt>`" \
    https://`<privateIpAddress>`:6820/slurm/v0.0.43/job/`<job-id>`
```
