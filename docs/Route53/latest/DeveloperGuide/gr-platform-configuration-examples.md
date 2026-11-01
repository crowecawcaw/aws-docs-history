

# Platform configuration examples
<a name="gr-platform-configuration-examples"></a>

Use these platform-specific examples to configure client devices with your Route 53 Global Resolver access tokens and connection details.

## Windows configuration
<a name="gr-windows-configuration"></a>

Follow these steps to configure Windows clients to use DoH with access tokens using the netsh command.

1. Open Command Prompt as an administrator.

1. Enable the global DoH setting:

   ```
   netsh dns add global doh=yes
   ```

1. Register DoH servers with access tokens. Replace the example values with your actual resolver details:

   ```
   netsh dns add encryption server=3.3.3.3 dohtemplate=https://a1bc234567890a.route53globalresolver.global.on.aws/dns-query?token=<your-token> autoupgrade=yes
   netsh dns add encryption server=3.3.3.4 dohtemplate=https://a1bc234567890a.route53globalresolver.global.on.aws/dns-query?token=<your-token> autoupgrade=yes
   ```

1. Flush the DNS cache:

   ```
   ipconfig /flushdns
   ```

1. Verify the configuration:

   ```
   netsh dns show global
   ```

## macOS configuration
<a name="gr-macOS-configuration"></a>

Follow these steps to configure macOS clients using a mobile configuration profile for DoH with access tokens.

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
          <string>{{3.3.3.3}}</string>
          <string>{{3.3.3.4}}</string>
        </array>
        <key>ServerURL</key>
        <string>https://{{a1bc234567890a.route53globalresolver.global.on.aws}}/dns-query/token/{{your-token}}</string>
      </dict>
      <key>PayloadType</key>
      <string>com.apple.dnsSettings.managed</string>
      <key>PayloadDisplayName</key>
      <string>Global Resolver DoH</string>
      <key>PayloadIdentifier</key>
      <string>{{com.example.dnssettings}}</string>
      <key>PayloadUUID</key>
      <string>{{uuid-1}}</string>
      <key>PayloadVersion</key>
      <integer>1</integer>
    </dict>
  </array>
  <key>PayloadType</key>
  <string>Configuration</string>
  <key>PayloadIdentifier</key>
  <string>{{com.example.dnssettings.profile}}</string>
  <key>PayloadUUID</key>
  <string>{{uuid-2}}</string>
  <key>PayloadVersion</key>
  <integer>1</integer>
  <key>PayloadDisplayName</key>
  <string>Global Resolver DoH</string>
</dict>
</plist>
```

**Note**  
On macOS, pass the token as a path segment (`/dns-query/token/<your-token>`), not a query parameter. macOS strips query parameters from the DoH server URL, so the token never reaches Global Resolver.

Replace the example values:
+ {{a1bc234567890a.route53globalresolver.global.on.aws}}: your Global Resolver's DNS name.
+ {{3.3.3.3}} and {{3.3.3.4}}: your Global Resolver's IPv4 addresses. For dual-stack resolvers, you can also list its IPv6 addresses.
+ {{your-token}}: your access token value, as returned by `GetAccessToken`. Don't use the token ID.
+ {{com.example.dnssettings}} and {{com.example.dnssettings.profile}}: reverse-DNS identifiers for the DNS payload and the profile. {{uuid-1}} and {{uuid-2}}: unique UUIDs for each (for example, generate them with `uuidgen`).

Install the profile manually on the device, or deploy it through your mobile device management (MDM) solution.