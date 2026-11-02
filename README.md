# 个人记账本 Expense Tracker

我的第一个完整项目。目标不是做得多高级，而是**从零到部署，完整走一遍**。

## 现在做到哪了

在下面把做完的任务打勾。

- [ ] T1 命令行版：增、删、查（数据存内存）
- [ ] T2 接入 SQLite：建表 + 增删查改成 SQL
- [ ] T3 统计功能：按分类、按月份汇总
- [ ] T4 Web 接口：FastAPI 提供 REST API
- [ ] T5 网页界面：HTML 页面调接口
- [ ] T6 部署到 Linux：后台常驻运行
- [ ] T7 AI 自动分类：调大模型 API 判断分类
- [ ] T8 收尾：完善本 README + 录演示

## 技术栈（会逐步加进来）

- Python 3.13
- SQLite（数据存储）
- FastAPI（T4 开始）
- HTML + JavaScript（T5 开始）
- 大模型 API（T7 开始）

## 怎么跑（每完成一个任务就更新这里）

```bash
# T1 阶段
python main.py
```

## 目录说明

```
expense-tracker/
├── README.md      本文件，说明项目
├── LOG.md         每周复盘记录
├── main.py        程序入口（T1 开始写）
├── db.py          数据库操作（T2 开始用）
├── data.db        SQLite 数据文件（T2 生成，不进 Git）
└── .gitignore
```

## 我踩过的坑

（每遇到一个问题就记在这里，面试时这就是你的素材）

-
