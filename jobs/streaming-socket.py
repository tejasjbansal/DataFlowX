import json
import socket
import time
import pandas as pd

def handle_date(obj):
    if isinstance(obj, pd.Timestamp):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

def send_data_over_socket(file_path):
    
    chunk_size = 2
    # TCP/IP socket configuration
    TCP_IP = '0.0.0.0'
    TCP_PORT = 9999


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(1)

    last_sent_index = 0

    while True:
        print(f"Listening for connections on {TCP_IP}:{TCP_PORT}")
        conn,addr = sock.accept()
        print(f"Connections from {addr}")

        try:
            with open(file_path,'r') as file:
                # skip the lines that were already sent
                for _ in range(last_sent_index):
                    next(file)

                records = []
                for line in file:
                    records.append(json.loads(line))
                    if(len(records)) == chunk_size:
                        chunk = pd.DataFrame(records)
                        print(chunk)
                        for record in chunk.to_dict(orient='records'):
                            serialize_data = json.dumps(record, default=handle_date).encode('utf-8')
                            conn.send(serialize_data + b'\n')
                            time.sleep(5)
                            last_sent_index += 1

                        records = []

        except (BrokenPipeError, ConnectionResetError):
            print("Client disconnected.")
        finally:
            conn.close()
            print("Connection closed")


if __name__ == "__main__":
    send_data_over_socket("datasets/yelp_academic_dataset_review.json")


