# Detach and delete an EFA from an Amazon EC2 instance

You can detach an EFA from an Amazon EC2 instance and delete it in the same way as any
other elastic network interface in Amazon EC2.

## Detach an EFA

To detach an EFA from an instance, you must first stop the instance. You cannot
detach an EFA from an instance that is in the running state.

You detach an EFA from an instance in the same way that you detach an elastic network
interface from an instance. For more information, see [Detach a network interface](network-interface-attachments.md#detach_eni "network-interface-attachments.md#detach_eni").

## Delete an EFA

To delete an EFA, you must first detach it from the instance. You cannot delete
an EFA while it is attached to an instance.

You delete EFAs in the same way that you delete elastic network interfaces. For more
information, see [Delete a network interface](delete_eni.md "delete_eni.md").
