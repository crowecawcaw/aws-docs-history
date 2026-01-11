This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Limitations

The following features are not supported through AWS PrivateLink and require internet
connectivity:

- Wickr Open Access (WOA)
- Client Application Updates
  - Mobile Apps (iOS/Android)
    - **Source**: App Store/Google Play Store
    - **Requirement**: Internet access required

  - Desktop Applications
    - **Windows/Mac**: Uses global S3 endpoints (not
      AWS PrivateLink compatible)
    - **Linux**: Uses Snap Store (requires internet
      access)

- Debugging and Telemetry
  - Crash reports
  - Debug metrics
  - Client-side analytics links

- Mobile Push Notifications

These services require internet connectivity and cannot use
AWS PrivateLink:

    + Apple Push Notifications




    	- **Requirement**: Direct internet
    	 access
    	- **Ports**: 443, 2195, 2196, 5223
    	- **Reference**: [Apple Support
    	 Documentation](https://support.apple.com/en-us/102266 "https://support.apple.com/en-us/102266")
    + Google/Android Notifications




    	- **Requirement**: Firebase Cloud Messaging
    	 access
    	- **Reference**: [Firebase Documentation](https://firebase.google.com/docs/cloud-messaging/network-configuration "https://firebase.google.com/docs/cloud-messaging/network-configuration")

- AWS Wickr Console is not currently supported for Private Access. For
  more information, see [Supported AWS Regions, service consoles, and features for Private
  Access](../../../awsconsolehelpdocs/latest/gsg/supported-regions-consoles.md "../../../awsconsolehelpdocs/latest/gsg/supported-regions-consoles.md").

## Minimum required client

versions for AWS PrivateLink

The following client versions have been validated with AWS PrivateLink:

- iOS 6.64 (where applicable)
- Android 6.60 (where applicable)
- Desktop clients 6.60
- Bots 6.60

## Features requiring additional

configuration

**Wickr Bots**

- **Requirement**: Customer-managed infrastructure
- **Action**: Configure network paths for bot
  dependencies
- **Consideration**: Ensure bots can reach required AWS
  services through VPC endpoints

**File Downloads**

- **S3 Connectivity**: Required for file operations (except
  Frankfurt region)
- **Solution**: Create S3 VPC gateway endpoint
- **Reference**: [AWS PrivateLink for Amazon S3](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md")
