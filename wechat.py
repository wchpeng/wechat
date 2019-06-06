import hashlib

from flask import Flask, request

app = Flask(__name__)


@app.route("/wx/callback", methods=["GET", "POST"])
def callback():
    if request.method == "GET":
        # 微信服务器验证用
        signature = request.args.get("signature")
        nonce = request.args.get("nonce")
        echostr = request.args.get("echostr")
        timestamp = request.args.get("timestamp")
        token = "123456aabcdefg"
        print(signature, nonce, echostr, timestamp, token)
        li = [token, timestamp, nonce]
        if not all(li):
            print("li has none")
            return ""
        li.sort()
        sha1 = hashlib.sha1()
        sha1.update("".join(li).encode(encoding="utf-8"))
        hashcode = sha1.hexdigest()
        print("hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return echostr
        else:
            return ""

    elif request.method == "POST":
        print("request.data: ", request.data)
        print("request.get_json: ", request.get_json())
        print("request.is_json: ", request.is_json)

    return "success"


if __name__ == "__main__":
    app.run('localhost', 5587, debug=True)
