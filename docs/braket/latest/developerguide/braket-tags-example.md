# Example of AWS CLI tagging in Amazon Braket

When you are working with the AWS Command Line Interface (AWS CLI) to interact with Amazon Braket, the following code is
an example command that demonstrates how to create a tag that applies to a quantum task you
create. In this example, the task is being executed on the SV1 quantum
simulator with parameter settings specified for the Rigetti quantum processing unit (QPU).

It is imporant that inside the example command the tag is specified at the very end, after
all of the other required parameters. In this case, the tag has a **Key**
of `state` and **Value** of `Washington`. These
tags could be used to help categorize or identify this particular quantum task.

```
aws braket create-quantum-task --action /
"{\"braketSchemaHeader\": {\"name\": \"braket.ir.jaqcd.program\", /
    \"version\": \"1\"}, /
    \"instructions\": [{\"angle\": 0.15, \"target\": 0, \"type\": \"rz\"}], /
    \"results\": null, /
    \"basis_rotation_instructions\": null}" /
  --device-arn "arn:aws:braket:::device/quantum-simulator/amazon/sv1" /
  --output-s3-bucket  "my-example-braket-bucket-name" /
  --output-s3-key-prefix "my-example-username"  /
  --shots 100   /
  --device-parameters /
  "{\"braketSchemaHeader\": /
     {\"name\": \"braket.device_schema.rigetti.rigetti_device_parameters\", /
      \"version\": \"1\"}, \"paradigmParameters\": /
       {\"braketSchemaHeader\": /
         {\"name\": \"braket.device_schema.gate_model_parameters\", /
          \"version\": \"1\"}, /
          \"qubitCount\": 2}}" /
          --tags {\"state\":\”Washington\"}
```

This example demonstrates how you can apply tags to your quantum tasks when running them through the
AWS CLI, which is helpful for organizing and tracking your Braket resources.
