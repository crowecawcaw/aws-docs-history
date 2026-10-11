

# Troubleshooting the bandwidth test
<a name="bwtest-troubleshooting"></a>

## The connection is refused, or the page will not load
<a name="bwtest-ts-refused"></a>

For information about general port 1500 reachability, including firewalls and network ACLs, see [Verifying network connectivity](verifying-network-connectivity.md). Then check the following, which are specific to this test endpoint:

1. Confirm the source address has not changed. An internet egress address can rotate. On the testing machine, compare `curl -sS https://checkip.amazonaws.com` against the address in your security group.

1. Confirm you are using the right kind of address for your case. A rule naming a public address does not admit the same host's private address, and the reverse. An in-VPC client reaching the endpoint's public IP hairpins through the internet gateway and arrives bearing its public source address, so a rule that allows only its private `/32` refuses it.

1. Confirm the rule is the shape you think it is: a `tcp` rule from port `1500` to port `1500` for only the source addresses you intended, with no rule on any other port and no unexpected IPv6, security-group-reference, or prefix-list entry. Any of those can admit traffic you did not intend, and an allow-all IPv6 rule in particular can render as an empty list that looks harmless.

1. Confirm the endpoint process is still running. It does not survive a reboot, and nothing relaunches it. Restart it from [Start the endpoint](bwtest-software-install.md#bwtest-endpoint-start).

1. Confirm the instance has not been isolated. If its security group is no longer the one you created, see [Security considerations for the test endpoint](network-bandwidth-test.md#bwtest-security).

## The client reports that the server is not responding
<a name="bwtest-ts-backend-down"></a>

The client prints the following message and then exits with status 0:

```
Selected server {{name}} ({{host}}) is not responding at the moment, try again later
```

A zero exit code from this client does not mean the test succeeded, so read the output rather than trusting the exit code. The client reports the same "not responding" message for several distinct failures, including a malformed server URL and a rejected certificate. Check these causes:

1. The port in the `server` URL. If `PORT` was empty when you wrote the server list, the URL contains an empty port (`https://{{host}}:/backend/`) and the client cannot connect. Confirm `PORT` is set to 1500 in the shell where you run the command-line test, then write the server list again. See [Write the server list](bwtest-cli-test.md#bwtest-cli-serverlist).

1. The `/backend/` suffix on the `server` URL. Without it, every route returns 404 and the client reports the server as not responding. See [Write the server list](bwtest-cli-test.md#bwtest-cli-serverlist).

1. The security group. Confirm it admits this source server's address on TCP port 1500. On a newly launched endpoint, the endpoint's public DNS name might resolve to its public address rather than the private one, so a rule that allows only the source server's private address refuses the connection. In one observed case, a rerun a minute later passed. Check what `ENDPOINT_HOST` resolves to with `getent hosts "$ENDPOINT_HOST"`, and retry.

1. Certificate verification. A certificate the client rejects, because of a name that is not in the SAN or a trust anchor that does not match, produces the same message and the same exit code 0. Check the certificate SAN against the exact host string in the server list, and confirm you copied the right certificate. See [Copy the certificate to the client](bwtest-cli-test.md#bwtest-cli-copycert).

## The browser page returns 404
<a name="bwtest-ts-404"></a>

The `configs.toml` file was not deleted. Return to [Delete the shipped config file](bwtest-software-install.md#bwtest-delete-config). The CLI endpoints keep working in this state, which makes it easy to misdiagnose.

## Verification fails with a name mismatch
<a name="bwtest-ts-name-mismatch"></a>

The name you connected by is not in the certificate SAN as the right kind of entry, or the instance was stopped and started and its public address changed. Re-run [Generate the TLS certificate](bwtest-software-install.md#bwtest-generate-cert) against the current addresses.