

# What is Nitro Enclaves?
<a name="nitro-enclave"></a>

AWS Nitro Enclaves is an Amazon EC2 feature that allows you to create isolated execution environments, called *enclaves*, from Amazon EC2 instances. Enclaves are separate, hardened, and highly-constrained virtual machines. They provide only secure local socket connectivity with their parent instance. They have no persistent storage, interactive access, or external networking. Users cannot SSH into an enclave, and the data and applications inside the enclave cannot be accessed by the processes, applications, or users (root or admin) of the parent instance. Using Nitro Enclaves, you can secure your most sensitive data, such as personally identifiable information (PII), and your data processing applications.

![Overview](https://docs.aws.amazon.com/enclaves/latest/user/images/enclave-overview.png)


**Note**  
Nitro Enclaves is processor agnostic and it is supported on most Intel, AMD, and AWS Graviton-based Amazon EC2 instance types built on the AWS Nitro System.

Nitro Enclaves also supports an attestation feature, which allows you to verify an enclave's identity and ensure that only authorized code is running inside it. Nitro Enclaves is integrated with the AWS Key Management Service, which provides built-in support for attestation and enables you to prepare and protect your sensitive data for processing inside enclaves. Nitro Enclaves can also be used with other key management services.

Nitro Enclaves use the same Nitro Hypervisor technology that provides CPU and memory isolation for Amazon EC2 instances in order to isolate the vCPUs and memory for an enclave from a parent instance. The Nitro Hypervisor ensures that the parent instance has no access to the isolated vCPUs and memory of the enclave.

To learn more about creating your first enclave using a sample enclave application, see [Getting started: Hello Enclaves sample application](getting-started.md).

**Topics**
+ [Learn more](#learn-more)
+ [Requirements](#nitro-enclave-reqs)
+ [Considerations](#nitro-enclave-considerations)
+ [Pricing](#nitro-enclave-pricing)
+ [Related services](#nitro-enclave-related)

## Learn more
<a name="learn-more"></a>
+ To learn about the concepts used in Nitro Enclaves, see [Nitro Enclaves concepts](nitro-enclave-concepts.md).
+ To get started with your first enclave using a sample enclave application, see [Getting started: Hello Enclaves sample application](getting-started.md).
+ To learn about using the AWS Nitro Enclaves CLI to manage the lifecycle of enclaves, see [Nitro Enclaves Command Line Interface](nitro-enclave-cli.md).
+ To learn about developing custom enclave applications and the AWS Nitro Enclaves SDK, see [Nitro Enclaves application development](developing-applications.md).
+ To learn about multiple enclaves, see [Working with multiple enclaves](multiple-enclaves.md).

## Requirements
<a name="nitro-enclave-reqs"></a>

Nitro Enclaves has the following requirements:
+ **Parent instance requirements:**
  + The parent instance must use one of the following instance types and a Linux or Windows (2016 or later) operating system.

------
#### [ General purpose ]


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


------
#### [ Compute optimized ]


<table>
<thead>
  <tr><th>Instance family</th><th>Exceptions</th></tr>
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


------
#### [ Memory optimized ]


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


------
#### [ Storage optimized ]


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


------
#### [ Accelerated computing ]


<table>
<thead>
  <tr><th>Instance family</th><th>Instance types</th></tr>
</thead>
<tbody>
  <tr><td>DL1</td><td>All instance types.</td></tr>
  <tr><td>DL2q</td><td>All instance types.</td></tr>
  <tr><td>F2</td><td>All instance types.</td></tr>
  <tr><td>G4dn</td><td>All instance types, <b>except</b>: <code>g4dn.metal</code></td></tr>
  <tr><td>G5</td><td>All instance types.</td></tr>
  <tr><td>G6</td><td>All instance types.</td></tr>
  <tr><td>G6e</td><td>All instance types.</td></tr>
  <tr><td>G6f</td><td>All instance types, <b>except</b>: <code>g6f.large</code></td></tr>
  <tr><td>Gr6</td><td>All instance types.</td></tr>
  <tr><td>Gr6f</td><td>All instance types.</td></tr>
  <tr><td>G7</td><td>All instance types.</td></tr>
  <tr><td>G7e</td><td>All instance types.</td></tr>
  <tr><td>Inf1</td><td>All instance types.</td></tr>
  <tr><td>Inf2</td><td>All instance types.</td></tr>
  <tr><td>P4d</td><td>All instance types.</td></tr>
  <tr><td>P4de</td><td>All instance types.</td></tr>
  <tr><td>P5</td><td>All instance types.</td></tr>
  <tr><td>P5e</td><td>All instance types.</td></tr>
  <tr><td>P5en</td><td>All instance types.</td></tr>
  <tr><td>P6-B300</td><td>All instance types.</td></tr>
  <tr><td>P6e-GB200</td><td>All instance types.</td></tr>
  <tr><td>Trn2</td><td>All instance types.</td></tr>
  <tr><td>Trn2u</td><td>All instance types.</td></tr>
</tbody>
</table>


------
+ **Enclave requirements:**
  + The enclave must run a Linux operating system.

## Considerations
<a name="nitro-enclave-considerations"></a>

Keep the following in mind when using Nitro Enclaves:
+ Nitro Enclaves is supported in all AWS Regions, including the AWS GovCloud (US) Regions.
+ You can create up to four individual enclaves per parent instance.
+ Enclaves can communicate only with the parent instance. Enclaves running on the same or different parent instances cannot communicate with each other.
+ Enclaves are active only while their parent instance is in the `running` state. If the parent instance is stopped or terminated, its enclaves are terminated.
+ You cannot enable hibernation and enclaves on the same instance.
+ Nitro Enclaves is not supported on Outposts.
+ Nitro Enclaves is not supported in Local Zones or Wavelength Zones.

## Pricing
<a name="nitro-enclave-pricing"></a>

There are no additional charges for using Nitro Enclaves. You are billed the standard charges for the Amazon EC2 instance and for the other AWS services that you use.

## Related services
<a name="nitro-enclave-related"></a>

Nitro Enclaves is integrated with the following AWS services:

**AWS Key Management Service**  
AWS Key Management Service (KMS) makes it easy for you to create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications. Nitro Enclaves integrates with AWS KMS and it allows you to perform selected KMS operations from the enclave using the [AWS Nitro Enclaves SDK](https://github.com/aws/aws-nitro-enclaves-sdk-c). These operations can be tied to the [cryptographic attestation](set-up-attestation.md) process of Nitro Enclaves by setting a AWS KMS key policy to ensure that the operation works only when the measurements of the enclave match the KMS key policy. For more information, see [AWS KMS condition keys for Nitro Enclaves](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-nitro-enclaves) in the *AWS Key Management Service Developer Guide*.

**AWS Certificate Manager**  
AWS Certificate Manager (ACM) is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources. SSL/TLS certificates are used to secure network communications and to establish the identity of websites over the internet, as well as resources on private networks. ACM removes the time-consuming manual process of purchasing, uploading, and renewing SSL/TLS certificates. For more information, see [AWS Certificate Manager for Nitro Enclaves](nitro-enclave-refapp.md).