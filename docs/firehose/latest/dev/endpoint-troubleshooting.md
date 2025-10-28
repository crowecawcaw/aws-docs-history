# Troubleshooting Firehose endpoint

reachability

If the Firehose API encounters a timeout, perform the following steps to test endpoint reachability:

- Check if API requests are made from a host in a VPC. All traffic from a VPC requires setting up a Firehose VPC endpoint. For more information, see [Using Firehose with AWS PrivateLink](vpc.md "vpc.md").
- If traffic is coming from a public network or VPC with the Firehose VPC endpoint set up in a particular subnet, run the following commands from the host to check network connectivity.
  The Firehose endpoint can be found at [Firehose endpoints and quotas](../../../general/latest/gr/fh.md "../../../general/latest/gr/fh.md").

      + Use tools like **traceroute** or **tcping** to check if the network setup is correct. If that fails, check your network setting:


      For example:



      ```
      traceroute firehose.us-east-2.amazonaws.com
      ```

      or



      ```
      tcping firehose.us-east-2.amazonaws.com 443
      ```
      + If it appears the network setting is correct and the following command fails, check whether the [Amazon CA (Certficate Authority)](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md") is in the trust chain.


      For example:



      ```
      curl firehose.us-east-2.amazonaws.com
      ```

  If the above commands succeed, try the API again to see if there is a response returned from the API.
