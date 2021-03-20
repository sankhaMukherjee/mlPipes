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

1. Install Minikube
1. Create a `pv` (persistant volume) (`kubectl apply -f configs/ai-volume.yaml`)
2. Create a `pvc` (persistant volume claim) () 




# References

1. [Minikube installation](https://www.notion.so/Minikube-423387aee1d247d8a136eaf1fb673678)
