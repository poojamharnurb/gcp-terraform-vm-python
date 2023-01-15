 in instances_result["items"]:
            output_row = []
            metadata_dict = {}
            # print(instance_row)
            output_row.append(project_id) # Project ID as the first field
            output_row.extend([instance_row["name"],instance_row["machineType"],instance_row["status"],instance_row["serviceAccounts"],instance_row["disks"],instance_row["metadata"]])

    output.append(output_row)
    
    return output

def json_write_output(header,output):
    result = {}
    # print(type(output))

    for i in range(len(output)):
        # print(','.join(row))
        # print(output[i])
        result = {}
        temp = output[i]
        for j in header:
            for k in temp:
                result[j]= k
                temp.remove(k)
                break
            
        print(result)
        print("_________________________________\n")
    metadata = result["metadata"]["items"] 
    print(type(metadata))
    meta = {}
    for l in range (len(metadata)):
        t1= metadata[l]
        meta[t1["key"]]=(t1["value"])
        print(metadata[l])

    return result,meta




header = ["project_id","name","machine_type","status","service_account","disks","metadata"]
# Use default credentials
credentials = GoogleCredentials.get_application_default()
compute_client = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)
cloud_billing_client = googleapiclient.discovery.build('cloudbilling', 'v1', credentials=credentials)
output = get_instance_data(compute_client,project_id="kpmg-test-project-374714") # get instance details for the list of projects
json_result,meta = json_write_output(header,output)

print(meta)
print(meta["email"])
