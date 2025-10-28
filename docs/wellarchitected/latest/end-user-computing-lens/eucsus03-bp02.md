# EUCSUS03-BP02 Adapt the AutoStop timeout and idle disconnect timeout for Amazon DCV

The AutoStop timeout in WorkSpaces is only available with AutoStop. This is not applicable
to AlwaysOn WorkSpaces. In WorkSpaces, you can configure how long a user can be inactive while
connected to a WorkSpace before they are disconnected. Amazon DCV (Desktop Cloud Virtualization)
is the remote display protocol used by Amazon WorkSpaces to stream pixels, keystrokes and mouse
movements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

By default, AutoStop time (in
hours**)** is set to one hour,
which means that the WorkSpace stops automatically an hour
after the WorkSpace is disconnected.  Keep the AutoStop time
at the default value, as this is the lowest value offered.
