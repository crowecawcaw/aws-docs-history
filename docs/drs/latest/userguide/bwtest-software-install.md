

# Install the endpoint software
<a name="bwtest-software-install"></a>

Everything in this task runs on the Amazon EC2 instance, as an ordinary user rather than root. The procedure needs no elevated privilege. Installing the optional diagnostic tools, such as `sysstat` for the `sar` command in [Do not compare headline figures between runs](bwtest-interpreting.md#bwtest-run-variance), does need `sudo`. The whole task takes about 20 seconds after you have a shell.

## Download and unpack the endpoint software
<a name="bwtest-download-software"></a>

The endpoint is speedtest-rust, an open-source Rust implementation of the LibreSpeed server. It ships as a single binary with a built-in browser test page, which is why this procedure needs no web server, no runtime, and no `sudo`. This task downloads speedtest-rust from [librespeed/speedtest-rust on the GitHub website](https://github.com/librespeed/speedtest-rust). Review the project before you run it in your account.

**Important**  
This procedure uses third-party, open-source software (librespeed/speedtest-rust here, and librespeed/speedtest-cli in [Test with the command line](bwtest-cli-test.md)) that is not developed, maintained, or supported by AWS. It is provided on an "AS IS" basis, with no guarantee of completeness, accuracy or timeliness, and without warranty or representations of any kind, expressed or implied. In no event will AWS and/or its subsidiaries and/or their employees or service providers be liable to you or anyone else for any decision made or action taken in reliance on this software or for any direct, indirect, consequential, special or similar damages (including any kind of loss), even if advised of the possibility of such damages. AWS is not responsible for the update, validation or support of this software. Review each project and confirm it meets your organization's security and licensing requirements before you run it on servers in your account.

```
export LIBRESPEED_RS_VERSION=1.4.0
export ARCH_TARGET=x86_64-unknown-linux-musl        # aarch64-unknown-linux-gnu on Graviton.
export PORT=1500                                    # the TLS port the endpoint listens on.
export CERT_DAYS=7                                  # certificate lifetime; the rig should not outlive it.

mkdir -p ~/bwtest && cd ~/bwtest
curl -sSLO "https://github.com/librespeed/speedtest-rust/releases/download/v${LIBRESPEED_RS_VERSION}/librespeed-rs-${ARCH_TARGET}.tar.xz"
```

**Note**  
The project's GitHub release page lists a SHA-256 digest beside each archive. The digest covers the archive, not the extracted binary, so hash the archive and compare it with that digest before you unpack it:  

```
sha256sum "librespeed-rs-${ARCH_TARGET}.tar.xz"
```

```
tar -xJf "librespeed-rs-${ARCH_TARGET}.tar.xz"
chmod +x librespeed-rs
```

The archive is about 11 MB and unpacks to roughly 48 MB, of which a 42 MB ASN database is never used by this procedure.

**Note**  
Downloading the archive is the only step that needs internet access from the endpoint. Use one of the following three ways to satisfy it, in order of preference:  
Download the archive on a machine that has egress and copy it in. An endpoint in a subnet with no internet route can be staged this way, and everything downstream behaves identically. Then continue from the `tar -xJf` command.  

   ```
   scp -i /path/to/key.pem librespeed-rs-*.tar.xz {{USER}}@{{PRIVATE_IP}}:~/bwtest/
   ```
Put a NAT gateway on the subnet, if one is not already there.
Give the instance a public IP for the install, and accept the exposure described in [Security considerations for the test endpoint](network-bandwidth-test.md#bwtest-security).

## Delete the shipped config file
<a name="bwtest-delete-config"></a>

```
rm configs.toml
```

**Important**  
The shipped file points at an assets directory that does not exist at your install path. Left in place, the program logs Config assets directory failed \! and then serves 404 on `/`, so the browser page is dead although the CLI endpoints keep working, which is easy to misdiagnose.

Deleting the file also stops the program from creating a `speedtest.db` in your working directory, and it removes the file as a thing to get wrong: with nothing to load, the defaults are used deterministically. Editing the file instead of deleting it is not a reliable substitute: depending on how the program is invoked, a partial or hand-edited config is either rejected with a parse error or silently ignored in favor of defaults. With no config file present, startup logs `Configs initialized with defaults` and `Config default assets directory.`, and `/` returns 200.

## Generate the TLS certificate
<a name="bwtest-generate-cert"></a>

The certificate's SAN must cover the exact address the client connects to, and it must cover it as the right kind of entry: a DNS name needs a `DNS:` entry, and a bare IP address needs an `IP Address:` entry.

Derive the addresses from the instance metadata service (IMDSv2):

```
TOKEN=$(curl -sS -X PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 300")

# -f is essential. See the following warning.
IMDS() { curl -fsS -H "X-aws-ec2-metadata-token: $TOKEN" \
  "http://169.254.169.254/latest/meta-data/$1" 2>/dev/null; }

PUB_DNS=$(IMDS public-hostname)
PUB_IP=$(IMDS public-ipv4)
PRIV_DNS=$(IMDS local-hostname)
PRIV_IP=$(IMDS local-ipv4)
printf 'PUB_DNS=[%s]\nPUB_IP=[%s]\nPRIV_DNS=[%s]\nPRIV_IP=[%s]\n' \
  "$PUB_DNS" "$PUB_IP" "$PRIV_DNS" "$PRIV_IP"
```

**Important**  
Use `curl -fsS`, not `curl -sS`. On an instance with no public address, the `public-hostname` and `public-ipv4` metadata paths return a 404 HTML error page with exit status 0. Without `-f`, `curl` prints that page to stdout and succeeds, so `PUB_DNS` and `PUB_IP` fill with an XHTML document instead of being empty, and `openssl` then fails and writes no certificate. With `-f`, the same request fails cleanly and the variables are left empty, which is correct and expected. If those two variables contain HTML, you dropped the `-f`.

```
cd ~/bwtest && mkdir -p certs

SAN="DNS:${PRIV_DNS},IP:${PRIV_IP}"
[ -n "$PUB_IP" ] && SAN="IP:${PUB_IP},${SAN}"
[ -n "$PUB_DNS" ] && SAN="DNS:${PUB_DNS},${SAN}"
CN=${PUB_DNS:-$PRIV_DNS}
echo "CN=$CN"; echo "SAN=$SAN"

openssl req -x509 -newkey rsa:2048 -nodes -sha256 -days "$CERT_DAYS" \
  -keyout certs/server.key -out certs/server.crt \
  -subj "/CN=${CN}/O=DRS-Bandwidth-Test/OU=throwaway" \
  -addext "subjectAltName=${SAN}" \
  -addext "basicConstraints=critical,CA:TRUE" \
  -addext "keyUsage=digitalSignature,keyEncipherment,keyCertSign" \
  -addext "extendedKeyUsage=serverAuth"

chmod 600 certs/server.key
chmod 644 certs/server.crt
openssl x509 -in certs/server.crt -noout -subject -dates -ext subjectAltName
```

`basicConstraints=critical,CA:TRUE` is deliberate: it makes this one certificate act as its own trust anchor, which is what the CLI uses to run with full verification in the command-line test instead of disabling it. Add `,DNS:localhost,IP:127.0.0.1` to `SAN` if you also want to test from the instance itself.

**Note**  
The certificate expires after `CERT_DAYS`. The rig should be torn down long before that. If it is still up when the certificate expires, verification starts failing, and the correct response is teardown, not a new certificate.

## Start the endpoint
<a name="bwtest-endpoint-start"></a>

```
cd ~/bwtest
nohup ./librespeed-rs -p "$PORT" --enable-tls true \
  --tls-cert-file "$HOME/bwtest/certs/server.crt" \
  --tls-key-file  "$HOME/bwtest/certs/server.key" > ~/bwtest/server.log 2>&1 &
```

Starting it with `nohup ... &` keeps it in the same shell you used for the earlier steps, so the `PORT` and certificate variables are still in scope, and the endpoint keeps running after you log out. Read its output from the log file rather than a live foreground:

```
sleep 1 && cat ~/bwtest/server.log
```

The log opens with an ASCII-art banner. Each line after it is timestamped and prefixed `INFO librespeed_rs`, so it will not match the following literally:

```
Config default assets directory.
Configs initialized with defaults
Database disabled
Server started on 0.0.0.0:1500
Server base url : /backend/
Server TLS successfully configured
```

## Verify TLS with a cleartext probe that must fail
<a name="bwtest-verify-tls"></a>

**Important**  
Do not confirm TLS by reading the log. The log misleads in both directions: it prints `Server started` before dying on a bad certificate, and it prints a healthy log while serving plaintext. If the certificate flags are supplied but `--enable-tls` is omitted, the endpoint serves plaintext HTTP 200 with a working page and no error output, and the throughput number it produces is inflated because no encryption was performed.

The only reliable check is a negative one. Run both of these from the instance:

```
# NEGATIVE control - cleartext on the TLS port. This MUST FAIL.
curl -sS -m 5 "http://127.0.0.1:${PORT}/" -o /dev/null -w 'http_rc=%{http_code}\n'; echo "curl_rc=$?"

# POSITIVE control - TLS on the same port. This MUST return 200.
curl -sSk -m 5 "https://127.0.0.1:${PORT}/" -o /dev/null -w 'http_rc=%{http_code}\n'; echo "curl_rc=$?"
```

The following table lists the verdict for each pair of results:


| Negative probe | Positive probe | Verdict | 
| --- | --- | --- | 
| Non-zero curl\_rc, no page | http\_rc=200 | TLS is on. Continue. | 
| http\_rc=200 | Non-zero curl\_rc | TLS is off, and you are about to measure plaintext. Stop, check --enable-tls true, and restart. | 
| Non-zero curl\_rc, no page | Non-zero curl\_rc, no page | Both probes failed, so this is not a TLS pass. Nothing is listening on the port you probed, which happens when PORT is unset in this shell and both probes went to a port with no server. The negative probe failing here does not confirm TLS. Confirm PORT is set to 1500, confirm the endpoint is running, and run both probes again. | 

Against a correctly configured endpoint, the negative probe returns immediately rather than burning its five-second timeout, reporting `http_rc=000` and `curl_rc=1`. For a second confirmation, the following command reports `wrong version number` against a plaintext endpoint:

```
openssl s_client -connect "127.0.0.1:${PORT}" -brief </dev/null
```

Expect `Protocol version: TLSv1.3` and `Verification error: self-signed certificate`. The verification error is the expected shape here; the trust path is established on the client side in [Copy the certificate to the client](bwtest-cli-test.md#bwtest-cli-copycert), not in this probe. You might also see `Can't use SSL_get_servername`: this message is benign, because it only reports that no Server Name Indication (SNI) value was sent on this probe, and it does not affect the result.