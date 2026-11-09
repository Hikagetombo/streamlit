import streamlit as st
import math

def round_half_up(val, ndigits=0):
    p = 10 ** ndigits
    # 負の数も絶対値基準で正しく扱う処理
    sign = math.copysign(1, val)
    return sign * ((abs(val) * p * 2 + 1) // 2) / p
# サイドバーの作成
st.sidebar.title("設定")

# スライダー
height = st.sidebar.slider("身長", 150, 200, 165)
weight = st.sidebar.slider("体重",  20, 100,  60)

# テキスト入力
name = st.sidebar.text_input("お名前を入力してください")

# タイトル
st.title("あなたのBMI")

bmi = weight / (height / 100) ** 2
bmi = round_half_up(bmi, 1)

# 条件分岐
if name:
    st.write(f"{name}さん、{bmi}ですね！")