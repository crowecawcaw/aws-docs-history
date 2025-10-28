This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Installing Wickr Enterprise

After your connection to the Kubernetes cluster has been made, you can begin installing
Wickr Enterprise using the `kubectl kots` plugin. You will need your KOTS
License file (a `.yaml` file provided by Wickr) and your Config Values file,
which were saved to the file `wickr-config.json` in the Generate KOTS Config
section. For more information about Generate KOTS Config, see [Generate KOTS Config](getting-started.md#getting-started-generate-kots-config "getting-started.md#getting-started-generate-kots-config").

## Installing

Wickr Enterprise manually

The following command will begin the installation of Wickr Enterprise:

```
kubectl kots install wickr-enterprise-ha \
    --license-file `./license.yaml` \
    --config-values `./wickr-config.json`  \
    --namespace wickr \
    --skip-preflights
```

You will be prompted to enter a password for the KOTS Admin Console. Save this password
because you will need it to upgrade or change the configuration of your Wickr Enterprise
installation in the future.

When the installation is complete, `kubectl kots` will open up a local port
(usually `http://localhost:8080`), which provides access to the KOTS Admin
Console. You can change or monitor the status of your Wickr Enterprise installation on
this site, or begin setting up Wickr by visiting the domain name that you configured for
your installation in your browser.

## Installing

Wickr Enterprise with Lambda

During the CDK deployment, a Lambda is created and invoked to complete the
Wickr Enterprise installation on your behalf automatically. To invoke it manually,
open the AWS console and find `WickrLambda-func*` lambda function, under
test tab, select `test`, the input is irrelevant.
