# AI agent skills for Deadline Cloud

For background on working with AI agents, see
[Using AI agents with Deadline Cloud](ai-agents.md "ai-agents.md"). The
[skills](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/skills "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/skills")
directory on the GitHub website provides the following Deadline Cloud AI agent skills
(`SKILL.md` files) that you can load into an agent so it
follows a known-good procedure:

- [deadline-cloud-job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/skills/deadline-cloud-job "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/skills/deadline-cloud-job")
  — Walks the agent through creating an Open Job Description job bundle for
  Deadline Cloud, optionally with a conda package recipe for custom
  dependencies. Covers designing parameters and steps, writing the
  template, validating with `openjd check`, iterating
  locally with `openjd run --tasks`, and submitting to a
  farm.
- [conda-builder](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/skills/conda-builder "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/skills/conda-builder")
  — Walks the agent through creating or updating a conda recipe that
  uses [rattler-build](https://prefix-dev.github.io/rattler-build/ "https://prefix-dev.github.io/rattler-build/")
  on the prefix.dev website for a DCC, mimicking the structure of existing recipes
  in the samples repository. Recipes build inside an Amazon Linux 2023
  (AL2023) Docker container to match the GLIBC version on
  service-managed fleet workers, and the agent indexes the result
  into a local conda channel for testing. The skill currently covers
  Blender. Per-DCC guides are in the `dcc/`
  subdirectory.
- [host-config-from-installer](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/skills/host-config-from-installer "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/skills/host-config-from-installer")
  — Walks a customer through installing any Windows
  `.exe` software locally, verifying it works, uploading
  the installer to Amazon Simple Storage Service (Amazon S3), and converting the verified
  install steps into a PowerShell host configuration script for
  Windows service-managed fleet workers. Use it when the software isn't
  covered by a more specific skill (for example, the 3ds Max host
  configuration).
