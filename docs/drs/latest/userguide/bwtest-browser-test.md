

# Test with the browser
<a name="bwtest-browser-test"></a>

This test is an alternative to the command-line test in [Test with the command line](bwtest-cli-test.md). The endpoint serves its own single-page test UI at `/`. Use the browser instead of the command-line client when you want a quick interactive result from a source server that has a desktop, or when you want a person to watch the test run.

**Note**  
The browser is a convenience surface. It does not let you set the number of concurrent streams, which is why the command-line client in [Test with the command line](bwtest-cli-test.md) produces the figure you should quote. Against a fast private path, the browser can understate the CLI figure substantially. Do not report a browser number as your link speed. It is, however, a useful second instrument; see [Optionally compare the browser and the CLI to find the bottleneck](bwtest-interpreting.md#bwtest-browser-vs-cli).

## Open the page from the source server
<a name="bwtest-browser-open"></a>

```
https://{{PRIV_DNS}}:1500/         # source server in the same VPC
https://{{PUB_DNS}}:1500/          # source server on the public internet
```

Use whichever name or address you put in the certificate SAN in [Generate the TLS certificate](bwtest-software-install.md#bwtest-generate-cert). Pick the name that matches the path you want to measure, not only the certificate. From inside the VPC, a public DNS name resolves to the instance's private IP, so an in-VPC client that uses {{PUB\_DNS}} stays on the private path. An in-VPC client that must cross the internet gateway has to use the public IP literal. A source server over VPN or Direct Connect has to use `https://{{PRIV_IP}}:1500/`, because on-premises DNS usually cannot resolve the private DNS name.

## Accept the certificate warning
<a name="bwtest-browser-cert-warning"></a>

The certificate is self-signed, so every browser shows an interstitial warning. Chrome reports NET::ERR\_CERT\_AUTHORITY\_INVALID under "Your connection is not private", and Firefox reports "Warning: Potential Security Risk Ahead". Choose the advanced or details option and proceed (in Chrome, **Advanced**, **Proceed**; in Firefox, **Advanced**, **Accept the Risk and Continue**; in Safari, **Show Details**, **visit this website**).

**Important**  
Accepting this warning is a deliberate bypass of certificate validation. It is acceptable here because the endpoint is a throwaway instance you launched minutes ago and the test carries no sensitive data. Confirm that the hostname in the warning is your own instance before you proceed. You should not see a name-mismatch complaint; if you do, the SAN in [Generate the TLS certificate](bwtest-software-install.md#bwtest-generate-cert) does not cover the name you connected by.

## Run the test
<a name="bwtest-browser-run"></a>

Choose the start button on the page and let it run to completion. It reports download, upload, ping, and jitter, and it shows the address it saw your request arrive from, which is a useful confirmation that the traffic really came from where you think. The run takes about 18 seconds, fixed by the page's own configuration and not operator-settable.