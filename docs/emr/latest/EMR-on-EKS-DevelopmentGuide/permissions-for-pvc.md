# Troubleshooting jobs that use

PersistentVolumeClaims (PVC)

If you need to create, list, or delete PersistentVolumeClaims (PVC) for a job but
don't add PVC permissions to the default Kubernetes role
_emr-containers_, the job fails when you submit it. Without these
permissions, the _emr-containers_ role can’t create necessary roles
for the Spark driver or Spark client. It isn't enough to add permissions to the Spark
driver or client roles, as suggested by error messages. The
_emr-containers_ primary role must include the required
permissions also. This section explains how to add the required permissions to the
_emr-containers_ primary role.

## Verification

To verify whether or not your _emr-containers_ role has the
necessary permissions, set the NAMESPACE variable with your own value and then run
the following command:

```
export NAMESPACE=YOUR_VALUE
kubectl describe role emr-containers -n ${NAMESPACE}
```

In addition, to verify whether the Spark and client roles have the necessary
permissions, run the following command:

```
kubectl describe role emr-containers-role-spark-driver -n ${NAMESPACE}
kubectl describe role emr-containers-role-spark-client -n ${NAMESPACE}
```

If the permissions aren’t there, proceed with the patch, as follows.

## Patch

1. If the jobs without the permissions are currently running, stop these
   jobs.
2. Create a file named _RBAC_Patch.py_ as
   follows:

```
import os
import subprocess as sp
import tempfile as temp
import json
import argparse
import uuid

def delete_if_exists(dictionary: dict, key: str):
    if dictionary.get(key, None) is not None:
        del dictionary[key]

def doTerminalCmd(cmd):
    with temp.TemporaryFile() as f:
        process = sp.Popen(cmd, stdout=f, stderr=f)
        process.wait()
        f.seek(0)
        msg = f.read().decode()
    return msg

def patchRole(roleName, namespace, extraRules, skipConfirmation=False):
    cmd = f"kubectl get role {roleName} -n {namespace} --output json".split(" ")
    msg = doTerminalCmd(cmd)
    if "(NotFound)" in msg and "Error" in msg:
        print(msg)
        return False
    role = json.loads(msg)
    rules = role["rules"]
    rulesToAssign = extraRules[::]
    passedRules = []
    for rule in rules:
        apiGroups = set(rule["apiGroups"])
        resources = set(rule["resources"])
        verbs = set(rule["verbs"])
        for extraRule in extraRules:
            passes = 0
            apiGroupsExtra = set(extraRule["apiGroups"])
            resourcesExtra = set(extraRule["resources"])
            verbsExtra = set(extraRule["verbs"])
            passes += len(apiGroupsExtra.intersection(apiGroups)) >= len(apiGroupsExtra)
            passes += len(resourcesExtra.intersection(resources)) >= len(resourcesExtra)
            passes += len(verbsExtra.intersection(verbs)) >= len(verbsExtra)
            if passes >= 3:
                if extraRule not in passedRules:
                    passedRules.append(extraRule)
                    if extraRule in rulesToAssign:
                        rulesToAssign.remove(extraRule)
                break
    prompt_text = "Apply Changes?"
    if len(rulesToAssign) == 0:
        print(f"The role {roleName} seems to already have the necessary permissions!")
        prompt_text = "Proceed anyways?"
    for ruleToAssign in rulesToAssign:
        role["rules"].append(ruleToAssign)
    delete_if_exists(role, "creationTimestamp")
    delete_if_exists(role, "resourceVersion")
    delete_if_exists(role, "uid")
    new_role = json.dumps(role, indent=3)
    uid = uuid.uuid4()
    filename = f"Role-{roleName}-New_Permissions-{uid}-TemporaryFile.json"
    try:
        with open(filename, "w+") as f:
            f.write(new_role)
            f.flush()
        prompt = "y"
        if not skipConfirmation:
            prompt = input(
                doTerminalCmd(f"kubectl diff -f {filename}".split(" ")) + f"\n{prompt_text} y/n: "
            ).lower().strip()
            while prompt != "y" and prompt != "n":
                prompt = input("Please make a valid selection. y/n: ").lower().strip()
        if prompt == "y":
            print(doTerminalCmd(f"kubectl apply -f {filename}".split(" ")))
    except Exception as e:
        print(e)
    os.remove(f"./{filename}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--namespace",
                        help="Namespace of the Role. By default its the VirtualCluster's namespace",
                        required=True,
                        dest="namespace"
                        )

    parser.add_argument("-p", "--no-prompt",
                        help="Applies the patches without asking first",
                        dest="no_prompt",
                        default=False,
                        action="store_true"
                        )
    args = parser.parse_args()

    emrRoleRules = [
        {
            "apiGroups": [""],
            "resources": ["persistentvolumeclaims"],
            "verbs": ["list", "create", "delete", "patch"]
         }

    ]

    driverRoleRules = [
        {
            "apiGroups": [""],
            "resources": ["persistentvolumeclaims"],
            "verbs": ["list", "create", "delete", "patch", "deletecollection"]
        },
        {
            "apiGroups": [""],
            "resources": ["services"],
            "verbs": ["get", "list", "describe", "create", "delete", "watch", "deletecollection"]
        },
        {
            "apiGroups": [""],
            "resources": ["configmaps", "pods"],
            "verbs": ["deletecollection"]
        }
    ]

    clientRoleRules = [
        {
            "apiGroups": [""],
            "resources": ["persistentvolumeclaims"],
            "verbs": ["list", "create", "delete", "patch"]
        }
    ]

    patchRole("emr-containers", args.namespace, emrRoleRules, args.no_prompt)
    patchRole("emr-containers-role-spark-driver", args.namespace, driverRoleRules, args.no_prompt)
    patchRole("emr-containers-role-spark-client", args.namespace, clientRoleRules, args.no_prompt)

```

3. Run the Python script:

```
python3 RBAC_Patch.py -n ${NAMESPACE}
```

4. A kubectl diff between the new permissions and the old ones appears. Press
   y to patch the role.
5. Verify the three roles with additional permissions as follows:

```
kubectl describe role -n ${NAMESPACE}
```

6. Run the python script:

```
python3 RBAC_Patch.py -n ${NAMESPACE}
```

7. After running the command, it will show a kubectl diff between the new
   permissions and the old ones. Press y to patch the role.
8. Verify the three roles with additional permissions:

```
kubectl describe role -n ${NAMESPACE}
```

9. Submit the job again.

## Manual patch

If the permission that your application requires applies to something other than
the PVC rules, you can manually add Kubernetes permissions for your Amazon EMR virtual
cluster as needed.

###### Note

The role _emr-containers_ is a primary role. This means
that it must provide all the necessary permissions before you can change your
underlying driver or client roles.

1. Download the current permissions into yaml files by running the commands
   below:

```
kubectl get role -n ${NAMESPACE} emr-containers -o yaml >> emr-containers-role-patch.yaml
kubectl get role -n ${NAMESPACE} emr-containers-role-spark-driver -o yaml >> driver-role-patch.yaml
kubectl get role -n ${NAMESPACE} emr-containers-role-spark-client -o yaml >> client-role-patch.yaml
```

2. Based on the permission your application requires, edit each file and add
   additional rules such as the following:
   - emr-containers-role-patch.yaml

   ```
   - apiGroups:
     - ""
     resources:
     - persistentvolumeclaims
     verbs:
     - list
     - create
     - delete
     - patch
   ```

   - driver-role-patch.yaml

   ```
   - apiGroups:
     - ""
     resources:
     - persistentvolumeclaims
     verbs:
     - list
     - create
     - delete
     - patch
     - deletecollection
   - apiGroups:
     - ""
     resources:
     - services
     verbs:
     - get
     - list
     - describe
     - create
     - delete
     - watch
     - deletecollection
   - apiGroups:
     - ""
     resources:
     - configmaps
     - pods
     verbs:
     - deletecollection

   ```

   - client-role-patch.yaml

   ```
   - apiGroups:
     - ""
     resources:
     - persistentvolumeclaims
     verbs:
     - list
     - create
     - delete
     - patch
   ```

3. Remove the following attributes with their values. This is necessary to
   apply the update.
   - creationTimestamp
   - resourceVersion
   - uid

4. Finally, run the patch:

```
kubectl apply -f emr-containers-role-patch.yaml
kubectl apply -f driver-role-patch.yaml
kubectl apply -f client-role-patch.yaml
```
