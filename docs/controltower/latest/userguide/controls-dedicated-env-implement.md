# Implementation Process

If you proceed without AWS Config, your environment will be immediately ready for preventive and proactive controls
within the Control Catalog.

However, when you're ready to enable your first detective control, you'll need to enable AWS Config recording through
the new `ConfigBaseline` being enabled on the target OUs. This is a one-time setup process per OU
and incurs AWS Config pricing based on the number of accounts per OU and resources per account, per AWS Region.
