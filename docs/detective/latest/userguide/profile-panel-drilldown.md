# Exploring activity details on a profile panel

During an investigation, you might want to investigate further into the pattern of activity
for an entity.

On the following profile panels, you can display a summary of the activity details:

- **Overall API call volume**, except for the profile panel on the user
  agent profile
- **Newly observed geolocations**
- **Overall VPC flow volume**
- **VPC flow volume to and from the finding IP address**, for findings that
  are associated with a single IP address
- **Container details**
- **VPC flow volume** for clusters
- **Overall Kubernetes API activity**
  The activity details can answer these types of questions:

- Which IP addresses were used?
- Where were those IP addresses located?
- Which API calls did each IP address make, and from which services did they make those
  calls?
- Which principals or access key identifiers (AKIDs) were used to make the calls?
- What resources were used to make those calls?
- How many calls were made? How many succeeded and failed?
- What volume of VPC flow log data was sent to or from each IP address?
- What containers were active for a given cluster, image, or pod?

###### Topics

- [Activity details for Overall API
  call volume](profile-panel-drilldown-overall-api-volume.md "profile-panel-drilldown-overall-api-volume.md")
- [Activity details for a
  geolocation](profile-panel-drilldown-new-geolocations.md "profile-panel-drilldown-new-geolocations.md")
- [Activity details for overall VPC
  flow volume](profile-panel-drilldown-overall-vpc-volume.md "profile-panel-drilldown-overall-vpc-volume.md")
- [Overall Kubernetes API activity involving EKS cluster](profile-panel-drilldown-kubernetes-api-volume.md "profile-panel-drilldown-kubernetes-api-volume.md")
