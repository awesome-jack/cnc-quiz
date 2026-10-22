# 题库数据格式（data/cnc_question_bank.json）

网页和未来 APP 共用这一份 JSON。

## questions（选择题）
`id` 编号 · `cat` 章节 · `q` 题干 · `options` 4 个选项 · `answer` 正确选项下标 0–3 · `explain` 解析 · `source` 出处

## glossary（A–Z 地址字）
`letter` · `meaning`；`glossary_source` 为出处

## bugs（程序找错）
`id` · `title` 场景 · `system` 控制系统 · `code` 程序行数组 · `bad` 出错行下标（从 0 开始） · `explain` 错误原因 · `fix` 正确写法 · `source` 出处

## drawings（看图编程）
`id` · `title` · `system` · `code` 程序行数组，空位写作 `{{1}}`、`{{2}}`… · `blanks[n-1]` 对应第 n 个空：`options` 4 个、`answer` 下标、`why` 理由 · `explain` 整题思路 · `source` 出处
`drawing`：
- `type: "lathe"`：`points` 为 `[z, 直径]` 轮廓点（右端面 z=0，向左为负），第三项 `{"r":R,"dir":"G02|G03"}` 表示圆弧段；`bore: true` 表示内孔轮廓；`callouts` 标注；`stock`、`origin`、`notes`
- `type: "mill"`：`stock {w,h,t}`；`contour` 轮廓点（程序坐标），第三项 `{"r":R}` 为圆角；`holes [{x,y,d,label}]`；`circles [{x,y,r,label,dashed}]`；`origin`、`notes`

## judges（判断题）
`id` · `cat` 章节 · `q` 陈述句 · `answer` true/false · `explain` · `source`

## multis（多选题）
`id` · `cat` · `q` · `options` 5 个选项 · `answer` 正确下标数组（2–4 个） · `explain`（逐项 A✓/B✗） · `source`

## typeins（口令速答·手输代码）
`id` · `cat` · `system` · `q` 功能描述 · `answer` 可接受答案数组 · `hint` 提示 · `explain` · `source`
判分时去空格、全角转半角、转大写，并把 G/M 后的前导 0 去掉（G01 = G1）。

## lessons（课文）
`cat` 章节 · `order` 学习顺序 · `title` · `minutes` · `goals[]` · `sections[{h, blocks[{t,x}]}]` · `pitfalls[]` · `mnemonic` · `sources[]`
块类型 `t`：p（可含 **加粗**）、ul、ol、code、table（首行表头）、tip（老师傅提示）、warn（注意）。
