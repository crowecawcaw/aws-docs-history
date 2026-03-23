# Starting a practice run zonal shift

The steps in this section explain how to start an on-demand practice run zonal shift on the ARC console.
To work with zonal shift and zonal autoshift programmatically, see the [Zonal Shift and Zonal Autoshift API Reference Guide](../../../arc-zonal-shift/latest/api/Welcome.md "../../../arc-zonal-shift/latest/api/Welcome.md").

You can start a practice run zonal shift after you configure zonal autoshift and create a practice run configuration.

# To start a practice run zonal shift

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/](https://console.aws.amazon.com/route53recovery/zonalshift/home#/ "https://console.aws.amazon.com/route53recovery/zonalshift/home#/").
2. Under **Zonal autoshift resources**, browse to an individual resource that has zonal autoshift
   configured.
3. On the **Resource overview** page, choose **Start practice run**.
4. Select an Availability Zone, and then enter a comment for your practice run. The practice run will shift traffic
   away from the Availability Zone that you selected.
5. Choose **Start**.
