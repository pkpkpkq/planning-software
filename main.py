import json
def loaddata():
    # 加载数据函数
    try:
        with open("data.json", "r", encoding='utf-8') as f:
            return{json.load(f)}
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading data.json: {e}")
        return{}
def main():
    data = loaddata()
    