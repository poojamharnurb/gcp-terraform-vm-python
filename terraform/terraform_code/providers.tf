provider "google" {
  credentials = file("cred.json")
  project     = var.project
  region      = var.region
}

provider "google-beta" {
  credentials = file("cred.json")
  project     = var.project
  region      = var.region
}

terraform {
  required_version = ">= 0.13"

  required_providers {
    google      = "~> 3.26"
    google-beta = "~> 3.34.0"

  }
  backend "gcs" {
    credentials = "cred.json"
    bucket      = "test--tf-bucket-state"
    prefix      = "test-tfstate"

  }

}