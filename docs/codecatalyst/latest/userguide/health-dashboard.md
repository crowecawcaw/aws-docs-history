Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Understanding current service status with the CodeCatalyst health report

The Amazon CodeCatalyst health report is a public dashboard that provides users with an aggregated
list of up-to-the-minute notifications regarding resource performance and availability of
services in CodeCatalyst that have widespread impact. You can see which resources are having
problems and may affect applications in CodeCatalyst. This allows you to track outages and other
resource downtime system wide. When an incident occurs, a blue indicator appears on the
health report icon. Additionally, CodeCatalyst automatically sends an alert and email notification
to all users with the **Space administrator** role in the project, providing
details and a history of the incident in near real time.

The dashboard provides a list of all active events and a record of up to 100 previous
incidents occurring in the last 30 days. You can organize the list of incidents based on the
date the incident was updated. You can also refresh the list of incidents for up to the
minute updates.

Here is a possible workflow for using the CodeCatalyst health report:

Mateo Jackson is a developer in the Budding Space with Space administrator
permissions. While attempting to create a pull request, he keeps getting an error message.
He checks his email and discovers he received an auto-generated system incident email from
CodeCatalyst providing a detailed history about the system issue affecting his space. He
chooses **View update** and is taken to the CodeCatalyst health report where he
can view all system-reported incidents. He chooses the incident from the list to find out
more information. A split screen opens that provides a timestamp of the last update,
history, impacted capabilities, start time, and current status of the incident. He can also
see that the issue is ongoing, but the service team has begun working on it. Each time there
is an update to the history or status of the incident, he receives an email. In the event
that he does not have access to his email, he can choose the bell icon in the top panel to
get to the CodeCatalyst health report.

## CodeCatalyst health report concepts

Learning the following concepts will help you understand the CodeCatalyst health report and
how they enable you to track the health of your applications, services, and
resources.

### Incident

The _incident_ is the system event that is affecting
applications and resources within CodeCatalyst. You can choose the incident to view a
detailed history of the event, including the time it began and if the service team
is working on resolving it.

### Status

The _status_ is the real-time status of the incident. It will
show as **Ongoing** or **Resolved**.

### Impacted capabilities

The _impacted capabilities_ are the resources or applications affected by the incident. A single incident can affect multiple areas in the system, including **pull requests**, **issues**, **workflows**, **test**, **deploy**, and **source**.

### Updated on

_Updated on_ provides a timestamp of the last update for the incident.
