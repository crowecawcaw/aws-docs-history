This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Troubleshooting

## Deleting the Wickr

namespace

If you need to delete the `wickr` namespace to start over, it's important
that you first back up any Service Accounts that were created by CDK within that
namespace. These Service Accounts allow Wickr services to communicate with AWS APIs
through IAM roles. Without them, tasks like file uploads through Amazon Simple Storage Service (Amazon S3) will
no longer work.

Use the following command to back up the Service Accounts and delete and recreate the
`wickr` namespace and the appropriate Service Accounts:

```
kubectl -n wickr get sa fileproxy -o yaml > fileproxy-sa.yaml && \
  kubectl delete ns wickr && \
  kubectl create ns wickr && \
  kubectl apply -f fileproxy-sa.yaml

```

## Resetting

the KOTS Admin Console password

You can reset your KOTS Admin Console password with the following command:

```
kubectl kots -n wickr **reset-password**
```

When you change this password you may also want to update the `wickr/kots`
Secrets Manager secret as well, although it will generally not be used again by any
automation.

## Issues connecting to

EKS cluster with bastion

If your connection to the EKS cluster through the bastion seems slow or is timing out
occasionally, you may see the following error when running `kubectl`
commands:

net/http: request canceled while waiting for connection (Client.Timeout exceeded while
awaiting headers)

This issue can often be remedied by logging into the bastion host via SSM (see the
`BastionSSMCommand` on the WickrEks stack) and restarting the
`tinyproxy` service:

```
sudo systemctl restart tinyproxy
```
