# 网页 + APP 路线图

## 现在
- `web/index.html` 单文件网页，题库内联；已加 PWA 清单和 Service Worker，手机浏览器可"添加到主屏幕"，离线可玩。

## 下一步（建议顺序）
1. **数据外置**：网页改为运行时读取 `data/cnc_question_bank.json`，题库只维护一份。
2. **进度持久化**：在 GitHub Pages / APP 环境中用 localStorage（网页）或本地存储（APP）保存错题本、最高分。
3. **APP 封装**：用 Capacitor 把 `web/` 打包成 iOS / Android APP，复用全部网页代码；需要原生能力（震动反馈、通知提醒每日一练）时再加插件。
4. **账号与同步（可选）**：网页与 APP 共享错题本和成绩，需要一个轻量后端（如 Supabase / Firebase）。
5. **内容扩充**：新题按 `docs/DATA_FORMAT.md` 写入 `data/`，CI 会自动跑 `scripts/check_bank.py` 校验。
