# Internal-only change types

You can see change types that are for internal use only. This is so you know what actions AMS can, or does, take.
If there is an internal-only change type
that you would like to have available for your use, submit a service request.

For example, there is a Management | Monitoring and notification | CloudWatch alarm suppression | Update CT that is
internal-only. AMS uses it to deploy infrastructure updates (such as patching) to turn off alarm notifications
that the updates might erroneously trigger.
When this CT is submitted, you will notice the RFC for the CT in your RFC list. Any internal-only CT that is
deployed in an RFC appears in your RFC list.
