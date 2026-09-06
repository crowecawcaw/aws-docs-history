

# Deploying a model with Ray Serve
<a name="sagemaker-hyperpod-ray-deploy-model"></a>

You deploy a model with a `RayService` resource. The `serveConfigV2` field holds your Serve applications and their deployments, and KubeRay creates the Ray cluster that runs them. HyperPod does not modify KubeRay, so a `RayService` you already run continues to work.

## A RayService manifest
<a name="sagemaker-hyperpod-ray-deploy-model-manifest"></a>

The following manifest runs one Serve application with a single GPU-backed deployment. Replace `import_path` with the module and application object in your working directory.

```
apiVersion: ray.io/v1
kind: RayService
metadata:
  name: my-service
  namespace: my-namespace
spec:
  serveConfigV2: |
    applications:
      - name: my-app
        import_path: my_module:app
        route_prefix: /
        deployments:
          - name: Model
            num_replicas: 2
            ray_actor_options:
              num_gpus: 1
  rayClusterConfig:
    rayVersion: "2.56.1"
    headGroupSpec:
      rayStartParams:
        dashboard-host: "0.0.0.0"
      template:
        spec:
          containers:
            - name: ray-head
              image: rayproject/ray:2.56.1
              ports:
                - { containerPort: 8265, name: dashboard }
                - { containerPort: 8000, name: serve }
    workerGroupSpecs:
      - groupName: gpu-workers
        replicas: 1
        rayStartParams: {}
        template:
          spec:
            nodeSelector:
              node.kubernetes.io/instance-type: ml.g5.xlarge
            containers:
              - name: ray-worker
                image: rayproject/ray:2.56.1-gpu
                resources:
                  limits: { nvidia.com/gpu: "1" }
                  requests: { cpu: "4", memory: "16Gi", nvidia.com/gpu: "1" }
```

Apply and confirm the service is ready:

```
kubectl apply -f my-service.yaml -n my-namespace
kubectl get rayservice my-service -n my-namespace
```

## Reaching the endpoint
<a name="sagemaker-hyperpod-ray-deploy-model-endpoint"></a>

Ray Serve listens on port `8000` on the head pod. From inside the cluster, send requests to the service that KubeRay creates for the `RayService`. For quick testing, you can use `kubectl port-forward`:

```
kubectl port-forward svc/{{ray-service-head-svc}} 8000:8000
curl http://localhost:8000/
```

For the Serve deployment API and request handling, see [Ray Serve API](https://docs.ray.io/en/latest/serve/api/index.html) in the Ray documentation.