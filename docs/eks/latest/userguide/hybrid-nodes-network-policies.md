**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure Kubernetes Network Policies for hybrid nodes

AWS supports Kubernetes Network Policies (Layer 3 / Layer 4) for pod ingress and egress traffic when using Cilium as the CNI with EKS Hybrid Nodes. If you are running EKS clusters with nodes in AWS Cloud, AWS supports the [Amazon VPC CNI for Kubernetes Network Policies](cni-network-policy.md "cni-network-policy.md").

This topic covers how to configure Cilium and Kubernetes Network Policies with EKS Hybrid Nodes. For detailed information on Kubernetes Network Policies, see [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/ "https://kubernetes.io/docs/concepts/services-networking/network-policies/") in the Kubernetes documentation.

## Configure network policies

### Considerations

- AWS supports the upstream Kubernetes Network Policies and specfication for pod ingress and egress. AWS currently does not support `CiliumNetworkPolicy` or `CiliumClusterwideNetworkPolicy`.
- The `policyEnforcementMode` Helm value can be used to control the default Cilium policy enforcement behavior. The default behavior allows all egress and ingress traffic. When an endpoint is selected by a network policy, it transitions to a default-deny state, where only explicitly allowed traffic is allowed. See the Cilium documentation for more information on the [default policy mode](https://docs.cilium.io/en/stable/security/policy/intro/#policy-mode-default "https://docs.cilium.io/en/stable/security/policy/intro/#policy-mode-default") and [policy enforcement modes](https://docs.cilium.io/en/stable/security/policy/intro/#policy-enforcement-modes "https://docs.cilium.io/en/stable/security/policy/intro/#policy-enforcement-modes").
- If you are changing `policyEnforcementMode` for an existing Cilium installation, you must restart the Cilium agent DaemonSet to apply the new policy enforcement mode.
- Use `namespaceSelector` and `podSelector` to allow or deny traffic to/from namespaces and pods with matching labels. The `namespaceSelector` and `podSelector` can be used with `matchLabels` or `matchExpressions` to select namespaces and pods based on their labels.
- Use `ingress.ports` and `egress.ports` to allow or deny traffic to/from ports and protocols.
- The `ipBlock` field cannot be used to selectively allow or deny traffic to/from pod IP addresses ([#9209](https://github.com/cilium/cilium/issues/9209 "https://github.com/cilium/cilium/issues/9209")). Using `ipBlock` selectors for node IPs is a beta feature in Cilium and is not supported by AWS.
- See the [NetworkPolicy resource](https://kubernetes.io/docs/concepts/services-networking/network-policies/#networkpolicy-resource "https://kubernetes.io/docs/concepts/services-networking/network-policies/#networkpolicy-resource") in the Kubernetes documentation for information on the available fields for Kubernetes Network Policies.

### Prerequisites

- Cilium installed following the instructions in [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md").
- Helm installed in your command-line environment, see [Setup Helm instructions](helm.md "helm.md").

### Procedure

The following procedure sets up network policies for a sample microservices application so that components can only talk to other components that are required for the application to function. The procedure uses the [Istio Bookinfo](https://istio.io/latest/docs/examples/bookinfo/ "https://istio.io/latest/docs/examples/bookinfo/") sample microservices application.

The Bookinfo application consists of four separate microservices with the following relationships:

- **productpage**. The productpage microservice calls the details and reviews microservices to populate the page.
- **details**. The details microservice contains book information.
- **reviews**. The reviews microservice contains book reviews. It also calls the ratings microservice.
- **ratings**. The ratings microservice contains book ranking information that accompanies a book review.
  1.  Create the sample application.

  ```
  kubectl apply -f https://raw.githubusercontent.com/istio/istio/refs/heads/master/samples/bookinfo/platform/kube/bookinfo.yaml
  ```

  2.  Confirm the application is running successfully and note the pod IP address for the productpage microservice. You will use this pod IP address to query each microservice in the subsequent steps.

  ```
  kubectl get pods -o wide
  ```

  ```
  NAME                              READY   STATUS    RESTARTS   AGE   IP            NODE
  details-v1-766844796b-9wff2       1/1     Running   0          7s    10.86.3.7     mi-0daa253999fe92daa
  productpage-v1-54bb874995-lwfgg   1/1     Running   0          7s    10.86.2.193   mi-082f73826a163626e
  ratings-v1-5dc79b6bcd-59njm       1/1     Running   0          7s    10.86.2.232   mi-082f73826a163626e
  reviews-v1-598b896c9d-p2289       1/1     Running   0          7s    10.86.2.47    mi-026d6a261e355fba7
  reviews-v2-556d6457d-djktc        1/1     Running   0          7s    10.86.3.58    mi-0daa253999fe92daa
  reviews-v3-564544b4d6-g8hh4       1/1     Running   0          7s    10.86.2.69    mi-09183e8a3d755abf6
  ```

  3.  Create a pod that will be used throughout to test the network policies. Note the pod is created in the `default` namespace with the label `access: true`.

  ```
  kubectl run curl-pod --image=curlimages/curl -i --tty --labels=access=true --namespace=default --overrides='{"spec": { "nodeSelector": {"eks.amazonaws.com/compute-type": "hybrid"}}}' -- /bin/sh
  ```

  4.  Test access to the productpage microservice. In the example below, we use the pod IP address of the productpage pod (`10.86.2.193`) to query the microservice. Replace this with the pod IP address of the productpage pod in your environment.

  ```
  curl -s http://10.86.2.193:9080/productpage | grep -o "<title>.*</title>"
  ```

  ```
  <title>Simple Bookstore App</title>
  ```

  5.  You can exit the test curl pod by typing `exit` and can reattach to the pod by running the following command.

  ```
  kubectl attach curl-pod -c curl-pod -i -t
  ```

  6.  To demonstrate the effects of the network policies in the following steps, we first create a network policy that denies all traffic for the BookInfo microservices. Create a file called `network-policy-deny-bookinfo.yaml` that defines the deny network policy.

  ```
  apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    name: deny-bookinfo
    namespace: default
  spec:
    podSelector:
      matchExpressions:
      - key: app
        operator: In
        values: ["productpage", "details", "reviews", "ratings"]
    policyTypes:
    - Ingress
    - Egress
  ```

  7.  Apply the deny network policy to your cluster.

  ```
  kubectl apply -f network-policy-default-deny-bookinfo.yaml
  ```

  8.  Test access to the BookInfo application. In the example below, we use the pod IP address of the productpage pod (`10.86.2.193`) to query the microservice. Replace this with the pod IP address of the productpage pod in your environment.

  ```
  curl http://10.86.2.193:9080/productpage --max-time 10
  ```

  ```
  curl: (28) Connection timed out after 10001 milliseconds
  ```

  9. Create a file called `network-policy-productpage.yaml` that defines the productpage network policy. The policy has the following rules:
     - allows ingress traffic from pods with the label `access: true` (the curl pod created in the previous step)
     - allows egress TCP traffic on port `9080` for the details, reviews, and ratings microservices
     - allows egress TCP/UDP traffic on port `53` for CoreDNS which runs in the `kube-system` namespace

     ```
     apiVersion: networking.k8s.io/v1
     kind: NetworkPolicy
     metadata:
       name: productpage-policy
       namespace: default
     spec:
       podSelector:
         matchLabels:
           app: productpage
       policyTypes:
       - Ingress
       - Egress
       ingress:
       - from:
         - podSelector:
             matchLabels:
               access: "true"
       egress:
       - to:
         - podSelector:
             matchExpressions:
             - key: app
               operator: In
               values: ["details", "reviews", "ratings"]
         ports:
         - port: 9080
           protocol: TCP
       - to:
         - namespaceSelector:
             matchLabels:
               kubernetes.io/metadata.name: kube-system
           podSelector:
             matchLabels:
               k8s-app: kube-dns
         ports:
         - port: 53
           protocol: UDP
         - port: 53
           protocol: TCP
     ```

  10. Apply the productpage network policy to your cluster.

  ```
  kubectl apply -f network-policy-productpage.yaml
  ```

  11. Connect to the curl pod and test access to the Bookinfo application. Access to the productpage microservice is now allowed, but the other microservices are still denied because they are still subject to the deny network policy. In the examples below, we use the pod IP address of the productpage pod (`10.86.2.193`) to query the microservice. Replace this with the pod IP address of the productpage pod in your environment.

  ```
  kubectl attach curl-pod -c curl-pod -i -t
  ```

  ```
  curl -s http://10.86.2.193:9080/productpage | grep -o "<title>.*</title>"
  <title>Simple Bookstore App</title>
  ```

  ```
  curl -s http://10.86.2.193:9080/api/v1/products/1
  {"error": "Sorry, product details are currently unavailable for this book."}
  ```

  ```
  curl -s http://10.86.2.193:9080/api/v1/products/1/reviews
  {"error": "Sorry, product reviews are currently unavailable for this book."}
  ```

  ```
  curl -s http://10.86.2.193:9080/api/v1/products/1/ratings
  {"error": "Sorry, product ratings are currently unavailable for this book."}
  ```

  12. Create a file called `network-policy-details.yaml` that defines the details network policy. The policy allows only ingress traffic from the productpage microservice.

  ```
  apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    name: details-policy
    namespace: default
  spec:
    podSelector:
      matchLabels:
        app: details
    policyTypes:
    - Ingress
    ingress:
    - from:
      - podSelector:
          matchLabels:
            app: productpage
  ```

  13. Create a file called `network-policy-reviews.yaml` that defines the reviews network policy. The policy allows only ingress traffic from the productpage microservice and only egress traffic to the ratings microservice and CoreDNS.

  ```
  apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    name: reviews-policy
    namespace: default
  spec:
    podSelector:
      matchLabels:
        app: reviews
    policyTypes:
    - Ingress
    - Egress
    ingress:
    - from:
      - podSelector:
          matchLabels:
            app: productpage
    egress:
    - to:
      - podSelector:
          matchLabels:
            app: ratings
    - to:
      - namespaceSelector:
          matchLabels:
            kubernetes.io/metadata.name: kube-system
        podSelector:
          matchLabels:
            k8s-app: kube-dns
      ports:
      - port: 53
        protocol: UDP
      - port: 53
        protocol: TCP
  ```

  14. Create a file called `network-policy-ratings.yaml` that defines the ratings network policy. The policy allows only ingress traffic from the productpage and reviews microservices.

  ```
  apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    name: ratings-policy
    namespace: default
  spec:
    podSelector:
      matchLabels:
        app: ratings
    policyTypes:
    - Ingress
    ingress:
    - from:
      - podSelector:
          matchExpressions:
          - key: app
            operator: In
            values: ["productpage", "reviews"]
  ```

  15. Apply the details, reviews, and ratings network policies to your cluster.

  ```
  kubectl apply -f network-policy-details.yaml
  kubectl apply -f network-policy-reviews.yaml
  kubectl apply -f network-policy-ratings.yaml
  ```

  16. Connect to the curl pod and test access to the Bookinfo application. In the examples below, we use the pod IP address of the productpage pod (`10.86.2.193`) to query the microservice. Replace this with the pod IP address of the productpage pod in your environment.

  ```
  kubectl attach curl-pod -c curl-pod -i -t
  ```

  Test the details microservice.

  ```
  curl -s http://10.86.2.193:9080/api/v1/products/1
  ```

  ```
  {"id": 1, "author": "William Shakespeare", "year": 1595, "type": "paperback", "pages": 200, "publisher": "PublisherA", "language": "English", "ISBN-10": "1234567890", "ISBN-13": "123-1234567890"}
  ```

  Test the reviews microservice.

  ```
  curl -s http://10.86.2.193:9080/api/v1/products/1/reviews
  ```

  ```
  {"id": "1", "podname": "reviews-v1-598b896c9d-p2289", "clustername": "null", "reviews": [{"reviewer": "Reviewer1", "text": "An extremely entertaining play by Shakespeare. The slapstick humour is refreshing!"}, {"reviewer": "Reviewer2", "text": "Absolutely fun and entertaining. The play lacks thematic depth when compared to other plays by Shakespeare."}]}
  ```

  Test the ratings microservice.

  ```
  curl -s http://10.86.2.193:9080/api/v1/products/1/ratings
  ```

  ```
  {"id": 1, "ratings": {"Reviewer1": 5, "Reviewer2": 4}}
  ```

  17. Clean up the resources you created in this procedure.

  ```
  kubectl delete -f network-policy-deny-bookinfo.yaml
  kubectl delete -f network-policy-productpage.yaml
  kubectl delete -f network-policy-details.yaml
  kubectl delete -f network-policy-reviews.yaml
  kubectl delete -f network-policy-ratings.yaml
  kubectl delete -f https://raw.githubusercontent.com/istio/istio/refs/heads/master/samples/bookinfo/platform/kube/bookinfo.yaml
  kubectl delete pod curl-pod
  ```
