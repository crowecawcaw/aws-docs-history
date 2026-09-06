

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Generating a self-signed certificate for FSx for ONTAP
<a name="fsx-ontap-generate-certs"></a>

To generate a self-signed CA and client certificate, save the following script as `generate-fsx-mgn-certs.sh` and run it:

```
[~]$ chmod +x generate-fsx-mgn-certs.sh
./generate-fsx-mgn-certs.sh "{{YourOrg}}" "{{US}}"
```

```
#!/bin/bash
set -e
ORG="${1:-YourOrg}"
COUNTRY="${2:-US}"
DAYS_CA="${3:-3650}"
DAYS_CLIENT="${4:-365}"

# Generate CA private key and certificate
openssl genrsa -out ca.key 4096
openssl req -new -x509 -key ca.key -out ca.crt -days "$DAYS_CA" \
  -subj "/CN=FSx-ONTAP-Client-CA/O=$ORG/C=$COUNTRY" \
  -addext basicConstraints=critical,CA:TRUE \
  -addext keyUsage=critical,keyCertSign,cRLSign \
  -addext subjectKeyIdentifier=hash

# Generate client key
openssl genrsa -out fsx-mgn-client.key 2048

# Create OpenSSL config
cat > openssl-client.cnf << EOF
[ req ]
default_bits = 2048
prompt = no
default_md = sha256
distinguished_name = dn
req_extensions = req_ext
[ dn ]
CN = cert_usr
O = $ORG
C = $COUNTRY
[ req_ext ]
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth
subjectKeyIdentifier = hash
[ usr_cert ]
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth
authorityKeyIdentifier = keyid,issuer
subjectKeyIdentifier = hash
EOF

# Create CSR and sign it
openssl req -new -key fsx-mgn-client.key -out fsx-mgn-client.csr \
  -config openssl-client.cnf
openssl x509 -req -in fsx-mgn-client.csr \
  -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out fsx-mgn-client.crt -days "$DAYS_CLIENT" \
  -extfile openssl-client.cnf -extensions usr_cert

# Convert key to PKCS#8 format
openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt \
  -in fsx-mgn-client.key -out fsx-mgn-client.key

# Verify
openssl verify -CAfile ca.crt fsx-mgn-client.crt
```

**Output files:**
+ `fsx-mgn-client.crt` – Client certificate
+ `fsx-mgn-client.key` – Private key (PKCS\#8 format)
+ `ca.crt` – CA certificate (install on FSx for ONTAP)

**Manual steps (alternative):**

If you prefer to run each step individually:

1. Create a Certification Authority (CA):

   ```
   # Generate CA private key
   [~]$ openssl genrsa -out ca.key 4096
   
   # Create self-signed CA certificate
   [~]$ openssl req -new -x509 -key ca.key -out ca.crt -days 3650 \
     -subj "/CN=FSx-ONTAP-Client-CA/O={{YourOrg}}/C={{US}}" \
     -addext basicConstraints=critical,CA:TRUE \
     -addext keyUsage=critical,keyCertSign,cRLSign \
     -addext subjectKeyIdentifier=hash
   ```

1. Generate a client key:

   ```
   [~]$ openssl genrsa -out fsx-mgn-client.key 2048
   ```

1. Create an `openssl-client.cnf` file:

   ```
   [ req ]
   default_bits       = 2048
   prompt             = no
   default_md         = sha256
   distinguished_name = dn
   req_extensions     = req_ext
   
   [ dn ]
   CN = cert_usr
   O  = {{YourOrg}}
   C  = {{US}}
   
   [ req_ext ]
   keyUsage         = critical, digitalSignature, keyEncipherment
   extendedKeyUsage = clientAuth
   subjectKeyIdentifier = hash
   
   [ usr_cert ]
   keyUsage         = critical, digitalSignature, keyEncipherment
   extendedKeyUsage = clientAuth
   authorityKeyIdentifier = keyid,issuer
   subjectKeyIdentifier  = hash
   ```

1. Create a new certificate signing request (CSR):

   ```
   [~]$ openssl req -new -key fsx-mgn-client.key -out fsx-mgn-client.csr \
     -config openssl-client.cnf
   ```

1. Sign the CSR with your CA:

   ```
   [~]$ openssl x509 -req -in fsx-mgn-client.csr \
       -CA ca.crt -CAkey ca.key -CAcreateserial \
       -out fsx-mgn-client.crt -days 365 \
       -extfile openssl-client.cnf -extensions usr_cert
   ```

1. Convert key to PKCS\#8 format:

   ```
   [~]$ openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt \
     -in fsx-mgn-client.key -out fsx-mgn-client.key
   ```

1. Verify the certificate:

   ```
   [~]$ openssl verify -CAfile ca.crt fsx-mgn-client.crt
   ```