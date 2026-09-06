

# Can't override job definition resource requirements
<a name="override-resource-requirements"></a>

The memory and vCPU overrides that are specified in the `memory` and `vcpus` members of the [containerOverrides](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerOverrides.html) structure, which passed to [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html), can't override the memory and vCPU requirements that are specified in the [resourceRequirements](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerProperties.html#Batch-Type-ContainerProperties-resourceRequirements) structure in the job definition.

If you try to override these resource requirements, you might see the following error message:

"This value was submitted in a deprecated key and may conflict with the value provided by the job definition's resource requirements."

To correct this, specify the memory and vCPU requirements in the [resourceRequirements](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerOverrides.html#Batch-Type-ContainerOverrides-resourceRequirements) member of the [containerOverrides](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerOverrides.html). For example, if your memory and vCPU overrides are specified in the following lines.

```
"containerOverrides": {
   "memory": {{8192}},
   "vcpus": {{4}}
}
```

Change them to the following:

```
"containerOverrides": {
   "resourceRequirements": [
      {
         "type": "MEMORY",
         "value": "{{8192}}"
      },
      {
         "type": "VCPU",
         "value": "{{4}}"
      }
   ],
}
```

Do the same change to the memory and vCPU requirements that are specified in the [containerProperties](https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerProperties.html) object in the job definition. For example, if your memory and vCPU requirements are specified in the following lines.

```
{
   "containerProperties": {
      "memory": {{4096}},
      "vcpus": {{2}},
}
```

Change them to the following:

```
"containerProperties": {
   "resourceRequirements": [
      {
         "type": "MEMORY",
         "value": "{{4096}}"
      },
      {
         "type": "VCPU",
         "value": "{{2}}"
      }
   ],
}
```