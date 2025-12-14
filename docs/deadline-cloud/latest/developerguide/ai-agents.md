# Using AI agents with Deadline Cloud

Use AI agents to write job bundles, develop conda packages, and troubleshoot jobs in Deadline Cloud.
This topic explains what AI agents are, key points for working with them effectively, and
resources to help agents understand Deadline Cloud.

An AI agent is a software tool that uses a large language model (LLM) to perform tasks
autonomously. AI agents can read and write files, run commands, and iterate on solutions based
on feedback. Examples include command-line tools like [Kiro](https://kiro.dev "https://kiro.dev")
and IDE-integrated assistants.

**Key points for working with AI agents**

The following key points help you get better results when you use AI agents with
Deadline Cloud.

- **Provide grounding** – AI agents perform best when
  they have access to relevant documentation, specifications, and examples. You can provide
  grounding by pointing the agent to specific documentation pages, sharing existing example
  code as references, cloning relevant open source repositories into the local workspace,
  and providing documentation for third-party applications.
- **Specify success criteria** – Define the expected
  outcome and technical requirements for the agent. For example, when you ask an agent to
  develop a job bundle, specify the job inputs, parameters, and expected outputs. If you're
  unsure about the specifications, ask the agent to propose options first, then refine the
  requirements together.
- **Enable a feedback loop** – AI agents iterate more
  effectively when they can test their solutions and receive feedback. Instead of expecting
  a working solution on the first attempt, give the agent the ability to run its solution
  and review the results. This approach works well when the agent can access status updates,
  logs, and validation errors. For example, when you develop a job bundle, allow the agent
  to submit the job and review the logs.
- **Expect to iterate** – Even with good context, agents
  can get off track or make assumptions that don't match your environment. Observe how the
  agent approaches the task and provide guidance along the way. Add missing context if the
  agent struggles, help find errors by pointing to specific log files, refine requirements
  as you discover them, and add negative requirements to explicitly state what the agent
  should avoid.
  **Resources for agent context**

The following resources help AI agents understand Deadline Cloud concepts and produce accurate
output.

- **Deadline Cloud Model Context Protocol (MCP) server** – For agents that support the
  Model Context Protocol, the [deadline-cloud](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud") repository
  contains the Deadline Cloud client which includes an MCP server for interacting with jobs.
- **AWS Documentation MCP server** – For agents that
  support MCP, configure the [AWS
  Documentation MCP server](https://github.com/awslabs/mcp/tree/main/src/aws-documentation-mcp-server "https://github.com/awslabs/mcp/tree/main/src/aws-documentation-mcp-server") to give the agent direct access to AWS documentation,
  including the Deadline Cloud User Guide and Developer Guide.
- **Open Job Description specification** – The [Open Job Description
  specification](https://github.com/OpenJobDescription/openjd-specifications "https://github.com/OpenJobDescription/openjd-specifications") on GitHub defines the schema for job templates. Reference this
  repository when agents need to understand the structure and syntax of job
  templates.
- **deadline-cloud-samples** – The [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples")
  repository contains sample job bundles, conda recipes, and CloudFormation templates for
  common applications and use cases.
- **aws-deadline GitHub organization** – The [aws-deadline](https://github.com/aws-deadline/ "https://github.com/aws-deadline/") GitHub organization contains
  reference plugins for many third-party applications that you can use as examples for
  other integrations.
  **Example prompt: Writing a job bundle**

The following example prompt demonstrates how to use an AI agent to create job bundles
that train a LoRA (Low-Rank Adaptation) adapter for generating AI images. The prompt
illustrates the key points discussed earlier: it provides grounding by pointing to relevant
repositories, defines success criteria for the job bundle outputs, and outlines a feedback
loop for iterative development.

```
Write a pair of job bundles for Deadline Cloud that use the diffusers Python library to train a LoRA adapter on a set of images and then generate images from it.

Requirements:
- The training job takes a set of JPEG images as input, uses an image description, LoRA rank, learning rate, batch size, and number of training steps as parameters, and outputs a `.safetensors` file.
- The generation job takes the `.safetensors` file as input and the number of images to generate, then outputs JPEG images. The jobs use Stable Diffusion 1.5 as the base model.
- The jobs run `diffusers` as a Python script. Install the necessary packages using conda by setting the job parameters:
    - `CondaChannels`: `conda-forge`
    - `CondaPackages`: list of conda packages to install

For context, clone the following repositories to your workspace and review their documentation and code:
- OpenJobDescription specification: https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/wiki/2023-09-Template-Schemas.md
- Deadline Cloud sample job bundles: https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles
- diffusers library: https://github.com/huggingface/diffusers

Read through the provided context before you start. To develop a job bundle, iterate with the following steps until the submitted job succeeds. If a step fails, update the job bundle and restart the loop:
1. Create a job bundle.
2. Validate the job template syntax: `openjd check`
3. Submit the job to Deadline Cloud: `deadline bundle submit`
4. Wait for the job to complete: `deadline job wait`
5. View the job status and logs: `deadline job logs`
6. Download the job output: `deadline job download-output`

To verify the training and generation jobs work together, iterate with the following steps until the generation job produces images that resemble the dog in the training data:
1. Develop and submit a training job using the training images in `./exdog`
2. Wait for the job to succeed then download its output.
3. Develop and submit a generation job using the LoRA adapter from the training job.
4. Wait for the job to succeed then download its output.
5. Inspect the generated images. If they resemble the dog in the training data, you're done. Otherwise, review the job template, job parameters, and job logs to identify and fix the issue.
```
