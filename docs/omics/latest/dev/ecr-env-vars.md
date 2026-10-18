

# Environment variables for HealthOmics workflows
<a name="ecr-env-vars"></a>

HealthOmics provides environment variables that have information about the workflow running in the container. You can use the values of these variables in the logic of your workflow tasks.

All HealthOmics workflow variables except `AWS_REGION` and `AWS_HEALTHOMICS_RESOURCE_TYPE` start with the `AWS_WORKFLOW_` prefix. This prefix is a protected environment variable prefix. Don't use this prefix for your own variables in workflow containers. 

HealthOmics provides the following workflow environment variables:

**AWS\_HEALTHOMICS\_RESOURCE\_TYPE**  
This variable is the accelerator type of the active resource profile, or `cpu` for a CPU-only profile. HealthOmics sets this variable for tasks that use the `omicsResourceFallbackOrder` directive. For more information, see [Environment variables](advanced-resource-configuration.md#advanced-resource-configuration-environment-variables) in [Advanced resource configuration](advanced-resource-configuration.md).

**AWS\_REGION**  
This variable is the region where the container is running.

**AWS\_WORKFLOW\_RUN**  
This variable is the name of the current run.

**AWS\_WORKFLOW\_RUN\_ID**  
This variable is the run identifier of the current run.

**AWS\_WORKFLOW\_RUN\_UUID**  
This variable is the run UUID of the current run.

**AWS\_WORKFLOW\_TASK**  
This variable is the name of the current task.

**AWS\_WORKFLOW\_TASK\_ID**  
This variable is the task identifier of the current task.

**AWS\_WORKFLOW\_TASK\_UUID**  
This variable is the task UUID of the current task.

The following example shows typical values for each environment variable:

```
AWS Region: us-east-1
Workflow Run: arn:aws:omics:us-east-1:123456789012:run/6470304
Workflow Run ID: 6470304
Workflow Run UUID: a1b2c3d4-5678-90ab-cdef-EXAMPLE22222
Workflow Task: arn:aws:omics:us-east-1:123456789012:task/4192063
Workflow Task ID: 4192063
Workflow Task UUID: a1b2c3d4-5678-90ab-cdef-EXAMPLE33333
```