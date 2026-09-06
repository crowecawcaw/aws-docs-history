

# Train a robot manipulation policy with MuJoCo on Deadline Cloud
<a name="examples-jb-mujoco"></a>

The [mujoco\_sim\_to\_policy job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/mujoco_sim_to_policy) on the GitHub website trains and renders a learned robot-manipulation policy on Deadline Cloud using a simulation of the Strands Robots so100 arm in [MuJoCo](https://mujoco.org/) on the MuJoCo website. The job runs three dependent steps on managed GPU workers:

1. **Datagen** — Scripted joint-space pick of a cube in MuJoCo, recorded as a LeRobot dataset. Each episode is verified by a cube-height check and discarded if it fails.

1. **Train** — Finetunes a LeRobot ACT policy on the generated dataset (CUDA).

1. **Render** — Drives a MuJoCo rollout with the finetuned policy and records the result as an MP4 video and PNG frames.

The bundle requires a Linux x86\_64 GPU fleet (steps render headless through EGL and train on CUDA) and a conda queue environment that consumes the `CondaPackages` and `CondaChannels` job parameters. The default conda packages are `python=3.12 pip git ffmpeg` on `conda-forge`.

From the `job_bundles` directory, submit the job:

```
OUT="$(pwd)/output"; mkdir -p "$OUT"
deadline bundle submit mujoco_sim_to_policy -p "OutputDir=$OUT" --yes
```