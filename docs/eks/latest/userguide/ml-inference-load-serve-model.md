**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Load & Serve Models on Amazon EKS

###### Tip

[Register](https://events.eksworkshop.com/workshops/genai/ "https://events.eksworkshop.com/workshops/genai/") for upcoming Amazon EKS AI/ML workshops.

The steps in this section deploy a large language model (LLM) on Amazon EKS, serve it with vLLM, and interact with the inference endpoint.

The walkthrough uses the following tools:

- [vLLM](https://docs.vllm.ai/en/latest/ "https://docs.vllm.ai/en/latest/") — A high-throughput inference engine optimized for LLM serving and GPU memory management.
- [Run:ai Model Streamer](https://github.com/run-ai/runai-model-streamer "https://github.com/run-ai/runai-model-streamer") — Streams model weights directly from Amazon S3 to GPU memory, reducing load time from minutes to seconds.
- [Open WebUI](https://openwebui.com/ "https://openwebui.com/") — A self-hosted chat frontend that connects to vLLM’s OpenAI-compatible API.
  This section uses the [Ministral-3-8B-Instruct-2512 model](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512 "https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512"), but you can deploy any AI model that vLLM supports. For a list of supported models, see [Supported models](https://docs.vllm.ai/en/latest/models/supported_models/#text-generation "https://docs.vllm.ai/en/latest/models/supported_models/#text-generation") in the vLLM documentation.

###### Important

Use the cluster you created in the [Set up Amazon EKS cluster for AI/ML workloads](ml-cluster-setup.md "ml-cluster-setup.md") section. The instructions in this walkthrough work for both EKS Auto Mode and self-managed Karpenter.

![Architecture diagram showing LLM inference workflow with vLLM on Amazon EKS](images/ml-inference-load-serve-model-arch.png)
The architecture diagram shows the end-to-end flow:

1. Model weights are downloaded from Hugging Face to Amazon S3.
2. vLLM streams the model directly from S3 to GPU memory using Run:ai Model Streamer.
3. Users send inference requests to the vLLM endpoint.
   When you complete these steps, you have a vLLM inference endpoint that you can use to interact with a Ministral model through a chat frontend application.

## Prerequisites

Complete the steps in the [Cluster setup section](ml-cluster-setup.md "ml-cluster-setup.md").

If you opened a new terminal, set the cluster name and region you used in the [Cluster Setup via CLI](ml-cluster-setup-cli.md "ml-cluster-setup-cli.md") section:

```
export CLUSTER_NAME=ai-eks-docs
export AWS_REGION=us-east-2
```

Look up the model weights bucket you created in the [Model weights S3 bucket](ml-cluster-setup-cli.md#cluster-setup-cli-model-bucket "ml-cluster-setup-cli.md#cluster-setup-cli-model-bucket") step:

```
MODEL_BUCKET=$(aws s3api list-buckets \
  --query "Buckets[?starts_with(Name, '${CLUSTER_NAME}-models-')].Name | [0]" \
  --output text)
echo "Model bucket: ${MODEL_BUCKET}"
```

## Step 1: Download the model from Hugging Face

In this step, you deploy a Kubernetes Job that downloads the model from Hugging Face and uploads it to the S3 bucket that you created in the prerequisites section.

To download the model, apply the following Job manifest:

###### Example Model download Job manifest

```
cat << EOF | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: model-download
  namespace: default
  labels:
    guide: ai-eks-docs
spec:
  backoffLimit: 10
  activeDeadlineSeconds: 3600
  ttlSecondsAfterFinished: 86400
  template:
    spec:
      restartPolicy: Never
      serviceAccountName: model-storage-sa
      containers:
      - name: downloader
        image: python:3.11-slim
        command: ["/bin/bash", "-c"]
        args:
        - |
          set -e
          pip install -q huggingface_hub boto3
          echo "Downloading Ministral-3-8B-Instruct-2512 from Hugging Face..."
          python3 -c "from huggingface_hub import snapshot_download; snapshot_download('mistralai/Ministral-3-8B-Instruct-2512', local_dir='/tmp/mistral', allow_patterns=['*.json', '*.txt', '*.md', 'consolidated.safetensors'], ignore_patterns=['model-*.safetensors', 'model.safetensors.index.json'])"
          echo "Uploading to S3 bucket: \${MODEL_BUCKET}"
          python3 << 'PYTHON'
          import boto3
          import os
          from pathlib import Path

          s3 = boto3.client('s3')
          bucket = os.environ.get('MODEL_BUCKET')
          local_dir = Path("/tmp/mistral")

          for file_path in local_dir.rglob("*"):
              if file_path.is_file():
                  if '.cache' in file_path.parts:
                      continue
                  s3_key = f"Ministral-3-8B-Instruct-2512/{file_path.relative_to(local_dir)}"
                  print(f"Uploading {file_path.name}...")
                  s3.upload_file(str(file_path), bucket, s3_key)
          print("Upload complete!")
          PYTHON
        env:
        - name: MODEL_BUCKET
          value: "${MODEL_BUCKET}"
        - name: HF_HUB_DISABLE_XET
          value: "1"
        resources:
          requests:
            memory: "2Gi"
            cpu: "1"
          limits:
            memory: "4Gi"
            cpu: "2"
EOF
```

Wait for the Job to complete. The model weights (consolidated.safetensors) are approximately 10.4 GB, and this step typically takes 3-5 minutes.

```
kubectl wait --for=condition=complete job/model-download --timeout=600s
```

Expected output:

```
job.batch/model-download condition met
```

Verify that the model weights were uploaded to S3:

```
aws s3 ls s3://$(kubectl get job model-download -o jsonpath='{.spec.template.spec.containers[0].env[?(@.name=="MODEL_BUCKET")].value}')/Ministral-3-8B-Instruct-2512/ --recursive
```

Expected output:

```
2026-05-18 10:29:53      20311 Ministral-3-8B-Instruct-2512/README.md
2026-05-18 10:29:53       2361 Ministral-3-8B-Instruct-2512/SYSTEM_PROMPT.txt
2026-05-18 10:29:53       1903 Ministral-3-8B-Instruct-2512/config.json
2026-05-18 10:29:54 10420633176 Ministral-3-8B-Instruct-2512/consolidated.safetensors
2026-05-18 10:29:53        131 Ministral-3-8B-Instruct-2512/generation_config.json
2026-05-18 10:29:53       1185 Ministral-3-8B-Instruct-2512/params.json
2026-05-18 10:29:53        976 Ministral-3-8B-Instruct-2512/processor_config.json
2026-05-18 10:29:53   16753777 Ministral-3-8B-Instruct-2512/tekken.json
2026-05-18 10:29:53   17077402 Ministral-3-8B-Instruct-2512/tokenizer.json
2026-05-18 10:29:53      21168 Ministral-3-8B-Instruct-2512/tokenizer_config.json
```

The consolidated.safetensors file contains the model weights (approximately 10.4 GB). The remaining files are configuration and tokenizer files that vLLM requires to serve the model.

## Step 2: Deploy the inference container

In this section, you deploy vLLM as a Kubernetes Deployment to serve the model you uploaded to Amazon S3.

This section uses [AWS Deep Learning Containers](https://github.com/aws/deep-learning-containers/tree/master "https://github.com/aws/deep-learning-containers/tree/master") (DLCs), which are Docker images preinstalled with deep learning frameworks and optimized for performance on AWS infrastructure. DLCs include security patches, validated framework versions, and optimized GPU driver configurations.

This deployment uses the following AWS DLC for [vLLM 0.21.0](https://gallery.ecr.aws/deep-learning-containers/vllm "https://gallery.ecr.aws/deep-learning-containers/vllm") with SOCI support: `public.ecr.aws/deep-learning-containers/vllm:0.21.0-gpu-py312-cu130-ubuntu22.04-ec2-v1.0-soci`.

The image tag indicates vLLM 0.21.0 with GPU support, Python 3.12, CUDA 13.0, Ubuntu 22.04, optimized for EC2-based workloads, and SOCI-enabled for faster container startup.

This manifest creates a Deployment that runs vLLM on a GPU node and streams the model directly from S3 into GPU memory using Run:ai Model Streamer. The manifest also creates a ClusterIP Service that exposes the vLLM endpoint on port 8000 for in-cluster access.

Apply the manifest:

###### Example vLLM Deployment and Service YAML

```
cat << EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-inference-app
  labels:
    guide: ai-eks-docs
spec:
  replicas: 1
  selector:
    matchLabels:
      app: vllm-inference-app
  template:
    metadata:
      labels:
        app: vllm-inference-app
        guide: ai-eks-docs
    spec:
      serviceAccountName: model-storage-sa
      tolerations:
      - key: nvidia.com/gpu
        operator: Exists
        effect: NoSchedule
      nodeSelector:
        karpenter.sh/nodepool: gpu-inf
      containers:
      - name: vllm-inference
        image: public.ecr.aws/deep-learning-containers/vllm:0.21.0-gpu-py312-cu130-ubuntu22.04-ec2-v1.0-soci
        ports:
        - containerPort: 8000
        args:
        - "--model=s3://${MODEL_BUCKET}/Ministral-3-8B-Instruct-2512/"
        - "--host=0.0.0.0"
        - "--port=8000"
        - "--tensor-parallel-size=1"
        - "--gpu-memory-utilization=0.9"
        - "--max-model-len=8192"
        - "--max-num-seqs=128"
        - "--load-format=runai_streamer"
        - "--enforce-eager"
        - "--tokenizer_mode=mistral"
        - "--config_format=mistral"
        - "--enable-auto-tool-choice"
        - "--tool-call-parser=mistral"
        resources:
          limits:
            nvidia.com/gpu: 1
          requests:
            memory: "40Gi"
            cpu: "8"
---
apiVersion: v1
kind: Service
metadata:
  name: vllm-inference-svc
  namespace: default
  labels:
    app: vllm-inference-app
spec:
  selector:
    app: vllm-inference-app
  ports:
  - name: http
    port: 8000
    targetPort: 8000
    protocol: TCP
EOF
```

Check that the vLLM pod is in the Ready state:

```
kubectl get pod -l app=vllm-inference-app -w
```

Expected output:

```
NAME                                  READY   STATUS    RESTARTS   AGE
vllm-inference-app-65df5fddc8-5kmjm   1/1     Running   0          86s
```

It may take ~2 minutes for the container image to pull and for vLLM to stream model weights from S3 into GPU memory. Wait until the pod shows `1/1` in the READY column before you proceed.

The combination of EKS, SOCI, and Run:ai Model Streamer enables fast pod startup. To check the startup time for each stage, view the pod events:

```
kubectl describe pod -l app=vllm-inference-app | grep -A 20 "Events:"
```

Expected output:

```
Events:
  Type     Reason            Age   From                   Message
  ----     ------            ----  ----                   -------
  Warning  FailedScheduling  86s   default-scheduler      0/2 nodes are available: 2 node(s) had untolerated taint(s).
  Normal   Nominated         85s   eks-auto-mode/compute  Pod should schedule on: nodeclaim/gpu-inf-kqkq6
  Normal   Scheduled         55s   default-scheduler      Successfully assigned default/vllm-inference-app-d9d54586d-csmd7 to i-04f8792414384d2d3
  Normal   Pulling           52s   kubelet                Pulling image "public.ecr.aws/deep-learning-containers/vllm:0.21.0-gpu-py312-cu130-ubuntu22.04-ec2-v1.0-soci"
  Normal   Pulled            4s    kubelet                Successfully pulled image "public.ecr.aws/deep-learning-containers/vllm:0.21.0-gpu-py312-cu130-ubuntu22.04-ec2-v1.0-soci" in 48.376s (48.376s including waiting). Image size: 8802823997 bytes.
  Normal   Created           4s    kubelet                Created container vllm-inference
  Normal   Started           4s    kubelet                Started container vllm-inference
```

In this example, the GPU node was provisioned in 30 seconds and the 8.8 GB container image was pulled in approximately 48 seconds using SOCI. Fast image pulls reduce cold start times for large inference containers, which allows you to scale GPU pods dynamically instead of over-provisioning idle GPU capacity.

Next, check the vLLM logs to verify the model loading time:

```
kubectl logs $(kubectl get pod -l app=vllm-inference-app -o jsonpath='{.items[0].metadata.name}') | grep -i 'Model loading took'
```

Expected output:

```
INFO 05-18 18:41:49 [gpu_model_runner.py:4959] Model loading took 9.81 GiB memory and 5.023344 seconds
```

The log confirms that Run:ai Model Streamer loaded the 10.4 GB model weights directly from S3 into GPU memory in approximately 5 seconds, consuming 9.8 GiB of GPU memory.

The image download time in this example was using a g6e.4xlarge instance, which has 20 Gbps sustained network bandwidth. Image pulls and model loading times will vary on other instance types depending on available network bandwidth.

## Step 3: Run inference

With the vLLM Deployment running, validate the inference endpoint and deploy a chat frontend to interact with the model.

### Run a model validation test

Expose the inference endpoint via port forward:

```
kubectl port-forward svc/vllm-inference-svc 8000:8000
```

Open a new terminal window, and then validate that the inference container is responding:

```
curl -sI -X GET http://localhost:8000/health
```

Expected output:

```
HTTP/1.1 200 OK
date: Fri, 18 May 2026 00:39:23 GMT
server: uvicorn
content-length: 0
```

## Step 4: Monitor vLLM

vLLM exposes Prometheus metrics out of the box, including request rate, token throughput, end-to-end latency, and GPU KV cache utilization. In this section, you use these metrics with the monitoring stack you set up in the [Cluster setup](ml-cluster-setup.md "ml-cluster-setup.md") steps and view them on a pre-provisioned Grafana dashboard.

###### Important

You must complete the [Monitoring](ml-cluster-setup-cli.md#cluster-setup-cli-monitoring "ml-cluster-setup-cli.md#cluster-setup-cli-monitoring") subsection of the [Cluster Setup via CLI](ml-cluster-setup-cli.md "ml-cluster-setup-cli.md") section before continuing. This step depends on the kube-prometheus-stack being installed and the vLLM Grafana dashboard already provisioned in the values file.

### Apply the vLLM ServiceMonitor

A ServiceMonitor tells Prometheus where to scrape vLLM metrics.

```
cat << EOF | kubectl apply -f -
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: vllm-inference-app
  namespace: default
  labels:
    release: kube-prometheus-stack
spec:
  selector:
    matchLabels:
      app: vllm-inference-app
  endpoints:
  - port: http
    path: /metrics
    interval: 15s
EOF
```

Verify that the ServiceMonitor was created:

```
kubectl get servicemonitor vllm-inference-app
```

Expected output:

```
NAME                  AGE
vllm-inference-app    5s
```

To populate the dashboard with metrics, generate inference traffic against the vLLM endpoint you already exposed via port-forward in the validation step.

Discover the served model name:

```
MODEL_NAME=$(curl -s http://localhost:8000/v1/models | jq -r '.data[0].id')
echo "Using model: $MODEL_NAME"
```

Send 50 chat completion requests in parallel:

```
for i in $(seq 1 50); do
  curl -s -X POST http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d "{\"model\": \"$MODEL_NAME\", \"messages\": [{\"role\": \"user\", \"content\": \"Write a short poem about Kubernetes.\"}], \"max_tokens\": 128}" \
    > /dev/null &
done
wait
```

While traffic is flowing (or immediately after), check token-throughput metrics directly from the vLLM `/metrics` endpoint:

```
curl -s http://localhost:8000/metrics | grep -E '^vllm:(prompt_tokens_total|generation_tokens_total|avg_generation_throughput_toks_per_s|avg_prompt_throughput_toks_per_s)' | head
```

The `vllm:prompt_tokens_total` and `vllm:generation_tokens_total` metrics are monotonically increasing counters of input and output tokens served. The `vllm:avg_prompt_throughput_toks_per_s` and `vllm:avg_generation_throughput_toks_per_s` metrics are rolling-average throughput gauges. These same metrics power the Grafana dashboard you open in the following subsection.

### View the vLLM Grafana dashboard

The kube-prometheus-stack values file from the [Monitoring](ml-cluster-setup-cli.md#cluster-setup-cli-monitoring "ml-cluster-setup-cli.md#cluster-setup-cli-monitoring") section already provisions the community [vLLM dashboard (gnetId 25263)](https://grafana.com/grafana/dashboards/25263-vllm-metrics/ "https://grafana.com/grafana/dashboards/25263-vllm-metrics/") under the **GPU Monitoring** folder, so no extra import is needed.

Access Grafana through the load balancer you set up in the [Access Grafana](ml-cluster-setup-cli.md#cluster-setup-cli-grafana-loadbalancer "ml-cluster-setup-cli.md#cluster-setup-cli-grafana-loadbalancer") section. Print its URL:

```
echo "http://$(kubectl get ingress kube-prometheus-stack-grafana -n monitoring -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')"
```

Open the URL in your browser and log in with username `admin` and the password from the following command:

```
kubectl --namespace monitoring get secrets kube-prometheus-stack-grafana -o jsonpath="{.data.admin-password}" | base64 -d ; echo
```

Navigate to **Dashboards > GPU Monitoring > vLLM Metrics**.

**vLLM Grafana dashboard**

![vLLM Grafana dashboard showing request rate, token throughput, end-to-end latency, and GPU KV cache utilization](images/ml-inference-load-serve-model-vllm-monitoring.png)

The dashboard displays request rate, prompt and generation token throughput, latency percentiles, and GPU KV cache utilization for the vLLM inference endpoint.

## Step 5: Deploy chat application

In this step, you deploy Open WebUI as a chat frontend to interact with the model. Open WebUI is an open source, self-hosted AI interface that supports OpenAI-compatible APIs and provides a chat interface with conversation history and markdown rendering. Because vLLM exposes an OpenAI-compatible API, Open WebUI connects to it directly as a backend.

To deploy the Open WebUI application, apply the following manifest:

###### Example Open WebUI Deployment and Service YAML

```
cat << 'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: open-webui
  namespace: default
  labels:
    app: open-webui
    guide: ai-eks-docs
spec:
  replicas: 1
  selector:
    matchLabels:
      app: open-webui
  template:
    metadata:
      labels:
        app: open-webui
        guide: ai-eks-docs
    spec:
      containers:
      - name: open-webui
        image: ghcr.io/open-webui/open-webui:v0.9.2
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: "500m"
            memory: "500Mi"
          limits:
            cpu: "1000m"
            memory: "2Gi"
        env:
        - name: OPENAI_API_BASE_URLS
          value: "http://vllm-inference-svc:8000/v1"
        - name: OPENAI_API_KEY
          value: "dummy"
        - name: WEBUI_AUTH
          value: "False"
        - name: ENABLE_OLLAMA_API
          value: "False"
        - name: ENABLE_EVALUATION_ARENA_MODELS
          value: "False"
        - name: RAG_EMBEDDING_ENGINE
          value: ""
        volumeMounts:
        - name: webui-volume
          mountPath: /app/backend/data
      volumes:
      - name: webui-volume
        emptyDir: {}
---
apiVersion: v1
kind: Service
metadata:
  name: open-webui
  namespace: default
  labels:
    app: open-webui
spec:
  type: ClusterIP
  selector:
    app: open-webui
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
EOF
```

Wait for the Open WebUI pod to be ready:

```
kubectl wait --for=condition=ready pod -l app=open-webui --timeout=300s
```

Expected output:

```
pod/open-webui-6cbfc9867f-jf9w9 condition met
```

To access the application, expose Open WebUI through an internet-facing AWS Application Load Balancer (ALB) using the `alb`
`IngressClass` you created in [Set up load balancing](ml-cluster-setup-cli.md#cluster-setup-cli-loadbalancing "ml-cluster-setup-cli.md#cluster-setup-cli-loadbalancing").

###### Open WebUI is publicly accessible with no authentication

Open WebUI runs with authentication disabled (`WEBUI_AUTH: "False"`), so anyone who reaches the load balancer gets an unauthenticated chat interface backed by your GPU inference endpoint and can consume GPU capacity. Automated scanners find public load balancers within minutes. You **must** restrict access with the `alb.ingress.kubernetes.io/inbound-cidrs` annotation and treat source-IP allowlisting as a minimum safeguard rather than a complete one. For a stronger posture, use an internal scheme, add a TLS certificate, and enable Open WebUI authentication.

Find your public IP address and store it as a `/32` CIDR:

```
export MY_CIDR="$(curl -s https://checkip.amazonaws.com)/32"
echo $MY_CIDR
```

The result looks like `203.0.113.4/32`. If your network assigns addresses dynamically, your IP address can change, in which case you might need a broader range such as `203.0.113.0/24`.

Apply the following `Ingress` to create the ALB:

```
cat << EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: open-webui
  namespace: default
  labels:
    guide: ai-eks-docs
  annotations:
    alb.ingress.kubernetes.io/load-balancer-name: ai-eks-docs-chat-app
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/inbound-cidrs: ${MY_CIDR}
    alb.ingress.kubernetes.io/healthcheck-path: /health
spec:
  ingressClassName: alb
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: open-webui
            port:
              number: 80
EOF
```

###### Health check path

The `healthcheck-path` annotation points the load balancer health checks at the Open WebUI `/health` endpoint, because the ALB default health check matcher expects a 200 response.

The load balancer is created asynchronously and takes a minute or two. Print the URL:

```
echo "http://$(kubectl get ingress open-webui -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')"
```

Open the URL in your browser. The chat interface appears and you can interact with the Ministral model.

###### Port-forwarding as an alternative

Port-forwarding (`kubectl port-forward svc/open-webui 8080:80`) remains an option for local testing without provisioning a load balancer.

![Screenshot of Open WebUI chat interface showing a conversation with the Ministral model](images/ml-inference-load-serve-model-chatui.png)

## Clean up

To remove the workload resources that you created in this section, delete the Open WebUI application, the vLLM inference server, and the model-download Job:

```
kubectl delete ingress open-webui
kubectl delete deployment open-webui
kubectl delete service open-webui
kubectl delete deployment vllm-inference-app
kubectl delete service vllm-inference-svc
kubectl delete servicemonitor vllm-inference-app
kubectl delete job model-download
```

For instructions on removing infrastructure resources such as the cluster, NodePool, and S3 bucket, see [Cluster Setup Cleanup](ml-cluster-setup-cli.md#cluster-setup-cli-cleanup "ml-cluster-setup-cli.md#cluster-setup-cli-cleanup").
