# Granting AWS Resilience Hub access to

resources in your Amazon EKS cluster

AWS Resilience Hub allows you to access resources located on Amazon EKS clusters provided
you have configured the required permissions.

###### To grant required permissions to AWS Resilience Hub for discovering and assessing

resources within Amazon EKS cluster

1. Configure an IAM role to access Amazon EKS cluster.

If you have configured your application using role-based access, you
can skip this step and proceed to step 2 and use the role that you had
used for creating the application. For more information about how
AWS Resilience Hub uses IAM roles, see [How AWS Resilience Hub works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

If you have configured your application using current IAM user
permissions, you must create
`AwsResilienceHubAssessmentEKSAccessRole` IAM role in
the same account as that of the Amazon EKS cluster. This IAM role will then
be used while accessing your Amazon EKS cluster.

While importing and assessing your application, AWS Resilience Hub uses an
IAM role to access the resources in your Amazon EKS cluster. This role
should be created in the same account as your Amazon EKS cluster and it will
be mapped with a Kubernetes group that includes the permissions required
by AWS Resilience Hub to assess your Amazon EKS cluster.

If your Amazon EKS cluster is in the same account as the AWS Resilience Hub calling
account, the role should be created using the following IAM trust
policy. In this IAM trust policy, `caller_IAM_role` is used
in the current account to call the APIs for AWS Resilience Hub.

###### Note

The `caller_IAM_role` is the role that is associated
with your AWS user account.

If your Amazon EKS cluster is in a cross account (a different account than
the AWS Resilience Hub calling account), you must create the
`AwsResilienceHubAssessmentEKSAccessRole` IAM role
using the following IAM trust policy:

###### Note

As a prerequisite, to access Amazon EKS cluster that is deployed in a
different account than the AWS Resilience Hub user’s account, you must
configure multi-account access. For more information, see 2. Create `ClusterRole` and `ClusterRoleBinding`
(or `RoleBinding`) roles for AWS Resilience Hub application.

Creating `ClusterRole` and `ClusterRoleBinding`
will grant the required read-only permissions for AWS Resilience Hub to analyze
and assess resources that are a part of the certain namespaces in your
Amazon EKS cluster.

AWS Resilience Hub enables you to limit its access to your namespaces for
generating resiliency assessments by completing one of the
following:

    1. Grant read access across all namespaces to AWS Resilience Hub
     application.


    For AWS Resilience Hub to assess the resiliency of resources across all
     the namespaces within an Amazon EKS cluster, you must create the
     following `ClusterRole` and
     `ClusterRoleBinding`.




    	* `resilience-hub-eks-access-cluster-role`
    	 (`ClusterRole`) – Defines the
    	 permissions required by AWS Resilience Hub to assess your Amazon EKS
    	 cluster.
    	* `resilience-hub-eks-access-cluster-role-binding`
    	 (`ClusterRoleBinding`) – Defines a
    	 group named `resilience-hub-eks-access-group`
    	 in your Amazon EKS cluster granting its users, the required
    	 permissions to run resiliency assessments in
    	 AWS Resilience Hub.
    The template to grant read access across all namespaces to
     AWS Resilience Hub application is as follows:



    ```

    cat << EOF | kubectl apply -f -
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: resilience-hub-eks-access-cluster-role
    rules:
    - apiGroups:
        - ""
      resources:
        - pods
        - replicationcontrollers
        - nodes
      verbs:
        - get
        - list
    - apiGroups:
        - apps
      resources:
        - deployments
        - replicasets
      verbs:
        - get
        - list
    - apiGroups:
        - policy
      resources:
        - poddisruptionbudgets
      verbs:
        - get
        - list
    - apiGroups:
        - autoscaling.k8s.io
      resources:
        - verticalpodautoscalers
      verbs:
        - get
        - list
    - apiGroups:
        - autoscaling
      resources:
        - horizontalpodautoscalers
      verbs:
        - get
        - list
    - apiGroups:
        - karpenter.sh
      resources:
        - provisioners
        - nodepools
      verbs:
        - get
        - list
    - apiGroups:
        - karpenter.k8s.aws
      resources:
        - awsnodetemplates
        - ec2nodeclasses
      verbs:
        - get
        - list
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: resilience-hub-eks-access-cluster-role-binding
    subjects:
      - kind: Group
        name: resilience-hub-eks-access-group
        apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: ClusterRole
      name: resilience-hub-eks-access-cluster-role
      apiGroup: rbac.authorization.k8s.io
    ---
    EOF

    ```
    2. Granting AWS Resilience Hub the access to read specific
     namespaces.


    You can limit AWS Resilience Hub to access resources within a specific
     set of namespaces using `RoleBinding`. To achieve
     this, you must create the following roles:




    	* `ClusterRole` – For AWS Resilience Hub to
    	 access the resources in specific namespaces within an
    	 Amazon EKS cluster and assess its resiliency, you must create
    	 the following `ClusterRole` roles.




    		+ `resilience-hub-eks-access-cluster-role`
    		 – Specifies the necessary permissions to
    		 assess the resources within specific
    		 namespaces.
    		+ `resilience-hub-eks-access-global-cluster-role`
    		 – Specifies the necessary permissions to
    		 assess cluster-scoped resources, which are not
    		 associated to a specific namespace, within your
    		 Amazon EKS clusters. AWS Resilience Hub requires permissions to
    		 access cluster-scoped resources (such as nodes) on
    		 your Amazon EKS cluster to assess the resiliency of
    		 your application.
    	The template to create `ClusterRole` role
    	 is as follows:



    	```

    	cat << EOF | kubectl apply -f -
    	apiVersion: rbac.authorization.k8s.io/v1
    	kind: ClusterRole
    	metadata:
    	  name: resilience-hub-eks-access-cluster-role
    	rules:
    	  - apiGroups:
    	      - ""
    	    resources:
    	      - pods
    	      - replicationcontrollers
    	    verbs:
    	      - get
    	      - list
    	  - apiGroups:
    	      - apps
    	    resources:
    	      - deployments
    	      - replicasets
    	    verbs:
    	      - get
    	      - list
    	  - apiGroups:
    	      - policy
    	    resources:
    	      - poddisruptionbudgets
    	    verbs:
    	      - get
    	      - list
    	  - apiGroups:
    	      - autoscaling.k8s.io
    	    resources:
    	      - verticalpodautoscalers
    	    verbs:
    	      - get
    	      - list
    	  - apiGroups:
    	      - autoscaling
    	    resources:
    	      - horizontalpodautoscalers
    	    verbs:
    	      - get
    	      - list

    	---
    	apiVersion: rbac.authorization.k8s.io/v1
    	kind: ClusterRole
    	metadata:
    	  name: resilience-hub-eks-access-global-cluster-role
    	rules:
    	  - apiGroups:
    	      - ""
    	    resources:
    	      - nodes
    	    verbs:
    	      - get
    	      - list
    	  - apiGroups:
    	      - karpenter.sh
    	    resources:
    	      - provisioners
    	      - nodepools
    	    verbs:
    	      - get
    	      - list
    	  - apiGroups:
    	      - karpenter.k8s.aws
    	    resources:
    	      - awsnodetemplates
    	      - ec2nodeclasses
    	    verbs:
    	      - get
    	      - list

    	---
    	EOF

    	```
    	* `RoleBinding` role – This role
    	 grants the required permissions for AWS Resilience Hub to access
    	 resources within specific namespaces. That is, you must
    	 create `RoleBinding` role in each namespace
    	 to enable AWS Resilience Hub to access resources within the given
    	 namespace.


    	###### Note

    	If you are using `ClusterAutoscaler`
    	 for autoscaling, you must additionally create
    	 `RoleBinding` in the
    	 `kube-system`. This is necessary to
    	 assess your `ClusterAutoscaler`, which is
    	 a part of the `kube-system`
    	 namespace.

    	By doing this, you will grant AWS Resilience Hub the
    	 required permissions to assess resources inside the
    	 `kube-system` namespace while assessing
    	 your Amazon EKS cluster.


    	The template to create `RoleBinding` role
    	 is as follows:



    	```

    	cat << EOF | kubectl apply -f -
    	apiVersion: rbac.authorization.k8s.io/v1
    	kind: RoleBinding
    	metadata:
    	  name: resilience-hub-eks-access-cluster-role-binding
    	  namespace: <namespace>
    	subjects:
    	  - kind: Group
    	    name: resilience-hub-eks-access-group
    	    apiGroup: rbac.authorization.k8s.io
    	roleRef:
    	  kind: ClusterRole
    	  name: resilience-hub-eks-access-cluster-role
    	  apiGroup: rbac.authorization.k8s.io

    	---
    	EOF

    	```
    	* `ClusterRoleBinding` role – This
    	 role grants the required permissions for AWS Resilience Hub to
    	 access cluster-scoped resources.


    	The template to create `ClusterRoleBinding`
    	 role is as follows:



    	```

    	cat << EOF | kubectl apply -f -
    	---
    	apiVersion: rbac.authorization.k8s.io/v1
    	kind: ClusterRoleBinding
    	metadata:
    	  name: resilience-hub-eks-access-global-cluster-role-binding
    	subjects:
    	  - kind: Group
    	    name: resilience-hub-eks-access-group
    	    apiGroup: rbac.authorization.k8s.io
    	roleRef:
    	  kind: ClusterRole
    	  name: resilience-hub-eks-access-global-cluster-role
    	  apiGroup: rbac.authorization.k8s.io

    	---
    	EOF

    	```

3. Update the `aws-auth ConfigMap` to map the
   `resilience-hub-eks-access-group` with the IAM role
   that is used for accessing Amazon EKS cluster.

This step creates a mapping between the IAM role used in step 1 with
the Kubernetes group created in step 2. This mapping grants permissions
to IAM roles for accessing resources inside the Amazon EKS cluster.

###### Note

    * `ROLE-NAME` refers to the IAM role that is
     used for accessing Amazon EKS cluster.




    	+ If your application is configured to use
    	 role-based access, the role should be either the
    	 invoker role or secondary account role that is
    	 passed to AWS Resilience Hub while creating the
    	 application.
    	+ If your application is configured to use the
    	 current IAM user for accessing resources, it must
    	 be the
    	 `AwsResilienceHubAssessmentEKSAccessRole`.

    * `ACCOUNT-ID` should be the AWS account ID of
     the Amazon EKS cluster.

You can create the `aws-auth`
`ConfigMap` using one of the following ways:

    * Using `eksctl`


    Use the following command to update the `aws-auth`
    `ConfigMap`:



    ```
    eksctl create iamidentitymapping \
     --cluster <cluster-name> \
     --region=<region-code> \
     --arn arn:aws:iam::<ACCOUNT-ID>:role/<ROLE-NAME>\
     --group resilience-hub-eks-access-group \
     --username AwsResilienceHubAssessmentEKSAccessRole
    ```
    * You can manually edit `aws-auth`
    `ConfigMap` by adding the IAM role details to
     `mapRoles` section of the `ConfigMap`
     under data. Use the following command to edit the
     `aws-auth`
    `ConfigMap`.


    `kubectl edit -n kube-system
     configmap/aws-auth`


    `mapRoles` section consists of the following
     parameters:




    	+ `rolearn` – The [Amazon Resource Name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") of the IAM
    	 role to be added.




    		- ARN Syntax –
    		 `arn:aws:iam::<ACCOUNT-ID>:role/<ROLE-NAME>`.
    	+ `username` – The username within
    	 Kubernetes to be mapped to the IAM role
    	 (`AwsResilienceHubAssessmentEKSAccessRole`).
    	+ `groups` – The group names should
    	 match the group names created in **Step 2**
    	 (`resilience-hub-eks-access-group`).
    ###### Note

    If `mapRoles` section does not exist, you must
     manually add this section.


    Use the following template to add the IAM role details to
     `mapRoles` section of the `ConfigMap`
     under data.



    ```
        - groups:
          - resilience-hub-eks-access-group
          rolearn: arn:aws:iam::<ACCOUNT-ID>:role/<ROLE-NAME>
          username: AwsResilienceHubAssessmentEKSAccessRole
    ```
