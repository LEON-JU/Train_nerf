import json

test_path = r'./data/desk/transforms_test.json'
train_path = r'./data/desk/transforms_train.json'
val_path = r'./data/desk/transforms_val.json'

# 读取JSON文件
with open(test_path, 'r') as file:
    test_data = json.load(file)

with open(train_path, 'r') as file:
    train_data = json.load(file)

with open(val_path, 'r') as file:
    val_data = json.load(file)

# 提取"frames"下所有的"file_path"并打印
for frame in test_data['frames']:
    file_path = frame['file_path']
    print(file_path)

# print(f"length of test case: {len(test_data['frames'])}")
# print(f"length of train case: {len(train_data['frames'])}")
# print(f"length of val case: {len(val_data['frames'])}")