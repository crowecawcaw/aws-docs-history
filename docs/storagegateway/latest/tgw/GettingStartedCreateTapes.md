# Creating new virtual tapes for

Tape Gateway

This section describes how to create new virtual tapes using AWS Storage Gateway. You can create
new virtual tapes manually using either the AWS Storage Gateway console or the Storage Gateway API. You can
also configure your Tape Gateway to create them automatically, which helps decrease the
need for manual tape management, makes your large deployments simpler, and helps scale
on-premises and archive storage needs.

Tape Gateway supports _write once, read many_ (WORM) and
_tape retention lock_ on virtual tapes. WORM-activated
virtual tapes help ensure that the data on active tapes in your virtual tape library cannot
be overwritten or erased. For more information about WORM protection for virtual tapes, see
the section following, [Write Once, Read Many (WORM) Tape Protection](#WORM "#WORM").

With tape retention lock, you can specify the retention mode and period on archived
virtual tapes, preventing them from being deleted for a fixed amount of time up to 100
years. It includes permission controls on who can delete tapes or modify the retention
settings. For more information about tape retention lock, see [Using Tape Retention Lock](CreatingCustomTapePool.md#TapeRetentionLock "CreatingCustomTapePool.md#TapeRetentionLock").

###### Note

You are charged only for the amount of data that you write to the tape, not the tape
capacity.

You can use AWS Key Management Service (AWS KMS) to encrypt data written to a virtual tape that is stored
in Amazon Simple Storage Service (Amazon S3). Currently, you can do this by using the AWS Storage Gateway API or AWS Command Line Interface
(AWS CLI). For more information, see [CreateTapes](../APIReference/API_CreateTapes.md "../APIReference/API_CreateTapes.md") or [create-tapes](../../../cli/latest/reference/storagegateway/create-tapes.md "../../../cli/latest/reference/storagegateway/create-tapes.md").

## Write Once, Read Many (WORM) Tape Protection

You can prevent virtual tapes from being overwritten or erased by activating WORM
protection for virtual tapes in AWS Storage Gateway. WORM protection for virtual tapes is
activated when creating tapes.

Data that is written to WORM virtual tapes can't be overwritten. Only new data can be
appended to WORM virtual tapes, and existing data can't be erased. Activating WORM
protection for virtual tapes helps protect those tapes while they are in active use,
before they are ejected and archived.

WORM configuration can only be set when tapes are created, and that configuration
cannot be changed after the tapes are created.

**Next Step**

[Using Your
Tape Gateway](GettingStarted-create-tape-gateway.md "GettingStarted-create-tape-gateway.md")
