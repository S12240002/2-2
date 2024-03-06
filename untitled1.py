#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:54:24 2024

@author: chenbailun
"""

def collect_user_data():
    name = input("請輸入您的姓名：")
    age = int(input("請輸入您的年齡："))
    height = float(input("請輸入您的身高（米）："))
    favorite_color = input("請輸入您喜愛的顏色：")

    user_data = {
        "name": name,
        "age": age,
        "height": height,
        "favorite_color": favorite_color
    }

    return user_data

def format_user_summary(user_data):
    summary = "{}, {}歲, 身高{}米, 喜愛的顏色是{}。".format(
        user_data["name"], user_data["age"], user_data["height"], user_data["favorite_color"]
    )
    return summary

def main():
    user_data = collect_user_data()
    summary = format_user_summary(user_data)
    print("個人資料摘要：", summary)

if __name__ == "__main__":
    main()

