# Verifying TLS is enabled for Amazon ECS

Service Connect

Service Connect initiates TLS at the Service Connect agent and terminates it at
the destination agent. As a result, the application code never sees TLS
interactions. Use the following steps to verify that TLS is enabled.

1. Include the `openssl` CLI in your application image.
2. Enable [ECS Exec](ecs-exec.md "ecs-exec.md") on
   your services to connect to your tasks via SSM. Alternately, you can
   launch an Amazon EC2 instance in the same Amazon VPC as the service.
3. Retrieve the IP and port of a task from a service that you want to verify.
   You can retrieve the task IP address in the AWS Cloud Map console. The information
   is on the service details page for the namespace.
4. Log on to any of your tasks using `execute-command` like in the
   following example. Alternately, log on to the Amazon EC2 instance created in
   **Step 2**.

```
$ aws ecs execute-command --cluster `cluster-name` \
    --task `task-id`  \
    --container `container-name` \
    --interactive \
    --command "/bin/sh"
```

###### Note

Calling the DNS name directly does not reveal the certificate. 5. In the connected shell, use the `openssl` CLI to verify and
view the certificate attached to the task.

Example:

```
openssl s_client -connect 10.0.147.43:6379 < /dev/null 2> /dev/null \
| openssl x509 -noout -text
```

Example response:

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            <serial-number>
        Signature Algorithm: ecdsa-with-SHA256
        Issuer: <issuer>
        Validity
            Not Before: Jan 23 21:38:12 2024 GMT
            Not After : Jan 30 22:38:12 2024 GMT
        Subject: <subject>
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                pub:
                    <pub>
                ASN1 OID: prime256v1
                NIST CURVE: P-256
        X509v3 extensions:
            X509v3 Subject Alternative Name:
                DNS:redis.yelb-cftc
            X509v3 Basic Constraints:
                CA:FALSE
            X509v3 Authority Key Identifier:
                keyid:<key-id>

            X509v3 Subject Key Identifier:
                1D:<id>
            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment
            X509v3 Extended Key Usage:
                TLS Web Server Authentication, TLS Web Client Authentication
    Signature Algorithm: ecdsa-with-SHA256
        <hash>
```
