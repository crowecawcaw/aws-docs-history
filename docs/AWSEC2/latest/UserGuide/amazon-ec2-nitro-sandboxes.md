

# Isolate workloads with AWS Nitro Sandboxes
<a name="amazon-ec2-nitro-sandboxes"></a>

AWS Nitro Sandboxes is an Amazon EC2 feature that runs a workload in its own lightweight virtual machine, called a *Nitro Sandbox*. A Nitro Sandbox runs alongside an Amazon EC2 instance, called the *parent instance*, on vCPUs and memory that the parent instance contributes. A virtual machine monitor (VMM) on the parent instance manages it, and the AWS Nitro System enforces the boundary around it. To use Nitro Sandboxes, you must enable AWS Nitro Enclaves when you launch the parent instance.

You can use Nitro Sandboxes in the following ways:
+ For containers on Amazon Elastic Kubernetes Service (Amazon EKS), the service runs each pod in its own Nitro Sandbox. For more information, see [Sandboxing on Amazon EKS with isolated and confidential pods](https://docs.aws.amazon.com/eks/latest/userguide/sandboxing.html) in the *Amazon EKS User Guide*.
+ For containers on Amazon Elastic Container Service (Amazon ECS), the service runs each task in its own Nitro Sandbox. For more information, see [Isolated and confidential tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html) in the *Amazon Elastic Container Service Developer Guide*.
+ With your own orchestrator on an Amazon EC2 instance, you launch Nitro Sandboxes with Firecracker. For more information, see [Run Nitro Sandboxes with Firecracker](nitro-sandboxes-run-firecracker.md).

For confidential workloads, you verify the attestation of each Nitro Sandbox with an AWS Key Management Service (AWS KMS) key policy, whichever way you launch it.

There are no additional charges for using Nitro Sandboxes. Nitro Sandboxes run on the vCPUs and memory of the parent instance, so you pay the standard charges for the Amazon EC2 instance and for the other AWS services that you use.

**Topics**
+ [How it works](#nitro-sandboxes-how-it-works)
+ [Confidential and direct modes](#nitro-sandboxes-modes)
+ [When to use Nitro Sandboxes](#nitro-sandboxes-when-to-use)
+ [Supported features](#nitro-sandboxes-features)
+ [Cryptographic attestation](#nitro-sandboxes-attestation-overview)
+ [Considerations and limitations](#nitro-sandboxes-considerations)
+ [Run Nitro Sandboxes with Firecracker](nitro-sandboxes-run-firecracker.md)
+ [Attest a Nitro Sandbox](nitro-sandboxes-attestation.md)

## How it works
<a name="nitro-sandboxes-how-it-works"></a>

A Nitro Sandbox runs on the Nitro Hypervisor alongside its parent instance, the same way that an Amazon EC2 instance does, so its vCPUs run at Amazon EC2 instance level performance. The Nitro System isolates Nitro Sandboxes from each other, and code in a Nitro Sandbox can't access the memory of the parent instance. A Nitro Sandbox reaches the parent instance only through its virtual devices.

The VMM creates Nitro Sandboxes through the Nitro Enclaves driver on the parent instance and implements their virtual devices. Currently, Firecracker is the only VMM that supports Nitro Sandboxes, and the driver is available for Linux. For the supported versions, see [Prerequisites](nitro-sandboxes-run-firecracker.md#nitro-sandboxes-prerequisites).

## Confidential and direct modes
<a name="nitro-sandboxes-modes"></a>

For each Nitro Sandbox, you choose how much the parent instance can observe. You choose the mode at launch, and you can't change it later.

Confidential mode (default)  
The Nitro System removes the memory of the Nitro Sandbox from the parent instance, so neither the parent instance nor its administrators can read or change that memory. Each virtual device exchanges data through its own dedicated buffer. A Nitro Security Module (NSM) in the Nitro Sandbox provides cryptographic attestation.  
The parent instance still carries the device traffic, chooses the image, and controls when the Nitro Sandbox runs. Encrypt data that leaves the Nitro Sandbox, and use attestation to check its image before you give it secrets.  
Use confidential mode for workloads that you keep private from the administrators of the parent instance.

Direct mode  
The parent instance shares the memory of the Nitro Sandbox and can read and write it. There is no NSM and no attestation. The virtual devices exchange data directly through the memory of the Nitro Sandbox, without dedicated buffers, and the trust model is equivalent to that of a nested virtual machine.  
Use direct mode when the same trusted party operates both the Nitro Sandbox and the parent instance.

## When to use Nitro Sandboxes
<a name="nitro-sandboxes-when-to-use"></a>

Choose by how much of the machinery you want to run yourself:
+ None of it: use [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html), with no instances or networking to manage.
+ Your instance, with AWS enforcing the boundary between workloads: use Nitro Sandboxes. This is the general case for sharing an instance between independent workloads, such as AI agents that run code from their users, workloads of different tenants, and build jobs.
+ A small, tightly scoped job on highly sensitive data: use [Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html). An enclave has no persistent storage, interactive access, or external networking, only a local socket to its parent instance. Choose it when that minimal interface is what your job needs.
+ Your own hypervisor or operating system: use [nested virtualization](amazon-ec2-nested-virtualization.md).

Nitro Sandboxes run on instances with Intel, AMD, and AWS Graviton processors. Nested virtualization is available only on instances with Intel processors.

## Supported features
<a name="nitro-sandboxes-features"></a>

Your applications run unmodified in a Nitro Sandbox, which can use the following:

Storage  
A Nitro Sandbox can use block devices on storage of the parent instance and resize them while it runs. Over the network, a workload can use Amazon Simple Storage Service (Amazon S3), Amazon Elastic File System (Amazon EFS), and other network storage through a client in your image.

Networking  
Each Nitro Sandbox runs its own network stack. The network backend of the VMM on the parent instance decides how that stack connects to the network of the parent instance. A local socket (vsock) connects the Nitro Sandbox to the parent instance.

## Cryptographic attestation
<a name="nitro-sandboxes-attestation-overview"></a>

In confidential mode, the Nitro System measures the boot image, the launch settings, the virtual devices at boot (unless you enable hot plug), and the identity of the parent instance. The NSM signs these measurements in an attestation document that the parent instance can't forge.

AWS KMS releases a secret only when the document matches the conditions in your key policy. Always check the measurement of the image in the key policy. The measurements of the parent instance alone also match a Nitro Sandbox in debug mode, a development setting that shows the guest console and records no image measurements. For more information, see [Attest a Nitro Sandbox](nitro-sandboxes-attestation.md).

## Considerations and limitations
<a name="nitro-sandboxes-considerations"></a>

The following considerations apply when you use Nitro Sandboxes:

Supported instance types  
Nitro Sandboxes are not available on flex instances, such as C7i-flex, M7i-flex, C8i-flex, M8i-flex, and R8i-flex. The following instance types support Nitro Sandboxes.  


**General purpose instances that support Nitro Sandboxes**  

<table>
<thead>
  <tr><th>Instance family</th><th>Instance types</th></tr>
</thead>
<tbody>
  <tr><td>M5</td><td>All instance types, <b>except</b>: <code>m5.large</code> | <code>m5.metal</code></td></tr>
  <tr><td>M5a</td><td>All instance types, <b>except</b>: <code>m5a.large</code></td></tr>
  <tr><td>M5ad</td><td>All instance types, <b>except</b>: <code>m5ad.large</code></td></tr>
  <tr><td>M5d</td><td>All instance types, <b>except</b>: <code>m5d.large</code> | <code>m5d.metal</code></td></tr>
  <tr><td>M5dn</td><td>All instance types, <b>except</b>: <code>m5dn.large</code> | <code>m5dn.metal</code></td></tr>
  <tr><td>M5n</td><td>All instance types, <b>except</b>: <code>m5n.large</code> | <code>m5n.metal</code></td></tr>
  <tr><td>M5zn</td><td>All instance types, <b>except</b>: <code>m5zn.large</code> | <code>m5zn.metal</code></td></tr>
  <tr><td>M6a</td><td>All instance types, <b>except</b>: <code>m6a.large</code> | <code>m6a.metal</code></td></tr>
  <tr><td>M6g</td><td>All instance types, <b>except</b>: <code>m6g.medium</code> | <code>m6g.metal</code></td></tr>
  <tr><td>M6gd</td><td>All instance types, <b>except</b>: <code>m6gd.medium</code> | <code>m6gd.metal</code></td></tr>
  <tr><td>M6i</td><td>All instance types, <b>except</b>: <code>m6i.large</code> | <code>m6i.metal</code></td></tr>
  <tr><td>M6id</td><td>All instance types, <b>except</b>: <code>m6id.large</code> | <code>m6id.metal</code></td></tr>
  <tr><td>M6idn</td><td>All instance types, <b>except</b>: <code>m6idn.large</code> | <code>m6idn.metal</code></td></tr>
  <tr><td>M6in</td><td>All instance types, <b>except</b>: <code>m6in.large</code> | <code>m6in.metal</code></td></tr>
  <tr><td>M7a</td><td>All instance types, <b>except</b>: <code>m7a.medium</code> | <code>m7a.large</code> | <code>m7a.metal-48xl</code></td></tr>
  <tr><td>M7g</td><td>All instance types, <b>except</b>: <code>m7g.medium</code> | <code>m7g.metal</code></td></tr>
  <tr><td>M7gd</td><td>All instance types, <b>except</b>: <code>m7gd.medium</code> | <code>m7gd.metal</code></td></tr>
  <tr><td>M7i</td><td>All instance types, <b>except</b>: <code>m7i.large</code> | <code>m7i.metal-24xl</code> | <code>m7i.metal-48xl</code></td></tr>
  <tr><td>M8a</td><td>All instance types, <b>except</b>: <code>m8a.medium</code> | <code>m8a.metal-24xl</code> | <code>m8a.metal-48xl</code></td></tr>
  <tr><td>M8azn</td><td>All instance types, <b>except</b>: <code>m8azn.medium</code> | <code>m8azn.metal-12xl</code> | <code>m8azn.metal-24xl</code></td></tr>
  <tr><td>M8g</td><td>All instance types, <b>except</b>: <code>m8g.medium</code> | <code>m8g.metal-24xl</code> | <code>m8g.metal-48xl</code></td></tr>
  <tr><td>M8gb</td><td>All instance types, <b>except</b>: <code>m8gb.medium</code> | <code>m8gb.metal-24xl</code> | <code>m8gb.metal-48xl</code></td></tr>
  <tr><td>M8gd</td><td>All instance types, <b>except</b>: <code>m8gd.medium</code> | <code>m8gd.metal-24xl</code> | <code>m8gd.metal-48xl</code></td></tr>
  <tr><td>M8gn</td><td>All instance types, <b>except</b>: <code>m8gn.medium</code> | <code>m8gn.metal-24xl</code> | <code>m8gn.metal-48xl</code></td></tr>
  <tr><td>M8i</td><td>All instance types, <b>except</b>: <code>m8i.large</code> | <code>m8i.metal-48xl</code> | <code>m8i.metal-96xl</code></td></tr>
  <tr><td>M8id</td><td>All instance types, <b>except</b>: <code>m8id.large</code> | <code>m8id.metal-48xl</code> | <code>m8id.metal-96xl</code></td></tr>
  <tr><td>M8in</td><td>All instance types, <b>except</b>: <code>m8in.large</code> | <code>m8in.metal-48xl</code> | <code>m8in.metal-96xl</code></td></tr>
  <tr><td>M8idn</td><td>All instance types, <b>except</b>: <code>m8idn.large</code> | <code>m8idn.metal-48xl</code> | <code>m8idn.metal-96xl</code></td></tr>
  <tr><td>M8ine</td><td>All instance types, <b>except</b>: <code>m8ine.large</code></td></tr>
  <tr><td>M8ib</td><td>All instance types, <b>except</b>: <code>m8ib.large</code> | <code>m8ib.metal-48xl</code> | <code>m8ib.metal-96xl</code></td></tr>
  <tr><td>M8idb</td><td>All instance types, <b>except</b>: <code>m8idb.large</code> | <code>m8idb.metal-48xl</code> | <code>m8idb.metal-96xl</code></td></tr>
  <tr><td>M9g</td><td>All instance types, <b>except</b>: <code>m9g.medium</code> | <code>m9g.metal-48xl</code></td></tr>
  <tr><td>M9gd</td><td>All instance types, <b>except</b>: <code>m9gd.medium</code> | <code>m9gd.metal-48xl</code></td></tr>
</tbody>
</table>



**Compute optimized instances that support Nitro Sandboxes**  

<table>
<thead>
  <tr><th>Instance family</th><th>Instance types</th></tr>
</thead>
<tbody>
  <tr><td>C5</td><td>All instance types, <b>except</b>: <code>c5.large</code> | <code>c5.metal</code></td></tr>
  <tr><td>C5a</td><td>All instance types, <b>except</b>: <code>c5a.large</code></td></tr>
  <tr><td>C5ad</td><td>All instance types, <b>except</b>: <code>c5ad.large</code></td></tr>
  <tr><td>C5d</td><td>All instance types, <b>except</b>: <code>c5d.large</code> | <code>c5d.metal</code></td></tr>
  <tr><td>C5n</td><td>All instance types, <b>except</b>: <code>c5n.large</code> | <code>c5n.metal</code></td></tr>
  <tr><td>C6a</td><td>All instance types, <b>except</b>: <code>c6a.large</code> | <code>c6a.metal</code></td></tr>
  <tr><td>C6g</td><td>All instance types, <b>except</b>: <code>c6g.medium</code> | <code>c6g.metal</code></td></tr>
  <tr><td>C6gd</td><td>All instance types, <b>except</b>: <code>c6gd.medium</code> | <code>c6gd.metal</code></td></tr>
  <tr><td>C6gn</td><td>All instance types, <b>except</b>: <code>c6gn.medium</code></td></tr>
  <tr><td>C6i</td><td>All instance types, <b>except</b>: <code>c6i.large</code> | <code>c6i.metal</code></td></tr>
  <tr><td>C6id</td><td>All instance types, <b>except</b>: <code>c6id.large</code> | <code>c6id.metal</code></td></tr>
  <tr><td>C6in</td><td>All instance types, <b>except</b>: <code>c6in.large</code> | <code>c6in.metal</code></td></tr>
  <tr><td>C7a</td><td>All instance types, <b>except</b>: <code>c7a.medium</code> | <code>c7a.large</code> | <code>c7a.metal-48xl</code></td></tr>
  <tr><td>C7g</td><td>All instance types, <b>except</b>: <code>c7g.medium</code> | <code>c7g.metal</code></td></tr>
  <tr><td>C7gd</td><td>All instance types, <b>except</b>: <code>c7gd.medium</code> | <code>c7gd.metal</code></td></tr>
  <tr><td>C7i</td><td>All instance types, <b>except</b>: <code>c7i.large</code> | <code>c7i.metal-24xl</code> | <code>c7i.metal-48xl</code></td></tr>
  <tr><td>C8a</td><td>All instance types, <b>except</b>: <code>c8a.medium</code> | <code>c8a.metal-24xl</code> | <code>c8a.metal-48xl</code></td></tr>
  <tr><td>C8g</td><td>All instance types, <b>except</b>: <code>c8g.medium</code> | <code>c8g.metal-24xl</code> | <code>c8g.metal-48xl</code></td></tr>
  <tr><td>C8gb</td><td>All instance types, <b>except</b>: <code>c8gb.medium</code> | <code>c8gb.metal-24xl</code> | <code>c8gb.metal-48xl</code></td></tr>
  <tr><td>C8gd</td><td>All instance types, <b>except</b>: <code>c8gd.medium</code> | <code>c8gd.metal-24xl</code> | <code>c8gd.metal-48xl</code></td></tr>
  <tr><td>C8gn</td><td>All instance types, <b>except</b>: <code>c8gn.medium</code> | <code>c8gn.metal-24xl</code> | <code>c8gn.metal-48xl</code></td></tr>
  <tr><td>C8i</td><td>All instance types, <b>except</b>: <code>c8i.large</code> | <code>c8i.metal-48xl</code> | <code>c8i.metal-96xl</code></td></tr>
  <tr><td>C8id</td><td>All instance types, <b>except</b>: <code>c8id.large</code> | <code>c8id.metal-48xl</code> | <code>c8id.metal-96xl</code></td></tr>
  <tr><td>C8in</td><td>All instance types, <b>except</b>: <code>c8in.large</code> | <code>c8in.metal-48xl</code> | <code>c8in.metal-96xl</code></td></tr>
  <tr><td>C8ine</td><td>All instance types, <b>except</b>: <code>c8ine.large</code></td></tr>
  <tr><td>C8ib</td><td>All instance types, <b>except</b>: <code>c8ib.large</code> | <code>c8ib.metal-48xl</code> | <code>c8ib.metal-96xl</code></td></tr>
  <tr><td>C9g</td><td>All instance types, <b>except</b>: <code>c9g.medium</code> | <code>c9g.metal-48xl</code></td></tr>
  <tr><td>C9gd</td><td>All instance types, <b>except</b>: <code>c9gd.medium</code> | <code>c9gd.metal-48xl</code></td></tr>
</tbody>
</table>



**Memory optimized instances that support Nitro Sandboxes**  

<table>
<thead>
  <tr><th>Instance family</th><th>Instance types</th></tr>
</thead>
<tbody>
  <tr><td>R5</td><td>All instance types, <b>except</b>: <code>r5.large</code> | <code>r5.metal</code></td></tr>
  <tr><td>R5a</td><td>All instance types, <b>except</b>: <code>r5a.large</code></td></tr>
  <tr><td>R5ad</td><td>All instance types, <b>except</b>: <code>r5ad.large</code></td></tr>
  <tr><td>R5b</td><td>All instance types, <b>except</b>: <code>r5b.large</code> | <code>r5b.metal</code></td></tr>
  <tr><td>R5d</td><td>All instance types, <b>except</b>: <code>r5d.large</code> | <code>r5d.metal</code></td></tr>
  <tr><td>R5dn</td><td>All instance types, <b>except</b>: <code>r5dn.large</code> | <code>r5dn.metal</code></td></tr>
  <tr><td>R5n</td><td>All instance types, <b>except</b>: <code>r5n.large</code> | <code>r5n.metal</code></td></tr>
  <tr><td>R6a</td><td>All instance types, <b>except</b>: <code>r6a.large</code> | <code>r6a.metal</code></td></tr>
  <tr><td>R6g</td><td>All instance types, <b>except</b>: <code>r6g.medium</code> | <code>r6g.metal</code></td></tr>
  <tr><td>R6gd</td><td>All instance types, <b>except</b>: <code>r6gd.medium</code> | <code>r6gd.metal</code></td></tr>
  <tr><td>R6i</td><td>All instance types, <b>except</b>: <code>r6i.large</code> | <code>r6i.metal</code></td></tr>
  <tr><td>R6id</td><td>All instance types, <b>except</b>: <code>r6id.large</code> | <code>r6id.metal</code></td></tr>
  <tr><td>R6idn</td><td>All instance types, <b>except</b>: <code>r6idn.large</code> | <code>r6idn.metal</code></td></tr>
  <tr><td>R6in</td><td>All instance types, <b>except</b>: <code>r6in.large</code> | <code>r6in.metal</code></td></tr>
  <tr><td>R7a</td><td>All instance types, <b>except</b>: <code>r7a.medium</code> | <code>r7a.large</code> | <code>r7a.metal-48xl</code></td></tr>
  <tr><td>R7g</td><td>All instance types, <b>except</b>: <code>r7g.medium</code> | <code>r7g.metal</code></td></tr>
  <tr><td>R7gd</td><td>All instance types, <b>except</b>: <code>r7gd.medium</code> | <code>r7gd.metal</code></td></tr>
  <tr><td>R7i</td><td>All instance types, <b>except</b>: <code>r7i.large</code> | <code>r7i.metal-24xl</code> | <code>r7i.metal-48xl</code></td></tr>
  <tr><td>R7iz</td><td>All instance types, <b>except</b>: <code>r7iz.large</code> | <code>r7iz.metal-16xl</code> | <code>r7iz.metal-32xl</code></td></tr>
  <tr><td>R8a</td><td>All instance types, <b>except</b>: <code>r8a.medium</code> | <code>r8a.metal-24xl</code> | <code>r8a.metal-48xl</code></td></tr>
  <tr><td>R8g</td><td>All instance types, <b>except</b>: <code>r8g.medium</code> | <code>r8g.metal-24xl</code> | <code>r8g.metal-48xl</code></td></tr>
  <tr><td>R8gb</td><td>All instance types, <b>except</b>: <code>r8gb.medium</code> | <code>r8gb.metal-24xl</code> | <code>r8gb.metal-48xl</code></td></tr>
  <tr><td>R8gd</td><td>All instance types, <b>except</b>: <code>r8gd.medium</code> | <code>r8gd.metal-24xl</code> | <code>r8gd.metal-48xl</code></td></tr>
  <tr><td>R8gn</td><td>All instance types, <b>except</b>: <code>r8gn.medium</code> | <code>r8gn.metal-24xl</code> | <code>r8gn.metal-48xl</code></td></tr>
  <tr><td>R8i</td><td>All instance types, <b>except</b>: <code>r8i.large</code> | <code>r8i.metal-48xl</code> | <code>r8i.metal-96xl</code></td></tr>
  <tr><td>R8id</td><td>All instance types, <b>except</b>: <code>r8id.large</code> | <code>r8id.metal-48xl</code> | <code>r8id.metal-96xl</code></td></tr>
  <tr><td>R8in</td><td>All instance types, <b>except</b>: <code>r8in.large</code> | <code>r8in.metal-48xl</code> | <code>r8in.metal-96xl</code></td></tr>
  <tr><td>R8idn</td><td>All instance types, <b>except</b>: <code>r8idn.large</code> | <code>r8idn.metal-48xl</code> | <code>r8idn.metal-96xl</code></td></tr>
  <tr><td>R8ib</td><td>All instance types, <b>except</b>: <code>r8ib.large</code> | <code>r8ib.metal-48xl</code> | <code>r8ib.metal-96xl</code></td></tr>
  <tr><td>R8idb</td><td>All instance types, <b>except</b>: <code>r8idb.large</code> | <code>r8idb.metal-48xl</code> | <code>r8idb.metal-96xl</code></td></tr>
  <tr><td>R9g</td><td>All instance types, <b>except</b>: <code>r9g.medium</code> | <code>r9g.metal-48xl</code></td></tr>
  <tr><td>R9gd</td><td>All instance types, <b>except</b>: <code>r9gd.medium</code> | <code>r9gd.metal-48xl</code></td></tr>
  <tr><td>X2gd</td><td>All instance types, <b>except</b>: <code>x2gd.medium</code> | <code>x2gd.metal</code></td></tr>
  <tr><td>X2idn</td><td>All instance types, <b>except</b>: <code>x2idn.metal</code></td></tr>
  <tr><td>X2iedn</td><td>All instance types, <b>except</b>: <code>x2iedn.metal</code></td></tr>
  <tr><td>X2iezn</td><td>All instance types, <b>except</b>: <code>x2iezn.metal</code></td></tr>
  <tr><td>X8g</td><td>All instance types, <b>except</b>: <code>x8g.medium</code> | <code>x8g.metal-24xl</code> | <code>x8g.metal-48xl</code></td></tr>
  <tr><td>X8aedz</td><td>All instance types, <b>except</b>: <code>x8aedz.metal-12xl</code> | <code>x8aedz.metal-24xl</code></td></tr>
  <tr><td>X8i</td><td>All instance types, <b>except</b>: <code>x8i.large</code> | <code>x8i.metal-48xl</code> | <code>x8i.metal-96xl</code></td></tr>
  <tr><td>z1d</td><td>All instance types, <b>except</b>: <code>z1d.large</code> | <code>z1d.metal</code></td></tr>
</tbody>
</table>



**Storage optimized instances that support Nitro Sandboxes**  

<table>
<thead>
  <tr><th>Instance family</th><th>Instance types</th></tr>
</thead>
<tbody>
  <tr><td>D3</td><td>All instance types.</td></tr>
  <tr><td>D3en</td><td>All instance types.</td></tr>
  <tr><td>I3en</td><td>All instance types, <b>except</b>: <code>i3en.large</code> | <code>i3en.metal</code></td></tr>
  <tr><td>I4g</td><td>All instance types.</td></tr>
  <tr><td>I4i</td><td>All instance types, <b>except</b>: <code>i4i.large</code> | <code>i4i.metal</code></td></tr>
  <tr><td>I7i</td><td>All instance types, <b>except</b>: <code>i7i.large</code> | <code>i7i.metal-24xl</code> | <code>i7i.metal-48xl</code></td></tr>
  <tr><td>I7ie</td><td>All instance types, <b>except</b>: <code>i7ie.large</code> | <code>i7ie.metal-24xl</code> | <code>i7ie.metal-48xl</code></td></tr>
  <tr><td>I8g</td><td>All instance types, <b>except</b>: <code>i8g.metal-24xl</code> | <code>i8g.metal-48xl</code></td></tr>
  <tr><td>I8ge</td><td>All instance types, <b>except</b>: <code>i8ge.metal-24xl</code> | <code>i8ge.metal-48xl</code></td></tr>
</tbody>
</table>

On accelerated computing instances, a Nitro Sandbox runs CPU workloads only.  


**Accelerated computing instances that support Nitro Sandboxes**  

<table>
<thead>
  <tr><th>Instance family</th><th>Instance types</th></tr>
</thead>
<tbody>
  <tr><td>G5</td><td><code>g5.xlarge</code> | <code>g5.2xlarge</code> | <code>g5.4xlarge</code> | <code>g5.8xlarge</code> | <code>g5.12xlarge</code> | <code>g5.16xlarge</code> | <code>g5.24xlarge</code> | <code>g5.48xlarge</code></td></tr>
  <tr><td>G5g</td><td><code>g5g.xlarge</code> | <code>g5g.2xlarge</code> | <code>g5g.4xlarge</code> | <code>g5g.8xlarge</code> | <code>g5g.16xlarge</code></td></tr>
  <tr><td>G6</td><td><code>g6.xlarge</code> | <code>g6.2xlarge</code> | <code>g6.4xlarge</code> | <code>g6.8xlarge</code> | <code>g6.12xlarge</code> | <code>g6.16xlarge</code> | <code>g6.24xlarge</code> | <code>g6.48xlarge</code></td></tr>
  <tr><td>G6e</td><td><code>g6e.xlarge</code> | <code>g6e.2xlarge</code> | <code>g6e.4xlarge</code> | <code>g6e.8xlarge</code> | <code>g6e.12xlarge</code> | <code>g6e.16xlarge</code> | <code>g6e.24xlarge</code> | <code>g6e.48xlarge</code></td></tr>
  <tr><td>Gr6</td><td><code>gr6.4xlarge</code> | <code>gr6.8xlarge</code></td></tr>
  <tr><td>G7</td><td><code>g7.2xlarge</code> | <code>g7.4xlarge</code> | <code>g7.8xlarge</code> | <code>g7.12xlarge</code> | <code>g7.24xlarge</code> | <code>g7.48xlarge</code></td></tr>
  <tr><td>G7e</td><td><code>g7e.2xlarge</code> | <code>g7e.4xlarge</code> | <code>g7e.8xlarge</code> | <code>g7e.12xlarge</code> | <code>g7e.24xlarge</code> | <code>g7e.48xlarge</code></td></tr>
  <tr><td>P3dn</td><td><code>p3dn.24xlarge</code></td></tr>
</tbody>
</table>


Number of Nitro Sandboxes and vCPUs  
Each vCPU of a Nitro Sandbox either has a dedicated hardware thread of the parent instance or, with *CPU overcommit*, shares the vCPUs of the parent instance. You choose this for each Nitro Sandbox at launch.  
You can run up to 5 Nitro Sandboxes for each vCPU of the parent instance, and at most 896 Nitro Sandboxes on one parent instance. Each Nitro Sandbox can have at most as many vCPUs as the parent instance. With CPU overcommit, all Nitro Sandboxes together can have up to 5 times as many vCPUs as the parent instance. The following table shows an example.  


**Nitro Sandboxes with CPU overcommit on a parent instance with 4 vCPUs**  
<a name="nitro-sandboxes-budget-example"></a>
<table>
<thead>
  <tr><th>vCPUs for each Nitro Sandbox</th><th>Maximum Nitro Sandboxes</th></tr>
</thead>
<tbody>
  <tr><td>1</td><td>20</td></tr>
  <tr><td>2</td><td>10</td></tr>
  <tr><td>4</td><td>5</td></tr>
</tbody>
</table>

Without CPU overcommit, the vCPUs of all Nitro Sandboxes together can't exceed the vCPUs of the parent instance, minus the vCPUs of its first core. For more information, see [Set the size of a Nitro Sandbox](nitro-sandboxes-run-firecracker.md#nitro-sandboxes-resize).

CPU on instances with two threads per core  
On instances with two threads per core, a core runs only one Nitro Sandbox, or only the parent instance, at a time. The compute available to Nitro Sandboxes is therefore bounded by the physical cores, about half the vCPUs. AWS Graviton instances have one thread per core.

Memory  
Nitro Sandbox memory comes from a memory pool that the parent instance reserves at boot. Each Nitro Sandbox uses its own memory plus 2 MiB of the pool, and in confidential mode another 16 MiB for each virtual device.  
Each running Nitro Sandbox also uses one of the Nitro Sandbox slots of the parent instance. The parent instance starts with 4 slots, and you can add more in steps of 8. Each step uses another 128 MiB of the pool. For more information, see [Prepare the parent instance](nitro-sandboxes-run-firecracker.md#nitro-sandboxes-prepare-parent).  
Give each Nitro Sandbox at least 256 MiB of memory.

Devices  
Each Nitro Sandbox supports up to 32 virtual devices, including devices that you hot plug. You can't remove a device from a running Nitro Sandbox.

GPU passthrough  
GPU passthrough into a Nitro Sandbox is currently unavailable.

Lifecycle  
When you stop, reboot, or terminate the parent instance, its Nitro Sandboxes stop too. You can't enable [hibernation](Hibernate.md) on a parent instance.  
You can't change the vCPUs or memory of a running Nitro Sandbox. Nitro Sandboxes do not support snapshot and restore, pause and resume, or live migration.

Storage  
The parent instance can read every block device that it presents to a Nitro Sandbox, including encrypted Amazon Elastic Block Store (Amazon EBS) volumes. Amazon EBS encryption and server-side encryption with AWS KMS keys (SSE-KMS) do not protect data from the parent instance. To keep data confidential, encrypt it inside the Nitro Sandbox with a key that AWS KMS releases only to an attested Nitro Sandbox.

Networking and instance metadata  
A Nitro Sandbox has no [instance metadata service (IMDS)](ec2-instance-metadata.md) of its own. If the parent instance routes traffic from a Nitro Sandbox, for example with NAT, the Nitro Sandbox can reach the IMDS of the parent instance and read its AWS Identity and Access Management (IAM) role credentials. IMDSv2 and the hop limit of 2 that Amazon Linux 2023 AMIs use do not prevent this. To block this access, reject traffic from Nitro Sandboxes to `169.254.169.254` on the parent instance.  
One Nitro Sandbox can exhaust network resources that all Nitro Sandboxes share on the parent instance, such as the connection tracking table, so limit these resources for each Nitro Sandbox.

Nested virtualization  
You can't use Nitro Sandboxes or Nitro Enclaves on an instance that has [nested virtualization](amazon-ec2-nested-virtualization.md) enabled.

Credential Guard  
You can't use Nitro Sandboxes and [Credential Guard](credential-guard.md) on the same instance during the same boot. If Credential Guard starts first, creating a Nitro Sandbox fails. If a Nitro Sandbox starts first, Windows stops with an error when Credential Guard starts. Nitro Enclaves on its own is not affected.