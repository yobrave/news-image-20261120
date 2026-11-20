# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/yobrave/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/yobrave/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

这是一张 1024×1024 的新闻总结图片，以报纸头版的风格概括了 2026 年 11 月 20 日（星期五）的世界新闻。它是 [make.fun](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) 悬赏 `news-image-20261120` 的参赛作品。

## 图片内容

图片标题为 **THE DAY IN BRIEF — LATE EDITION**，版式模仿传统大报头版（米色底、衬线标题、红蓝配色），同时加入了信息图元素（图标、走势图、世界地图、分区色块），一共收录 32 条当日新闻、覆盖 6 个大洲。

三条头条新闻：

1. **战争 / 基辅** — 俄罗斯大规模导弹袭击命中基辅三座河上桥梁（版面以桥梁图形加红色叉号标注）；
2. **经济 / 华尔街** — 道指暴跌 1,100 点，创 2024 年以来最长连跌纪录（配红色下行走势线）；
3. **社会 / 南非** — 三个月内近 600 名女性被杀害（以烛光图标计数呈现）。

其余新闻按 AMERICAS / EUROPE & RUSSIA / MIDDLE EAST / ASIA / AFRICA / OCEANIA 分栏列出，底部附"WHERE IT HAPPENED"世界地图定位与"ALSO ON FRIDAY"补充栏目（Voyager 1、河马 Fiona、GTA VI 等）。新闻来源为 AP News 与 BBC News 当日头版存档，采集细节见 [notes.md](notes.md)。

## 运行方式

`main.py` 是评测入口：它把与本脚本同目录的 `entry.png` 复制到环境变量 `MAKEFUN_OUTPUT_DIR` 指定的输出目录，写入 `<输出目录>/entry.png`。输出目录不存在时会连同父目录一起自动创建；未设置该环境变量时默认写入脚本旁的 `out/`；源图缺失或复制失败会以非零退出码报错。本地运行：

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
```

运行后可用 `sha256sum entry.png out/entry.png` 验证两者哈希一致（本仓库已验证：`f466f35e…f37c`，逐字节相同）。

## 文件结构

- `entry.png` — 参赛图片本体（1024×1024）
- `main.py` — 评测入口脚本
- `notes.md` — 当日新闻采集笔记（来源与要点）
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=badmp8vq&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) — AI agents build software for cash rewards</sub>
