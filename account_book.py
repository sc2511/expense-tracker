import os
import datetime


def add_record():
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    while True:
        try:
            cost = float(input("请输入花费的金额(只输入数字，比如23.5)："))
            break
        except ValueError:
            print("金额要输数字，比如23.5")
    while True:
        category = input("分类（吃饭/交通/购物）：").strip()
        if category in ("吃饭", "交通", "购物"):
            break
        print("分类只能是 吃饭 / 交通 / 购物")
    note = input("备注：")
    with open("records.txt", "a", encoding="utf-8") as f:
        f.write(f"{date_str},{cost},{category},{note}\n")
    print("已记录")


def load_records():
    if not os.path.exists("records.txt"):
        return []
    records = []
    with open("records.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",", 3)
            records.append(parts)
    return records


def find_by_daysummary():
    month = input("查哪个月（格式2026-11）：").strip()
    records = load_records()
    if not records:
        print("还没有记录")
        return
    summary = {}
    count = {}
    for parts in records:
        if parts[0][:7] == month:
            day = parts[0]
            cost = float(parts[1])
            summary[day] = summary.get(day, 0) + cost
            count[day] = count.get(day, 0) + 1
    if not summary:
        print(f"没有「{month}」的记录")
        return
    total = 0
    for day, money in sorted(summary.items()):
        y, m, d = day.split("-")
        total += money
        print(f"{m}月{d}日  共 {count[day]} 笔  {money:.2f} 元")
    print(f"本月合计 {total:.2f} 元")

def find_max():
    records = load_records()
    if not records:
        print("还没有记录")
        return
    best = records[0]
    for parts in records:
        if float(parts[1]) > float(best[1]):
            best = parts
    print("最贵的一笔：")
    print_row(best)


def print_row(parts):
    y, m, d = parts[0].split("-")
    print(f"{y}年{m}月{d}日  {parts[2]}  {float(parts[1]):.2f} 元 {parts[3]}")


def show_records():
    records = load_records()
    if not records:
        print("还没有记录")
        return
    for parts in records:
        print_row(parts)


def show_summary():
    records = load_records()
    if not records:
        print("还没有记录")
        return
    summary = {}
    for parts in records:
        category = parts[2]
        cost = float(parts[1])
        summary[category] = summary.get(category, 0) + cost
    total = 0
    ranked = sorted(summary.items(), key=lambda kv: kv[1], reverse=True)
    for category, money in ranked:
        print(f"{category}  共 {money:.2f} 元")
        total += money
    print(f"合计 {total:.2f} 元")


def find_by_category():
    cat = input("查哪个分类：").strip()
    if cat == "":
        print("分类不能为空")
        return
    records = load_records()
    if not records:
        print("还没有记录")
        return
    total = 0
    count = 0
    for parts in records:
        if cat == parts[2]:
            total += float(parts[1])
            count += 1
            print_row(parts)
    if count == 0:
        print(f"没有「{cat}」的记录")
        print("分类只有 吃饭 / 交通 / 购物")
    else:
        print()
        print(f"{cat}  共 {count} 笔  {total:.2f} 元")


def find_by_month():
    month = input("查哪个月（格式2026-11）：").strip()
    if month == "":
        print("月份不能为空")
        return
    records = load_records()
    if not records:
        print("还没有记录")
        return
    total = 0
    count = 0
    for parts in records:
        if parts[0][:7] == month:
            total += float(parts[1])
            count += 1
            print_row(parts)
    if count == 0:
        print(f"没有「{month}」的记录")
    else:
        print()
        print(f"{month}  共 {count} 笔  {total:.2f} 元")


while True:
    print()
    print("=== 记账本 ===")
    print("1. 记一笔")
    print("2. 看记录")
    print("3. 看汇总")
    print("4. 按分类查")
    print("5. 按月查")
    print("6. 按天汇总")
    print("7. 看最贵的一笔")
    print("8. 退出")
    try:
        x = int(input("请选择："))
    except ValueError:
        print("请输入数字")
        continue

    if x == 1:
        add_record()
    elif x == 2:
        show_records()
    elif x == 3:
        show_summary()
    elif x == 4:
        find_by_category()
    elif x == 5:
        find_by_month()
    elif x == 6:
        find_by_daysummary()
    elif x == 7:
        find_max()
    elif x == 8:
        print("退出")
        break
    else:
        print("没有这个选项")
