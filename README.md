# Anomaly-Detection

This is aimed at implementing the ML lifecycle flow from data preprocessing to model deployment on the Anomaly dataset. The model here predicts if the network has an anomaly or not based on certain input features.

## DATA AVAILABILITY:

The data is a csv file.

### LIST OF COLUMNS FOR THE DATA SET:

["protocol_type","service", "flag","src_bytes","dst_bytes", "land","wrong_fragment", "hot", "num_failed_logins" , "logged_in" ,"num_compromised" , "root_shell" , "su_attempted", "num_root", "num_file_creations","num_shells", "num_access_files", "num_outbound_cmds", "is_guest_login", "count" , "srv_count", "serror_rate" , "srv_serror_rate" , "rerror_rate" , "srv_rerror_rate" , "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate" , "dst_host_count" , "dst_host_srv_count", "dst_host_same_srv_rate" , "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
"dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate" ,"dst_host_rerror_rate", "dst_host_srv_rerror_rate", "class"]
                 
### BASIC FEATURES OF EACH NETWORK CONNECTION VECTOR:

1. **Protocol_type** : Protocol used in the connection 
2. **Service** : Destination network service used 
3. **Flag** : Status of the connection – Normal or Error
4. **Src_bytes** : Number of data bytes transferred from source to destination in single connection 
5. **Dst_bytes** : Number of data bytes transferred from destination to source in single connection 
6. **Land** : if source and destination IP addresses and port numbers are equal then, this variable takes value 1 else 0 
7. **Wrong_fragment** : Total number of wrong fragments in this connection 

### CONTENT RELATED FEATURES OF EACH NETWORK CONNECTION VECTOR:

1. **Hot** : Number of "hot" indicators in the content such as: entering a system directory, creating programs and executing programs 
2. **Num_failed _logins** : Count of failed login attempts 
3. **Logged_in** : 1 if successfully logged in; 0 otherwise 
4. **Num_compromised** : Number of "compromised" conditions 
5. **Root_shell** : 1 if root shell is obtained; 0 otherwise 
6. **Su_attempted** : 1 if "su root" command attempted or used; 0 otherwise 
7. **Num_root** : Number of "root" accesses or number of operations performed as a root in the connection 
8. **Num_file_creations** : Number of file creation operations in the connection 
9. **Num_shells** : Number of shell prompts
10. **Num_access_files** : Number of operations on access control files 
11. **Num_outbound_cmds** : Number of outbound commands in an ftp session 
12. **Is_guest_login** : 1 if the login is a "guest" login; 0 otherwise 


### TIME RELATED TRAFFIC FEATURES OF EACH NETWORK CONNECTION VECTOR:

1. **Count** : Number of connections to the same destination host as the current connection in the past two seconds
2. **Srv_count** : Number of connections to the same service (port number) as the current connection in the past two seconds
3. **Serror_rate** : The percentage of connections that have activated the flag s0, s1, s2 or s3, among the connections aggregated in count 
4. **Srv_serror_rate** : The percentage of connections that have activated the flag  s0, s1, s2 or s3, among the connections aggregated in srv_count
5. **Rerror_rate** : The percentage of connections that have activated the flag  REJ, among the connections aggregated in count 
6. **Srv_rerror_rate** : The percentage of connections that have activated the flag REJ, among the connections aggregated in srv_count 
7. **Same_srv_rate** : The percentage of connections that were to the same service, among the connections aggregated in count
8. **Diff_srv_rate** : The percentage of connections that were to different services, among the connections aggregated in count


### HOST BASED TRAFFIC FEATURES IN A NETWORK CONNECTION VECTOR:
1. **Dst_host_count** : Number of connections having the same destination host IP address
2. **Dst_host_srv_count** : Number of connections having the same port number
3. **Dst_host_same_srv_rate** : The percentage of connections that were to the same service, among the connections aggregated in dst_host_count 
4. **Dst_host_diff_srv_rate** : The percentage of connections that were to different services, among the connections aggregated in dst_host_count 
5. **Dst_host_same_src_port_rate** : The percentage of connections that were to the same source port, among the connections aggregated in dst_host_srv_count
6. **Dst_host_srv_diff_host_rate** : The percentage of connections that were to different destination machines, among the connections aggregated in dst_host_srv_count
7. **Dst_host_serror_rate** : The percentage of connections that have activated the flag s0, s1, s2 or s3, among the connections aggregated in dst_host_count 
8. **Dst_host_srv_serror_rate** : The percent of connections that have activated the flag s0, s1, s2 or s3, among the connections aggregated in dst_host_srv_count 
9. **Dst_host_rerror_rate** : The percentage of connections that have activated the flag REJ, among the connections aggregated in dst_host_count 
10. **Dst_host_srv_rerror_rate** : The percentage of connections that have activated the flag REJ, among the connections aggregated in dst_host_srv_count


