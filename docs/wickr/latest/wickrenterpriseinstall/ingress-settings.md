This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Ingress settings

**Ingress Controller**

Wickr Enterprise supports four ingress controller types:

- LoadBalancer (Default)
  - The loadbalancer object may require explicit configuration in fully on-prem
    installations, even though it is often provided by cloud providers.
  - Deploys the ingress controller (ingress-nginx) service with the LoadBalancer service
    type. This requires that the Kubernetes cluster is running on a platform which supports
    external load balancers.

- Existing ALB
  - Attaches the ingress controller to an existing ALB.
  - You will need to supply the existing Application Load Balancer Target Group ARN.

- Existing NLB
  - Attaches the ingress controller to an existing NLB.
  - You will need to supply the existing Network Load Balancer Target Group ARN.

- NodePort
  - The ingress controller (ingress-nginx) will be configured to use the NodePort service
    type, which opens a port on all nodes in the Kubernetes cluster and forwards traffic to the
    ingress. Client traffic can then be directed to these nodes either through DNS or some
    external load balancer.
  - You can choose a port range from 1-65535, or a random port from 30000-32767 will be
    used.

- Ingress

      + Bring your own ingress controller. This configuration will accept an ingress class name
       which the services will then use in their Ingress manifests. This implies that the ingress
       controller has some external connectivity already configured via some other load balancing
       mechanism.
      + Currently only the [ingress-nginx](https://github.com/kubernetes/ingress-nginx/ "https://github.com/kubernetes/ingress-nginx/") controller is supported.

  **Wildcard Hostname**

By default, Ingress routes will be defined with a host value of `\*`. Disable this setting to
use the defined hostname for the Wickr Enterprise Server. Wildcard Hostname is required for IP
based hostnames.
