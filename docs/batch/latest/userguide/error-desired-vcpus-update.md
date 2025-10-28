# Error message when you update the

`desiredvCpus` setting

You see the following error message when you use the AWS Batch API to update the desired
vCPUs (`desiredvCpus`) setting.

`Manually scaling down compute environment is not supported. Disconnecting job queues
 from compute environment will cause it to scale-down to minvCpus`.

This issue occurs if the updated `desiredvCpus` value is less than the current
`desiredvCpus` value. When you update the `desiredvCpus` value, both of
the following must be true:

- The `desiredvCpus` value must be between the `minvCpus` and
  `maxvCpus` values.
- The updated `desiredvCpus` value must be greater than or equal to the current
  `desiredvCpus` value.
