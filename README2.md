### Assignment 3 Instructions
## Haseeb Tahir 10190846


- Navigate to the Assignment3 Directory 

```bash
cd assignment3
```
<img width="782" alt="Screenshot 2024-04-07 at 11 20 41 PM" src="https://github.com/thisdontw0rk/pop/assets/144601350/31c7f99a-565e-41bb-b699-d0fc85f92ba3">


- Then Run the Following Commands In Order:

```bash
minikube start
minikube addons enable ingress
kubectl apply -f '*.yaml'
curl http://$(minikube ip)/

```

Or You May Individually Run Each File:
```bash
kubectl apply -f nginx-dep.yaml
kubectl apply -f nginx-configmap.yaml
kubectl apply -f nginx-svc.yaml
kubectl apply -f nginx-ingress.yaml 
kubectl apply -f app-1-dep.yaml
kubectl apply -f app-1-svc.yaml
kubectl apply -f app-1-ingress.yaml
kubectl apply -f app-2-dep.yaml
kubectl apply -f app-2-svc.yaml
kubectl apply -f app-2-ingress.yaml
```


Once You have Ran One of These Two Methods You should see an output similar to this 
<img width="682" alt="Screenshot 2024-04-09 at 10 05 03 PM" src="https://github.com/thisdontw0rk/pop/assets/144601350/45d495c0-5927-4aaa-b106-365a35c45954">


Here is the output showcasing the `kubectl get all command`

<img width="677" alt="Screenshot 2024-04-09 at 10 05 43 PM" src="https://github.com/thisdontw0rk/pop/assets/144601350/684856d7-b777-4a26-bb87-62fae14f2217">

Verify that all pods are running:

<img width="677" alt="Screenshot 2024-04-09 at 10 05 43 PM" src="https://github.com/thisdontw0rk/pop/assets/144601350/a4325f91-2469-47b9-a8e7-abb7d42f656b">

 Ensure that services are created:

 <img width="677" alt="Screenshot 2024-04-09 at 10 06 30 PM" src="https://github.com/thisdontw0rk/pop/assets/144601350/f1852e04-121e-48ab-8ca2-96dbae28e64e">

 

If you are done with the program enter the following command to delete the cluster:
```bash
minikube delete
```
