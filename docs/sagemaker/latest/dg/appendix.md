

# Appendix
<a name="appendix"></a>

Use the following information to get information about monitoring and analyzing training results.

## Monitor training results
<a name="monitor-training-results"></a>

Monitoring and analyzing training results is essential for developers to assess convergence and troubleshoot issues. SageMaker HyperPod recipes offer Tensorboard integration to analyze training behavior. To address the challenges of profiling large distributed training jobs, these recipes also incorporate VizTracer. VizTracer is a low-overhead tool for tracing and visualizing Python code execution. For more information about VizTracer, see [VizTracer](https://viztracer.readthedocs.io/en/latest/installation.html).

The following sections guide you through the process of implementing these features in your SageMaker HyperPod recipes.

### Tensorboard
<a name="tensorboard"></a>

Tensorboard is a powerful tool for visualizing and analyzing the training process. To enable Tensorboard, modify your recipe by setting the following parameter:

```
exp_manager:
  exp_dir: null
  name: experiment
  create_tensorboard_logger: True
```

After you enable the Tensorboard logger, the training logs are generated and stored within the experiment directory. The experiment directed is defined in exp\_manager.exp\_dir. To access and analyze these logs locally, use the following procedure:

**To access and analyze logs**

1. Download the Tensorboard experiment folder from your training environment to your local machine.

1. Open a terminal or command prompt on your local machine.

1. Navigate to the directory containing the downloaded experiment folder.

1. Launch Tensorboard with the following the command.

   ```
   tensorboard --port={{<port>}} --bind_all --logdir experiment.
   ```

1. Open your web browser and visit http://localhost:8008.

You can now see the status and visualizations of your training jobs within the Tensorboard interface. Seeing the status and visualizations helps you monitor and analyze the training process. Monitoring and analyzing the training process helps you gain insights into the behavior and performance of your models. For more information about how you monitor and analyze the training with Tensorboard, see the [NVIDIA NeMo Framework User Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/index.html).

### VizTracer
<a name="viztracer"></a>

To enable VizTracer, you can modify your recipe by setting the model.viztracer.enabled parameter to true. For example, you can update your llama recipe to enable VizTracer by adding the following configuration:

```
model:
  viztracer:
    enabled: true
```

After the training has completed, your VizTracer profile is in the experiment folder exp\_dir/result.json. To analyze your profile, you can download it and open it using the vizviewer tool:

```
vizviewer --port <port> result.json
```

This command launches the vizviewer on port 9001. You can view your VizTracer by specifying http://localhost:<port> in your browser. After you open VizTracer, you begin analyzing the training. For more information about using VizTracer, see VizTracer documentation.

## SageMaker JumpStart versus SageMaker HyperPod
<a name="sagemaker-jumpstart-vs-hyperpod"></a>

While SageMaker JumpStart provides fine-tuning capabilities, the SageMaker HyperPod recipes provide the following:
+ Additional fine-grained control over the training loop
+ Recipe customization for your own models and data
+ Support for model parallelism

Use the SageMaker HyperPod recipes when you need access to the model's hyperparameters, multi-node training, and customization options for the training loop.

For more information about fine-tuning your models in SageMaker JumpStart, see [Fine-tune publicly available foundation models with the `JumpStartEstimator` class](jumpstart-foundation-models-use-python-sdk-estimator-class.md)