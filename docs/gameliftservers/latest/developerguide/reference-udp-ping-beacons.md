# Amazon GameLift Servers UDP ping beacons

UDP ping beacons provide a way to measure network latency between player devices and Amazon GameLift Servers
hosting locations. With ping beacons, you can collect accurate latency data to make informed
decisions about game server placement and improve player matchmaking based on latency
requirements.

## How UDP ping beacons work

Amazon GameLift Servers provides fixed UDP endpoints (ping beacons) in each hosting location where you
can deploy game servers. Because most game servers communicate using UDP, measuring
latency with UDP ping beacons provides more accurate results than using ICMP pings. Network
devices often handle ICMP packets differently from UDP packets, which can lead to
latency measurements that don't reflect the true performance your players will
experience.

With UDP ping beacons, your game client can send UDP messages to these endpoints and receive
asynchronous responses, giving you latency measurements that better represent actual
game traffic conditions between a player's device and potential hosting locations. The
endpoints are permanent and remain available as long as Amazon GameLift Servers supports game hosting in
that location.

## Common use cases for

UDP ping beacons

You can use UDP ping beacons in several ways to optimize your game's networking
experience.

###### Choosing optimal hosting locations

Collect latency data across different geographic regions to identify the best
primary and backup locations for hosting game servers for your player base.

###### Placing game sessions based on player latency

Include player latency data when requesting new game sessions to help pick
locations that provide the lowest latency experience.

###### Optimizing matchmaking based on latency

Provide player latency data when requesting matchmaking to help match players with
similar latency profiles and place game sessions in optimal locations for matched
players.

###### Note

When creating matchmaking requests, you should not provide latency information to
locations where you don't have fleets. If you do, Amazon GameLift Servers might try to place the
game session in locations where there's no fleet capacity, resulting in matchmaking
request failures.

## Getting beacon endpoints

To retrieve ping beacon domain and port information for Amazon GameLift Servers locations, use the
[ListLocations](../apireference/API_ListLocations.md "../apireference/API_ListLocations.md") API
operation. The set of locations returned by this API depends on the AWS Region you
specify when calling it (or your default Region if you don't specify one). When
you call from:

- **A home Region of a fleet that supports
  multi-locations**: API returns information for
  _all_ hosting locations
- **A home Region of a fleet that supports a single
  location**: API returns information for that location

Note that if you call this API using a location that can only be a remote location in
a multi-location fleet, the API will return an error because that type of location doesn't
have a service endpoint.

Consult the table of supported locations in [Supported AWS locations](gamelift-regions.md#gamelift-regions-hosting-home "gamelift-regions.md#gamelift-regions-hosting-home") to identify home Regions that
support single and multi-location fleets.

**Example**

```
aws gamelift list-locations --region ap-northeast-2
```

This AWS Region supports multi-location fleets, therefore multiple locations will be
returned. Here is an example of one of the return values:

```
[...]
{
    "LocationName": "ap-northeast-1",
    "PingBeacon": {
        "UDPEndpoint": {
            "Domain": "gamelift-ping.ap-northeast-1.api.aws",
            "Port": 7770
        }
    }
}
```

###### Important

Cache the ping beacon information rather than calling `ListLocations`
before each latency measurement. The domain and port information are static and
the API isn't designed for high-volume requests.

## Implementing latency

measurements

Follow these best practices when implementing latency measurements using
UDP ping beacons:

1. Store ping beacon information using one of these approaches:
   - Hardcode the endpoints in your game client.
   - Cache the information in your game backend.
   - Implement a periodic update mechanism (daily/weekly) to refresh the
     information.

2. Send UDP ping messages:
   - Put whatever you want in the message body, as long as it is not empty,
     and you keep messages under the maximum size of 300 bytes.
   - Observe the following rate limits for each location:
     - 3 transactions per second (TPS) per unique sender IP address
       and port combination
     - 1000 TPS per unique sender IP address

3. Calculate latency:
   - Send multiple pings to each location to calculate an average
     latency.
   - Consider sending concurrent pings to multiple locations for faster
     results.
   - Use retry logic as needed to send new packets for any packet that
     wasn’t returned within a short time (typically 1 - 3 seconds), since UDP
     does not have 100% guaranteed delivery.
   - Calculate the time difference between sending a message and receiving
     the response.
   - If a large portion of UDP pings to a location consistently do not get
     a response back, calculate latency using ICMP pings to our standard
     [Amazon GameLift Servers service
     endpoints](../../../general/latest/gr/gamelift.md#gamelift_region "../../../general/latest/gr/gamelift.md#gamelift_region") as a fallback.

###### Tip

We recommend that you include port 7770 wherever you document the list of ports
that your players must have open on their local network. This is another reason why
you should have a fallback for measuring latency (using ICMP, for example) in case
this port is blocked.

## Code examples

Here are some simple examples showing how to send UDP pings and calculate latency.

C++

```
#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <chrono>

int main() {
    // Replace with Amazon GameLift Servers UDP ping beacon domain for your desired location
    const char* domain = "gamelift-ping.ap-south-1.api.aws";
    const int port = 7770;
    const char* message = "Ping";        // Your message
    const int num_pings = 3;             // Number of pings to send

    // Create socket
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    }

    // Resolve domain name to IP address
    struct hostent* host = gethostbyname(domain);
    if (host == nullptr) {
        std::cerr << "Error resolving hostname" << std::endl;
        close(sock);
        return 1;
    }

    // Set up the server address structure
    struct sockaddr_in server_addr;
    std::memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    std::memcpy(&server_addr.sin_addr, host->h_addr, host->h_length);

    // Set socket timeout
    struct timeval tv;
    tv.tv_sec = 1;  // 1 second timeout
    tv.tv_usec = 0;
    if (setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv)) < 0) {
        std::cerr << "Error setting socket timeout" << std::endl;
        close(sock);
        return 1;
    }

    double total_latency = 0;
    int successful_pings = 0;

    for (int i = 0; i < num_pings; ++i) {
        auto start = std::chrono::high_resolution_clock::now();

        // Send the message
        ssize_t bytes_sent = sendto(sock, message, std::strlen(message), 0,
                                    (struct sockaddr*)&server_addr, sizeof(server_addr));

        if (bytes_sent < 0) {
            std::cerr << "Error sending message" << std::endl;
            continue;
        }

        // Receive response
        char buffer[1024];
        socklen_t server_addr_len = sizeof(server_addr);
        ssize_t bytes_received = recvfrom(sock, buffer, sizeof(buffer), 0,
                                          (struct sockaddr*)&server_addr, &server_addr_len);

        auto end = std::chrono::high_resolution_clock::now();

        if (bytes_received < 0) {
            std::cerr << "Error receiving response or timeout" << std::endl;
        } else {
            std::chrono::duration<double, std::milli> latency = end - start;
            total_latency += latency.count();
            successful_pings++;

            std::cout << "Received response, latency: " << latency.count() << " ms" << std::endl;
        }

        // Wait a bit before next ping
        usleep(1000000);  // 1s
    }

    // Close the socket
    close(sock);

    if (successful_pings > 0) {
        double avg_latency = total_latency / successful_pings;
        std::cout << "Average latency: " << avg_latency << " ms" << std::endl;
    } else {
        std::cout << "No successful pings" << std::endl;
    }

    return 0;
}
```

C#

```
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Diagnostics;
using System.Threading.Tasks;

class UdpLatencyTest
{
    static async Task Main()
    {
        // Replace with Amazon GameLift Servers UDP ping beacon domain for your desired location
        string domain = "gamelift-ping.ap-south-1.api.aws";
        int port = 7770;
        string message = "Ping";         // Your message
        int numPings = 3;                // Number of pings to send
        int timeoutMs = 1000;            // Timeout in milliseconds

        await MeasureLatency(domain, port, message, numPings, timeoutMs);
    }

    static async Task MeasureLatency(string domain, int port, string message, int numPings, int timeoutMs)
    {
        using (var udpClient = new UdpClient())
        {
            try
            {
                // Resolve domain name to IP address
                IPAddress[] addresses = await Dns.GetHostAddressesAsync(domain);
                if (addresses.Length == 0)
                {
                    Console.WriteLine("Could not resolve domain name.");
                    return;
                }

                IPEndPoint endPoint = new IPEndPoint(addresses[0], port);
                byte[] messageBytes = Encoding.UTF8.GetBytes(message);

                // Set receive timeout
                udpClient.Client.ReceiveTimeout = timeoutMs;

                double totalLatency = 0;
                int successfulPings = 0;
                var stopwatch = new Stopwatch();

                for (int i = 0; i < numPings; i++)
                {
                    try
                    {
                        stopwatch.Restart();

                        // Send message
                        await udpClient.SendAsync(messageBytes, messageBytes.Length, endPoint);

                        // Wait for response
                        UdpReceiveResult result = await ReceiveWithTimeoutAsync(udpClient, timeoutMs);

                        stopwatch.Stop();
                        double latency = stopwatch.Elapsed.TotalMilliseconds;

                        totalLatency += latency;
                        successfulPings++;

                        string response = Encoding.UTF8.GetString(result.Buffer);
                        Console.WriteLine($"Ping {i + 1}: {latency:F2}ms - Response: {response}");
                    }
                    catch (SocketException ex)
                    {
                        Console.WriteLine($"Ping {i + 1}: Failed - {ex.Message}");
                    }
                    catch (TimeoutException)
                    {
                        Console.WriteLine($"Ping {i + 1}: Timeout");
                    }

                    // Wait before next ping
                    await Task.Delay(1000); // 1s between pings
                }

                if (successfulPings > 0)
                {
                    double averageLatency = totalLatency / successfulPings;
                    Console.WriteLine($"\nSummary:");
                    Console.WriteLine($"Successful pings: {successfulPings}/{numPings}");
                    Console.WriteLine($"Average latency: {averageLatency:F2}ms");
                }
                else
                {
                    Console.WriteLine("\nNo successful pings");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }

    static async Task<UdpReceiveResult> ReceiveWithTimeoutAsync(UdpClient client, int timeoutMs)
    {
        using var cts = new System.Threading.CancellationTokenSource(timeoutMs);
        try
        {
            return await client.ReceiveAsync().WaitAsync(cts.Token);
        }
        catch (OperationCanceledException)
        {
            throw new TimeoutException("Receive operation timed out");
        }
    }
}
```

Python

```
import socket
import time
import statistics
from datetime import datetime

def udp_ping(host, port, timeout=2):
    """
    Send a UDP ping and return the round trip time in milliseconds.
    Returns None if timeout occurs.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    message = b'ping'

    try:
        # Resolve hostname first
        try:
            socket.gethostbyname(host)
        except socket.gaierror as e:
            print(f"Could not resolve hostname: {e}")
            return None

        start_time = time.time()
        sock.sendto(message, (host, port))

        # Wait for response
        data, server = sock.recvfrom(1024)
        end_time = time.time()

        # Calculate round trip time in milliseconds
        rtt = (end_time - start_time) * 1000
        return rtt

    except socket.timeout:
        print(f"Request timed out")
        return None
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        return None
    finally:
        sock.close()

def main():
    # Replace with Amazon GameLift Servers UDP ping beacon domain for your desired location
    host = "gamelift-ping.ap-south-1.api.aws"
    port = 7770
    num_pings = 3
    latencies = []

    print(f"\nPinging {host}:{port} {num_pings} times...")
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    for i in range(num_pings):
        print(f"Ping {i+1}:")
        rtt = udp_ping(host, port)

        if rtt is not None:
            print(f"Response from {host}: time={rtt:.2f}ms")
            latencies.append(rtt)

        # Wait 1 second between pings
        if i < num_pings - 1:
            time.sleep(1)
        print()

    # Calculate and display statistics
    print("-" * 50)
    print(f"Ping statistics for {host}:")
    print(f"    Packets: Sent = {num_pings}, Received = {len(latencies)}, "
          f"Lost = {num_pings - len(latencies)} "
          f"({((num_pings - len(latencies)) / num_pings * 100):.1f}% loss)")

    if latencies:
        print("\nRound-trip latency statistics:")
        print(f"    Minimum = {min(latencies):.2f}ms")
        print(f"    Maximum = {max(latencies):.2f}ms")
        print(f"    Average = {statistics.mean(latencies):.2f}ms")

    print(f"\nEnd time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
```
