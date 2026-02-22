# Steps to take after installation

This section assumes that you've installed AWS ParallelCluster. You will learn how to verify
that AWS ParallelCluster installed correctly, how to update to the latest version of
AWS ParallelCluster, and how to uninstall.

You can verify that AWS ParallelCluster was installed correctly by running [pcluster version](pcluster.md "pcluster.md").

```
`$` `pcluster version`
`{
"version": "3.14.2"
}`
```

AWS ParallelCluster is updated regularly. To update to the latest version of AWS ParallelCluster, run the installation command again. For more
information about the latest version of AWS ParallelCluster, see the
[AWS ParallelCluster release notes](https://github.com/aws/aws-parallelcluster/blob/v3.1.1/CHANGELOG.md "https://github.com/aws/aws-parallelcluster/blob/v3.1.1/CHANGELOG.md").

```
`$` `pip3 install aws-parallelcluster --upgrade --user`
```

To uninstall AWS ParallelCluster, use `pip3 uninstall`.

```
`$` `pip3 uninstall aws-parallelcluster`
```

If you don't have Python and `pip3`, use the procedure for your environment.
