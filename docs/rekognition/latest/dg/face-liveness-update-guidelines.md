# Face Liveness update

guidelines

AWS regularly updates Face Liveness AWS SDKs (used in customer backend) and
FaceLivenessDetector components of AWS Amplify SDKs (used in client applications) to
provide new features, updated APIs, enhanced security, bug fixes, usability
improvements, and more. We recommend that you keep the SDKs up-to-date to ensure optimal
functioning of the feature. If you continue to use older versions of SDKs, requests may
be blocked for maintainability and security reasons.

Face Liveness requires that you use the FaceLivenessDetector component, included in
the AWS Amplify SDKs (React, iOS, Android).

## Versioning and

time-frames

We are versioning the following key components of the Face Liveness feature. We
follow a semantic versioning format. For example, a version format of X.Y.Z where X
represents the major version, Y represents the minor version, and Z represents the
patch version.

- Face Liveness user challenges (For example,FaceMovementAndLightChallenge
  challenge) are partof the StartFaceLivenessSession API
- FaceLivenessDetector components delivered through AWS Amplify SDKs are
  used in client applications

_Major_ versions: We reserve major version updates for critical
security, breaking API, and show-stopper usability updates. Applications and the
customer backend must be updated as soon as possible for you to continue to use Face
Liveness features. Once we release a new major version, we support the previous
major version for 120 days from the day of the new release. We may block the
requests coming from the previous major version after 120 days.

_Minor_ versions: We reserve minor version updates for
important security and usability features and improvements. We highly recommend
applying these updates. While we strive to ensure minor updates are backward
compatible for as long as possible, we may announce end-of-support for a previous
minor version 180 days after the release of a new minor version.

_Patch_ versions: We reserve patch version updates for optional
bug fixes and improvements. While we recommend that you keep your version up-to-date
for the best security and user experience, we strive to ensure patch updates are
fully backward compatible until we release a new major or minor version.

The versioning time window (120 days for major and 180 days for minor) applies to
updating the SDK in your app, uploading your app to the app store or website, and
users downloading the latest version of the app.

## Version release and

compatiblity matrix

The release of a major version for FaceLivenessDetector component or user
challenge often coincide. To help you keep a track of version dependencies, see the
resources linked in the following tables.

**SDK versions and changelogs:**

|                                                                                                                                                |                                                                                                                                                                                                  |                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| FaceLivenessDetector for web SDK                                                                                                               | FaceLivenessDetector for iOS SDK                                                                                                                                                                 | FaceLivenessDetector for Android SDK                                                                                                                               |
| [Current version](https://www.npmjs.com/package/@aws-amplify/ui-react-liveness "https://www.npmjs.com/package/@aws-amplify/ui-react-liveness") | [Changelog](https://github.com/aws-amplify/amplify-ui/blob/main/packages/react-liveness/CHANGELOG.md "https://github.com/aws-amplify/amplify-ui/blob/main/packages/react-liveness/CHANGELOG.md") | [Current version/Changelog](https://github.com/aws-amplify/amplify-ui-swift-liveness/releases "https://github.com/aws-amplify/amplify-ui-swift-liveness/releases") | [Current version/Changelog](https://github.com/aws-amplify/amplify-ui-android/releases "https://github.com/aws-amplify/amplify-ui-android/releases") |

**User challenges:**

|                               |         |              |             |
| ----------------------------- | ------- | ------------ | ----------- |
| Challenge Name                | Version | Release date | Retire date |
| FaceMovementAndLightChallenge | v1.0.0  | 4/10/2023    | N/A         |
| FaceMovementChallenge         | v1.0.0  | 4/30/2025    | N/A         |

## Communication of new

releases

AWS communicates new releases through the following channels:

- Service health update email notifications sent to the account email
  associated with the Face Liveness account ID.
- Published updates for AWS SDKs and associated notifications at the
  respective GitHub repos.
- Published updates for AWS Amplify SDKs and associated notifications at
  the respective GitHub repos.

We recommend that you subscribe to these channels to stay up-to-date.
