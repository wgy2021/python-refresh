# Python Refresh

Python 基础复习与小项目练习。

## Log Analyzer

一个简单的日志分析脚本，能够：

- 读取 `sample.log`
- 统计 INFO、WARNING、ERROR 日志数量
- 将 ERROR 日志写入 `errors.log`
- 将统计结果保存为 `report.json`

## Run

```bash
python log_analyzer.py