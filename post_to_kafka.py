from kafka import KafkaProducer
import json
def create_event(data):
    try:
        producer = KafkaProducer(bootstrap_servers="10.4.0.6:9092",
                             security_protocol='SSL',
                             ssl_check_hostname=False,
                             ssl_cafile='kafka-ca-cert.pem',
                             ssl_certfile='kafka-client-cert.pem',
                             ssl_keyfile='kafka-client-key.pem',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send("kafka-topic-names", data)
        producer.flush()
    except Exception as e:
        print(e)

data1 = {"timestamp":"2023-07-10T05:35:20.834591+0000.","flow_id":960814233730079,"in_iface":"ens160","event_type":"alert","src_ip":"172.17.5.21","src_port":52248,"dest_ip":"172.17.5.1","dest_port":53,"proto":"UDP","alert":{"action":"allowed","gid":1,"signature_id":2021575,"rev":4,"signature":"Zeus GameOver/FluBot Related DGA NXDOMAIN Responses","category":"Service Attack::DoS","severity":1,"metadata":{"updated_at":["2015_08_01"],"created_at":["2015_08_01"]}},"dns":{"query":[{"type":"query","id":0,"rrname":"WybNtsGDCH37GIALLND","rrtype":"TKEY","tx_id":0}]},"app_proto":"dns","flow":{"pkts_toserver":1,"pkts_toclient":0,"bytes_toserver":145,"bytes_toclient":0,"start":"2023-07-10T05:35:20.834591+0000."},"payload":"AAAAAAABAAAAAAABE1d5Yk50c0dEQ0gzN0dJQUxMTkQAAPkAARNXeWJOdHNHRENIMzdHSUFMTE5EAAAQAAFOk8gJACMiNklVdVBjTXJaelE1eFBoOEJvWFU0YWJXT2VhWk9vdGVUbg==","payload_printable":".............WybNtsGDCH37GIALLND......WybNtsGDCH37GIALLND.....N....#\"6IUuPcMrZzQ5xPh8BoXU4abWOeaZOoteTn","stream":0}

data2 = {"timestamp":"2023-07-10:17:45.028142+0000","flow_id":960810105531886,"in_iface":"ens160","event_type":"alert","src_ip":"172.17.5.21","src_port":52248,"dest_ip":"172.17.5.1","dest_port":53,"proto":"UDP","alert":{"action":"allowed","gid":1,"signature_id":2021575,"rev":4,"signature":"Zeus GameOver/FluBot Related DGA NXDOMAIN Responses","category":"Service Attack::DoS","severity":1,"metadata":{"updated_at":["2015_08_01"],"created_at":["2015_08_01"]}},"dns":{"query":[{"type":"query","id":0,"rrname":"WybNtsGDCH37GIALLND","rrtype":"TKEY","tx_id":0}]},"app_proto":"dns","flow":{"pkts_toserver":1,"pkts_toclient":0,"bytes_toserver":145,"bytes_toclient":0,"start":"2023-07-10T06:17:45.028142+0000"},"payload":"AAAAAAABAAAAAAABE1d5Yk50c0dEQ0gzN0dJQUxMTkQAAPkAARNXeWJOdHNHRENIMzdHSUFMTE5EAAAQAAFOk8gJACMiNklVdVBjTXJaelE1eFBoOEJvWFU0YWJXT2VhWk9vdGVUbg==","payload_printable":".............WybNtsGDCH37GIALLND......WybNtsGDCH37GIALLND.....N....#\"6IUuPcMrZzQ5xPh8BoXU4abWOeaZOoteTn","stream":0}
data3 = {"timestamp":"2023-07-10T06:25:24.623158+0000","flow_id":960810135618102,"in_iface":"ens160","event_type":"alert","src_ip":"172.17.5.21","src_port":52248,"dest_ip":"172.17.5.1","dest_port":53,"proto":"UDP","alert":{"action":"allowed","gid":1,"signature_id":2021575,"rev":4,"signature":"Zeus GameOver/FluBot Related DGA NXDOMAIN Responses","category":"Service Attack::DoS","severity":1,"metadata":{"updated_at":["2015_08_01"],"created_at":["2015_08_01"]}},"dns":{"query":[{"type":"query","id":0,"rrname":"WybNtsGDCH37GIALLND","rrtype":"TKEY","tx_id":0}]},"app_proto":"dns","flow":{"pkts_toserver":1,"pkts_toclient":0,"bytes_toserver":145,"bytes_toclient":0,"start":"2023-07-10T06:25:24.623158+0000"},"payload":"AAAAAAABAAAAAAABE1d5Yk50c0dEQ0gzN0dJQUxMTkQAAPkAARNXeWJOdHNHRENIMzdHSUFMTE5EAAAQAAFOk8gJACMiNklVdVBjTXJaelE1eFBoOEJvWFU0YWJXT2VhWk9vdGVUbg==","payload_printable":".............WybNtsGDCH37GIALLND......WybNtsGDCH37GIALLND.....N....#\"6IUuPcMrZzQ5xPh8BoXU4abWOeaZOoteTn","stream":0}

create_event(data1)
create_event(data2)
create_event(data3)

