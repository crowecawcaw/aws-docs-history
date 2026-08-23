# IDE and notebooks with Ray

Interactive development connects an IDE or notebook session to a running Ray cluster, so
you write and run distributed Python against live compute. You develop in a
_space_, and you manage clusters and spaces in Studio.

A space is the workspace: a JupyterLab, Code Editor, or remote IDE session with its own
storage, image, and attached Ray cluster. `ray.init()` inside the space connects
to that cluster. Studio is the web interface: you create clusters, create spaces, and
connect them there, then do the work inside the space.

The space runs in its own pod, decoupled from the Ray head pod. When you attach it to a
cluster, the space joins that cluster as a zero-compute worker node. With this setup,
`ray.init()` inside the space connects directly to the cluster. Setup is two steps:
create the space, then attach a Ray cluster to it. You attach an existing cluster or create a
new one.

## Use cases

**Development environments on a multi-tenant cluster.** A
platform team runs one Kubernetes cluster and gives each data scientist their own space
on it. Each space carries its own storage and image, and attaches to a Ray cluster in the
same namespace as the space.

**Interactive development in a notebook.** You develop a
Ray application end to end in one session: data preparation, training, and inference. You
iterate and debug as you go, and visualize results in place. You can also start a large
training run from the notebook, because HyperPod recovers faulty nodes underneath
it. For more information, see [Automatic node recovery with Ray](sagemaker-hyperpod-ray-node-recovery.md "sagemaker-hyperpod-ray-node-recovery.md").

No more `kubectl port-forward` or a shell into the head pod.

The following pages cover setup and use, in order.

###### Topics

- [Setting up the Spaces add-on](sagemaker-hyperpod-ray-spaces-addon-setup.md "sagemaker-hyperpod-ray-spaces-addon-setup.md")
- [Attaching Ray cluster to Space](sagemaker-hyperpod-ray-attach-space.md "sagemaker-hyperpod-ray-attach-space.md")
- [Accessing your development environment](sagemaker-hyperpod-ray-remote-ide.md "sagemaker-hyperpod-ray-remote-ide.md")
- [Managing dependencies with runtime\_env](sagemaker-hyperpod-ray-runtime-env.md "sagemaker-hyperpod-ray-runtime-env.md")
- [Scaling a development cluster](sagemaker-hyperpod-ray-scaling-dev-cluster.md "sagemaker-hyperpod-ray-scaling-dev-cluster.md")
