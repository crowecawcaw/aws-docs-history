# Isolation on physical hosts

Different WorkSpaces on the same physical host are isolated from each other through the
hypervisor. It is as though they are on separate physical hosts. When a WorkSpace is deleted,
the memory allocated to it is scrubbed (set to zero) by the hypervisor before it is allocated
to a new WorkSpace.
