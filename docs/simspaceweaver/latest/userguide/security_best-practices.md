End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Security best practices for SimSpace Weaver

This section describes security best practices that are specific to SimSpace Weaver.
To learn more about security best practices in AWS, see [Best Practices for Security, Identity, and Compliance](https://aws.amazon.com/architecture/security-identity-compliance "https://aws.amazon.com/architecture/security-identity-compliance").

###### Topics

- [Encrypt communications between your apps and their clients](#security_best-practice_encrypt-client-communications "#security_best-practice_encrypt-client-communications")
- [Periodically backup your simulation state](#security_best-practice_backup-simulation-state "#security_best-practice_backup-simulation-state")
- [Maintain your apps and SDKs](#security_best-practice_maintain-apps-and-sdks "#security_best-practice_maintain-apps-and-sdks")

##

Encrypt communications between your apps and their clients

SimSpace Weaver doesn't manage communications between your apps and their clients.
You should implement some form of authentication and encryption for client sessions.

##

Periodically backup your simulation state

SimSpace Weaver doesn't save your simulation state. Simulations that are stopped (as
a result of an API call, console option, or system crash) do not save their state and have
no inherent way to recover them. Stopped simulations cannot be restarted. The only way to
perform the equivalent of a restart is to recreate your simulation using the same configuration
and data. You can use backups of your simulation state to initialize the new simulation.
AWS offers highly reliable and available cloud
[storage](https://aws.amazon.com/products/storage "https://aws.amazon.com/products/storage") and
[database](https://aws.amazon.com/products/databases/ "https://aws.amazon.com/products/databases/") services that you can use to
save your simulation state.

##

Maintain your apps and SDKs

Maintain your apps, local installations of the AWS software development kits (SDKs), and
the SimSpace Weaver app SDK. You can download and install new versions of the AWS SDKs. Test new
versions of the SimSpace Weaver app SDK with non-production app builds to ensure that your apps continue
to run as expected. You cannot update your apps in a running simulation. To update your apps:

1. Update and test the app code locally (or in a test environment).
2. Stop changing your simulation state and save it (if necessary).
3. Stop your simulation (once stopped, it cannot be restarted).
4. Delete your simulation (stopped simulations that aren't deleted count towards your service limits).
5. Recreate your simulation with the same configuration and the updated app code.
6. Initialize your simulation using saved state data (if available).
7. Start your new simulation.

###### Note

A new simulation created with the same configuration is separate from the old simulation.
It will have a new simulation ID and send logs to a new log stream in Amazon CloudWatch.
