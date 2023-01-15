resource "google_cloud_run_service" "default" {
  name     = var.cloudrun_name
  location = var.cloudrun_location

  template {
    spec {
      containers {
        image = var.image     #"us-docker.pkg.dev/cloudrun/container/hello"
      }
    }
  }

  traffic {
    percent         = var.traffic_percent
    latest_revision = true
  }
}