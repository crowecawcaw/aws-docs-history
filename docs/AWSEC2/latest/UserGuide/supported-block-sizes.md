

# Block sizes for torn write prevention on Amazon EC2
<a name="supported-block-sizes"></a>

Torn write prevention supports write operations for 4 KiB, 8 KiB, and 16 KiB blocks of data. The data block start logical block address (LBA) must be aligned to the respective block boundary size of 4 KiB, 8 KiB, or 16 KiB. For example, for 16 KiB write operations, the data block start LBA must be aligned to a block boundary size of 16 KiB.

The following table shows support across storage and instance types.


<table>
<thead>
  <tr><th> </th><th>4 KiB blocks</th><th>8 KiB blocks</th><th>16 KiB blocks</th></tr>
</thead>
<tbody>
  <tr><td><b>Instance store volumes</b></td><td>All NVMe instance store volumes attached to current generation I-family instances.</td><td colspan="2">I4i, Im4gn, Is4gen, I7i, I7ie, I8g, and I8ge instances supported by AWS Nitro SSD.</td></tr>
  <tr><td><b>Amazon EBS volumes</b></td><td colspan="3">All Amazon EBS volumes attached to <a href="instance-types.md#instance-hypervisor-type">Nitro-based instances</a>.</td></tr>
</tbody>
</table>


To confirm whether your instance and volume support torn write prevention, query to check if the instance supports torn write prevention and other details, like supported block and boundary sizes. For more information, see [Check Amazon EC2 instance support for torn write prevention](twp-namespace.md).