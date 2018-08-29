#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading

# クライアントのアドレス情報
addr = "192.168.100.113"

def main():
    global addr

    # サーバ側ポートの指定
    port = int(raw_input("[300] Server port : "))

    # ソケットを生成しバインド
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))

    # コネクションの上限を5に設定し、リスニング開始
    server.listen(5)

    print "[*] Server started on %s:%d" % ("0.0.0.0", port)

    while True:
        # クライアント接続の認識
        client,addr = server.accept()

        print "[*] Connection received from %s:%d" % (addr[0],addr[1])
        client.send("[<=] Hello! This is echo server.\n")
        client.send("[!!] If you want to disconnect, please type \"quit\".")

        # クライアントのコネクションをハンドリングするスレッドの生成と実行
        client_handle_thread = threading.Thread(
            target=client_handler,
            args=(client,)
        ).start()

def client_handler(client):
    global addr

    while True:
        # メッセージの受信と整形
        message = client.recv(4096)
        message = message.rstrip()

        print "[=>] Received message \"%s\" from %s:%d" % (message, addr[0], addr[1])
        if message != "quit":
            client.send("[<=] Echo : %s" % message)
        else:
            client.send("[<=] Goodbye.")
            print "[*] Connection end %s:%d" % (addr[0],addr[1])
            client.close()
            break

main()