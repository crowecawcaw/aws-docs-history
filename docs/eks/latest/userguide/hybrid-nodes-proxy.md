**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure proxy for hybrid nodes

If you are using a proxy server in your on-premises environment for traffic leaving your data center or edge environment, you need to separately configure your nodes and your cluster to use your proxy server.

Cluster

On your cluster, you need to configure `kube-proxy` to use your proxy server. You must configure `kube-proxy` after creating your Amazon EKS cluster.

Nodes

On your nodes, you must configure the operating system, `containerd`, `kubelet`, and the Amazon SSM agent to use your proxy server. You can make these changes during the build process for your operating system images or before you run `nodeadm init` on each hybrid node.

## Node-level configuration

You must apply the following configurations either in your operating system images or before running `nodeadm init` on each hybrid node.

### `containerd` proxy configuration

`containerd` is the default container management runtime for Kubernetes. If you are using a proxy for internet access, you must configure `containerd` so it can pull the container images required by Kubernetes and Amazon EKS.

Create a file on each hybrid node called `http-proxy.conf` in the `/etc/systemd/system/containerd.service.d` directory with the following contents. Replace `proxy-domain` and `port` with the values for your environment.

```
 [Service]
Environment="HTTP_PROXY=http://<replaceable>proxy-domain:port</replaceable>"
Environment="HTTPS_PROXY=http://<replaceable>proxy-domain:port</replaceable>"
Environment="NO_PROXY=localhost"
```

#### `containerd` configuration from user data

The `containerd.service.d` directory will need to be created for this file. You will need to reload systemd to pick up the configuration file without a reboot. In AL2023, the service will likely already be running when your script executes, so you will also need to restart it.

```
 mkdir -p /etc/systemd/system/containerd.service.d
echo '[Service]' > /etc/systemd/system/containerd.service.d/http-proxy.conf
echo 'Environment="HTTP_PROXY=http://<replaceable>proxy-domain:port</replaceable>"' >> /etc/systemd/system/containerd.service.d/http-proxy.conf
echo 'Environment="HTTPS_PROXY=http://<replaceable>proxy-domain:port</replaceable>"' >> /etc/systemd/system/containerd.service.d/http-proxy.conf
echo 'Environment="NO_PROXY=localhost"' >> /etc/systemd/system/containerd.service.d/http-proxy.conf
systemctl daemon-reload
systemctl restart containerd
```

### `kubelet` proxy configuration

`kubelet` is the Kubernetes node agent that runs on each Kubernetes node and is responsible for managing the node and pods running on it. If you are using a proxy in your on-premises environment, you must configure the `kubelet` so it can communicate with your Amazon EKS cluster’s public or private endpoints.

Create a file on each hybrid node called `http-proxy.conf` in the `/etc/systemd/system/kubelet.service.d/` directory with the following content. Replace `proxy-domain` and `port` with the values for your environment.

```
 [Service]
Environment="HTTP_PROXY=http://<replaceable>proxy-domain:port</replaceable>"
Environment="HTTPS_PROXY=http://<replaceable>proxy-domain:port</replaceable>"
Environment="NO_PROXY=localhost"
```

#### `kubelet` configuration from user data

The `kubelet.service.d` directory must be created for this file. You will need to reload systemd to pick up the configuration file without a reboot. In AL2023, the service will likely already be running when your script executes, so you will also need to restart it.

```
 mkdir -p /etc/systemd/system/kubelet.service.d
echo '[Service]' > /etc/systemd/system/kubelet.service.d/http-proxy.conf
echo 'Environment="HTTP_PROXY=http://<replaceable>proxy-domain:port</replaceable>"' >> /etc/systemd/system/kubelet.service.d/http-proxy.conf
echo 'Environment="HTTPS_PROXY=http://<replaceable>proxy-domain:port</replaceable>"' >> /etc/systemd/system/kubelet.service.d/http-proxy.conf
echo 'Environment="NO_PROXY=localhost"' >> /etc/systemd/system/kubelet.service.d/http-proxy.conf
systemctl daemon-reload
systemctl restart kubelet
```

### `ssm` proxy configuration

`ssm` is one of the credential providers that can be used to initialize a hybrid node. `ssm` is responsible for authenticating with AWS and generating temporary credentials that is used by `kubelet`. If you are using a proxy in your on-premises environment and using `ssm` as your credential provider on the node, you must configure the `ssm` so it can communicate with Amazon SSM service endpoints.

Create a file on each hybrid node called `http-proxy.conf` in the path below depending on the operating system

- Ubuntu - `/etc/systemd/system/snap.amazon-ssm-agent.amazon-ssm-agent.service.d/http-proxy.conf`
- Amazon Linux 2023 and Red Hat Enterprise Linux - `/etc/systemd/system/amazon-ssm-agent.service.d/http-proxy.conf`

Populate the file with the following contents. Replace `proxy-domain` and `port` with the values for your environment.

```
 [Service]
Environment="HTTP_PROXY=http://<replaceable>proxy-domain:port</replaceable>"
Environment="HTTPS_PROXY=http://<replaceable>proxy-domain:port</replaceable>"
Environment="NO_PROXY=localhost"
```

#### `ssm` configuration from user data

The `ssm` systemd service file directory must be created for this file. The directory path depends on the operating system used on the node.

- Ubuntu - `/etc/systemd/system/snap.amazon-ssm-agent.amazon-ssm-agent.service.d`
- Amazon Linux 2023 and Red Hat Enterprise Linux - `/etc/systemd/system/amazon-ssm-agent.service.d`

Replace the systemd service name in the restart command below depending on the operating system used on the node

- Ubuntu - `snap.amazon-ssm-agent.amazon-ssm-agent`
- Amazon Linux 2023 and Red Hat Enterprise Linux - `amazon-ssm-agent`

```
 mkdir -p <replaceable>systemd-service-file-directory
echo '[Service]' > [.replaceable]#systemd-service-file-directory/http-proxy.conf
echo 'Environment="HTTP_PROXY=http://[.replaceable]#proxy-domain:port</replaceable>"' >> <replaceable>systemd-service-file-directory/http-proxy.conf
echo 'Environment="HTTPS_PROXY=http://[.replaceable]#proxy-domain:port</replaceable>"' >> [.replaceable]#systemd-service-file-directory/http-proxy.conf
echo 'Environment="NO_PROXY=localhost"' >> [.replaceable]#systemd-service-file-directory/http-proxy.conf
systemctl daemon-reload
systemctl restart [.replaceable]#systemd-service-name
```

### Operating system proxy configuration

If you are using a proxy for internet access, you must configure your operating system to be able to pull the hybrid nodes dependencies from your operating systems' package manager.

**Ubuntu**

1. Configure `snap` to use your proxy with the following commands:

```
 sudo snap set system proxy.https=http://<replaceable>proxy-domain:port</replaceable>
sudo snap set system proxy.http=http://<replaceable>proxy-domain:port</replaceable>
```

2. To enable proxy for `apt`, create a file called `apt.conf` in the `/etc/apt/` directory. Replace proxy-domain and port with the values for your environment.

```
 Acquire::http::Proxy "http://<replaceable>proxy-domain:port</replaceable>";
Acquire::https::Proxy "http://<replaceable>proxy-domain:port</replaceable>";
```

**Amazon Linux 2023**

1. Configure `dnf` to use your proxy. Create a file `/etc/dnf/dnf.conf` with the proxy-domain and port values for your environment.

```
 proxy=http://<replaceable>proxy-domain:port</replaceable>
```

**Red Hat Enterprise Linux**

1. Configure `yum` to use your proxy. Create a file `/etc/yum.conf` with the proxy-domain and port values for your environment.

```
 proxy=http://<replaceable>proxy-domain:port</replaceable>
```

### IAM Roles Anywhere proxy configuration

The IAM Roles Anywhere credential provider service is responsible for refreshing credentials when using IAM Roles Anywhere with the `enableCredentialsFile` flag (see [EKS Pod Identity Agent](hybrid-nodes-add-ons.md#hybrid-nodes-add-ons-pod-id "hybrid-nodes-add-ons.md#hybrid-nodes-add-ons-pod-id")). If you are using a proxy in your on-premises environment, you must configure the service so it can communicate with IAM Roles Anywhere endpoints.

Create a file called `http-proxy.conf` in the `/etc/systemd/system/aws_signing_helper_update.service.d/` directory with the following content. Replace `proxy-domain` and `port` with the values for your environment.

```
 [Service]
Environment="HTTP_PROXY=http://<replaceable>proxy-domain:port</replaceable>"
Environment="HTTPS_PROXY=http://<replaceable>proxy-domain:port</replaceable>"
Environment="NO_PROXY=localhost"
```

## Cluster wide configuration

The configurations in this section must be applied after you create your Amazon EKS cluster and before running `nodeadm init` on each hybrid node.

### kube-proxy proxy configuration

Amazon EKS automatically installs `kube-proxy` on each hybrid node as a DaemonSet when your hybrid nodes join the cluster. `kube-proxy` enables routing across services that are backed by pods on Amazon EKS clusters. To configure each host, `kube-proxy` requires DNS resolution for your Amazon EKS cluster endpoint.

1. Edit the `kube-proxy` DaemonSet with the following command

```
 kubectl -n kube-system edit ds kube-proxy
```

This will open the `kube-proxy` DaemonSet definition on your configured editor. 2. Add the environment variables for `HTTP_PROXY` and `HTTPS_PROXY`. Note the `NODE_NAME` environment variable should already exist in your configuration. Replace `proxy-domain` and `port` with values for your environment.

```
 containers:
  - command:
    - kube-proxy
    - --v=2
    - --config=/var/lib/kube-proxy-config/config - --hostname-override=$(NODE_NAME)
    env:
    - name: HTTP_PROXY
      value: http://<replaceable>proxy-domain:port</replaceable>
    - name: HTTPS_PROXY
      value: http://<replaceable>proxy-domain:port</replaceable>
    - name: NODE_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: spec.nodeName
```
