# Install AWS ParallelCluster as a standalone application

Install AWS ParallelCluster as a standalone application on your environment. Follow the instructions for
installing AWS ParallelCluster on an available OS in the following section.

###### Prerequisites

- An environment with an operating system compatible with an available version of the installer.

###### Note

AWS ParallelCluster requires NodeJS. AWS ParallelCluster Installer includes a bundled version of NodeJS (v18), which is installed
if it does not already exist. If your system is not compatible with NodeJS v18, you should install NodeJS before
installing AWS ParallelCluster.

Linux x86 (64-bit)

###### Install AWS ParallelCluster on your environment.

1. Download the latest [pcluster installer](https://us-east-1-aws-parallelcluster.s3.amazonaws.com/parallelcluster/3.14.0/installer/pcluster-installer-bundle-3.14.0.1209-node-v20.18.3-Linux_x86_64-signed.zip "https://us-east-1-aws-parallelcluster.s3.amazonaws.com/parallelcluster/3.14.0/installer/pcluster-installer-bundle-3.14.0.1209-node-v20.18.3-Linux_x86_64-signed.zip") ([checksum](https://us-east-1-aws-parallelcluster.s3.amazonaws.com/parallelcluster/3.14.0/installer/pcluster-installer-bundle-3.14.0.1209-node-v20.18.3-Linux_x86_64-signed.zip-sha256sum "https://us-east-1-aws-parallelcluster.s3.amazonaws.com/parallelcluster/3.14.0/installer/pcluster-installer-bundle-3.14.0.1209-node-v20.18.3-Linux_x86_64-signed.zip-sha256sum")).
2. Unzip the installer bundle and install AWS ParallelCluster by using the following commands:

```
`$` `unzip pcluster-installer-bundle-`<VERSION>`-Linux_x86_64-signed.zip -d pcluster-installer-bundle`
`$` `cd pcluster-installer-bundle`
`$` `chmod +x install_pcluster.sh`
```

3. Run the following install script.

```
`$` `bash install_pcluster.sh`
```

4. Verify that AWS ParallelCluster is installed correctly.

```
`$` `pcluster version``{
 "version": "3.14.0"
}`
```

###### Troubleshooting `pcluster` installation errors

- If the AWS ParallelCluster version isn't returned in step 4, restart the terminal or `source` the `bash_profile` to update the
  `PATH` variable to include the new binary directory as shown in the following example:

```
`$` `source ~/.bash_profile`
```

- If you use your `pcluster` installation to create clusters with `CustomActions` specified as HTTPS resources, rather than S3 URIs, you might
  see a `WARNING` message indicating that these resources might not be verified ([`SSL: CERTIFICATE_VERIFY_FAILED`]).
  This is caused by a known issue and you can ignore this warning if you trust the authenticity of the specified resources.

###### Previous installer bundle versions

- None
