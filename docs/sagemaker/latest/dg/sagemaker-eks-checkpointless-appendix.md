# Appendix

**Monitor training results via HyperPod recipes**

SageMaker HyperPod recipes offer Tensorboard integration to analyze training behavior. These recipes
also incorporate VizTracer, which is a low-overhead tool for tracing and visualizing Python code
execution. For more information, see [VizTracer](https://github.com/gaogaotiantian/viztracer "https://github.com/gaogaotiantian/viztracer").

The tensorboard logs are generated and stored within the `log_dir`. To access and analyze these logs locally, use the following procedure:

1. Download the Tensorboard experiment folder from your training environment to your local machine.
2. Open a terminal or command prompt on your local machine.
3. Navigate to the directory containing the downloaded experiment folder.
4. Launch Tensorboard by running the command:

```
tensorboard --port=<port> --bind_all --logdir experiment.
```

5. Open your web browser and visit `http://localhost:8008`.
   You can now see the status and visualizations of your training jobs within the Tensorboard
   interface. Seeing the status and visualizations helps you monitor and analyze the training process.
   Monitoring and analyzing the training process helps you gain insights into the behavior and
   performance of your models. For more information about how you monitor and analyze the
   training with Tensorboard, see the [NVIDIA NeMo Framework User Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html#experiment-manager "https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html#experiment-manager").

**VizTracer**

To enable VizTracer, you can modify your recipe by setting the environment variable `ENABLE_VIZTRACER` to `1`.
After the training has completed, your VizTracer profile is in the experiment folder `log_dir/viztracer_xxx.json`. To analyze your profile, you can download it and open it using the **vizviewer** tool:

```
vizviewer --port <port> viztracer_xxx.json
```

This command launches the vizviewer on port 9001. You can view your VizTracer by going to
http://localhost:<port> in your browser. After you open VizTracer, you begin
analyzing the training. For more information about using VizTracer, see [VizTracer documentation](https://viztracer.readthedocs.io/en/latest/installation.html "https://viztracer.readthedocs.io/en/latest/installation.html").
