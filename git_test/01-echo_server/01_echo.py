#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

def main():

    # 接続先サーバのポートの指定
    port = int(raw_input("[300] Server port : "))
    #数字を文字列に変換

    # ソケットの生成と接続
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #これから使うソケットタイプとアドレスファミリの体系と仕様の指定
    client.connect(("0.0.0.0", port))
    #サーバーにメッセージを送る
    print client.recv(4096)

    while True:
        # メッセージの入力
        message = raw_input("[=>] Message : ")

        if message != "quit":
            client.send(message)
            print client.recv(4096)
        else:
            client.send(message)
            print client.recv(4096)
            client.close()
            sys.exit(0)

main()