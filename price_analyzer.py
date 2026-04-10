from datetime import datetime, timedelta


def read_data(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            name, date_str, price = line.strip().split(",")
            data.append(
                (name.strip(),
                 datetime.strptime(date_str.strip(), "%Y-%m-%d"),
                 float(price))
            )
    return data

def filter_last_month(data, product_name):
    last_month = datetime.now() - timedelta(days=30)
    return [
        (date, price)
        for name, date, price in data
        if name == product_name and date >= last_month
    ]
