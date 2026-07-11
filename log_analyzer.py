import json
log_file_name = "sample.log"

with open(log_file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()

info_count = 0
warning_count = 0
error_count = 0
error_lines = []

for line in lines:
    line = line.strip()
    if line.startswith("INFO"):
        info_count += 1
    elif line.startswith("WARNING"):
        warning_count += 1
    elif line.startswith("ERROR"):
        error_count += 1
        error_lines.append(line)

print("总行数：", len(lines))
print("INFO：", info_count)
print("WARNING：", warning_count)
print("ERROR：", error_count)
with open("errors.log", "w", encoding="utf-8") as file:
    for error_line in error_lines:
        file.write(error_line + "\n")

print("错误日志已保存到 errors.log")
report = {
    "total_lines": len(lines),
    "info_count": info_count,
    "warning_count": warning_count,
    "error_count": error_count
}

with open("report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, ensure_ascii=False, indent=4)

print("统计报告已保存到 report.json")