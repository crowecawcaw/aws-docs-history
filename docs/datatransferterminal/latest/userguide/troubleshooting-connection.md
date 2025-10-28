# Troubleshooting network connection issues

If you experience issues connecting to the network while using AWS Data Transfer Terminal, such as not being able to connect the internet or slow connection speeds, consider the following troubleshooting tips.

###### Topics

- [Equipment connection issues](#physical-connection "#physical-connection")
- [Troubleshooting connectivity](#connection-issues "#connection-issues")
- [Network throughput](#throughput "#throughput")

## Equipment connection issues

If you are having difficulty establishing a physical connection while in the Data Transfer Terminal suite, consider the following:

- Each Data Transfer Terminal facility will have two (2) single-mode, LC fiber cables. If one or both of these cables are missing, contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") immediately.
- If one fiber optic cable is not working, try rolling the cable first. If you are still unable to connect with the first cable, try using the other cable.

If you’re still unable to use the cables to connect, contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") immediately.

## Troubleshooting connectivity

If you’re able to connect your equipment but are not able to connect to the network, try the following troubleshooting suggestions.

- Confirm that your equipment configuration meets the specified network requirements. For more information, see [Technical requirements for using Data Transfer Terminal](tech-requirements.md "tech-requirements.md")
- Switch to the other fiber optic cable to connect.
- Reboot your device while keeping the fiber optic cables connected.
- Perform basic network diagnostics on the device to ensure the following:
  - DHCP is enabled
  - An IP address is assigned to the connected network interface
  - DNS servers are configured
  - The system clock is synchronized with NTP

If you’re still unable connect, contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") and provide them with the following outputs depending on what operating system (OS) is running on your device.

### Linux/Unix

- Get IP address and routing information in a terminal or command-line interface (CLI). Verify that an IP address is assigned to the network interface, and a default route with a default gateway address is added in the route table.

```
ip address show
ip route show
```

    + Alternatively, if `iproute2` is not installed on the device and `ip` commands are not available, use the following commands:



    ```
    ifconfig
    netstat -rn
    ```

- Collect DNS server information. This should show two IP addresses starting with the `nameserver` keyword.

```
cat /etc/resolv.conf
```

- Collect the output of basic connectivity tests. Replace the `default_gateway_address` with the IP address of the default gateway assigned.

```
ping -c 5 <default_gateway_address>
ping -c 5 s3.amazonaws.com
traceroute s3.amazonaws.com
```

- Collect the output of the HTTPS connectivity test. The following command should show a `HTTP 200 OK` response from Amazon S3.

```
curl -i https://s3.amazonaws.com/ping
```

### Windows

- Get the IP address, routing and DNS server information in the command prompt. Verify that an IP address is assigned to the network interface, two DNS servers assigned, and a default route with a default gateway address is added in the route table.

```
ipconfig /all
route print
```

- Collect the output of the basic connectivity tests in the command prompt. Replace the `default_gateway_address` with the IP address of the assigned default gateway.

```
ping <default_gateway_address>
ping s3.amazonaws.com
tracert s3.amazonaws.com
```

- Collect the output of the HTTPS connectivity test in PowerShell. The following command should show a `HTTP 200 OK` response.

```
Invoke-WebRequest -Uri "https://s3.amazonaws.com/ping"
```

## Network throughput

Network throughput, which measures the actual data transfer rate in a network, can be influenced by various factors. The following may impact your data transfer speeds:

- **Hardware**: The hardware components of the device may cause reduced connection speeds when uploading data. The CPU and disks used in the device could be reaching their performance limits. Consider using NVME SSDs in a RAID array. Make sure you use the AWS CRT library for better performance and to lower CPU usage.
- **Encryption overhead**: Secure transmissions, such as HTTPS, increase processing time due to encryption overhead.
- **Latency**: Latency refers to the time taken for a data packet to travel from source to destination. High latency can be observed when uploading to an Amazon S3 bucket in a different geographic region, which can lead to delays in data transfer and lower throughput. Best practice is to make data transfers within the same region, whenever possible.
- **Packet loss**: Lost packets require retransmission, slowing the data transfer.
