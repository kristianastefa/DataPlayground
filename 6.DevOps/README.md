# Recommender System Deployment on Kubernetes

This project involves deploying a **recommender system** on **Kubernetes** composed of five microservices that interact to simulate user activity, generate recommendations, collect feedback, and monitor system performance. The system consists of the following components:

**1. User Activity Simulator:** Generates (user, item) pairs based on the MovieLens dataset, which are fed into the recommender system.

**2. Recommender Module:** Estimates scores for the user-item pairs using a pre-trained model (SVD).

**3. Feedback Collector:** Tracks feedback by calculating the Root Mean Squared Error (RMSE) between actual and estimated scores and counts unique users.

**4. Prometheus Monitoring:** Collects metrics (RMSE and unique user count) from the feedback collector.

**5. Grafana Dashboard:**  Visualizes the collected metrics, offering insights into the system's performance using Prometheus on a Grafana dashboard.


For each microservice, Docker images were built using the provided Dockerfiles in the respective folders inside the docker_files folder. After building the Docker images, composing up, and pushing images in the online Docker Hub site, each service was deployed to Kubernetes cluster and later exposed.
