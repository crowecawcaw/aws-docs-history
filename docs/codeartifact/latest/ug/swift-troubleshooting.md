# Swift troubleshooting

The following information might help you troubleshoot common issues with Swift and CodeArtifact.

## I'm getting a 401 error in Xcode even after configuring the Swift Package Manager

**Problem:** When you are trying to add a package from your CodeArtifact repository as a dependency
to your Swift project in Xcode, you are getting a 401 unauthorized error even after you have followed the instructions for
[connecting Swift to CodeArtifact](configure-swift.md "configure-swift.md").

**Possible fixes:** This can be caused by an issue with the macOS Keychain application, where
your CodeArtifact credentials are stored. To fix this, we recommend opening the Keychain application and deleting all of
the CodeArtifact entries and configuring the Swift Package Manager with your CodeArtifact repository again by following the instructions in
[Configure the Swift Package Manager with CodeArtifact](configure-swift.md "configure-swift.md").

## Xcode hangs on CI machine due to keychain prompt for password

**Problem:** When you are trying to pull Swift packages from CodeArtifact as part of an Xcode
build on a continuous integration (CI) server, such as with GitHub Actions, authentication with CodeArtifact can hang and eventually fail with an error
message similar to the following:

`Failed to save credentials for \'https://`my_domain`-`111122223333`.d.codeartifact.`us-west-2`.amazonaws.com\' to keychain: status -60008`

**Possible fixes:** This is caused by credentials not being saved to the keychain on CI machines, and Xcode
only supporting credentials saved in Keychain. To fix this, we recommend creating the keychain entry manually using the following steps:

1. Prepare the keychain.

```
KEYCHAIN_PASSWORD=$(openssl rand -base64 20)
KEYCHAIN_NAME=login.keychain
SYSTEM_KEYCHAIN=/Library/Keychains/System.keychain

if [ -f $HOME/Library/Keychains/"${KEYCHAIN_NAME}"-db ]; then
    echo "Deleting old ${KEYCHAIN_NAME} keychain"
    security delete-keychain "${KEYCHAIN_NAME}"
fi
echo "Create Keychain"
security create-keychain -p "${KEYCHAIN_PASSWORD}" "${KEYCHAIN_NAME}"

EXISTING_KEYCHAINS=( $( security list-keychains | sed -e 's/ *//' | tr '\n' ' ' | tr -d '"') )
sudo security list-keychains -s "${KEYCHAIN_NAME}" "${EXISTING_KEYCHAINS[@]}"

echo "New keychain search list :"
security list-keychain

echo "Configure keychain : remove lock timeout"
security unlock-keychain -p "${KEYCHAIN_PASSWORD}" "${KEYCHAIN_NAME}"
security set-keychain-settings "${KEYCHAIN_NAME}"
```

2. Get a CodeArtifact authentication token and your repository endpoint.

```

export CODEARTIFACT_AUTH_TOKEN=`aws codeartifact get-authorization-token \
                                    --region `us-west-2` \
                                    --domain `my_domain`   \
                                    --domain-owner `111122223333`   \
                                    --query authorizationToken  \
                                    --output text`

export CODEARTIFACT_REPO=`aws codeartifact get-repository-endpoint  \
                              --region `us-west-2`   \
                              --domain `my_domain`   \
                              --domain-owner `111122223333`   \
                              --format swift     \
                              --repository `my_repo`    \
                              --query repositoryEndpoint   \
                              --output text`
```

3. Manually create the Keychain entry.

```
SERVER=$(echo $CODEARTIFACT_REPO | sed  's/https:\/\///g' | sed 's/.com.*$/.com/g')
AUTHORIZATION=(-T /usr/bin/security -T /usr/bin/codesign -T /usr/bin/xcodebuild -T /usr/bin/swift \
               -T /Applications/Xcode-15.2.app/Contents/Developer/usr/bin/xcodebuild)

security delete-internet-password -a token -s $SERVER -r htps "${KEYCHAIN_NAME}"

security add-internet-password -a token \
                               -s $SERVER \
                               -w $CODEARTIFACT_AUTH_TOKEN \
                               -r htps \
                               -U \
                               "${AUTHORIZATION[@]}" \
                               "${KEYCHAIN_NAME}"

security set-internet-password-partition-list \
             -a token \
             -s $SERVER \
             -S "com.apple.swift-package,com.apple.security,com.apple.dt.Xcode,apple-tool:,apple:,codesign" \
             -k "${KEYCHAIN_PASSWORD}" "${KEYCHAIN_NAME}"

security find-internet-password   "${KEYCHAIN_NAME}"
```

For more information about this error and the solution, see [https://github.com/apple/swift-package-manager/issues/7236](https://github.com/apple/swift-package-manager/issues/7236 "https://github.com/apple/swift-package-manager/issues/7236").
