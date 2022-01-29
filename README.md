# riverbank_test

### The app
Flask App runs on a docker container. 
The app uses an environment varibale which to be set using a configmap.

### The Reverse Proxy (nginx)
Nginx proxy listening on LoadBalancer service forward requests to based on location /develop /qa /prod
Nginx configuration is set using a configmap

### Kubernetes Cluster
2 nodes running on GKE cluster 
3 environments/namespaces (develop, qa, prod)
Helm template to use the same kubernetes manifests with different values for each {{ .Release.Namespace }}  and {{ .Values. }}
Envrionment variable to distinguish between the environments


Todo
Add github-action.yaml pipeline and use the release tag as a value for the image tag 
github_tag ==> github_release ==> image_tag ==> helm_release 
Update nginx configuration using Helm

### Tree of the project
```
├── Dockerfile # Dockerfile of the python app
├── app # the folder of the flask app
│   ├── app.py # app running on default port (5000)
│   └── requirements.txt # installes requirements during image build
├── manifests
│   ├── nginx-configmap.yaml
│   ├── nginx-deployment.yaml
│   └── nginx-service.yaml
└── riverbank
    ├── Chart.yaml
    ├── charts
    ├── templates
    │   ├── configmap.yaml
    │   ├── deployment.yaml
    │   └── service.yaml
    ├── values-prod.yaml
    ├── values-qa.yaml
    └── values.yaml
```


### Commands 

```helm upgrade riverbank -f ./riverbank/values-prod.yaml ./riverbank/ --dry-run``` 
```kubectl create service loadbalancer nginx --tcp=80:80 --node-port=30080 --dry-run=client -o yaml```
```kubectl create deploy riverbank --image=riverbank:v0.1.0 --dry-run=client -o yaml```
```kubectl create service clusterip riverbank --tcp=5000:5000 --dry-run=client -oyaml```
