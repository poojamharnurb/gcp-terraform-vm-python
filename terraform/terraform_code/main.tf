module "bigquery" {
  source        = "./modules/big_query"
  dataset_id    = var.dataset_id
  friendly_name = var.friendly_name
  location      = var.location
  table_id      = var.table_id

}

module "cloud_run_src" {
  source            = "./modules/cloud_run"
  count             = length(var.cloudrun_name)
  cloudrun_name     = var.cloudrun_name[count.index]
  cloudrun_location = var.cloudrun_location
  image             = var.image[count.index] #"us-docker.pkg.dev/cloudrun/container/hello"
  traffic_percent   = var.traffic_percent
}