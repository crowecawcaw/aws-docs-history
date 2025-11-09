# Service environment state

definitions

Service environments can be in one of four possible states that indicate their current
operational status and readiness to process SageMaker Training jobs. Each state represents
a specific phase in the service environment lifecycle, from initial creation through
operational readiness to eventual deletion. The following table describes each state and
its meaning:

| State      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATING` | The initial state when you create a service environment. During<br>this state, AWS Batch validates the configuration parameters and<br>establishes integration with SageMaker AI services. The service environment<br>cannot process jobs, and any job queues associated with it will not<br>accept service job submissions. The creation process typically<br>completes within a few seconds for properly configured service<br>environments.              |
| `VALID`    | The operational state indicating that the service environment has<br>passed all configuration validation checks and is ready to process<br>SageMaker Training jobs. This state indicates that the service<br>environment configuration is correct, all required permissions are<br>in place, and AWS Batch can successfully submit jobs to SageMaker AI on your<br>behalf. Service environments spend most of their operational<br>lifecycle in this state. |
| `INVALID`  | A state indicating that the service environment has encountered a<br>configuration or permissions issue that prevents it from processing<br>SageMaker Training jobs. Job queues associated with invalid service environments cannot<br>process new service job submissions until the underlying issues are<br>resolved.                                                                                                                                     |
| `DELETING` | The state that occurs when you request deletion of a service<br>environment. During this state, AWS Batch ensures that no active<br>SageMaker Training jobs are associated with the environment and<br>performs necessary cleanup operations. Service environments in this<br>state cannot process new job submissions, and the deletion process<br>completes once all associated resources are properly cleaned<br>up.                                     |

## Service environment state

transitions

Service environment state transitions occur automatically based on configuration
changes, validation results, and operational health monitoring. The AWS Batch service
continuously monitors service environment health and updates states accordingly.
Understanding these transitions helps you anticipate when configuration changes will
take effect and how to resolve issues that cause invalid states.

After successful creation and validation, service environments transition from
`CREATING` to `VALID`. This transition confirms that all
configuration parameters are correct, required IAM permissions are properly
configured, and the service environment can successfully integrate with SageMaker AI
services. Once in the `VALID` state, associated job queues can begin
processing service job submissions.

Service environments transition from `VALID` to `INVALID`
when configuration validation fails or when dependencies become unavailable. This
can occur due to IAM role modifications, capacity limit changes that violate
quotas, or external resource modifications that affect the service environment's
ability to function. The status reason field provides specific details about what
caused the invalid state.

Service environments can transition back to `VALID` from
`INVALID` once the underlying issues are resolved. This might involve
updating IAM permissions, correcting capacity configurations, or restoring access
to required AWS resources. The transition typically occurs automatically once
AWS Batch detects that the configuration issues have been addressed.
