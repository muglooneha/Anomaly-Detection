# Anomaly-Detection

This is aimed at implementing the ML lifecycle flow from data preprocessing to model deployment on the Anomaly dataset. The model here predicts if the network has an anomaly or not based on certain input features.

## DATA AVAILABILITY:

The data is a csv file.

### LIST OF COLUMNS FOR THE DATA SET:

["protocol_type","service", "flag","src_bytes","dst_bytes", "land","wrong_fragment", "hot", "num_failed_logins" , "logged_in" ,"num_compromised" , "root_shell" , "su_attempted", "num_root", "num_file_creations","num_shells", "num_access_files", "num_outbound_cmds", "is_guest_login", "count" , "srv_count", "serror_rate" , "srv_serror_rate" , "rerror_rate" , "srv_rerror_rate" , "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate" , "dst_host_count" , "dst_host_srv_count", "dst_host_same_srv_rate" , "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
"dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate" ,"dst_host_rerror_rate", "dst_host_srv_rerror_rate", "class"
                 
### BASIC FEATURES OF EACH NETWORK CONNECTION VECTOR:

Protocol_type: Protocol used in the connection
Service: Destination network service used
Flag: Status of the connection – Normal or Error
Src_bytes: Number of data bytes transferred from source to destination in single connection
Dst_bytes: Number of data bytes transferred from destination to source in single connection
Land: if source and destination IP addresses and port numbers are equal then, this variable takes value 1 else 0
Wrong_fragment: Total number of wrong fragments in this connection

### CONTENT RELATED FEATURES OF EACH NETWORK CONNECTION VECTOR:

Hot: Number of "hot" indicators in the content such as: entering a system directory, creating programs and executing programs
Num_failed _logins: Count of failed login attempts
Logged_in Login Status: 1 if successfully logged in; 0 otherwise
Num_compromised: Number of "compromised" conditions
Root_shell: 1 if root shell is obtained; 0 otherwise
Su_attempted: 1 if "su root" command attempted or used; 0 otherwise
Num_root: Number of "root" accesses or number of operations performed as a root in the connection
Num_file_creations: Number of file creation operations in the connection
Num_shells: Number of shell prompts
Num_access_files: Number of operations on access control files
Num_outbound_cmds: Number of outbound commands in an ftp session
Is_guest_login: 1 if the login is a "guest" login; 0 otherwise


### TIME RELATED TRAFFIC FEATURES OF EACH NETWORK CONNECTION VECTOR:

Count: Number of connections to the same destination host as the current connection in the past two seconds
Srv_count: Number of connections to the same service (port number) as the current connection in the past two seconds
Serror_rate: The percentage of connections that have activated the flag (4) s0, s1, s2 or s3, among the connections aggregated in count (23)
Srv_serror_rate: The percentage of connections that have activated the flag (4) s0, s1, s2 or s3, among the connections aggregated in srv_count (24)
Rerror_rate: The percentage of connections that have activated the flag (4) REJ, among the connections aggregated in count (23)
Srv_rerror_rate: The percentage of connections that have activated the flag (4) REJ, among the connections aggregated in srv_count (24)
Same_srv_rate: The percentage of connections that were to the same service, among the connections aggregated in count (23)
Diff_srv_rate: The percentage of connections that were to different services, among the connections aggregated in count (23)


### HOST BASED TRAFFIC FEATURES IN A NETWORK CONNECTION VECTOR:
Dst_host_count: Number of connections having the same destination host IP address
Dst_host_srv_count: Number of connections having the same port number
Dst_host_same_srv_rate: The percentage of connections that were to the same service, among the connections aggregated in dst_host_count (32)
Dst_host_diff_srv_rate: The percentage of connections that were to different services, among the connections aggregated in dst_host_count (32)
Dst_host_same_src_port_rate: The percentage of connections that were to the same source port, among the connections aggregated in dst_host_srv_c ount (33)
Dst_host_srv_diff_host_rate: The percentage of connections that were to different destination machines, among the connections aggregated in dst_host_srv_count (33)
Dst_host_serror_rate: The percentage of connections that have activated the flag (4) s0, s1, s2 or s3, among the connections aggregated in dst_host_count (32)
Dst_host_srv_serror_rate: The percent of connections that have activated the flag (4) s0, s1, s2 or s3, among the connections aggregated in dst_host_srv_c ount (33)
Dst_host_rerror_rate: The percentage of connections that have activated the flag (4) REJ, among the connections aggregated in dst_host_count (32)
Dst_host_srv_rerror_rate: The percentage of connections that have activated the flag (4) REJ, among the connections aggregated in dst_host_srv_c ount (33)


