import datetime


def unix_to_datetime(timestamp: str) -> datetime:
    return datetime.datetime.fromtimestamp(int(timestamp))


if __name__ == '__main__':
    dt = unix_to_datetime('1538402919')
    print(dt.strftime('%Y/%m/%d %H:%M:%S'))
