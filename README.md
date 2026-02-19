# basic-docker-kubernetes

A minimal FastAPI todo API backed by Postgres, with Alembic migrations and Docker Compose.

## Quick start

```sh
docker compose up --build
docker ps
docker logs -f <container_id>
docker exec -it <container_id> bash
docker compose down
```

```sh
# Build image locally
docker build -t todo-api:latest .
```

The API will be available at http://localhost:8000.

## API endpoints

- `GET /healthz`
- `GET /todos`
- `POST /todos` (body: `{ "title": "..." }`)
- `GET /todos/{id}`
- `PATCH /todos/{id}` (body: `{ "title": "...", "is_done": true }`)
- `DELETE /todos/{id}`

## Kubernetes with Minikube 

### Prerequisites
- Docker Desktop installed and running
- Minikube v1.38.0+ 

### Quick Start with Minikube

**Enable Dashboard:**
```sh
minikube addons enable dashboard
minikube addons enable metrics-server
```

**Access Dashboard:**
```sh
minikube dashboard
```



2. **Deploy your application** (Recommended: Build locally to avoid Docker API issues):
```sh
# Build image locally
docker build -t todo-api:latest .

# Load into minikube
minikube image load todo-api:latest

# Deploy
kubectl apply -f k8s/postgres.yaml
kubectl apply -f k8s/api.yaml
```

3. **Check deployment status**:
```sh
kubectl get pods
kubectl get deployments
kubectl get svc

kubectl describe pod <pod_name>
kubectl get pod <pod_name> -o yaml
kubectl delete pod <pod_name>

```

4. **Access the API**:
```sh
# Port forward (recommended)
kubectl port-forward svc/todo-api-service 8000:8000

# Or use minikube service
minikube service todo-api-service
```

**Note:** If you encounter `Docker API version too old` errors, see [DOCKER_API_FIX.md](./DOCKER_API_FIX.md) and [MANUAL_DEPLOYMENT.md](./MANUAL_DEPLOYMENT.md)

### Useful Commands

```sh
# View logs
kubectl logs -l app=todo-api

# Port forward to access API locally
kubectl port-forward svc/todo-api-service 8000:8000

# Stop minikube
minikube stop

# Delete minikube cluster
minikube delete

```

## Local dev (without Docker)

Set `DATABASE_URL` to a Postgres connection string and run:

```sh
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```
