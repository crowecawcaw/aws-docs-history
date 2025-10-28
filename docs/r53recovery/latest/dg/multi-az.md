# Use zonal shift and zonal autoshift to recover applications in ARC

This section explains how to use capabilities in Amazon Application Recovery Controller (ARC) to reliably recover your AWS
resource from an issue in an impaired Availability Zone (AZ). Zonal shift and zonal
autoshift temporarily shift the traffic for a supported resource away from an impaired AZ,
which reduces time to recovery for your applications.

The primary difference between zonal shift and zonal autoshift is that one is a manual traffic shift that you control,
and the other shifts traffic away from an impairment automatically on your behalf.

- With zonal shift, you manually shift traffic for a supported resource in an AWS Region away
  from an Availability Zone.
- With zonal autoshift, the traffic for a supported resource is automatically shifted away from
  an impaired AZ and rerouted to healthy AZs in the same AWS Region.
  The following topics describe the zonal shift and zonal autoshift capabilities, and how to use them.

###### Topics

- [Zonal shift in ARC](arc-zonal-shift.md "arc-zonal-shift.md")
- [Zonal autoshift in ARC](arc-zonal-autoshift.md "arc-zonal-autoshift.md")
