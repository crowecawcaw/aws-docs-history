# Use APIs in Amazon Augmented AI

You can create a human review workflow or a worker task template programmatically. The APIs you use depend on whether you are creating a Amazon Rekognition, Amazon Textract, or custom task type. This topic provides links to API reference documentation for each task type and programming task.

The following APIs can be used with Augmented AI:

**Amazon Augmented AI**

Use the Augmented AI API to start, stop, and delete human review loops. You can also list all human review loops and return information about human review loops in your account.

Learn more about human review loop APIs in the [Amazon Augmented AI Runtime API Reference](../../../augmented-ai/2019-11-07/APIReference/Welcome.md "../../../augmented-ai/2019-11-07/APIReference/Welcome.md").

**Amazon Rekognition**
Use the **HumanLoopConfig** parameter of the
`DetectModerationLabels` API to
initiate
a human review workflow using Amazon Rekognition.

**Amazon SageMaker AI**

Use the Amazon SageMaker API to create a `FlowDefinition`, also known as a
_human review workflow_. You can also create a
`HumanTaskUi` or _worker task template_.

For more information, see the [`CreateFlowDefinition`](../APIReference/API_CreateFlowDefinition.md "../APIReference/API_CreateFlowDefinition.md") or the [`CreateHumanTaskUi`](../APIReference/API_CreateHumanTaskUi.md "../APIReference/API_CreateHumanTaskUi.md") API documentation.

**Amazon Textract**
Use the **HumanLoopConfig** parameter of the [AnalyzeDocument](../../../textract/latest/dg/API_AnalyzeDocument.md "../../../textract/latest/dg/API_AnalyzeDocument.md") API to initiate a human review workflow using
Amazon Textract.

## Programmatic Tutorials

The following tutorials provide example code and step-by-step instructions for creating
human review workflows and worker task templates programmatically.

- [Tutorial: Get Started Using the Amazon A2I API](a2i-get-started-api.md "a2i-get-started-api.md")
- [Create a Human Review Workflow (API)](a2i-create-flow-definition.md#a2i-create-human-review-api "a2i-create-flow-definition.md#a2i-create-human-review-api")
- [Create and Start a Human Loop](a2i-start-human-loop.md "a2i-start-human-loop.md")
- [Using Amazon Augmented AI with Amazon Rekognition](../../../rekognition/latest/dg/a2i-rekognition.md "../../../rekognition/latest/dg/a2i-rekognition.md") in the _Amazon Rekognition Developer Guide_
- [Using Amazon Augmented AI with Amazon Textract AnalyzeDocument](../../../textract/latest/dg/a2i-textract.md "../../../textract/latest/dg/a2i-textract.md") in the _Amazon Textract Developer Guide_
