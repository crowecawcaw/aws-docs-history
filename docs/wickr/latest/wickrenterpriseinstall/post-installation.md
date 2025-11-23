This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Post installation

There are two web consoles available for managing your Wickr Enterprise installation:
the KOTS Admin Console and the Wickr Admin Console.

###### Note

Make any changes needed to reflect your organization's backup and logging policies (Amazon S3 settings, ELB access logs, Amazon Virtual Private Cloud flow logs).

## KOTS Admin Console

This interface is used for managing the deployed version of Wickr Enterprise. You
can see the status of the installation, modify configurations, or perform upgrades. The
KOTS Admin Console is accessible only through a Kubernetes port forward, which can be
opened using the following command:

```
kubectl kots --**namespace** wickr admin-**console**
```

###### Note

You must first set up your bastion connection as described in the port forward to
the bastion section. For more information on port forward to the bastion, see [Proxying connections through the bastion](connecting.md#connecting-proxying-connections-through-the-bastion "connecting.md#connecting-proxying-connections-through-the-bastion").

When the port forward is successfully configured, the previous command will output the
following:

```
  • Press Ctrl+C to exit
  • Go to http://localhost:8800 to access the Admin Console
```

Use the provided URL to access the KOTS Admin Console. The password to log in is the
one you chose when running `kubectl kots install` during the installation. If
you need to reset your password, see [Resetting the KOTS Admin Console Password](troubleshooting.md#troubleshooting-resetting-the-kots-admin-console-password "troubleshooting.md#troubleshooting-resetting-the-kots-admin-console-password").

## Wickr Admin Console

This interface is used for configuring your Wickr Enterprise installation to set up
networks, users, and federation. It's accessible over HTTPS at the DNS name that you
configured to point to your Load Balancer. If DNS was configured automatically with a
public hosted zone, the domain name is the value of the `wickr/domainName`
context value.

The default username is `admin`, with the password
`Password123`. You will be required to change this password on first log
in.
