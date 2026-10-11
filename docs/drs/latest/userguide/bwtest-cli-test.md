

# Test with the command line
<a name="bwtest-cli-test"></a>

In this test you can set the stream count to match what Elastic Disaster Recovery actually does. Except where a step says otherwise, run this task on the source server, against the endpoint from [Install the endpoint software](bwtest-software-install.md).

**Important**  
Use five concurrent streams. The Elastic Disaster Recovery agent's replication channel is exactly five TCP sockets to one replication server. Five streams reproduces that socket count. A single-stream test measures something Elastic Disaster Recovery never does and can report a fast link as much slower than it is.  
Five streams are not equivalent to what the agent does with them. The agent sends one ordered stream and rotates successive chunks across the five sockets from a single sender, and the receiver reassembles them in strict order, so a socket that stalls stalls the whole channel. LibreSpeed runs five independent streams that cannot block one another. Treat the result as the path's upper limit. See [Interpreting the result](bwtest-interpreting.md).

**Important**  
Five parallel streams can saturate the source server's uplink for about a minute. On a production source server, that can slow business traffic and raise replication lag on other servers that replicate over the same link. Run the test off-peak, coordinate with whoever operates the network, and test one source server at a time.

## Install the client
<a name="bwtest-cli-install"></a>

The client is [librespeed/speedtest-cli](https://github.com/librespeed/speedtest-cli), the LibreSpeed command-line client.

```
export LIBRESPEED_CLI_VERSION=1.0.14
export CLI_ARCH=linux_amd64                 # see the release page for other platforms
export PORT=1500                            # must match the port the endpoint listens on
export STREAMS=5                            # matches the DRS agent; do not change without reading this task
export DURATION=30                          # seconds per direction

mkdir -p ~/bwclient && cd ~/bwclient
curl -sSLO "https://github.com/librespeed/speedtest-cli/releases/download/v${LIBRESPEED_CLI_VERSION}/librespeed-cli_${LIBRESPEED_CLI_VERSION}_${CLI_ARCH}.tar.gz"
```

**Note**  
The project's GitHub release page lists a SHA-256 digest beside each archive. The digest covers the archive, not the extracted binary, so hash the archive and compare it with that digest before you unpack it:  

```
sha256sum "librespeed-cli_${LIBRESPEED_CLI_VERSION}_${CLI_ARCH}.tar.gz"
```

```
tar -xzf "librespeed-cli_${LIBRESPEED_CLI_VERSION}_${CLI_ARCH}.tar.gz" librespeed-cli
chmod +x librespeed-cli
./librespeed-cli --version
```

**Note**  
The release page carries builds for other operating systems and architectures. The Windows builds are `.zip` archives, such as `librespeed-cli_1.0.14_windows_amd64.zip`, that contain `librespeed-cli.exe`. For Windows, see [Install on Windows](https://github.com/librespeed/speedtest-cli#install-on-windows) in the project's README. The commands on this page are for a Linux shell.

**Note**  
The published Linux client binaries for x86 and Arm are UPX-compressed, which some antivirus and endpoint detection and response (EDR) tools flag or quarantine as a heuristic. If that happens on a production source server, the download is not corrupt: add an exception for the binary, or run the client from a non-production host on the same network path.

## Copy the certificate to the client
<a name="bwtest-cli-copycert"></a>

Prefer real certificate verification over a bypass: copy the endpoint's certificate to the client and pass it as the trust anchor. This is the better option because the certificate is its own CA (`CA:TRUE` in [Generate the TLS certificate](bwtest-software-install.md#bwtest-generate-cert)), so verification genuinely checks that you are talking to the endpoint you built. A bypass checks nothing and also hides a TLS-intercepting middlebox, which is one of the things this test exists to detect.

Display the certificate on the endpoint instance, and copy its full output:

```
cat ~/bwtest/certs/server.crt
```

On the source server, write the copied certificate to `~/bwclient/target-ca.crt` with the following command. Paste the certificate, including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines, then press `Ctrl+D` on an empty line to end the input:

```
cat > ~/bwclient/target-ca.crt
```

The certificate is public material, so it is safe to display and paste; only the private key is secret, and it never leaves the instance. The paste travels over the shell session you already use, not over the measured TLS path on port 1500, so a TLS-intercepting middlebox on that path cannot substitute it. A paste error makes verification fail rather than pass silently.

**Note**  
If you genuinely cannot move the file, for example on an air-gapped source server with no SSH and no Session Manager path, substitute `--skip-cert-verify` for `--ca-cert` in [Run the measurement](#bwtest-cli-run). The client then accepts any certificate, including one presented by something intercepting the connection, and TLS interception is one of the conditions this test is meant to expose.

## Write the server list
<a name="bwtest-cli-serverlist"></a>

The client takes its target from a small JSON file. Field names are case-sensitive: note `dlURL`, `ulURL`, and `pingURL`, but `getIpURL` with a lowercase `p`.

```
ENDPOINT_HOST={{ENDPOINT_NAME}}        # the CN= value the certificate step printed; over VPN or Direct Connect, its PRIV_IP value instead

cat > ~/bwclient/servers-1500.json <<JSON
[
  {
    "id": 1,
    "name": "DRS bandwidth test endpoint (TLS :${PORT})",
    "server": "https://${ENDPOINT_HOST}:${PORT}/backend/",
    "dlURL": "garbage",
    "ulURL": "empty",
    "pingURL": "empty",
    "getIpURL": "getIP"
  }
]
JSON

cat ~/bwclient/servers-1500.json
```

**Important**  
The trailing `/backend/` on `server` is required. This endpoint serves its throughput routes under `backend/`, not at the root, and it has no `.php` route aliases. Without the suffix, every endpoint returns 404 and the client aborts at its pre-flight check, reporting that the server is not responding, before taking any measurement.

The host in `server` must match a SAN entry of the same kind: a DNS name must match a `DNS:` entry, and a bare IP address must match an `IP Address:` entry. In [Generate the TLS certificate](bwtest-software-install.md#bwtest-generate-cert) on the endpoint, the `echo "CN=$CN"` line printed a value; set `ENDPOINT_HOST` on this source server to that same value and the kinds match automatically.

The host must also match the path you intend to measure. A source server on-premises over VPN or Direct Connect has to use the endpoint's private IP literal, the `PRIV_IP` value from the same step, which the SAN lists as an `IP Address:` entry. On-premises DNS usually cannot resolve the private DNS name. The public DNS name resolves to the public address, which bypasses the tunnel.

An in-VPC client measuring the internet path has to use the endpoint's public IP literal here, because the public DNS name resolves to the private address from inside the VPC and the traffic would never leave.

## Run the measurement
<a name="bwtest-cli-run"></a>

```
cd ~/bwclient
./librespeed-cli \
  --local-json servers-1500.json \
  --server 1 \
  --concurrent "$STREAMS" \
  --duration "$DURATION" \
  --ca-cert target-ca.crt \
  --no-icmp
```
+ `--concurrent 5` matches the Elastic Disaster Recovery agent's five replication sockets. Without this flag, the client uses three.
+ `--duration 30` sets the length of each direction, not of the whole run. Expect about 62 seconds of wall-clock time: 30 seconds of download, then 30 of upload, plus pre-flight.
+ `--no-icmp` skips the ICMP ping probe, which many networks block regardless of TCP reachability. The client can still print a `Ping` line measured over HTTP, so a reported ping value does not mean ICMP was used.

Check that the client reports a client IP that is the source server's address, which proves the request really originated off-instance. Verification succeeded if the run completed without a certificate error and without `--skip-cert-verify`.

Run the tests one at a time unless you specifically want to measure contention.

**Note**  
Cross-Availability Zone paths add latency and are metered differently from same-Zone paths, so a figure measured within one Availability Zone should not be assumed to carry over to a cross-Zone path. See [Interpreting the result](bwtest-interpreting.md).