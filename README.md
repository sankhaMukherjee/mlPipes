# mlPipes

Information about creating ML Pipelines using kubernetes

# 1. Docker: Make sure that the docker stuff is working

1. Create a docker container that writes data to a docker volume (`docker build -t write-data:0.01 .` within `writeData`)
2. Create a docker container that reads data from a docker volume (`docker build -t read-data:0.01 .` within `readData`)
3. Cretae a docker volume `docker volume create test-volume`
4. write data within the volume `docker run -v test-volume:/data write-data:0.01`
5. read data within the volume `docker run -v test-volume:/data read-data:0.01`

If we are able to read the data properly, we know that we are ready to get to the next stage ...

# 2. Minikube: Start working on minikube

1. Install Minikube
1. Create a `pv` (persistant volume) (`kubectl apply -f configs/ai-volume.yaml`)
2. Create a `pvc` (persistant volume claim) (`kubectl apply -f configs/ai-volume-claim.yaml`) 
3. Put the docker as the minikube doccker in the docker in the current terminal (`eval (minikube docker-env)`)
4. build the docker image for writing data: (`docker build -t write-data:0.01 .` within `writeData`)
5. build the docker image for reading data: (`docker build -t write-data:0.01 .` within `writeData`)
6. Write data to the persistent volume claim (`kubectl apply -f configs/writeDeployment.yaml`)
7. Check that the data is written (`kubectl logs <write-data-name-of-pod>`)
8. Read data from the persistent volume claim (`kubectl apply -f configs/readDeployment.yaml`)
9. Check that the data is written (`kubectl logs <read-data-name-of-pod>`)



----
# 4. Local Kubeflow

## 4.1. deploy kubeflow pipelines on a local cluster

1. Use `kind` : `brew install kind`
2. Install kubeflow
    ```
    export PIPELINE_VERSION=1.4.1
    kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
    kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
    kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
    ```
3. Make sure that all pods have started -> `watch -n 0.5 kubectl get pods --all-namespaces`
4. Forward the port `kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80`
5. Go to `120.0.0.1:8080` on your browser to see the kubectl dashboard

## 4.2. Lightweight Python components

Generate lightweight python components using the kfp pipes API

2. Install a virtual environment 

```bash
python3 -m venv env
source env/bin/activate.fish
pip3 install --upgrade pip
pip3 install numpy
pip3 install jupyter notebook
pip3 install kfp
```

3. Run a pipeline `python3 kfpLightComponents/test_001.py`

Result: 
`RunPipelineResult(run_id=e4676be1-5af5-4f6f-a30b-7c7170e4934a)`


## Reference:
https://www.kubeflow.org/docs/components/pipelines/installation/localcluster-deployment/





# 3. Kubeflow

0. restart minikube with the right resources

`minikube start --cpus 4 --memory 8096 --disk-size=40g`  --> This is giving some problem (not enough resources for dicker)

1. Install kubeflow
   1.1. Download the required `tar` file
   1.2. Unzip the file, and put it in a good location
   1.3. set the paths to `kfctl`, the base folder, and the kubeflow folder

`set -x PATH $PATH /Users/sankhamukherjee/Documents/installers/kubeflow/`
`set -x BASE_DIR /Users/sankhamukherjee/Documents/installers/kubeflow/`
`set -x KF_DIR /Users/sankhamukherjee/Documents/installers/kubeflow/kf-test`

2. Set up kubeflow

`kfctl apply -V -f https://raw.githubusercontent.com/kubeflow/manifests/v1.2-branch/kfdef/kfctl_k8s_istio.v1.2.0.yaml`

WARN[0613] Encountered error applying application kubeflow-apps:  (kubeflow.error): Code 500 with message: Apply.Run : error when creating "/tmp/kout348277295": Internal error occurred: failed calling webhook "webhook.cert-manager.io": the server is currently unable to handle the request  filename="kustomize/kustomize.go:284

## 2.1. Minikube Reference

Allow ECR to be used ...

The information in the following location may be used:
 - https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/


In a particular terminal, run (`eval (minikube docker-env)`). This is going to allow you to run all docker
commands within your minikube cluster. Being able to do this is critical.

https://minikube.sigs.k8s.io/docs/handbook/pushing/
https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube/42564211#42564211
https://github.com/kubernetes/minikube/blob/0c616a6b42b28a1aab8397f5a9061f8ebbd9f3d9/README.md#reusing-the-docker-daemon
https://medium.com/bb-tutorials-and-thoughts/how-to-use-own-local-doker-images-with-minikube-2c1ed0b0968
https://minikube.sigs.k8s.io/docs/handbook/pushing/
https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/

For this, check the specific information within ECR
`kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>`

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
        


