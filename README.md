# mlPipes

Information about creating ML Pipelines using kubernetes

## 1. Make sure that the docker stuff is working

1. Create a docker container that writes data to a docker volume (`docker build -t write-data:0.01 .` within `writeData`)
2. Create a docker container that reads data from a docker volume (`docker build -t read-data:0.01 .` within `readData`)
3. Cretae a docker volume `docker volume create test-volume`
4. write data within the volume `docker run -v test-volume:/data write-data:0.01`
5. read data within the volume `docker run -v test-volume:/data read-data:0.01`

If we are able to read the data properly, we know that we are ready to get to the next stage ...

## 2. Start working on minikube

Allow ECR to be used ...

The information in the following location may be used:
 - https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/


In a particular terminal, run (`eval (minikube docker-env)`). This is going to allow you to run all docker
commands within your minikube cluster. Being able to do this is critical.

https://minikube.sigs.k8s.io/docs/handbook/pushing/
https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube/42564211#42564211

For this, check the specific information within ECR
`kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>`




1. Install Minikube
1. Create a `pv` (persistant volume) (`kubectl apply -f configs/ai-volume.yaml`)
2. Create a `pvc` (persistant volume claim) () 


aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 387826921024.dkr.ecr.ap-southeast-1.amazonaws.com

# References

1. [Minikube installation](https://www.notion.so/Minikube-423387aee1d247d8a136eaf1fb673678)


1. Getting a shell: 
    https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/
1. Deleting a stateful set
    https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application/
2. Diagnosing pods:
    https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application/

1. Persistent volumes
    https://kubernetes.io/docs/concepts/storage/persistent-volumes/
1. Kubernetes Volumes discussion (stackoverflow)
    https://stackoverflow.com/questions/44891319/kubernetes-persistent-volume-claim-indefinitely-in-pending-state
1. Even more persistent volumes
    https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/
1. Minikube persistent volumes
    https://minikube.sigs.k8s.io/docs/handbook/persistent_volumes/


1. Pull Image from a private repository
    https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
1. Pull data form private registries
    https://www.digitalocean.com/community/questions/do-k8s-pull-from-private-registry
1. More troubleshooting with registries
    https://medium.com/@xynova/keeping-aws-registry-pull-credentials-fresh-in-kubernetes-2d123f581ca6
1. Even more troubleshooting
    https://aws.amazon.com/premiumsupport/knowledge-center/eks-ecr-troubleshooting/

1. Troubleshooting problem pods
    https://managedkube.com/kubernetes/k8sbot/troubleshooting/imagepullbackoff/2019/02/23/imagepullbackoff.html
        


