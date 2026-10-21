# CNC 数控知识闯关

一款带音效、动画和连击反馈的 CNC 数控加工答题游戏，网页即开即玩，可安装到手机桌面（PWA），后续计划扩展为 iOS / Android APP。

## 内容

| 模式 | 数量 | 说明 |
|---|---|---|
| 闯关 / 随机 20 题 / 60 秒限时 | 304 道选择题，11 个章节 | 每题含详细解析与出处（ISO 6983、ISO 841、GB/T、FANUC 0i-F、SINUMERIK 手册等） |
| 程序找错 · 撞刀排雷 | 61 道 | 点出程序里会出事的那一行，附原因、正确写法、出处 |
| 看图编程 · 图纸填空 | 31 道 / 75 个空 | 看车削、铣削零件图，补全程序中的指令和坐标 |
| 字母速查 | A–Z | 地址字含义翻卡 |
| 错题本 | — | 三种题型通用 |

## 目录结构

```
web/                     可直接部署的网页（单文件 index.html，题库已内联）+ PWA 清单与离线缓存
data/cnc_question_bank.json   唯一的题库数据源（网页和未来 APP 共用）
data/sources/            分章节原始题目（q1–q13 选择题，bugs1–2 程序找错）
scripts/gen_drawings.py  生成"看图编程"题目并写入题库
scripts/check_bank.py    校验题库结构
docs/                    数据格式说明与 APP 路线图
```

## 本地运行

```bash
cd web && python3 -m http.server 8000
# 打开 http://localhost:8000
python3 scripts/check_bank.py   # 校验题库
```

## 说明

题目依据公开标准和厂家手册整理，仅供学习参考；具体机床请以厂家说明书为准。
