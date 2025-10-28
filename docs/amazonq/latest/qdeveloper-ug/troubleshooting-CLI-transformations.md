# Troubleshooting transformations on the command line

The following information can help you troubleshoot common issues when transforming applications on the command line with Amazon Q Developer.

## Why is my bearer token not refreshing?

If you see the following error, it means you need to refresh the bearer token used for authentication.

```
Refreshing bearer token
('Error refreshing bearer token due to: ', InvalidGrantException('An error occurred (InvalidGrantException) when calling the CreateToken operation: '))
('Error getting bearer token due to: ', RuntimeError(('Error refreshing bearer token due to: ', InvalidGrantException('An error occurred (InvalidGrantException) when calling the CreateToken operation: '))))
```

To address this error, run the following command:

```
rm ~/.aws/qcodetransform/credentials.json
```

Once you remove the outdated credentials file, run `qct transform` again to restart the transformation.

## Why isn't the most recent version of the command line tool being used?

When you download a new version of the command line tool for transformations,
sometimes a previous version of the tool still gets used.

To make you're using the most recent version of the tool, download the
[most recent version](transform-CLI-versions.md "transform-CLI-versions.md"). Then run the following command with
the path to where you unzipped the tool, based on your machine
architecture:

Linux_aarch64

```
pip install <path/to/unzipped-tool>/Linux_aarch64/amzn_qct_cli-1.2.1-py3-none-any.whl --force-reinstall
```

Linux_x86_64

```
pip install <path/to/unzipped-tool>/Linux_x86_64/amzn_qct_cli-1.2.1-py3-none-any.whl --force-reinstall
```

###### Note

If you're using an older version of the command line tool for transformations,
replace `1.2.1` with the [version](transform-CLI-versions.md "transform-CLI-versions.md") you downloaded.
