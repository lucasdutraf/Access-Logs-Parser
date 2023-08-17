import pandas as pd
import numpy as np

def read_data(file_path):
    tuple_list = []
    with open(file_path, "r") as f:
        for line in f:
            info = line.split(" ")
            tuple_list.append(tuple(info))
    return tuple_list

def mount_data(data):
    data = np.array(data)
    columns = ["type", "version", "time", "elb", "listener", "client:port", "destination:port", "connection_time", "tls_handshake_time", "received_bytes", "sent_bytes", "incoming_tls_alert", "chosen_cert_arn", "chosen_cert_serial", "tls_cipher", "tls_protocol_version", "tls_named_group", "domain_name", "alpn_fe_protocol", "alpn_be_protocol", "alpn_client_preference_list", "tls_connection_creation_time"]
    df = pd.DataFrame.from_records(data, columns=columns)
    return df

def write_data(data, file_path):
    output_name = file_path.split(".")[0]
    data.to_csv(f"{output_name}.csv", index=False)

if __name__ == "__main__":
    input_file = input("Enter the file path:")
    data = read_data(input_file)
    df = mount_data(data)
    write_data(df, input_file)
    print(f"Done!, check the output file in {input_file}.csv")