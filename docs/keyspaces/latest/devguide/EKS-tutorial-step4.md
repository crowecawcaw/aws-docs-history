# Step 4: Deploy the application to Amazon EKS and write

data to your table

In this step of the tutorial, you configure the Amazon EKS deployment for your application, and confirm that the application is
running and can connect to Amazon Keyspaces.

To deploy an application to Amazon EKS, you need to configure all relevant settings in a file called `deployment.yaml`.
This file is then used by Amazon EKS to deploy the application. The metadata in the file should contain the following information:

- **Application name**  the name of the application. For this tutorial,
  we use `my-keyspaces-app`.
- **Kubernetes namespace**  the namespace of the Amazon EKS cluster. For this tutorial,
  we use `my-eks-namespace`.
- **Amazon EKS service account name**  the name of the Amazon EKS service account. For this tutorial,
  we use `my-eks-serviceaccount`.
- **image name**  the name of the application image. For this tutorial,
  we use `my-keyspaces-app`.
- **Image URI**  the Docker image URI from Amazon ECR.
- **AWS account ID**  your AWS account ID.
- **IAM role ARN**  the ARN of the IAM role created for the service account to assume.
  For this tutorial, we use `my-iam-role`.
- **AWS Region of the Amazon EKS cluster**  the AWS Region you created your Amazon EKS cluster in.
  In this step, you deploy and run the application that connects to Amazon Keyspaces and writes data to the table.

1.  Configure the `deployment.yaml` file. You need to replace the following values:

        * `name`
        * `namespace`
        * `serviceAccountName`
        * `image`
        * `AWS_ROLE_ARN value`
        * The AWS Region in `CASSANDRA_HOST`
        * `AWS_REGION`

    You can use the following file as an example.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: `my-keyspaces-app`
  namespace: `my-eks-namespace`
spec:
  replicas: 1
  selector:
    matchLabels:
      app: `my-keyspaces-app`
  template:
    metadata:
      labels:
        app: `my-keyspaces-app`
    spec:
      serviceAccountName: `my-eks-serviceaccount`
      containers:
      - name: `my-keyspaces-app`
        image: `111122223333.dkr.ecr.`us-east-1`.amazonaws.com/`my-ecr-repository`:latest`
        ports:
        - containerPort: 8080
        env:
        - name: CASSANDRA_HOST
          value: "cassandra.``us-east-1``.amazonaws.com:9142"
        - name: CASSANDRA_DC
          value: "``us-east-1``"
        - name: AWS_WEB_IDENTITY_TOKEN_FILE
          value: /var/run/secrets/eks.amazonaws.com/serviceaccount/token
        - name: AWS_ROLE_ARN
          value: "`arn:aws:iam::`111122223333`:role/my-iam-role`"
        - name: AWS_REGION
          value: "``us-east-1``"


```

2. Deploy `deployment.yaml`.

```
kubectl apply -f deployment.yaml
```

The output should look like this.

```
`deployment.apps/my-keyspaces-app created`
```

3. Check the status of the Pod in your namespace of the Amazon EKS cluster.

```
kubectl get pods -n my-eks-namespace
```

The output should look similar to this example.

```
`NAME READY STATUS RESTARTS AGE
my-keyspaces-app-123abcde4f-g5hij 1/1 Running 0 75s`
```

For more details, you can use the following command.

```
kubectl describe pod `my-keyspaces-app-123abcde4f-g5hij` -n `my-eks-namespace`
```

```
`Name: my-keyspaces-app-123abcde4f-g5hij
Namespace: my-eks-namespace
Priority: 2000001000
Priority Class Name: system-node-critical
Service Account: my-eks-serviceaccount
Node: fargate-ip-192-168-102-209.ec2.internal/192.168.102.209
Start Time: Thu, 23 Nov 2023 12:15:43 +0000
Labels: app=my-keyspaces-app
 eks.amazonaws.com/fargate-profile=my-fargate-profile
 pod-template-hash=6c56fccc56
Annotations: CapacityProvisioned: 0.25vCPU 0.5GB
 Logging: LoggingDisabled: LOGGING_CONFIGMAP_NOT_FOUND
Status: Running
IP: 192.168.102.209
IPs:
 IP: 192.168.102.209
Controlled By: ReplicaSet/my-keyspaces-app-6c56fccc56
Containers:
 my-keyspaces-app:
 Container ID: containerd://41ff7811d33ae4bc398755800abcdc132335d51d74f218ba81da0700a6f8c67b
 Image: 111122223333.dkr.ecr.us-east-1.amazonaws.com/my_eks_repository:latest
 Image ID: 111122223333.dkr.ecr.us-east-1.amazonaws.com/my_eks_repository@sha256:fd3c6430fc5251661efce99741c72c1b4b03061474940200d0524b84a951439c
 Port: 8080/TCP
 Host Port: 0/TCP
 State: Running
 Started: Thu, 23 Nov 2023 12:15:19 +0000
 Finished: Thu, 23 Nov 2023 12:16:17 +0000
 Ready: True
 Restart Count: 1
 Environment:
 CASSANDRA_HOST: cassandra.us-east-1.amazonaws.com:9142
 CASSANDRA_DC: us-east-1
 AWS_WEB_IDENTITY_TOKEN_FILE: /var/run/secrets/eks.amazonaws.com/serviceaccount/token
 AWS_ROLE_ARN: arn:aws:iam::111122223333:role/my-iam-role
 AWS_REGION: us-east-1
 AWS_STS_REGIONAL_ENDPOINTS: regional
 Mounts:
 /var/run/secrets/eks.amazonaws.com/serviceaccount from aws-iam-token (ro)
 /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fssbf (ro)
Conditions:
 Type Status
 Initialized True
 Ready True
 ContainersReady True
 PodScheduled True
Volumes:
 aws-iam-token:
 Type: Projected (a volume that contains injected data from multiple sources)
 TokenExpirationSeconds: 86400
 kube-api-access-fssbf:
 Type: Projected (a volume that contains injected data from multiple sources)
 TokenExpirationSeconds: 3607
 ConfigMapName: kube-root-ca.crt
 ConfigMapOptional: <nil>
 DownwardAPI: true
QoS Class: BestEffort
Node-Selectors: <none>
Tolerations: node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
 Type Reason Age From Message
 ---- ------ ---- ---- -------
 Warning LoggingDisabled 2m13s fargate-scheduler Disabled logging because aws-logging configmap was not found. configmap "aws-logging" not found
 Normal Scheduled 89s fargate-scheduler Successfully assigned my-eks-namespace/my-keyspaces-app-6c56fccc56-mgs2m to fargate-ip-192-168-102-209.ec2.internal
 Normal Pulled 75s kubelet Successfully pulled image "111122223333.dkr.ecr.us-east-1.amazonaws.com/my_eks_repository:latest" in 13.027s (13.027s including waiting)
 Normal Pulling 54s (x2 over 88s) kubelet Pulling image "111122223333.dkr.ecr.us-east-1.amazonaws.com/my_eks_repository:latest"
 Normal Created 54s (x2 over 75s) kubelet Created container my-keyspaces-app
 Normal Pulled 54s kubelet Successfully pulled image "111122223333.dkr.ecr.us-east-1.amazonaws.com/my_eks_repository:latest" in 222ms (222ms including waiting)
 Normal Started 53s (x2 over 75s) kubelet Started container my-keyspaces-app`
```

4. Check the Pod's logs to confirm that your application is running and can connect to your Amazon Keyspaces
   table. You can do so with the following command. Make sure to replace the name
   of your deployment.

```
kubectl logs -f `my-keyspaces-app-123abcde4f-g5hij` -n `my-eks-namespace`
```

You should be able to see application log entries confirming the connection to Amazon Keyspaces like in the example below.

```
`2:47:20.553 [s0-admin-0] DEBUG c.d.o.d.i.c.metadata.MetadataManager - [s0] Adding initial contact points [Node(endPoint=cassandra.`us-east-1`.amazonaws.com/1.222.333.44:9142, hostId=null, hashCode=e750d92)]
22:47:20.562 [s0-admin-1] DEBUG c.d.o.d.i.c.c.ControlConnection - [s0] Initializing with event types [SCHEMA_CHANGE, STATUS_CHANGE, TOPOLOGY_CHANGE]
22:47:20.564 [s0-admin-1] DEBUG c.d.o.d.i.core.context.EventBus - [s0] Registering com.datastax.oss.driver.internal.core.metadata.LoadBalancingPolicyWrapper$$Lambda$812/0x0000000801105e88@769afb95 for class com.datastax.oss.driver.internal.core.metadata.NodeStateEvent
22:47:20.566 [s0-admin-1] DEBUG c.d.o.d.i.c.c.ControlConnection - [s0] Trying to establish a connection to Node(endPoint=cassandra.us-east-1.amazonaws.com/1.222.333.44:9142, hostId=null, hashCode=e750d92)`
```

5. Run the following CQL query on your Amazon Keyspaces table to confirm that one row of data has been written to your table:

```
SELECT * from aws.user;
```

You should see the following output:

```
`fname | lname | username | last_update_date
----------+-------+----------+-----------------------------
random | k | test | 2023-12-07 13:58:31.57+0000`
```
