# Job bundle examples for Deadline Cloud

A job bundle groups an Open Job Description template with the files and
metadata that AWS Deadline Cloud needs to run a job. The
[job\_bundles](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles")
directory in the deadline-cloud-samples repository provides ready-to-submit
bundles that you can use as starting points for your own work.

The following sections describe each example. Submit any example with the
Deadline Cloud CLI:

```
deadline bundle submit `bundle-directory`
```

Or open the GUI submitter:

```
deadline bundle gui-submit `bundle-directory`
```

###### Topics

- [Render Blender scenes on Deadline Cloud](examples-jb-blender-render.md "examples-jb-blender-render.md")
- [Render Autodesk Maya scenes on Deadline Cloud](examples-jb-maya-render.md "examples-jb-maya-render.md")
- [Render Arnold .ass files on Deadline Cloud](examples-jb-arnold-render.md "examples-jb-arnold-render.md")
- [Render USD scenes with Houdini Husk on Deadline Cloud](examples-jb-houdini-husk-usd.md "examples-jb-houdini-husk-usd.md")
- [Render Foundry Nuke scripts on Deadline Cloud](examples-jb-nuke-render.md "examples-jb-nuke-render.md")
- [Render Autodesk 3ds Max scenes with V-Ray on Deadline Cloud](examples-jb-3dsmax-vray-denoiser.md "examples-jb-3dsmax-vray-denoiser.md")
- [Render KeyShot scenes on Deadline Cloud](examples-jb-keyshot.md "examples-jb-keyshot.md")
- [Render Autodesk VRED scenes on Deadline Cloud](examples-jb-vred-render.md "examples-jb-vred-render.md")
- [Render Adobe After Effects projects on Deadline Cloud](examples-jb-aftereffects.md "examples-jb-aftereffects.md")
- [Render V-Ray standalone scenes on Deadline Cloud](examples-jb-vray-render.md "examples-jb-vray-render.md")
- [Render Redshift scenes on Deadline Cloud](examples-jb-redshift.md "examples-jb-redshift.md")
- [Render POV-Ray 3.7 scenes on Deadline Cloud](examples-jb-povray.md "examples-jb-povray.md")
- [Tile rendering on Deadline Cloud](examples-jb-tile-rendering.md "examples-jb-tile-rendering.md")
- [Group frames into chunks with task chunking on Deadline Cloud](examples-jb-task-chunking.md "examples-jb-task-chunking.md")
- [Encode video with FFmpeg on Deadline Cloud](examples-jb-ffmpeg-encode.md "examples-jb-ffmpeg-encode.md")
- [Render a turntable video with Maya and Arnold on Deadline Cloud](examples-jb-turntable.md "examples-jb-turntable.md")
- [Run a Monte Carlo simulation on Deadline Cloud](examples-jb-monte-carlo.md "examples-jb-monte-carlo.md")
- [Train 3D Gaussian Splatting from video on Deadline Cloud](examples-jb-gaussian-splatting.md "examples-jb-gaussian-splatting.md")
- [Train and use a FLUX.2 Klein LoRA on Deadline Cloud](examples-jb-flux-lora.md "examples-jb-flux-lora.md")
- [Benchmark LLMs with vLLM and lm-evaluation-harness on Deadline Cloud](examples-jb-vllm-leaderboard.md "examples-jb-vllm-leaderboard.md")
- [Run batch LLM inference with vLLM on Deadline Cloud](examples-jb-vllm-batch.md "examples-jb-vllm-batch.md")
- [Generate images in batch with a diffusion model on Deadline Cloud](examples-jb-text-to-image-batch.md "examples-jb-text-to-image-batch.md")
- [Fine-tune Hugging Face LLMs with LoRA on Deadline Cloud](examples-jb-hf-finetune-lora.md "examples-jb-hf-finetune-lora.md")
- [Predict protein structures with ESMFold on Deadline Cloud](examples-jb-esmfold.md "examples-jb-esmfold.md")
- [Classify satellite imagery in parallel on Deadline Cloud](examples-jb-satellite-classification.md "examples-jb-satellite-classification.md")
- [Run GROMACS molecular dynamics simulations on Deadline Cloud](examples-jb-gromacs.md "examples-jb-gromacs.md")
- [Run virtual screening with AutoDock Vina on Deadline Cloud](examples-jb-virtual-screening.md "examples-jb-virtual-screening.md")
- [Generate procedural 3D scenes with Infinigen on Deadline Cloud](examples-jb-infinigen.md "examples-jb-infinigen.md")
- [Train a robot manipulation policy with MuJoCo on Deadline Cloud](examples-jb-mujoco.md "examples-jb-mujoco.md")
- [Run autonomous driving simulations with CARLA on Deadline Cloud](examples-jb-carla.md "examples-jb-carla.md")
- [Publish renders to Autodesk Flow Production Tracking from Deadline Cloud](examples-jb-blender-turntable-flow.md "examples-jb-blender-turntable-flow.md")
- [Run VTK visualization scripts on Deadline Cloud](examples-jb-vtk.md "examples-jb-vtk.md")
- [Encode a movie from another Deadline Cloud job's output with FFmpeg](examples-jb-ffmpeg-from-job.md "examples-jb-ffmpeg-from-job.md")
- [Run a bash script on Deadline Cloud](examples-jb-cli-job.md "examples-jb-cli-job.md")
- [Use every Open Job Description GUI control on Deadline Cloud](examples-jb-gui-controls.md "examples-jb-gui-controls.md")
- [Use job environments on Deadline Cloud](examples-jb-job-environments.md "examples-jb-job-environments.md")
- [Job attachment tutorial bundles for Deadline Cloud](examples-jb-job-attachments-tutorial.md "examples-jb-job-attachments-tutorial.md")
- [Develop a job bundle through four stages on Deadline Cloud](examples-jb-job-progression.md "examples-jb-job-progression.md")
- [List available conda packages on Deadline Cloud](examples-jb-list-conda-packages.md "examples-jb-list-conda-packages.md")
- [Copy an S3 prefix to job attachments on Deadline Cloud](examples-jb-copy-s3-to-attachments.md "examples-jb-copy-s3-to-attachments.md")
- [SSH or RDP to a Deadline Cloud worker through Session Manager](examples-jb-ssh-to-worker.md "examples-jb-ssh-to-worker.md")
- [Build a custom submitter for Deadline Cloud](examples-jb-custom-submitters.md "examples-jb-custom-submitters.md")
