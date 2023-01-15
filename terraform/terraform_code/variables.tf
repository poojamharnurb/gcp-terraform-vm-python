/* Big Query Variables */
variable "dataset_id" {
  default = "test_dataset"
  type    = string
}
variable "friendly_name" {
  default = "test_dataset_bq"
  type    = string
}
variable "location" {
  default = "US"
  type    = string
}
variable "table_id" {
  default = "test_bq_table"
  type    = string
}

/* Cloud Run variables */
variable "cloudrun_name" {
  default = ["cloudrun-frontend", "cloudrun-backend"]
  type    = list(any)
}
variable "cloudrun_location" {
  default = "us-central1"
  type    = string
}
variable "image" {
  default = ["us-docker.pkg.dev/cloudrun/container/hello", "us-docker.pkg.dev/cloudrun/container/hello"]
  type    = list(string)
}
variable "traffic_percent" {
  default = 100
  type    = number
}


variable "project" {
  default = ""
  type    = string
}

variable "region" {
  default = "us-central1"
  type    = string
}