

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy a Sample Load Balancer Workload to EKS Auto Mode
<a name="auto-elb-example"></a>

This guide walks you through deploying a containerized version of the 2048 game on Amazon EKS, complete with load balancing and internet accessibility.

## Prerequisites
<a name="_prerequisites"></a>
+ An EKS Auto Mode cluster
+  `kubectl` configured to interact with your cluster
+ Appropriate IAM permissions for creating ALB resources

## Step 1: Create the Namespace
<a name="_step_1_create_the_namespace"></a>

First, create a dedicated namespace for the 2048 game application.

Create a file named `01-namespace.yaml`:

```
apiVersion: v1
kind: Namespace
metadata:
  name: game-2048
```

Apply the namespace configuration:

```
kubectl apply -f 01-namespace.yaml
```

## Step 2: Deploy the Application
<a name="_step_2_deploy_the_application"></a>

The application runs multiple replicas of the 2048 game container.

Create a file named `02-deployment.yaml`:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: game-2048
  name: deployment-2048
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: app-2048
  replicas: 5
  template:
    metadata:
      labels:
        app.kubernetes.io/name: app-2048
    spec:
      containers:
        - image: public.ecr.aws/l6m2t8p7/docker-2048:latest
          imagePullPolicy: Always
          name: app-2048
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "0.5"
```

**Note**  
If you receive an error loading the image `public.ecr.aws/l6m2t8p7/docker-2048:latest`, confirm your Node IAM role has sufficient permissions to pull images from ECR. For more information, see [Node IAM role](auto-learn-iam.md#auto-learn-node-iam-role). Also, the `docker-2048` image in the example is an `x86_64` image and will not run on other architectures.

 **Key components:** 
+ Deploys 5 replicas of the application
+ Uses a public ECR image
+ Requests 0.5 CPU cores per pod
+ Exposes port 80 for HTTP traffic

Apply the deployment:

```
kubectl apply -f 02-deployment.yaml
```

## Step 3: Create the Service
<a name="_step_3_create_the_service"></a>

The service exposes the deployment to the cluster network.

Create a file named `03-service.yaml`:

```
apiVersion: v1
kind: Service
metadata:
  namespace: game-2048
  name: service-2048
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  selector:
    app.kubernetes.io/name: app-2048
```

 **Key components:** 
+ Creates a ClusterIP service
+ Maps port 80 to the container’s port 80
+ Uses label selector to find pods

Apply the service:

```
kubectl apply -f 03-service.yaml
```

## Step 4: Configure Load Balancing
<a name="_step_4_configure_load_balancing"></a>

You will set up an ingress to expose the application to the internet.

First, create the `IngressClass`. Create a file named `04-ingressclass.yaml`:

```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  labels:
    app.kubernetes.io/name: LoadBalancerController
  name: alb
spec:
  controller: eks.amazonaws.com/alb
```

**Note**  
EKS Auto Mode requires subnet tags to identify public and private subnets.  
If you created your cluster with `eksctl`, you already have these tags.  
Learn how to [Tag subnets for EKS Auto Mode](tag-subnets-auto.md).

Then create the Ingress resource. Create a file named `05-ingress.yaml`:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  namespace: game-2048
  name: ingress-2048
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
spec:
  ingressClassName: alb
  rules:
    - http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: service-2048
                port:
                  number: 80
```

 **Key components:** 
+ Creates an internet-facing ALB
+ Uses IP target type for direct pod routing
+ Routes all traffic (/) to the game service

Apply the ingress configurations:

```
kubectl apply -f 04-ingressclass.yaml
kubectl apply -f 05-ingress.yaml
```

## Step 5: Verify the Deployment
<a name="_step_5_verify_the_deployment"></a>

1. Check that all pods are running:

   ```
   kubectl get pods -n game-2048
   ```

1. Verify the service is created:

   ```
   kubectl get svc -n game-2048
   ```

1. Get the ALB endpoint:

   ```
   kubectl get ingress -n game-2048
   ```

The ADDRESS field in the ingress output will show your ALB endpoint. Wait 2-3 minutes for the ALB to provision and register all targets.

## Step 6: Access the Game
<a name="_step_6_access_the_game"></a>

Open your web browser and browse to the ALB endpoint URL from the earlier step. You should see the 2048 game interface.

## Step 7: Cleanup
<a name="_step_7_cleanup"></a>

To remove all resources created in this tutorial:

```
kubectl delete namespace game-2048
```

This will delete all resources in the namespace, including the deployment, service, and ingress resources.

## What’s Happening Behind the Scenes
<a name="_whats_happening_behind_the_scenes"></a>

1. The deployment creates 5 pods running the 2048 game

1. The service provides stable network access to these pods

1. EKS Auto Mode:
   + Creates an Application Load Balancer in AWS 
   + Configures target groups for the pods
   + Sets up routing rules to direct traffic to the service

## Troubleshooting
<a name="auto-elb-troubleshooting"></a>

If the game doesn’t load:
+ Ensure all pods are running: `kubectl get pods -n game-2048` 
+ Check ingress status: `kubectl describe ingress -n game-2048` 
+ Verify ALB health checks: Check the target group health in the AWS Console