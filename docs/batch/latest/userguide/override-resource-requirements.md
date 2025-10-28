# Can't override job definition resource

requirements

The memory and vCPU overrides that are specified in the `memory` and
`vcpus` members of the [containerOverrides](../APIReference/API_ContainerOverrides.md "../APIReference/API_ContainerOverrides.md")
structure, which passed to [SubmitJob](../APIReference/API_SubmitJob.md "../APIReference/API_SubmitJob.md"), can't override the memory
and vCPU requirements that are specified in the [resourceRequirements](../APIReference/API_ContainerProperties.md#Batch-Type-ContainerProperties-resourceRequirements "../APIReference/API_ContainerProperties.md#Batch-Type-ContainerProperties-resourceRequirements") structure in the job definition.

If you try to override these resource requirements, you might see the following error
message:

"This value was submitted in a deprecated key and may conflict with the value provided by
the job definition's resource requirements."

To correct this, specify the memory and vCPU requirements in the [resourceRequirements](../APIReference/API_ContainerOverrides.md#Batch-Type-ContainerOverrides-resourceRequirements "../APIReference/API_ContainerOverrides.md#Batch-Type-ContainerOverrides-resourceRequirements") member of the [containerOverrides](../APIReference/API_ContainerOverrides.md "../APIReference/API_ContainerOverrides.md"). For
example, if your memory and vCPU overrides are specified in the following lines.

```
"containerOverrides": {
   "memory": `8192`,
   "vcpus": `4`
}
```

Change them to the following:

```
"containerOverrides": {
   "resourceRequirements": [
      {
         "type": "MEMORY",
         "value": "`8192`"
      },
      {
         "type": "VCPU",
         "value": "`4`"
      }
   ],
}
```

Do the same change to the memory and vCPU requirements that are specified in the [containerProperties](../APIReference/API_ContainerProperties.md "../APIReference/API_ContainerProperties.md") object in the job definition. For example, if your memory and vCPU
requirements are specified in the following lines.

```
{
   "containerProperties": {
      "memory": `4096`,
      "vcpus": `2`,
}
```

Change them to the following:

```
"containerProperties": {
   "resourceRequirements": [
      {
         "type": "MEMORY",
         "value": "`4096`"
      },
      {
         "type": "VCPU",
         "value": "`2`"
      }
   ],
}
```
