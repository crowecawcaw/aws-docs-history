# Use indicators of compromise (IOCs)

An _indicator of compromise_ (IOC) is an artifact observed
in or on a network, system, or environment that can (with a high level of confidence)
identify malicious activity or a security incident. IOCs can exist in a variety of
forms, including IP addresses, domains, network-level artifacts such as TCP
flags or payloads, system or host-level artifacts such as executables, file
names and hashes, log file entries, or registry entries, and more. They can
also be a combination of items or activities, such as the existence of specific
items or artifacts on a system (a certain file or set of files and registry items),
actions performed in certain order (a login to a system from a certain IP followed
by specific anomalous commands), or network activity (anomalous inbound or
outbound traffic to or from certain domains) that can indicate a specific
threat, attack, or attacker methodology.

As you work to iteratively improve your incident response program, you should
implement a framework to collect, manage, and utilize IOCs as a mechanism to
continuously build and improve detections and alerting and improve the speed
and efficacy of investigations. You can start by incorporating the collection
and management of IOCs into the analysis and investigation phases of your
incident response processes. By proactively identifying, collecting, and storing
IOCs as a standard part of your process, you can build a repository of data
(as part of a more comprehensive threat intelligence program) that in turn can
be used to improve existing detections and alerts, build additional detections
and alerts, identify where and when an artifact was seen before, build and
reference documentation of how investigations were previously done involving
matching IOCs, and more.
