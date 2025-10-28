# CPU Inference

This section guides you on running inference on Deep Learning Containers for EKS CPU
clusters using PyTorch, and TensorFlow.

For a complete list of Deep Learning Containers, see
[Available Deep Learning Containers Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md").

###### Contents

- [PyTorch CPU inference](#deep-learning-containers-eks-tutorials-cpu-inference-pytorch "#deep-learning-containers-eks-tutorials-cpu-inference-pytorch")
- [TensorFlow CPU inference](#deep-learning-containers-eks-tutorials-cpu-inference-tf "#deep-learning-containers-eks-tutorials-cpu-inference-tf")
- [Next steps](#deep-learning-containers-eks-tutorials-cpu-inference-next "#deep-learning-containers-eks-tutorials-cpu-inference-next")

## PyTorch CPU inference

In this approach, you create a Kubernetes Service and a Deployment to run CPU
inference with PyTorch. The Kubernetes Service exposes a process and its ports. When you
create a Kubernetes Service, you can specify the kind of Service you want using
`ServiceTypes`. The default `ServiceType` is `ClusterIP`.
The Deployment is responsible for ensuring that a certain number of pods is always up and
running.

1. Create the namespace. You may need to change the kubeconfig to point to the right
   cluster. Verify that you have setup a "training-cpu-1" or change this to your CPU
   cluster's config. For more information on setting up your cluster, see [Amazon EKS Setup](deep-learning-containers-eks-setup.md "deep-learning-containers-eks-setup.md").

```
`$` NAMESPACE=pt-inference; kubectl create namespace ${NAMESPACE}
```

2. (Optional step when using public models.) Setup your model at a network
   location that is mountable, like in Amazon S3. For information on how to upload a trained
   model to S3, see [TensorFlow CPU inference](#deep-learning-containers-eks-tutorials-cpu-inference-tf "#deep-learning-containers-eks-tutorials-cpu-inference-tf"). Apply the
   secret to your namespace. For more information on secrets, see the [Kubernetes Secrets
   documentation](https://kubernetes.io/docs/concepts/configuration/secret/ "https://kubernetes.io/docs/concepts/configuration/secret/").

```
`$` kubectl -n ${NAMESPACE} apply -f secret.yaml
```

3. Create a file named `pt_inference.yaml` with the following
   content. This example file specifies the model, PyTorch inference image used, and the
   location of the model. This example uses a public model, so you don't need to modify
   it.

```
`---
kind: Service
apiVersion: v1
metadata:
 name: `densenet-service`
 labels:
 app: `densenet-service`
spec:
 ports:
 - port: 8080
 targetPort: mms
 selector:
 app: `densenet-service`
---
kind: Deployment
apiVersion: apps/v1
metadata:
 name: `densenet-service`
 labels:
 app: `densenet-service`
spec:
 replicas: 1
 selector:
 matchLabels:
 app: `densenet-service`
 template:
 metadata:
 labels:
 app: `densenet-service`
 spec:
 containers:
 - name: `densenet-service`
 image: `763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.3.1-cpu-py36-ubuntu16.04`
 args:
 - multi-model-server
 - --start
 - --mms-config /home/model-server/config.properties
 - --models densenet=`https://dlc-samples.s3.amazonaws.com/pytorch/multi-model-server/densenet/densenet.mar`
 ports:
 - name: mms
 containerPort: 8080
 - name: mms-management
 containerPort: 8081
 imagePullPolicy: IfNotPresent`
```

4. Apply the configuration to a new pod in the previously defined
   namespace.

```
`$` kubectl -n ${NAMESPACE} apply -f pt_inference.yaml
```

Your output should be similar to the following:

```
service/`densenet-service` created
deployment.apps/`densenet-service` created
```

5. Check the status of the pod and wait for the pod to be in “RUNNING”
   state:

```
`$` kubectl get pods -n ${NAMESPACE} -w
```

Your output should be similar to the following:

```
NAME                     READY     STATUS    RESTARTS   AGE
densenet-service-xvw1    1/1       Running   0          3m
```

6. To further describe the pod, run the following:

```
`$` `kubectl describe pod `<pod_name>` -n ${NAMESPACE}`
```

7. Because the serviceType here is ClusterIP, you can forward the port from
   your container to your host machine.

```
`$` kubectl port-forward -n ${NAMESPACE} `kubectl get pods -n ${NAMESPACE} --selector=app=`densenet-service` -o jsonpath='{.items[0].metadata.name}'` 8080:8080 &
```

8. With your server started, you can now run inference from a different window using
   the following:

```
`$` curl -O https://s3.amazonaws.com/model-server/inputs/flower.jpg
curl -X POST http://127.0.0.1:8080/predictions/densenet -T flower.jpg
```

See [EKS Cleanup](../../../dlami/latest/devguide/deep-learning-containers-eks-setup.md#deep-learning-containers-eks-setup-cleanup "../../../dlami/latest/devguide/deep-learning-containers-eks-setup.md#deep-learning-containers-eks-setup-cleanup") for information on cleaning up a cluster after you're done using it.

## TensorFlow CPU inference

In this tutorial, you create a Kubernetes Service and a Deployment to run
CPU inference with TensorFlow. The Kubernetes Service exposes a process and its ports. When
you create a Kubernetes Service, you can specify the kind of Service you want using
`ServiceTypes`. The default `ServiceType` is `ClusterIP`.
The Deployment is responsible for ensuring that a certain number of pods is always up and
running.

1. Create the namespace. You may need to change the kubeconfig to point to the right
   cluster. Verify that you have setup a "training-cpu-1" or change this to your CPU
   cluster's config. For more information on setting up your cluster, see [Amazon EKS Setup](deep-learning-containers-eks-setup.md "deep-learning-containers-eks-setup.md").

```
`$` NAMESPACE=tf-inference; kubectl —kubeconfig=/home/ubuntu/.kube/eksctl/clusters/training-cpu-1 create namespace ${NAMESPACE}
```

2. Models served for inference can be retrieved in different ways,
   such as using shared volumes and Amazon S3. Because the Kubernetes Service requires access to
   Amazon S3 and Amazon ECR, you must store your AWS credentials as a Kubernetes secret. For the
   purpose of this example, use S3 to store and fetch trained models.

Verify your AWS credentials. They must have S3 write
access.

```
`$` cat ~/.aws/credentials
```

3. The output will be similar to the following:

```
`$` [default]
aws_access_key_id = `YOURACCESSKEYID`
aws_secret_access_key = `YOURSECRETACCESSKEY`
```

4. Encode the credentials using base64.

Encode the access key first.

```
`$` `echo -n '`YOURACCESSKEYID`' | base64`
```

Encode the secret access key next.

```
`$` `echo -n '`YOURSECRETACCESSKEY`' | base64`
```

Your output should look similar to the following:

```
$ echo -n '`YOURACCESSKEYID`' | base64
RkFLRUFXU0FDQ0VTU0tFWUlE
$ echo -n '`YOURSECRETACCESSKEY`' | base64
RkFLRUFXU1NFQ1JFVEFDQ0VTU0tFWQ==
```

5. Create a file named `secret.yaml` with the following
   content in your home directory. This file is used to store the secret.

```
`apiVersion: v1
kind: Secret
metadata:
name: aws-s3-secret
type: Opaque
data:
AWS_ACCESS_KEY_ID: `YOURACCESSKEYID`
AWS_SECRET_ACCESS_KEY: `YOURSECRETACCESSKEY``
```

6. Apply the secret to your namespace.

```
`$` kubectl -n ${NAMESPACE} apply -f secret.yaml
```

7. Clone the [tensorflow-serving](https://github.com/tensorflow/serving/ "https://github.com/tensorflow/serving/") repository.

```
`$` git clone https://github.com/tensorflow/serving/
`$` cd serving/tensorflow_serving/servables/tensorflow/testdata/

```

8. Sync the pretrained `saved_model_half_plus_two_cpu` model
   to your S3 bucket.

```
`$` `aws s3 sync saved_model_half_plus_two_cpu s3://`<your_s3_bucket>`/saved_model_half_plus_two`
```

9. Create a file named `tf_inference.yaml` with the
   following content. Update `--model_base_path` to use your S3 bucket. You can
   use this with either TensorFlow or TensorFlow 2. To use it with TensorFlow 2, change the
   Docker image to a TensorFlow 2 image.

```
`---
kind: Service
apiVersion: v1
metadata:
name: `half-plus-two`
labels:
 app: `half-plus-two`
spec:
ports:
- name: http-tf-serving
 port: 8500
 targetPort: 8500
- name: grpc-tf-serving
 port: 9000
 targetPort: 9000
selector:
 app: `half-plus-two`
 role: master
type: ClusterIP
---
kind: Deployment
apiVersion: apps/v1
metadata:
name: `half-plus-two`
labels:
 app: `half-plus-two`
 role: master
spec:
replicas: 1
selector:
 matchLabels:
 app: `half-plus-two`
 role: master
template:
 metadata:
 labels:
 app: `half-plus-two`
 role: master
 spec:
 containers:
 - name: `half-plus-two`
 image: `763104351884.dkr.ecr.us-east-1.amazonaws.com/tensorflow-inference:1.15.0-cpu-py36-ubuntu18.04`
 command:
 - /usr/bin/tensorflow_model_server
 args:
 - --port=9000
 - --rest_api_port=8500
 - --model_name=saved_model_half_plus_two
 - --model_base_path=s3://`tensorflow-trained-models/saved_model_half_plus_two`
 ports:
 - containerPort: 8500
 - containerPort: 9000
 imagePullPolicy: IfNotPresent
 env:
 - name: AWS_ACCESS_KEY_ID
 valueFrom:
 secretKeyRef:
 key: `AWS_ACCESS_KEY_ID`
 name: aws-s3-secret
 - name: AWS_SECRET_ACCESS_KEY
 valueFrom:
 secretKeyRef:
 key: `AWS_SECRET_ACCESS_KEY`
 name: aws-s3-secret
 - name: AWS_REGION
 value: `us-east-1`
 - name: S3_USE_HTTPS
 value: "true"
 - name: S3_VERIFY_SSL
 value: "true"
 - name: S3_ENDPOINT
 value: s3.`us-east-1`.amazonaws.com`

```

10. Apply the configuration to a new pod in the previously defined
    namespace.

```
`$` kubectl -n ${NAMESPACE} apply -f tf_inference.yaml

```

Your output should be similar to the following:

```
service/`half-plus-two` created
deployment.apps/`half-plus-two` created
```

11. Check the status of the pod.

```
`$` kubectl get pods -n ${NAMESPACE}
```

Repeat the status check until you see the following "RUNNING"
state:

```
NAME                     READY     STATUS    RESTARTS   AGE
`half-plus-two`-vmwp9  1/1       Running   0          3m
```

12. To further describe the pod, you can run:

```
`$` `kubectl describe pod `<pod_name>` -n ${NAMESPACE}`
```

13. Because the serviceType is ClusterIP, you can forward the port
    from your container to your host machine.

```
`$` kubectl port-forward -n ${NAMESPACE} `kubectl get pods -n ${NAMESPACE} --selector=app=`half-plus-two` -o jsonpath='{.items[0].metadata.name}'` 8500:8500 &
```

14. Place the following json string in a file named
    `half_plus_two_input.json`

```
{"instances": [1.0, 2.0, 5.0]}
```

15. Run inference on the model.

```
`$` curl -d @half_plus_two_input.json -X POST http://localhost:8500/v1/models/saved_model_half_plus_two_cpu:predict
```

Your output should look like the following:

```
{
"predictions": [2.5, 3.0, 4.5
]
}
```

## Next steps

To learn about using Custom Entrypoints with Deep Learning Containers on Amazon EKS, see [Custom Entrypoints](deep-learning-containers-eks-tutorials-custom-entry.md "deep-learning-containers-eks-tutorials-custom-entry.md").
