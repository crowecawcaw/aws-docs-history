# Platform configuration examples

Use these platform-specific examples to configure client devices with your Route 53 Global Resolver access
tokens and connection details.

## Windows configuration

Follow these steps to configure Windows clients to use DoH with access tokens using the netsh command.

1. Open Command Prompt as an administrator.
2. Enable the global DoH setting:

```
netsh dns add global doh=yes
```

3. Register DoH servers with access tokens. Replace the example values with your actual
   resolver details:

```
netsh dns add encryption server=3.3.3.3 dohtemplate=https://a1bc234567890a.route53globalresolver.global.on.aws/dns-query?token=<your-token> autoupgrade=yes
netsh dns add encryption server=3.3.3.4 dohtemplate=https://a1bc234567890a.route53globalresolver.global.on.aws/dns-query?token=<your-token> autoupgrade=yes
```

4. Flush the DNS cache:

```
ipconfig /flushdns
```

5. Verify the configuration:

```
netsh dns show global
```

## macOS configuration

Follow these steps to configure macOS clients using a mobile configuration profile for DoH with access
tokens.

Create a mobile configuration profile with the following structure:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>PayloadContent</key>
  <array>
    <dict>
      <key>DNSSettings</key>
      <dict>
        <key>DNSProtocol</key>
        <string>HTTPS</string>
        <key>ServerAddresses</key>
        <array>
          <string>3.3.3.3</string>
          <string>3.3.3.4</string>
        </array>
        <key>ServerURL</key>
        <string>https://a1bc234567890a.route53globalresolver.global.on.aws/dns-query?token=<your-token></string>
      </dict>
      <key>PayloadType</key>
      <string>com.apple.dnsSettings.managed</string>
    </dict>
  </array>
</dict>
</plist>
```

Install the profile through System Settings > Device Management.
