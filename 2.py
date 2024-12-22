import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime

# Define tasks with their start and end dates
tasks = [
    ("需求分析", "2024-12-25", "2024-12-27"),
    ("爬虫模块开发", "2024-12-28", "2024-12-30"),
    ("数据整理模块开发", "2024-12-31", "2024-01-02"),
    ("信息处理模块开发", "2024-01-03", "2024-01-05"),
    ("测试与验收", "2024-01-06", "2024-01-08")
]

# Prepare figure and axis for Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))

# Add tasks to the chart
for i, (task, start, end) in enumerate(tasks):
    start_date = date2num(datetime.datetime.strptime(start, "%Y-%m-%d"))
    end_date = date2num(datetime.datetime.strptime(end, "%Y-%m-%d"))
    ax.barh(i, end_date - start_date, left=start_date, color="skyblue")
    ax.text(start_date, i, task, va="center", ha="right", fontsize=10)

# Configure the chart
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([task for task, _, _ in tasks])
ax.set_xlabel("日期")
ax.xaxis_date()
ax.invert_yaxis()
plt.title("甘特图：项目开发进度")
plt.tight_layout()

# Show the Gantt chart
plt.show()
