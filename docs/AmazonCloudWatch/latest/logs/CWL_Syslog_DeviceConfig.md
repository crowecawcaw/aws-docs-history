

# Configuring syslog devices
<a name="CWL_Syslog_DeviceConfig"></a>

After setting up syslog ingestion, configure your syslog sources to send messages to the VPC endpoint DNS name. Your devices reach the endpoint via your VPN or Direct Connect connection to the VPC.

**Note**  
The following configurations are provided as examples. For complete configuration options and best practices, refer to the official documentation for your syslog implementation (rsyslog, syslog-ng, or your device vendor).

In the following examples, replace `{{VPCE_DNS}}` with the VPC endpoint DNS name from the setup procedure (for example, `vpce-0abc123def456.syslog-logs.us-east-1.vpce.amazonaws.com`).

## rsyslog
<a name="CWL_Syslog_DeviceConfig_Rsyslog"></a>

rsyslog is the default syslog daemon on most Linux distributions. Add the following configuration to `/etc/rsyslog.d/50-cwl-syslog.conf`.

**TCP \+ TLS:**

```
# Forward all logs to CloudWatch Logs via TCP+TLS
action(type="omfwd"
  target="{{VPCE_DNS}}"
  port="6514"
  protocol="tcp"
  StreamDriver="gtls"
  StreamDriverMode="1"
  StreamDriverAuthMode="x509/certvalid"
  template="RSYSLOG_SyslogProtocol23Format"
  queue.type="LinkedList"
  queue.filename="cwl_fwd"
  queue.saveOnShutdown="on"
  action.resumeRetryCount="-1")
```

**TCP plaintext:**

```
# Forward all logs to CloudWatch Logs via plaintext TCP
action(type="omfwd"
  target="{{VPCE_DNS}}"
  port="1514"
  protocol="tcp"
  template="RSYSLOG_SyslogProtocol23Format"
  queue.type="LinkedList"
  queue.filename="cwl_fwd"
  queue.saveOnShutdown="on"
  action.resumeRetryCount="-1")
```

**UDP:**

```
# Forward all logs to CloudWatch Logs via UDP
action(type="omfwd"
  target="{{VPCE_DNS}}"
  port="514"
  protocol="udp"
  template="RSYSLOG_SyslogProtocol23Format")
```

After adding the configuration, restart rsyslog:

```
sudo systemctl restart rsyslog
```

**Note**  
The `queue.type="LinkedList"` and `queue.saveOnShutdown="on"` directives enable disk-assisted queuing. If the connection to the VPC endpoint is temporarily lost, rsyslog buffers messages locally and retries delivery.

**Filtering by facility or severity:**

To send only specific messages, add a filter before the action:

```
# Send only auth messages via TCP+TLS
auth,authpriv.* action(type="omfwd"
  target="{{VPCE_DNS}}"
  port="6514"
  protocol="tcp"
  StreamDriver="gtls"
  StreamDriverMode="1"
  StreamDriverAuthMode="x509/certvalid"
  template="RSYSLOG_SyslogProtocol23Format")
```

## syslog-ng
<a name="CWL_Syslog_DeviceConfig_SyslogNg"></a>

syslog-ng is commonly used on network appliances and enterprise Linux systems. Add the following configuration to `/etc/syslog-ng/conf.d/cwl-syslog.conf`.

**TCP \+ TLS:**

```
destination d_cwl_syslog {
  network("{{VPCE_DNS}}"
    port(6514)
    transport("tls")
    tls(
      peer-verify(required-trusted)
      ca-dir("/etc/ssl/certs")
    )
  );
};

log {
  source(s_sys);
  destination(d_cwl_syslog);
};
```

**TCP plaintext:**

```
destination d_cwl_syslog {
  network("{{VPCE_DNS}}"
    port(1514)
    transport("tcp")
  );
};

log {
  source(s_sys);
  destination(d_cwl_syslog);
};
```

**UDP:**

```
destination d_cwl_syslog {
  network("{{VPCE_DNS}}"
    port(514)
    transport("udp")
  );
};

log {
  source(s_sys);
  destination(d_cwl_syslog);
};
```

After adding the configuration, restart syslog-ng:

```
sudo systemctl restart syslog-ng
```

## Quick validation
<a name="CWL_Syslog_DeviceConfig_QuickTest"></a>

Use the following commands from any host that can reach the VPC endpoint to verify connectivity.

**TCP plaintext (port 1514):**

```
echo "<134>1 $(date -u +%Y-%m-%dT%H:%M:%SZ) myhost myapp 1234 - - Hello from syslog" | \
  nc {{VPCE_DNS}} 1514
```

**TCP \+ TLS (port 6514):**

```
echo "<134>1 $(date -u +%Y-%m-%dT%H:%M:%SZ) myhost myapp 1234 - - Hello TLS syslog" | \
  openssl s_client -connect {{VPCE_DNS}}:6514 -quiet -no_ign_eof
```

**UDP (port 514):**

```
echo "<134>1 $(date -u +%Y-%m-%dT%H:%M:%SZ) myhost myapp 1234 - - Hello UDP syslog" | \
  nc -u -w1 {{VPCE_DNS}} 514
```

After sending test messages, verify delivery in CloudWatch Logs (usually within 10–20 seconds):

```
aws logs filter-log-events \
  --log-group-name /syslog/my-devices \
  --start-time $(date -d '5 minutes ago' +%s000 2>/dev/null || echo $(($(date -v-5M +%s) * 1000))) \
  --region $REGION
```

## Network appliances
<a name="CWL_Syslog_DeviceConfig_NetworkDevices"></a>

Most firewalls, routers, and switches support configuring an external syslog server by specifying a destination IP address and port. Use the private IP address of the VPC endpoint ENI (visible in the Amazon VPC console under **Endpoints**) and one of the supported ports (6514, 1514, or 514).

Consult your device's documentation for the specific configuration syntax. The key settings to configure are:
+ **Server address** – The VPC endpoint DNS name or ENI private IP address.
+ **Port** – 6514 (TCP\+TLS), 1514 (TCP), or 514 (UDP).
+ **Protocol** – TCP (recommended) or UDP.
+ **Format** – RFC 5424 (preferred) or RFC 3164 (legacy). Both are supported.

## TLS certificate trust
<a name="CWL_Syslog_DeviceConfig_TLS"></a>

The TLS connection on port 6514 uses an AWS-managed certificate issued by Amazon Trust Services. Most operating systems and syslog daemons trust this certificate automatically because the Amazon Trust Services root certificates are included in standard CA trust stores.

If your device does not trust the certificate by default, download the Amazon Trust Services root certificates from [https://www.amazontrust.com/repository/](https://www.amazontrust.com/repository/) and add them to your device's CA trust store.