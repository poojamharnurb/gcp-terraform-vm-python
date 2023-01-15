# metadata is added to VM using following gcloud command
# gcloud compute instances add-metadata VM_NAME \
# --metadata=user=pooja,

import googleapiclient.discovery
from oauth2client.client import GoogleCredentials

def get_instance_data(compute_client, project_id):

    # Get list & details of all instances for all projects in the project list
    output = []
    zone_name = "us-west4-b"
    instances_result = compute_client.instances().list(project=project_id, zone=zone_name).execute()
    if 'items' in instances_result: # Get instance details only when there are instances in the given zone
        for instance_row in instances_result["items"]:
            output_row = []
            metadata_dict = {}
            # print(instance_row)
        output_row.append(project_id) # Project ID as the first field
        output_row.extend([instance_row["name"],instance_row["machineType"],instance_row["status"],instance_row["serviceAccounts"],instance_row["disks"],instance_row["metadata"]])
        output.append(output_row)
    
    return output

def json_write_output(header,output):

    result = {}
    for i in range(len(output)):
        result = {}
        temp = output[i]
        for j in header:
            for k in temp:
                result[j]= k
                temp.remove(k)
                break
    
    metadata = result["metadata"]["items"] 
    meta = {}
    for l in range (len(metadata)):
        t1= metadata[l]
        meta[t1["key"]]=(t1["value"])

    return result,meta

def main():
    header = ["project_id","name","machine_type","status","service_account","disks","metadata"]
    # Use default credentials
    credentials = GoogleCredentials.get_application_default()
    compute_client = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)
    output = get_instance_data(compute_client,project_id="kpmg-test-project-374714") 
    json_result,meta = json_write_output(header,output)

    print("custom metadata =",meta)
    print(meta["email"])

if __name__ == "__main__":
    main()
