# Test GPU functionality

The following example job definition tests if the GPU workload AMI described in [Use a GPU workload AMI](batch-gpu-ami.md "batch-gpu-ami.md") is configured properly. This example job definition runs the
TensorFlow deep MNIST classifier [example](https://github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/examples/tutorials/mnist/mnist_deep.py "https://github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/examples/tutorials/mnist/mnist_deep.py") from GitHub.

```
{
    "containerProperties": {
        "image": "tensorflow/tensorflow:1.8.0-devel-gpu",
        "resourceRequirements": [
            {
                "type": "MEMORY",
                "value": "32000"
            },
            {
                "type": "VCPU",
                "value": "8"
            }
        ],
        "command": [
            "sh",
            "-c",
            "cd /tensorflow/tensorflow/examples/tutorials/mnist; python mnist_deep.py"
        ]
    },
    "type": "container",
    "jobDefinitionName": "tensorflow_mnist_deep"
}
```

You can create a file with the preceding JSON text called `tensorflow_mnist_deep.json` and
then register an AWS Batch job definition with the following command:

```
`aws batch register-job-definition --cli-input-json file://tensorflow_mnist_deep.json`
```
