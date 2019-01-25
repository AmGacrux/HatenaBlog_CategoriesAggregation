# はてブから情報を引っ張ってくるテストコード
import requests

hatena_id="AmGacrux"
blog_id="amgacrux.hateblo.jp"
password="e6epfhew05"
entry_id_list = ["98012380838540725"]

member_uri = "https://blog.hatena.ne.jp/{hatena_id}/{blog_id}/atom/entry/{entry_id}".format(hatena_id=hatena_id, blog_id=blog_id,entry_id=entry_id_list[0])
member_uri
res_member = requests.get(member_uri, auth=(hatena_id, password))
print(res_member.text)