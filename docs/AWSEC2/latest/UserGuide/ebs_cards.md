

# EBS cards
<a name="ebs_cards"></a>

Most instance types support one EBS card. Instance types that support multiple EBS cards provide higher EBS-optimized performance, both in EBS throughput and IOPS. Your Amazon EC2 instance maximum performance is spread equally across each EBS card. For example, on an EC2 instance that supports `1,000,000` total IOPS with 2 EBS cards, each EBS card can support up to `500,000` IOPS. For information about the supported Amazon EBS performance of your Amazon EC2 instance, see [Amazon EBS-optimized instance types](ebs-optimized.md).

When you attach an Amazon EBS volume to an instance that supports multiple EBS cards, you can select the EBS card for the volume by specifying the EBS card index. The root volume must be attached to EBS card index 0.

## Instance types with multiple EBS cards
<a name="instance-types-multiple-EBS-cards"></a>

The following instance types support multiple EBS cards. For information about the number of Amazon EBS volumes that an instance type supports, see [Amazon EBS volume limits for Amazon EC2 instances](volume_limits.md).


<table>
<thead>
  <tr><th>Instance Type</th><th>Number of EBS cards</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><b>General Purpose</b></td></tr>
  <tr><td>m8gb.48xlarge</td><td>2</td></tr>
  <tr><td>m8gb.metal-48xl</td><td>2</td></tr>
  <tr><td>m8gn.48xlarge</td><td>2</td></tr>
  <tr><td>m8gn.metal-48xl</td><td>2</td></tr>
  <tr><td>m8in.96xlarge</td><td>2</td></tr>
  <tr><td>m8in.metal-96xl</td><td>2</td></tr>
  <tr><td>m8idn.96xlarge</td><td>2</td></tr>
  <tr><td>m8idn.metal-96xl</td><td>2</td></tr>
  <tr><td>m8ib.96xlarge</td><td>2</td></tr>
  <tr><td>m8ib.metal-96xl</td><td>2</td></tr>
  <tr><td>m8idb.96xlarge</td><td>2</td></tr>
  <tr><td>m8idb.metal-96xl</td><td>2</td></tr>
  <tr><td colspan="2"><b>Compute Optimized</b></td></tr>
  <tr><td>c8gb.48xlarge</td><td>2</td></tr>
  <tr><td>c8gb.metal-48xl</td><td>2</td></tr>
  <tr><td>c8gn.48xlarge</td><td>2</td></tr>
  <tr><td>c8gn.metal-48xl</td><td>2</td></tr>
  <tr><td>c8in.96xlarge</td><td>2</td></tr>
  <tr><td>c8in.metal-96xl</td><td>2</td></tr>
  <tr><td>c8ib.96xlarge</td><td>2</td></tr>
  <tr><td>c8ib.metal-96xl</td><td>2</td></tr>
  <tr><td colspan="2"><b>Memory Optimized</b></td></tr>
  <tr><td>r8gb.48xlarge</td><td>2</td></tr>
  <tr><td>r8gb.metal-48xl</td><td>2</td></tr>
  <tr><td>r8gn.48xlarge</td><td>2</td></tr>
  <tr><td>r8gn.metal-48xl</td><td>2</td></tr>
  <tr><td>r8in.96xlarge</td><td>2</td></tr>
  <tr><td>r8in.metal-96xl</td><td>2</td></tr>
  <tr><td>r8idn.96xlarge</td><td>2</td></tr>
  <tr><td>r8idn.metal-96xl</td><td>2</td></tr>
  <tr><td>r8ib.96xlarge</td><td>2</td></tr>
  <tr><td>r8ib.metal-96xl</td><td>2</td></tr>
  <tr><td>r8idb.96xlarge</td><td>2</td></tr>
  <tr><td>r8idb.metal-96xl</td><td>2</td></tr>
  <tr><td colspan="2"><b>Accelerated Computing</b></td></tr>
  <tr><td>g7.48xlarge</td><td>2</td></tr>
</tbody>
</table>
