# Selecting which Android test host to use in Device Farm

###### Warning

The legacy Android Test Host will no longer be available on October 21, 2024. Note that the process
for deprecation is split across several dates:

- On April 22, 2024, jobs from any new account will be directed to the upgraded test host.
- On September 2, 2024, all new or modified test spec files must target the upgraded test host.
- On October 21, 2024, jobs will no longer be able to run on the legacy test host.
  Set your test spec files to the `amazon_linux_2` host to prevent compatibility
  issues.

Please note that the Legacy Android Test Host only supports Android versions 14 and lower. Use the
amazon_linux_2 host for Android versions 15 and higher.

AWS Device Farm uses Amazon Elastic Compute Cloud (EC2) host machines running Amazon Linux 2 to execute Android tests. For Android
tests, Device Farm requires the following field in your test spec file to choose the Amazon Linux 2 test
host:

```
android_test_host: amazon_linux_2 | legacy
```

Use `amazon_linux_2` to run your tests on the Amazon Linux 2 test host:

```
android_test_host: amazon_linux_2
```

Learn more about the benefits of Amazon Linux 2 [here](amazon-linux-2.md "amazon-linux-2.md").

Device Farm recommends using the Amazon Linux 2 host for Android tests instead of the legacy host environment.
If you'd prefer to use the legacy environment, then use `legacy` to run your tests on the legacy
test host:

```
android_test_host: legacy
```

By default, test spec files without a test host selection will run on the legacy test host.

## Deprecated syntax

Below is the deprecated syntax for choosing Amazon Linux 2 in your test spec file:

```
preview_features:
  android_amazon_linux_2_host: true
```

If you're using this flag, your tests will continue to run on Amazon Linux 2. However, we **strongly recommend** removing the `preview_features` flags section
and replacing it with the new `android_test_host` field in order to avoid maintenance
overhead in the future.

###### Warning

Using both the `android_test_host` and `android_amazon_linux_2_host` flags
in your test spec file will return an error. Only one should be used; we recommend
`android_test_host`.
