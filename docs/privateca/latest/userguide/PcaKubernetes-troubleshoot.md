# Troubleshoot Kubernetes with AWS Private CA

You can get the logs for `aws-private-ca-issuer` with the following
procedure:

1. Get the name of the pod:

```
kubectl get pods -A
```

2. To view the issuer logs, use the following command:

```
kubectl logs -n aws-privateca-issuer <pod-name> aws-privateca-issuer
```

3. To view the IAM Roles Anywhere logs, use the following command:

```
kubectl logs -n aws-privateca-issuer <pod-name> rolesanywhere-credentials-helper
```

To check the status of your AWS Private CA issuer, use one of the following:

**To check that your issuer is ready, use the following
command:**

```
kubectl get AWSPCAClusterIssuers -o json | jq '.items[].status
```

The response should be similar to the following:

```
{
  "conditions": [
    {
      "lastTransitionTime": "2024-07-03T13:56:37Z",
      "message": "Issuer verified",
      "reason": "Verified",
      "status": "True",
      "type": "Ready"
    }
  ]
}
```

If the issuer is not in the `Ready` state, the `message` field
provides information on why the issuer was unable to reach the `Ready`
state.

**To check that your certificate is ready, use the following
command:**

```
kubectl get certificates -o json | jq '.items[].status'
```

The response should be similar to the following:

```
{
  "conditions": [
    {
      "lastTransitionTime": "2024-07-03T13:58:13Z",
      "message": "Certificate is up to date and has not expired",
      "observedGeneration": 1,
      "reason": "Ready",
      "status": "True",
      "type": "Ready"
    }
  ],
  "notAfter": "2024-10-01T13:58:12Z",
  "notBefore": "2024-07-03T12:58:12Z",
  "renewalTime": "2024-09-16T13:58:12Z",
  "revision": 1
}
```

If the certificate is not in the `Ready` state, the `message` field
provides information on why the certificate was not able to reach the `Ready`
state.
