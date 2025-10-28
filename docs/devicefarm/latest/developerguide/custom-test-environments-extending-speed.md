# Speeding up Appium-based tests in Device Farm through desired

capabilities

When using Appium, you might find that the standard mode test suite is very slow. This is because Device Farm
applies the default settings and doesn't make any assumptions about how you want to use the Appium environment.
While these defaults are built around industry best practices, they might not apply to your situation. To
fine-tune the parameters of the Appium server, you can adjust the default Appium capabilities in your test spec.
For example, the following sets the `usePrebuildWDA` capability to `true` in an iOS
test suite to speed up initial start time:

```

phases:
  pre_test:
    - # ... Start up Appium
    - >-
    appium --log-timestamp
    --default-capabilities "{\"usePrebuiltWDA\": true, \"derivedDataPath\":\"$DEVICEFARM_WDA_DERIVED_DATA_PATH\",
    \"deviceName\": \"$DEVICEFARM_DEVICE_NAME\", \"platformName\":\"$DEVICEFARM_DEVICE_PLATFORM_NAME\", \"app\":\"$DEVICEFARM_APP_PATH\",
    \"automationName\":\"XCUITest\", \"udid\":\"$DEVICEFARM_DEVICE_UDID_FOR_APPIUM\", \"platformVersion\":\"$DEVICEFARM_DEVICE_OS_VERSION\"}"
    >> $DEVICEFARM_LOG_DIR/appiumlog.txt 2>&1 &


```

Appium capabilities must be a shell-escaped, quoted JSON structure.

The following Appium capabilities are common sources of performance improvements:

`noReset` and `fullReset`

These two capabilities, which are mutually exclusive, describe the behavior of Appium after each session
is complete. When `noReset` is set to `true`, the Appium server doesn't remove
data from your application when an Appium session ends, effectively doing no cleanup whatsoever.
`fullReset` uninstalls and clears all application data from the device after the session
has closed. For more information, see [Reset Strategies](http://appium.io/docs/en/writing-running-appium/other/reset-strategies/ "http://appium.io/docs/en/writing-running-appium/other/reset-strategies/") in
the Appium documentation.

`ignoreUnimportantViews` (Android only)

Instructs Appium to compress the Android UI hierarchy only to _relevant_ views for the test, speeding up certain element lookups. However, this can break some
XPath-based test suites because the hierarchy of the UI layout has been changed.

`skipUnlock` (Android only)

Informs Appium that there is no PIN code currently set, which speeds up tests after a screen off event
or other lock event.

`webDriverAgentUrl` (iOS only)

Instructs Appium to assume that an essential iOS dependency, `webDriverAgent`, is
already running and available to accept HTTP requests at the specified URL. If
`webDriverAgent` isn't already up and running, it can take Appium some time at the
beginning of a test suite to start the `webDriverAgent`. If you start
`webDriverAgent` yourself and set `webDriverAgentUrl` to
`http://localhost:8100` when starting Appium, you can boot up your test suite faster. Note that
this capability should never be used alongside the `useNewWDA` capability.

You can use the following code to start `webDriverAgent` from your test spec file on
the device's local port `8100`, then forward it to the test host's local port `8100`
(this allows you to set `webDriverAgentUrl`'s value to `http://localhost:8100`).
This code should be run during the install phase after any code for setting up the Appium and
`webDriverAgent` environment variables has been defined:

```
      # Start WebDriverAgent and iProxy
      - >-
        xcodebuild test-without-building -project /usr/local/avm/versions/$APPIUM_VERSION/node_modules/appium/node_modules/appium-webdriveragent/WebDriverAgent.xcodeproj
        -scheme WebDriverAgentRunner -derivedDataPath $DEVICEFARM_WDA_DERIVED_DATA_PATH
        -destination id=$DEVICEFARM_DEVICE_UDID_FOR_APPIUM IPHONEOS_DEPLOYMENT_TARGET=$DEVICEFARM_DEVICE_OS_VERSION
        GCC_TREAT_WARNINGS_AS_ERRORS=0 COMPILER_INDEX_STORE_ENABLE=NO >> $DEVICEFARM_LOG_DIR/webdriveragent_log.txt 2>&1 &

        iproxy 8100 8100 >> $DEVICEFARM_LOG_DIR/iproxy_log.txt 2>&1 &
```

Then, you can add the following code to your test spec file to ensure that
`webDriverAgent` started successfully. This code should be run at the end of the pre-test
phase after ensuring that Appium started successfully:

```
      # Wait for WebDriverAgent to start
      - >-
        start_wda_timeout=0;
        while [ true ];
        do
          if [ $start_wda_timeout -gt 60 ];
          then
              echo "WebDriverAgent server never started in 60 seconds.";
              exit 1;
          fi;
          grep -i "ServerURLHere" $DEVICEFARM_LOG_DIR/webdriveragent_log.txt >> /dev/null 2>&1;
          if [ $? -eq 0 ];
          then
              echo "WebDriverAgent REST http interface listener started";
              break;
          else
              echo "Waiting for WebDriverAgent server to start. Sleeping for 1 seconds";
              sleep 1;
              start_wda_timeout=$((start_wda_timeout+1));
          fi;
        done;
```

For more information on the capabilities that Appium supports, see [Appium Desired Capabilities](http://appium.io/docs/en/writing-running-appium/caps/ "http://appium.io/docs/en/writing-running-appium/caps/") in the Appium
documentation.

For more ways to extend your test suite and optimize your tests, see [Extending custom test environments in Device Farm](custom-test-environments-extending.md "custom-test-environments-extending.md").
