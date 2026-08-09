**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Share a target group across two clusters

The following example shares one target group between two clusters. The first cluster owns the Application Load Balancer through an Ingress, and the second cluster joins the shared target group through a manually created `TargetGroupBinding`. Before you begin, review [Configure multi-cluster target groups](auto-multi-cluster-target-groups.md "auto-multi-cluster-target-groups.md") to understand how MultiCluster support works and how to enable it.

## Cluster 1 — own the load balancer through an Ingress

Deploy your application (for example, a Deployment with a `NodePort` Service), then create an `IngressClass` and an `Ingress` that carries the multi-cluster annotation.

```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: alb-mc
spec:
  controller: eks.amazonaws.com/alb
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: echoserver
  namespace: echoserver
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: instance
    alb.ingress.kubernetes.io/multi-cluster-target-group: "true"
spec:
  ingressClassName: alb-mc
  rules:
    - http:
        paths:
          - path: /
            pathType: Exact
            backend:
              service:
                name: echoserver
                port:
                  number: 80
```

The controller provisions the load balancer and generates a `TargetGroupBinding` with `spec.multiClusterTargetGroup: true`. Note the following values from the generated `TargetGroupBinding` and Service — the second cluster needs all three:

- The `targetGroupARN`.
- The Service `nodePort`.
- The load balancer security group ID from `spec.networking.ingress[].from[].securityGroup.groupID`.

## Cluster 2 — join the shared target group through a TargetGroupBinding

Deploy the same application, pinning the Service to the `nodePort` from cluster 1, then create a `TargetGroupBinding` that references cluster 1’s target group ARN and security group ID.

```
apiVersion: eks.amazonaws.com/v1
kind: TargetGroupBinding
metadata:
  name: mc-echoserver
  namespace: echoserver
spec:
  multiClusterTargetGroup: true
  serviceRef:
    name: echoserver
    port: 80
  targetGroupARN: <cluster-1-target-group-arn>
  targetType: instance
  networking:
    ingress:
      - from:
          - securityGroup:
              groupID: <cluster-1-alb-security-group-id>
        ports:
          - port: <cluster-2-node-port>
            protocol: TCP
```

With MultiCluster support enabled on both bindings, each cluster registers and deregisters only its own targets. Both clusters' nodes stay healthy in the single shared target group, and the load balancer distributes traffic across all of them.
