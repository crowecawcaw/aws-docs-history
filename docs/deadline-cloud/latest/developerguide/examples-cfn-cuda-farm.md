# Deploy a Deadline Cloud CUDA farm with CloudFormation

The cuda\_farm CloudFormation template deploys a Deadline Cloud farm that you can use to
run CUDA jobs. The default configuration includes a queue for CUDA jobs, a
second queue for building conda packages, and a CUDA-capable fleet. For the
template source, see
[cuda\_farm](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm")
on the GitHub website.

This template specializes the [Deploy a starter Deadline Cloud farm with CloudFormation](examples-cfn-starter-farm.md "examples-cfn-starter-farm.md")
template for the CUDA use case:

- The default `CondaChannels` value is
  `deadline-cloud conda-forge`, which makes CUDA compilers,
  frameworks like PyTorch, and applications like COLMAP available.
- The Linux CUDA fleet is required, and the Windows and Linux CPU
  fleets are removed.
  This template provisions the infrastructure that the
  [Train 3D Gaussian Splatting from video on Deadline Cloud](examples-jb-gaussian-splatting.md "examples-jb-gaussian-splatting.md") and
  [Benchmark LLMs with vLLM and lm-evaluation-harness on Deadline Cloud](examples-jb-vllm-leaderboard.md "examples-jb-vllm-leaderboard.md") job bundles need.
