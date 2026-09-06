

# Lustre file system and client kernel compatibility
<a name="lustre-client-matrix"></a>

We highly recommend using the Lustre version for your FSx for Lustre file system that is compatible with the Linux kernel versions of your client instances.

## Amazon Linux clients
<a name="amz-linux-clients"></a>


<table>
<thead>
  <tr><th>Operating system</th><th>OS version</th><th>Minimum kernel version</th><th>Maximum kernel version</th><th>Lustre client version</th><th colspan="4">Lustre file system version</th></tr>
</thead>
<tbody>
  <tr><td></td><td></td><td></td><td></td><td></td><td><b>2.10</b></td><td><b>2.12</b></td><td><b>2.15</b></td><td></td></tr>
  <tr><td>Amazon Linux 2023</td><td>6.18</td><td>*</td><td>*</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>6.12</td><td>*</td><td>*</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>6.1</td><td>6.1.79-99.167</td><td>6.1.79-99.167+</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td>Amazon Linux 2</td><td>5.10</td><td>5.10.144-127.601</td><td>5.10.144-127.601+</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td></td><td></td><td>&lt;5.10.144-127.601</td><td>2.10</td><td>yes</td><td>yes</td><td>no</td><td></td></tr>
  <tr><td></td><td>5.4</td><td>5.4.214-120.368</td><td>5.4.214-120.368+</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td></td><td></td><td>&lt;5.4.214-120.368</td><td>2.10</td><td>yes</td><td>yes</td><td>no</td><td></td></tr>
  <tr><td></td><td>4.14</td><td>4.14.294-220.533</td><td>4.14.294-220.533+</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td></td><td></td><td>&lt;4.14.294-220.533</td><td>2.10</td><td>yes</td><td>yes</td><td>no</td><td></td></tr>
</tbody>
</table>


## Ubuntu clients
<a name="ubuntu-clients"></a>


<table>
<thead>
  <tr><th>Operating system</th><th>OS version</th><th>Minimum kernel version</th><th>Maximum kernel version</th><th>Lustre client version</th><th colspan="4">Lustre file system version</th></tr>
</thead>
<tbody>
  <tr><td></td><td></td><td></td><td></td><td></td><td><b>2.10</b></td><td><b>2.12</b></td><td><b>2.15</b></td><td></td></tr>
  <tr><td>Ubuntu</td><td>24</td><td>6.17.0-1007</td><td>6.17.0*</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td></td><td>6.14.0-1012</td><td>6.14.0-1018</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td></td><td>6.8.0-1024</td><td>6.8.0-1033</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>22</td><td>6.8.0-1017</td><td>6.8.0*</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td></td><td>6.5.0-1023</td><td>6.5.0-1024</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td></td><td>6.2.0-1017</td><td>6.2.0-1018</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td></td><td>5.15.0-1015-aws</td><td>5.15.0-1051-aws</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>20</td><td>5.15.0-1015-aws</td><td>5.15.0*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td></td><td>5.4.0-1011-aws</td><td>5.13.0-1031-aws</td><td>2.10</td><td>yes</td><td>yes</td><td>no</td><td></td></tr>
</tbody>
</table>


## RHEL/CentOS/Rocky Linux clients
<a name="rhel-clients"></a>

**Note**  
The FSx for Lustre client is compatible with kernels from the standard RHEL BaseOS repository. Kernels from RHEL Extended Update Support (EUS) repositories are not supported.


<table>
<thead>
  <tr><th>Operating system</th><th>OS version</th><th>Architecture</th><th>Minimum kernel version</th><th>Maximum kernel version</th><th>Lustre client version</th><th colspan="4">Lustre file system version</th></tr>
</thead>
<tbody>
  <tr><td></td><td></td><td></td><td></td><td></td><td></td><td><b>2.10</b></td><td><b>2.12</b></td><td><b>2.15</b></td><td></td></tr>
  <tr><td>RHEL/Rocky Linux</td><td>10.2</td><td>Arm + x86</td><td>6.12.0-211.18.1</td><td>6.12.0-211*</td><td>2.15</td><td>no</td><td>no</td><td>yes</td><td></td></tr>
  <tr><td></td><td>10.1</td><td>Arm + x86</td><td>6.12.0-124.8.1</td><td>6.12.0-124*</td><td>2.15</td><td>no</td><td>no</td><td>yes</td><td></td></tr>
  <tr><td>RHEL/Rocky Linux</td><td>9.8</td><td>Arm + x86</td><td>5.14.0-687.5.3</td><td>5.14.0-687*</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>9.7</td><td>Arm + x86</td><td>5.14.0-611.5.1</td><td>5.14.0-611*</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>9.6</td><td>Arm + x86</td><td>5.14.0-570.12.1</td><td>5.14.0-570*</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>9.5</td><td>Arm + x86</td><td>5.14.0-503.19.1</td><td>5.14.0-503*</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>9.4</td><td>Arm + x86</td><td>5.14.0-427.13.1</td><td>5.14.0-427*</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>9.3</td><td>Arm + x86</td><td>5.14.0-362.18.1</td><td>5.14.0-362.18.1</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>9.0</td><td>Arm + x86</td><td>5.14.0-70.13.1</td><td>5.14.0-70.30.1</td><td>2.15</td><td>no</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td>RHEL/CentOS/Rocky Linux</td><td>8.10</td><td>Arm + x86</td><td>4.18.0-553</td><td>4.18.0-553*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>8.9</td><td>Arm + x86</td><td>4.18.0-513*</td><td>4.18.0-513*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>8.8</td><td>Arm + x86</td><td>4.18.0-477*</td><td>4.18.0-477*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>8.7</td><td>Arm + x86</td><td>4.18.0-425*</td><td>4.18.0-425*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>8.6</td><td>Arm + x86</td><td>4.18.0-372*</td><td>4.18.0-372*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>8.5</td><td>Arm + x86</td><td>4.18.0-348*</td><td>4.18.0-348*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>8.4</td><td>Arm + x86</td><td>4.18.0-305*</td><td>4.18.0-305*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td>RHEL/CentOS</td><td>8.3</td><td>Arm + x86</td><td>4.18.0-240*</td><td>4.18.0-240*</td><td>2.10</td><td>yes</td><td>yes</td><td>no</td><td></td></tr>
  <tr><td></td><td>8.2</td><td>Arm + x86</td><td>4.18.0-193*</td><td>4.18.0-193*</td><td>2.10</td><td>yes</td><td>yes</td><td>no</td><td></td></tr>
  <tr><td></td><td>7.9</td><td>x86</td><td>3.10.0-1160*</td><td>3.10.0-1160*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>7.8</td><td>x86</td><td>3.10.0-1127*</td><td>3.10.0-1127*</td><td>2.10</td><td>yes</td><td>yes</td><td>no</td><td></td></tr>
  <tr><td></td><td>7.7</td><td>x86</td><td>3.10.0-1062*</td><td>3.10.0-1062*</td><td>2.10</td><td>yes</td><td>yes</td><td>no</td><td></td></tr>
  <tr><td>CentOS</td><td>7.9</td><td>Arm</td><td>4.18.0-193*</td><td>4.18.0-193*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
  <tr><td></td><td>7.8</td><td>Arm</td><td>4.18.0-147*</td><td>4.18.0-147*</td><td>2.12</td><td>yes</td><td>yes</td><td>yes</td><td></td></tr>
</tbody>
</table>
