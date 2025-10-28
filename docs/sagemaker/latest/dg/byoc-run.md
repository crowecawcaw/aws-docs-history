# Run Your Processing Container Using the SageMaker AI Python

SDK

You can use the SageMaker Python SDK to run your own processing image by using the
`Processor` class. The following example shows how to run your own
processing container with one input from Amazon Simple Storage Service (Amazon S3) and one output to
Amazon S3.

```
from sagemaker.processing import Processor, ProcessingInput, ProcessingOutput

processor = Processor(image_uri='<your_ecr_image_uri>',
                     role=role,
                     instance_count=1,
                     instance_type="ml.m5.xlarge")

processor.run(inputs=[ProcessingInput(
                        source='<s3_uri or local path>',
                        destination='/opt/ml/processing/input_data')],
                    outputs=[ProcessingOutput(
                        source='/opt/ml/processing/processed_data',
                        destination='<s3_uri>')],
                    )
```

Instead of building your processing code into your processing image, you can
provide a `ScriptProcessor` with your image and the command that you want
to run, along with the code that you want to run inside that container. For an
example, see [Run Scripts with Your Own Processing
Container](processing-container-run-scripts.md "processing-container-run-scripts.md").

You can also use the scikit-learn image that Amazon SageMaker Processing provides through
`SKLearnProcessor` to run scikit-learn scripts. For an example, see
[Run a Processing Job with scikit-learn](use-scikit-learn-processing-container.md "use-scikit-learn-processing-container.md").
