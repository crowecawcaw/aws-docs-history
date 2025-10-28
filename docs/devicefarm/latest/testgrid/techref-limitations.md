# Limitations of Device Farm desktop browser testing

Keep these limitations in mind when you use the desktop browser testing feature:

- The feature is only available in the `us-west-2` (Oregon) region.
- Not all Selenium interfaces are supported. The `pytest-selenium` package, for example,
  does not allow a command execution URL to be specified.
- Each session you create is isolated from other sessions. Testing that involves multi-window or
  multi-session interaction is not supported.
