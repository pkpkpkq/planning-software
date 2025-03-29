import json
def loaddata():
    # 加载数据函数
    try:
        with open("data.json", "r", encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading data.json: {e}")
        exit()
def sort(data):
    from operator import itemgetter
    return dict(sorted(data.items(), key=itemgetter(1), reverse=True))
def main():
    temp = {}
    data = loaddata()
    for key, value in data.items():
        temp[key] = value["urgency"] + value["importance"]
    print(sort(temp))

if __name__ == "__main__":
    main()