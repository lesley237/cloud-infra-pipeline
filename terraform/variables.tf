# These are reusable values. Change them in one place,
# and they update everywhere they are used.

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "cloud-infra-pipeline"
}

variable "location" {
  description = "Azure region where resources will be created"
  type        = string
  default     = "eastasia"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}